"""
Streamlit dashboard for LIGHTARK Multi-Regime Alpha System (MRAS v5)
Save as: streamlit_app.py

Instructions:
- Export your master_v5 dataframe to CSV at data/master_v5.csv (see snippet below)
- Install requirements: pip install -r requirements-streamlit.txt
- Run: streamlit run streamlit_app.py

Exports snippet (run once in your notebook):
# master_v5 is created by the notebook; save it
master_v5.to_csv('data/master_v5.csv')
# Also save subsystem NAVs if you want
master['nav_bnh'].to_csv('data/nav_bnh.csv')

Features:
- NAV chart (Master vs Buy & Hold)
- Regime timeline (color bands)
- Regime-level diagnostics (metrics)
- Recent trades / positions table
- Download data button
- Simple parameter controls in sidebar
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="LIGHTARK MRAS Dashboard", layout='wide')

st.title("LIGHTARK — Multi‑Regime Alpha System (MRAS v5)")
st.markdown("A lightweight Streamlit dashboard to visualise NAV, regimes, and trades.\n\n"+
            "Make sure you exported `master_v5` from the notebook into `data/master_v5.csv` before running this app.")

# Sidebar controls
st.sidebar.header("Data & Controls")
csv_path = st.sidebar.text_input('Path to master_v5 CSV', 'data/master_v5.csv')
resample = st.sidebar.selectbox('NAV resample frequency', ['D','W','M'])
show_regime_bands = st.sidebar.checkbox('Show regime bands', True)

@st.cache_data
def load_master(path):
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    return df

try:
    master = load_master(csv_path)
except Exception as e:
    st.error(f"Could not load file at {csv_path}: {e}")
    st.stop()

# Basic checks and rename columns if needed
if 'nav_v5' not in master.columns:
    # try common names
    possible = [c for c in master.columns if 'nav' in c.lower()]
    if possible:
        nav_col = possible[0]
        master['nav_v5'] = master[nav_col]
    else:
        st.error('No nav column found in CSV. Export master_v5.nav_v5 as nav_v5.')
        st.stop()

# page layout
col1, col2 = st.columns([3,1])

with col1:
    st.subheader('NAV — Master Strategy v5 vs Buy & Hold')
    nav = master['nav_v5'].dropna()
    bnh = master.get('nav_bnh', None)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=nav.index, y=nav.values, mode='lines', name='Master v5'))
    if bnh is not None:
        fig.add_trace(go.Scatter(x=bnh.index, y=bnh.values, mode='lines', name='Buy & Hold'))
    fig.update_layout(height=450, template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)

    # Regime timeline plot
    if show_regime_bands and 'state_hmm' in master.columns:
        st.subheader('Regime timeline')
        timeline = master[['state_hmm']].copy()
        timeline = timeline.reset_index()
        timeline['date'] = timeline['index']
        palette = {0: 'cyan', 1: 'gold', 2: 'red'}
        timeline['color'] = timeline['state_hmm'].map(palette)
        # create a stacked bar colored by state
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=timeline['date'], y=[1]*len(timeline), marker_color=timeline['color'], showlegend=False))
        fig2.update_layout(height=200, yaxis=dict(visible=False), template='plotly_dark')
        st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.subheader('Quick Metrics')
    # compute simple metrics
    def compute_simple_metrics(nav_series):
        total = nav_series.iloc[-1] / nav_series.iloc[0] - 1
        years = (nav_series.index[-1] - nav_series.index[0]).days / 365.25
        cagr = (1+total)**(1/years)-1 if years>0 else np.nan
        returns = nav_series.pct_change().dropna()
        ann_vol = returns.std()*np.sqrt(252)
        sharpe = (returns.mean()*252) / (returns.std()*np.sqrt(252)) if returns.std()>0 else np.nan
        drawdown = (nav_series / nav_series.cummax() -1).min()
        return dict(total=total, cagr=cagr, ann_vol=ann_vol, sharpe=sharpe, maxdd=drawdown)

    metrics = compute_simple_metrics(nav)
    st.metric('CAGR', f"{metrics['cagr']*100:.2f}%")
    st.metric('Annual Vol', f"{metrics['ann_vol']*100:.2f}%")
    st.metric('Sharpe', f"{metrics['sharpe']:.2f}")
    st.metric('Max Drawdown', f"{metrics['maxdd']*100:.2f}%")

# Regime diagnostics
st.markdown('---')
st.header('Regime Diagnostics')
if 'state_hmm' in master.columns:
    diag = []
    for s in sorted(master['state_hmm'].unique()):
        sub = master[master['state_hmm']==s]
        ret = sub['nav_v5'].pct_change().fillna(0).sum()
        ann_vol = sub['nav_v5'].pct_change().fillna(0).std()*np.sqrt(252)
        days_frac = len(sub)/len(master)
        days_invested = int(sub['final_pos_lag'].sum()) if 'final_pos_lag' in sub.columns else 0
        diag.append({'state':int(s),'total_ret':ret,'ann_vol':ann_vol,'days_frac':days_frac,'days_invested':days_invested})
    df_diag = pd.DataFrame(diag).set_index('state')
    st.dataframe(df_diag)
else:
    st.info('state_hmm column not found in data.')

st.markdown('---')
# Recent positions/trades
st.header('Recent Positions / Trades')
if 'final_pos' in master.columns or 'final_pos_lag' in master.columns:
    poscol = 'final_pos' if 'final_pos' in master.columns else 'final_pos_lag'
    recent = master[[poscol,'state_hmm']].tail(50)
    recent = recent.reset_index()
    recent['date'] = recent['index'].dt.strftime('%Y-%m-%d')
    st.table(recent[['date', poscol, 'state_hmm']])
else:
    st.info('No final_pos or final_pos_lag columns found; ensure your export includes position columns.')

# Download data
st.markdown('---')
with st.expander('Download CSVs'):
    st.download_button('Download master_v5 as CSV', master.to_csv(index=True), file_name='master_v5.csv')

st.markdown('---')
st.write('Tips:')
st.write('- To export data from notebook: `master_v5.to_csv("data/master_v5.csv")`')
st.write('- To host: use Streamlit Cloud or deploy on a small VM')

# footer
st.markdown('---')
st.caption('Built by LIGHTARK — Multi-Regime Alpha System (MRAS v5)')
