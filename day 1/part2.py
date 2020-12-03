# Replace the following code block with how you want to load your inputs
with open("res/expense report", 'r'):
	nums = list(map(int, files.readlines()))

for a in nums:
	for b in nums:
		for c in nums:
			if(a == b | b == c | a == c):
				continue
			if(a + b + c == 2020):
				print(str(a) + ":" + str(b) + ":" + str(c) + " -> " + str(a * b * c))