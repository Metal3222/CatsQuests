from datetime import datetime

start_time = datetime.now()
with open('input.txt', 'r') as f:
    n, *a = f.read().split('\n')

res_lower = {}

f = open('output.txt', 'w')
for i in range(int(n)):
    if res_lower.get(a[i].lower()) is not None:
        t = a[i]

        while res_lower.get(t.lower()) is not None:
            res_lower[a[i].lower()] = res_lower[a[i].lower()] + 1
            t = a[i] + str(res_lower[a[i].lower()])

        f.write(t + '\n')
        res_lower[t.lower()] = 0
    else:
        f.write(a[i] + '\n')
        res_lower[a[i].lower()] = 0
f.close()
print(datetime.now() - start_time)
