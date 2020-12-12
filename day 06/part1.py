with open("answers", 'r') as file:
	lines = file.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].replace('\n', '')

groups = []
i = 0
while(i < len(lines)):
	group = []
	line = lines[i]
	while(line):
		for answer in line:
			if(not answer in group):
				group.append(answer)
		i += 1
		if(i < len(lines)):
			line = lines[i]
		else:
			break
	i += 1
	groups.append(group)

count = 0
for group in groups:
	count += len(group)
print(count)