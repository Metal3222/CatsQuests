import io

import pandas as pd

n, k = map(int, input().split())
data = input()
test = data
data = data + ' PlayGolf'

def InputToDF(data, n:int):
    for i in range(n):
        data = data + '\n' + str(input())

    data = pd.DataFrame([x.split(' ') for x in data.split('\n')[1:]],
                        columns=[x for x in data.split('\n')[0].split(' ')])
    return data

data = InputToDF(data,n)
m = int(input())
test = InputToDF(test, m)


print(data)
print('------------------------------------------------')
print(test)