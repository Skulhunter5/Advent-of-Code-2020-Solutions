with open("res/expense report", 'r'):
	nums = list(map(int, files.readlines()))
'''
Replace "res/expense report" with the path to your file containing the inputs or
replace "file.readlines()" with a string containing the inputs
'''

for a in nums:
	for b in nums:
		if(a == b):
			continue
		if(a + b == 2020):
			print(str(a) + ":" + str(b) + " -> " + str(a * b))