import os, json, time, datetime as dt, csv, pathlib
from typing import Dict, List
import requests
import pandas as pd
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pathlib import Path




def Alpha_Pull(s):

    def safe_filename(prefix: str, meta: Dict[str, str]) -> str:
        mid = "_".join([f"{k}-{str(v).replace(' ', '-')[:20]}" for k, v in meta.items()])
        return f"{prefix}_{mid}_{safe_stamp()}.csv"

    def safe_stamp():
        return dt.datetime.now().strftime("%Y%m%d")
    
    SYMBOL = s
    load_dotenv('../.env')
    DATA_RAW= Path(os.getenv('DATA_DIR_RAW'))
    api_key = os.getenv('API_KEY')
    use_alpha = bool(api_key)
    print("Using Alpha Vantage:", use_alpha)
    
    if use_alpha:
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": SYMBOL,
            "outputsize": "compact",
            "apikey": api_key,
            "datatype": "json"
        }
        r = requests.get(url, params=params, timeout=30)
        r.raise_for_status()
        js = r.json()
    
        if "Error Message" in js:
            raise RuntimeError(f"Alpha Vantage error: {js['Error Message']}")
        elif "Information" in js:
            raise RuntimeError(f"Alpha Vantage notice: {js['Information']}")
        elif "Note" in js:
            raise RuntimeError(f"Alpha Vantage note: {js['Note']}")
    
    
        
        key = [k for k in js.keys() if "Time Series" in k]
        assert key, f"Unexpected response keys: {list(js.keys())}"
        series = js[key[0]]
        df_api = (pd.DataFrame(series).T
                  .rename_axis('date')
                  .reset_index())
        # The given was based on a premium account so I looked up the possible outcomes and 4. close was a free call
        df_api = df_api[['date', '4. close']].rename(columns={'4. close': 'close'})
        df_api['date'] = pd.to_datetime(df_api['date'])
        df_api['close'] = pd.to_numeric(df_api['close'])

        fname = safe_filename(prefix="api", meta={"source": "alpha" if use_alpha else "yfinance", "symbol": SYMBOL})
        out_path = DATA_RAW / fname
        df_api.to_csv(out_path, index=False)
        print("Saved:", out_path)