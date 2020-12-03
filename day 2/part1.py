# Replace the following code block with how you want to load your inputs
with open("passwords", 'r') as file:
	lines = file.readlines()

numberAllPasswords = 0
numberWrongPasswords = 0

for line in lines:
	numberAllPasswords += 1
	temp = line.split(': ')
	condition = temp[0]
	password = temp[1]
	temp = condition.split(' ')
	letter = temp[1]
	temp = temp[0].split('-')
	minTimes = int(temp[0])
	maxTimes = int(temp[1])

	counter = 0
	for l in password:
		if(l == '\n'):
			continue
		if(l == letter):
			counter += 1

	if(counter < minTimes or counter > maxTimes):
		numberWrongPasswords += 1

print("Wrong passwords: " + str(numberWrongPasswords))
print("Correct passwords: " + str(numberAllPasswords - numberWrongPasswords))