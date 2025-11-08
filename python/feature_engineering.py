from utils import calculate_rsi, calculate_ema

def add_features(df):
    df['rsi'] = calculate_rsi(df['price'])
    df['ema20'] = calculate_ema(df['price'], span=20)
    df['ema50'] = calculate_ema(df['price'], span=50)
    return df
