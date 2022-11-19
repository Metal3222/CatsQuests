import numpy as np

with open("input.txt", "r") as f:
    n, m, *y = map(float, f.read().split())

res = np.sum(int(n)*(y-np.average(y))**m) / (int(n)*int(n))

with open("output.txt", 'w') as f:
        f.write(np.format_float_positional(res, precision=3, trim='-'))