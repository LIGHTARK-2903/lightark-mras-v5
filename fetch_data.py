# fetch_data.py
import yfinance as yf
import pandas as pd
import os

def fetch_index(symbol="^NSEI", start="2013-01-01", end=None):
    print(f"Downloading {symbol} from {start} to {end or 'today'} ...")
    df = yf.download(symbol, start=start, end=end, progress=True)
    if df is None or df.empty:
        raise RuntimeError("Downloaded dataframe is empty. Check symbol, internet or yfinance availability.")
    os.makedirs("data", exist_ok=True)
    out_path = os.path.join("data", f"{symbol.replace('^','').replace('/','_')}.csv")
    df.to_csv(out_path)
    print(f"Saved {out_path} (rows: {len(df)})")
    return df

if __name__ == "__main__":
    df = fetch_index()
    print(df.head())
