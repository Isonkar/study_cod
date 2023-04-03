x = 0
y = 0
for i in range(int(input())):
    course = input().split()
    if course[0] == 'север':
        y += int(course[1])
    elif course[0] == 'юг':
        y -= int(course[1])
    elif course[0] == 'восток':
        x += int(course[1])
    elif course[0] == 'запад':
        x -= int(course[1])

print(x, y)
