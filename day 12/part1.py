with open("navigation instructions", 'r') as file:
	lines = file.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].replace('\n', '')
actions = []
for i in range(len(lines)):
	action = [lines[i][0], int(lines[i][1:])]
	actions.append(action)

angle = 0
x = 0
y = 0
for a in actions:
	if(a[0] == 'E'):
		x += a[1]
	elif(a[0] == 'S'):
		y -= a[1]
	elif(a[0] == 'W'):
		x -= a[1]
	elif(a[0] == 'N'):
		y += a[1]
	elif(a[0] == 'L'):
		angle = (angle + a[1]) % 360
	elif(a[0] == 'R'):
		angle = (angle - a[1]) % 360
	elif(a[0] == 'F'):
		if(angle == 0):
			x += a[1]
		elif(angle == 90):
			y += a[1]
		elif(angle == 180):
			x -= a[1]
		elif(angle == 270):
			y -= a[1]

print(abs(x) + abs(y))