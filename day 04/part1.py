with open("res/passports", 'r') as file:
	lines = file.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].replace('\n', '')

passports = []
current = {}
i = 0
while(i < len(lines)):
	passport = {}
	line = lines[i]
	while(line):
		tokens = line.split()
		for token in tokens:
			temp = token.split(':')
			passport[temp[0]] = temp[1]
		i += 1
		if(i < len(lines)):
			line = lines[i]
		else:
			break
	i += 1
	passports.append(passport)

nValid = 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in passports:
	try:
		for field in fields:
			temp = passport[field]
	except KeyError:
		continue
	nValid += 1

print(nValid)