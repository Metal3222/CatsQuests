import pandas as pd

def fillna_date(data: pd.DataFrame, function: str = 'mean') -> pd.DataFrame:
    print(data)
    data = data.fillna(data.mean())
    print('-----------------------------------------------------------------')
    print(data)
    return data

data = pd.read_csv('input.csv')
test = pd.read_csv('OutputT.csv')
t = fillna_date(data)

print(test)
