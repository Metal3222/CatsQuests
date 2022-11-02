import numpy as np

with open("input.txt", 'r') as f:
    n, m, *y = map(float, f.read().split())

y = np.array(y)
y = np.convolve(y, np.ones(int(m)), 'valid') / int(m)

with open("output.txt", 'w') as f:
    for i in y:
        f.write(np.format_float_positional(i, trim='-') + ' ')