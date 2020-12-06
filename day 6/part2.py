# Replace the following code block with how you want to load your inputs
with open("res/answers", 'r') as file:
	lines = file.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].replace('\n', '')

groups = []
i = 0
while(i < len(lines)):
	group = []
	groupMembers = []

	line = lines[i]
	while(line):
		groupMembers.append(line)
		for answer in line:
			if(not answer in group):
				group.append(answer)
		i += 1
		if(i < len(lines)):
			line = lines[i]
		else:
			break
	i += 1

	groupAnswers = []
	for answer in group:
		everyone = True
		for member in groupMembers:
			if(not answer in member):
				everyone = False
		if(everyone):
			groupAnswers.append(answer)
	groups.append(groupAnswers)

count = 0
for group in groups:
	count += len(group)
print(count)