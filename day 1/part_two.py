with open("res/expense report", 'r'):
	nums = map(int, files.readlines())

for a in nums:
	for b in nums:
		for c in nums:
			if(a == b | b == c | a == c):
				continue
			if(a + b + c == 2020):
				print(str(a) + ":" + str(b) + ":" + str(c) + " -> " + str(a * b * c))