with open("passwords", 'r') as file:
	lines = file.readlines()

nTotalPasswords = 0
nWrongPasswords = 0

for line in lines:
	nTotalPasswords += 1
	temp = line.split(': ')
	condition = temp[0]
	password = temp[1]
	temp = condition.split(' ')
	letter = temp[1]
	temp = temp[0].split('-')
	pos1 = int(temp[0]) - 1
	pos2 = int(temp[1]) - 1

	if(not ((password[pos1] == letter) != (password[pos2] == letter))):
		nWrongPasswords += 1

print("Invalid passwords: " + str(nWrongPasswords))
print("Valid passwords: " + str(nTotalPasswords - nWrongPasswords))