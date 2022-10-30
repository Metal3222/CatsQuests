from datetime import datetime

start_time = datetime.now()
with open('input.txt', 'r') as f:
    n, *a = f.read().split('\n')

res_lower = set()  # Результат в нижнем регистре
print(datetime.now() - start_time)
f = open('output1.txt', 'w')
for i in range(int(n)):
    j = 0
    print(str(i) + ' ' + str(datetime.now() - start_time))
    if a[i].lower() in res_lower:
        t = a[i].lower()
        while t.lower() in res_lower:
            j += 1
            t = a[i] + str(j)
            if j >= 10000: break
        f.write(t + '\n')
        res_lower.add(t.lower())
    else:
        f.write(a[i] + '\n')
        res_lower.add(a[i].lower())
f.close()
print(datetime.now() - start_time)
