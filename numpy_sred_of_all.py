import numpy as np

with open("input.txt", 'r') as f:
    n, *m = map(float, f.read().split())

m = np.reshape(m, (int(n),2))
m = [m[i][0] for i in range(int(n)) for j in range(int(m[i][1]))]

with open("output.txt", 'w') as f:
    f.write(np.format_float_positional(np.mean(m), trim='-') + ' ')
    f.write(np.format_float_positional(len(m)/np.sum([1.0/i for i in m]), trim='-') + ' ')
    f.write(np.format_float_positional(np.exp(np.mean(np.log(m))), trim='-'))