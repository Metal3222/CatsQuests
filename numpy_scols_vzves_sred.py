import numpy as np

with open("input.txt", "r") as f:
    n, m, *y = map(float, f.read().split())

m_v = y[0:int(m)]

y = [float(i) for i in y[int(m):]]
m_v = [i/np.sum(m_v) for i in m_v]
ves = m_v / np.sum(m_v)
res = np.convolve(y, ves, mode='valid')


print()
with open("output.txt", 'w') as f:
    for i in res:
        f.write(np.format_float_positional(i, precision=3, trim='-') + ' ')