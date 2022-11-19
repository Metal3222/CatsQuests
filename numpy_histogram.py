import numpy as np

with open("input.txt", "r") as f:
    n, *y = map(int, f.read().split())

y = np.histogram(y, bins=int(n))
print(y)
with open("output.txt", 'w') as f:
    for i in y:
        f.write(np.format_float_positional(i, trim='-'))