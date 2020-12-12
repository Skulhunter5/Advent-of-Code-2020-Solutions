with open("navigation instructions", 'r') as file:
	lines = file.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].replace('\n', '')
actions = []
for i in range(len(lines)):
	action = [lines[i][0], int(lines[i][1:])]
	actions.append(action)

sx = 0
sy = 0
wx = 10
wy = 1
for a in actions:
	if(a[0] == 'E'):
		wx += a[1]
	elif(a[0] == 'S'):
		wy -= a[1]
	elif(a[0] == 'W'):
		wx -= a[1]
	elif(a[0] == 'N'):
		wy += a[1]
	elif(a[0] == 'L'):
		if(a[1] == 90):
			v2 = (-wy, wx)
			wx, wy = v2
		elif(a[1] == 180):
			v2 = (-wx, -wy)
			wx, wy = v2
		elif(a[1] == 270):
			v2 = (wy, -wx)
			wx, wy = v2
	elif(a[0] == 'R'):
		if(a[1] == 90):
			v2 = (wy, -wx)
			wx, wy = v2
		elif(a[1] == 180):
			v2 = (-wx, -wy)
			wx, wy = v2
		elif(a[1] == 270):
			v2 = (-wy, wx)
			wx, wy = v2
	elif(a[0] == 'F'):
		dx = wx * a[1]
		dy = wy * a[1]
		sx += dx
		sy += dy

print(abs(sx) + abs(sy))