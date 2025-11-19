# LIGHTARK Multi-Regime Alpha System (MRAS v5)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![Notebook](https://img.shields.io/badge/notebook-Jupyter-orange)](#)

*A multi-regime quantitative trading engine using HMM, Trend-Following, Mean-Reversion, and Panic-Reversal subsystems.*

---

# 📘 Overview

This project implements a **professional-grade, multi-regime trading model** for index markets, controlled through a **Hidden Markov Model (HMM)** that separates the market into:

- **Regime 0 – Trend**
- **Regime 1 – Sideways / Mean-Reversion**
- **Regime 2 – Panic / Crash**

Each regime uses its **own specialized strategy**, and they are combined using a master allocator with volatility-adjusted sizing and risk-parity stabilisation.

This is a full hedge-fund-style project:
- Regime detection  
- Strategy design  
- Backtesting  
- Risk analysis  
- Portfolio-level signal combination  
- Transaction cost modeling  

---

# 🔥 Key Components

### ✔ **1. HMM-Based Regime Detection**
Regimes are learned using:
- Log returns  
- 20-day historical volatility  
- 20-day momentum  

Outputs:
- Transition matrix  
- State persistence  
- Average duration  
- Regime labeling by volatility structure  

---

### ✔ **2. Subsystems**

#### 🔵 **Trend Strategy (Regime 0 – Trending Markets)**
- Close > MA50  
- Breakout above 20-day high OR support bounce at MA20  
- ATR(14) trailing stop  
- RSI(14) confirmation  
- Designed to ride medium-term uptrends  

---

#### 🟡 **Mean Reversion v2.5 (Regime 1 – Sideways Markets)**
- RSI(2) oversold  
- Close vs MA20  
- Bollinger Mid reversal  
- 4-day exit rule  
- Low volatility, high stability subsystem  

---

#### 🔴 **Panic Reversal v3 (Regime 2 – Crash Conditions)**
Optimized specifically for Indian markets:

- RSI2 < 15  
- Close < Lower Bollinger Band  
- MA5 snapback  
- Max-hold = 2 days  
- Win rate ≈ **66%** in crash windows  

---

### ✔ **3. Master Strategy v5**
Combines all three subsystems using:

- Regime priority logic  
  **Panic → MR → Trend**
- Volatility-adjusted position sizing  
- Per-regime risk normalization  
- Transaction cost modeling (0.03% per round trip)  
- Rolling 60-day volatility  
- Portfolio NAV generation  

---

# 📈 Final Results — MASTER STRATEGY v5

| Metric | Value |
|-------|-------|
| **Total Return** | **17.86%** |
| **CAGR** | **1.30%** |
| **Annual Volatility** | **4.52%** |
| **Sharpe Ratio** | **0.315** |
| **Max Drawdown** | **-13.9%** |
| **Win Rate** | **53.5%** |
| **Exposure** | **30.3%** |
| **Number of Trades** | **133** |

---

# 🧠 Regime Contributions

| Regime | Market Condition | Return Contribution | Ann. Vol | Days (%) | Days Invested |
|--------|------------------|----------------------|----------|----------|----------------|
| **0** | Trend | **0.1016** | 0.059 | 47.9% | 719 |
| **1** | Sideways | **0.0577** | 0.025 | 38.4% | 194 |
| **2** | Panic | **0.0178** | 0.028 | 13.6% | 34 |

---

# 🧩 Architecture

Data → Feature Engineering → HMM Regime Model
→ Subsystem Strategies (Trend / MR / Panic)
→ Regime-Weighted Allocator
→ Transaction Cost Model
→ Portfolio NAV

---

# 🚀 How to Run

See **USAGE.md** for full instructions.

Quick version:

```bash
git clone https://github.com/LIGHTARK-2903/lightark-mras-v5.git
cd lightark-mras-v5

python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

python fetch_data.py
jupyter lab
```
Open the notebook in notebooks/.

# 🔧 Tech Stack

→ Python 3
→ NumPy / Pandas
→ hmmlearn
→ scikit-learn
→ matplotlib
→ yfinance
→ Jupyter Notebook

#🔮 Future Plans (v6)

→ Regime confidence score (posterior probabilistic weighting)
→ Kelly or volatility targeting position sizing
→ Cross-asset features (BANKNIFTY, USDINR, Gold)
→ Regime heatmap dashboard with Streamlit
→ Meta-strategy ensemble

#👤 Author

Naman Narendra Choudhary
B.Tech Student | Quant Enthusiast | Finance + Engineering
Interests: Quantitative Finance, Trading Systems, ML for Markets

#📄 License

MIT License © LIGHTARK

---

# 🎉 Done.
