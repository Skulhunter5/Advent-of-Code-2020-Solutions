with open("boarding passes", 'r') as file:
	lines = file.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].replace('\n', '')

seatIDs = []
for i in range(128):
	for j in range(8):
		seatIDs.append(i * 8 + j)

for line in lines:
	minRow = 0
	maxRow = 127
	for i in range(7):
		if(line[i] == 'B'):
			minRow = minRow + (maxRow + 1 - minRow) // 2
		elif(line[i] == 'F'):
			maxRow = maxRow - (maxRow + 1 - minRow) // 2
	minCol = 0
	maxCol = 7
	for i in range(3):
		if(line[7 + i] == 'R'):
			minCol = minCol + (maxCol + 1 - minCol) // 2
		elif(line[7 + i] == 'L'):
			maxCol = maxCol - (maxCol + 1 - minCol) // 2
	seatID = minRow * 8 + minCol
	seatIDs.remove(seatID)

for i in range(128):
	for j in range(8):
		seatID = i * 8 + j
		if(not seatID - 1 in seatIDs and not seatID + 1 in seatIDs and seatID in seatIDs):
			print(seatID)