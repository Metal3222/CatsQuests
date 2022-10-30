from sys import stdin
import copy

first_position_input = stdin.read().splitlines()

first_position_array = []

for i in first_position_input:
    first_position_array.append(list(i))

final_position_array = copy.deepcopy(first_position_array)

test_position_array = copy.deepcopy(first_position_array)

t = first_position_array[len(first_position_array)-1]
t.insert(0, first_position_array[len(first_position_array)-1][len(first_position_array[0])-1])
t.append(first_position_array[len(first_position_array)-1][1])

test_position_array.insert(0, t)

t = first_position_array[0]
t.insert(0, first_position_array[0][len(first_position_array[0])-1])
t.append(first_position_array[0][1])

test_position_array.append(t)

for i in range(1,len(test_position_array)-1):
    test_position_array[i].insert(0, test_position_array[i][len(test_position_array[i])-1])
    test_position_array[i].append(test_position_array[i][1])

first_position_array = copy.deepcopy(test_position_array)


def neighbours(j, i):
    counter = 0
    if i - 1 >= 0 and j - 1 >= 0 and first_position_array[j - 1][i - 1] == "#":
        counter += 1

    if i >= 0 and j - 1 >= 0 and first_position_array[j - 1][i] == "#":
        counter += 1

    if i + 1 >= 0 and j - 1 >= 0 and first_position_array[j - 1][i + 1] == "#":
        counter += 1

    if i - 1 >= 0 and j >= 0 and first_position_array[j][i - 1] == "#":
        counter += 1

    if i + 1 >= 0 and j >= 0 and first_position_array[j][i + 1] == "#":
        counter += 1

    if i - 1 >= 0 and j + 1 >= 0 and first_position_array[j + 1][i - 1] == "#":
        counter += 1

    if i >= 0 and j + 1 >= 0 and first_position_array[j + 1][i] == "#":
        counter += 1

    if i + 1 >= 0 and j + 1 >= 0 and first_position_array[j + 1][i + 1] == "#":
        counter += 1

    return counter

for i in range(1, len(first_position_array)-1):
    for j in range(1, len(first_position_array[i])-1):
        n = neighbours(i, j)
        if first_position_array[i][j] == '#' and n < 2:
            final_position_array[i-1][j-1] = '.'

        elif first_position_array[i][j] == '#' and n > 3:
            final_position_array[i-1][j-1] = '.'

        elif first_position_array[i][j] == '.' and n == 3:
            final_position_array[i-1][j-1] = '#'

print('\n'.join(map(''.join, map(lambda x: map(str, x), final_position_array))))

