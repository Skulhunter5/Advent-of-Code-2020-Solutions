with open("trees", 'r') as file:
	rows = file.readlines()
for i in range(len(rows)):
	rows[i] = rows[i].replace('\n', '')

nTreesEncountered = 0

x = 0
y = 0
while(y < len(rows)):
	if(rows[y][x % len(rows[0])] == '#'):
		nTreesEncountered += 1
	x += 3
	y += 1

print(nTreesEncountered)