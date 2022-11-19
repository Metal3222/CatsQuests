import numpy as np
from scipy import interpolate

n = int(input())+1
z = 1
y = list(map(float, input().split()))
x = np.arange(z, n)

res = interpolate.interp1d(x, y, fill_value='extrapolate')


print(res(n))


