def clean_data(df):
    df = df.drop_duplicates(subset='timestamp')
    df = df.fillna(method='ffill')
    return df
