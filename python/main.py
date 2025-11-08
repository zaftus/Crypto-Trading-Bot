from data_fetcher import fetch_crypto_history
from data_cleaner import clean_data
from feature_engineering import add_features
from predictor import train_predictor
from trader import execute_trade
from notifier import send_telegram_message
from logger import log_info
import config.config as cfg

cryptos = ['bitcoin', 'ethereum', 'ripple']

for crypto in cryptos:
    df = fetch_crypto_history(crypto)
    df = clean_data(df)
    df = add_features(df)
    model = train_predictor(df)
    
    latest_features = df[['rsi','ema20','ema50']].iloc[-1].values.reshape(1, -1)
    signal = model.predict(latest_features)[0]
    execute_trade(signal, crypto.upper(), cfg.trade_amount)
    send_telegram_message(f"{crypto.upper()} trade signal: {'BUY' if signal==1 else 'SELL'}")
    log_info(f"{crypto.upper()} signal: {signal}")
