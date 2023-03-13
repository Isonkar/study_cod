n = int(input())
a =[[0 for j in range(n)] for i in range(n)]

x = 0
y = 0
dx = 1
dy = 0

for i in range(n * n):
	a[y][x] = i + 1
	test = x + dx if dx else y + dy
	if test < 0 or test == n or a[y + dy][x + dx] != 0:
		dx, dy = -dy, dx
	x += dx
	y += dy

for y in range(n):
    print(*a[y])
    
    
    # spiral
