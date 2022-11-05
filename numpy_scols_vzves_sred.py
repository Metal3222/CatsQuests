import numpy as np

with open("input.txt", "r") as f:
    n, m, *y = map(int, f.read().split())

print(n)
print(m)
print(y)
m_v = y[0:m]
y = [float(i) for i in y[m:]]
print(m_v)
print(y)
res = np.convolve(y, m_v, 'valid')
print(res)
with open("output.txt", 'w') as f:
    for i in y:
        f.write(np.format_float_positional(i, trim='-') + ' ')