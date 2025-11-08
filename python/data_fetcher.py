import requests
import pandas as pd
from config.api_keys import COINGECKO_API_KEY
from logger import log_info, log_error

def fetch_crypto_history(crypto='bitcoin', days=90):
    url = f'https://api.coingecko.com/api/v3/coins/{crypto}/market_chart'
    params = {'vs_currency': 'usd', 'days': days}
    try:
        response = requests.get(url, params=params)
        data = response.json()
        df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    except Exception as e:
        log_error(f"Error fetching {crypto}: {e}")
        return pd.DataFrame()
