import pandas as pd

def join_dataframes(data: pd.DataFrame, states: pd.DataFrame) -> pd.DataFrame:
    res = data.join(states, on='State ID').drop('State ID', axis=1)
    return res


states = pd.read_csv('states.csv', index_col='ID')
data = pd.read_csv('data2.csv', index_col='ID')
joined_df = join_dataframes(data, states)


print(joined_df)