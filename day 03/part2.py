with open("trees", 'r') as file:
	rows = file.readlines()
for i in range(len(rows)):
	rows[i] = rows[i].replace('\n', '')

result = 1
for i in range(5):
	nTreesEncountered = 0

	xInc = 0
	yInc = 0
	if(i == 0):
		xInc = 1
		yInc = 1
	elif(i == 1):
		xInc = 3
		yInc = 1
	elif(i == 2):
		xInc = 5
		yInc = 1
	elif(i == 3):
		xInc = 7
		yInc = 1
	elif(i == 4):
		xInc = 1
		yInc = 2

	x = 0
	y = 0
	while(y < len(rows)):
		if(rows[y][x % len(rows[0])] == '#'):
			nTreesEncountered += 1
		x += xInc
		y += yInc

	result *= nTreesEncountered

print(result)