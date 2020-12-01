with open("res/expense report", 'r'):
	nums = list(map(int, files.readlines()))

for a in nums:
	for b in nums:
		if(a == b):
			continue
		if(a + b == 2020):
			print(str(a) + ":" + str(b) + " -> " + str(a * b))