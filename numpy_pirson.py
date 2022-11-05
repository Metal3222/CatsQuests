import numpy as np

with open("input.txt", "r") as f:
    n,m, *y = map(float, f.read().split())

y = np.split(np.array(y), n)
val = np.vstack([y[i] for i in range(len(y))])
res = np.corrcoef(val)


with open("output.txt", 'w') as f:
    for i in range(len(res)):
        for j in res[i]:
            f.write(np.format_float_positional(j,precision=3, trim='-') + ' ')
        f.write('\n')
