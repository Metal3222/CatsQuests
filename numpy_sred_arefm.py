import numpy as np

with open("input.txt", 'r') as f:
    n, *m = map(float, f.read().split())

with open("output.txt", 'w') as f:
    f.write(np.format_float_positional(np.mean(m), trim='-'))
