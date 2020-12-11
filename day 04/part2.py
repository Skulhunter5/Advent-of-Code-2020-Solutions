# Replace the following code block with how you want to load your inputs
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

def yrValid(value, nMin, nMax):
	if(not value):
		return False
	year = int(value)
	if(year < nMin or year > nMax):
		return False
	return True

def hgtValid(value):
	if(not value):
		return False
	if('cm' in value):
		hgtValue = int(value.replace('cm', ''))
		return ((150 <= hgtValue) and (hgtValue <= 193))
	elif('in' in value):
		hgtValue = int(value.replace('in', ''))
		return ((59 <= hgtValue) and (hgtValue <= 76))
	return False

hexLetters = "#1234567890abcdef"
def hclValid(value):
	if(not value):
		return False
	if(value[0] != '#'):
		return False
	if(len(value.replace('#', '')) != 6):
		return False
	for l in value:
		if(not l in hexLetters):
			return False
	return True	

validEcls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def eclValid(value):
	if(not value):
		return False
	if(value in validEcls):
		return True
	return False

def pidValid(value):
	if(not value):
		return False
	if(len(value) != 9):
		return False
	return True

nValid = 0
for passport in passports:
	try:
		byr = yrValid(passport['byr'], 1920, 2002)
		iyr = yrValid(passport['iyr'], 2010, 2020)
		eyr = yrValid(passport['eyr'], 2020, 2030)
		hgt = hgtValid(passport['hgt'])
		hcl = hclValid(passport['hcl'])
		ecl = eclValid(passport['ecl'])
		pid = pidValid(passport['pid'])
	except KeyError:
		continue
	if(byr and iyr and eyr and hgt and hcl and ecl and pid):
		nValid += 1

print(nValid)