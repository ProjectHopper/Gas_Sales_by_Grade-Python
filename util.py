import pandas as pd

def get_data(PATH):
    df = pd.read_csv(PATH)
    df.dropna(inplace=True)
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    return df