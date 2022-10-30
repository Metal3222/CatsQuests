with open('input.txt', 'r') as f:
    n, *a = f.read().split('\n')

a_lower = [i.lower() for i in a]
res = []
res_lower = [] # Результат в нижнем регистре

for i in range(int(n)):
    if a_lower[i] in res_lower:
        if a_lower[i] + str(res_lower.count(a_lower[i])) in res_lower:

            res_lower.append(a_lower[i] + str(res_lower.count(a_lower[i]) + 1))
            res.append(a[i] + str(res_lower.count(a_lower[i]) + 1))
            res_lower.append(a_lower[i])

        else:
            res_lower.append(a_lower[i] + str(res_lower.count(a_lower[i])))
            res.append(a[i] + str(res_lower.count(a_lower[i])))
            res_lower.append(a_lower[i])

    else:
        res.append(a[i])
        res_lower.append(a_lower[i])

with open('output.txt', 'w') as f:
    f.write('\n'.join(res))