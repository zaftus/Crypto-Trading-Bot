from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

def train_predictor(df):
    df = df.dropna()
    df['target'] = (df['price'].shift(-1) > df['price']).astype(int)
    features = ['rsi', 'ema20', 'ema50']
    X = df[features]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f"Model accuracy: {score}")
    return model
