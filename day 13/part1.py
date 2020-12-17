with open("input", 'r') as file:
	lines = file.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].replace('\n', '')

earliest = int(lines[0])
ids = []
for i in lines[1].split(','):
	if(i != 'x'):
		ids.append(int(i))

def dist(j):
	return j - earliest

best = [-1, 100000000]
for i in ids:
	cycle = earliest // i
	if(cycle == earliest / i):
		print(0)
		exit()
	elif(dist((cycle + 1) * i) < dist(best[1])):
		best = [i, (cycle + 1) * i]

print(best[0] * dist(best[1]))