import pandas as pd
from python.feature_engineering import add_features
from python.predictor import train_predictor

df = pd.DataFrame({'price':[1,2,3,4,5,6,7,8,9,10]})
df = add_features(df)
model = train_predictor(df)
assert model is not None
