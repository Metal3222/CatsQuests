import pandas as pd

def get_busiest_states(data: pd.DataFrame) -> pd.Series:
    data = data[['State', 'Total intl calls']]
    data = pd.Series(data=data['Total intl calls'].values, index=data['State'])
    data = data.groupby(['State']).sum()
    data = data.sort_values(ascending=False)
    return data


df = pd.read_csv('data1.csv')
busiest_states = get_busiest_states(df)
print(busiest_states)
