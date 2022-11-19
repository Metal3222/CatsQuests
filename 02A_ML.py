import pandas as pd

def get_businessmen(df: pd.DataFrame) -> pd.DataFrame:
    res = df.loc[df['Total intl calls'].values >= 20]
    return res


df = pd.read_csv('data.csv')
businessmen = get_businessmen(df)


