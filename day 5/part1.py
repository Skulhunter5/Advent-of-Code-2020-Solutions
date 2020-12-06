# Replace the following code block with how you want to load your inputs
with open("res/boarding passes", 'r') as file:
	lines = file.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].replace('\n', '')

maxSeatID = 0
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
	print(minRow, ":", minCol, ":", seatID)
	if(seatID > maxSeatID):
		maxSeatID = seatID

print(maxSeatID)