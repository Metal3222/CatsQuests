with open('input.txt') as f:
    students = list(map(str, f.read().split('\n')))
    students.remove(students[0])
print(students)
with open('output.txt', 'w') as f:
    f.write(str(students))