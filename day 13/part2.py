with open("input", 'r') as file:
	lines = file.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].replace('\n', '')

ids = []
for i in lines[1].split(','):
	if(i != 'x'):
		ids.append(int(i))
	else:
		ids.append(-1)

doneFlag = False
timestamp = 100000000000000
while(not doneFlag):
	if((timestamp - 100000000000000) % 100000 == 0):
		print(timestamp)
	incorrectFlag = False
	for offset, i in enumerate(ids):
		print(offset)
		if(i == -1):
			continue
		if((timestamp + offset) % i != 0):
			incorrectFlag = True
			break
	if(not incorrectFlag):
		doneFlag = True
		print(timestamp)
		exit()
	timestamp += 1
