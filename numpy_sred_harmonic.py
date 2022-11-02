import numpy as np

with open("input.txt", 'r') as f:
    n, *m = map(float, f.read().split())

with open("output.txt", 'w') as f:
    f.write(np.format_float_positional(n/np.sum([1.0/i for i in m]), trim='-'))