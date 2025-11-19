# LIGHTARK Multi-Regime Alpha System (MRAS v5)
**A professional, HMM-driven, multi-strategy quantitative trading model for index markets.**

This project implements a full-fledged **multi-regime trading architecture**, combining  
Trend-following, Mean-Reversion, and Panic-Reversal strategies, orchestrated through  
a **Hidden Markov Model (3 states)** that separates markets into:

- **Regime 0 – Trend**
- **Regime 1 – Sideways / Mean-Reversion**
- **Regime 2 – Panic / Crash**

The system dynamically adjusts position sizing, adapts to volatility, and applies  
risk-parity normalization, creating a stable and modular quantitative engine.

> This repository showcases a real hedge-fund-style project built from scratch —  
with end-to-end modeling, backtesting, risk analysis, and multi-regime strategy design.

---

## 🔥 Key Features

### ✓ **HMM-Based Regime Detection**
- Trained using: Log Returns, 20-day Volatility, 20-day Momentum  
- Finds three stable market regimes with clear behavior differences  
- Regime persistence and transition probabilities match real market cycles

### ✓ **Three Independent Subsystems**
1. **Trend Strategy (Regime 0)**
   - Momentum + MA filters  
   - Breakout + Dip entries  
   - ATR-based dynamic trailing stop  
   - Medium exposure, medium risk, steady gains

2. **Mean-Reversion Strategy v2.5 (Regime 1)**
   - RSI(2) oversold entries  
   - MA20 & mid-band confirmations  
   - 4-day decay model  
   - Low volatility, high stability, frequent trades

3. **Panic-Regime MR Strategy v3 (Regime 2)**
   - India-optimized crash entry logic  
   - RSI2 < 15 + Lower Bollinger Band  
   - MA5 reversals  
   - Very high win-rate (≈67%) during panic windows

### ✓ **Master Strategy v5**
Combines all regimes using:
- Regime-priority override system (Panic > MR > Trend)  
- Volatility-adjusted position sizing  
- Per-regime risk normalization  
- Transaction cost modeling  
- Portfolio-level risk controls  

---

## 📈 Final Results — Master Strategy v5

| Metric | Value |
|-------|-------|
| **Total Return** | **17.86%** |
| **CAGR** | **1.30%** |
| **Annual Volatility** | **4.52%** |
| **Sharpe Ratio** | **0.315** |
| **Max Drawdown** | **-13.9%** |
| **Exposure** | **30.3%** |
| **Number of Trades** | **133** |

### ➤ **Regime-Level Contributions**

| Regime | Interpretation | Return Contribution | Ann. Vol | Days (%) | Days Invested |
|--------|----------------|----------------------|----------|----------|----------------|
| **0** | Trend | **0.1016** | 0.059 | 47.9% | 719 |
| **1** | Sideways MR | **0.0577** | 0.025 | 38.4% | 194 |
| **2** | Panic | **0.0178** | 0.028 | 13.6% | 34 |

---

## 📊 Visuals
The notebook includes:

- Full NAV comparison: **Master Strategy v5 vs Buy & Hold**  
- Regime timeline plot  
- Rolling Sharpe  
- Drawdown graph  
- Subsystem NAVs  
- Return distribution charts  

---

## 🧠 Architecture Overview

### 1. Data Pipeline  
- Yahoo Finance → Cleaned OHLCV  
- Feature engineering  
- Log returns, volatility, momentum  
- Technical indicators: RSI(2), RSI(14), MA20/50, Bollinger Bands, ATR

### 2. Regime Modeling  
- KMeans clustering (initial)  
- HMM with 3 hidden states  
- State labeling by volatility/momentum characteristics  
- Stability check: transition matrix + durations

### 3. Subsystems  
- Independent strategy engines  
- Optimized entry/exit rules  
- ATR, MA, RSI-driven logic  
- Regime-specific logic and safety valves

### 4. Master Strategy  
- Combine subsystem signals  
- Volatility-weighted sizing  
- Risk parity  
- Transaction costs  
- Final NAV + metrics

---

## 🛠️ Tech Stack
- Python 3  
- NumPy, Pandas  
- hmmlearn  
- Scikit-Learn  
- Matplotlib  
- Jupyter  
- Yahoo Finance API (yfinance)

---

## 🧩 Future Improvements (v6)
- Regime confidence scoring using posterior probabilities  
- Position sizing via Kelly fraction or volatility targeting  
- Global macro regime features  
- Cross-asset signals (NIFTY, BANKNIFTY, VIX, Gold, USDINR)  
- Meta-strategy reinforcement learning  
- Streamlit dashboard  

---

## 👤 Author
**Naman Narendra Choudhary**  
B.Tech Student | Aspiring Quant | Finance + Engineering  
Quantitative Trading • Risk Modeling • Business Development

---

## 📘 License
MIT License

