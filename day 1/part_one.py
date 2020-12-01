file = open("res/expense report", 'r')
lines = file.readlines()

for a in lines:
	for b in lines:
		a = int(a)
		b = int(b)
		if(a == b):
			continue
		if(a + b == 2020):
			print(str(a) + ":" + str(b) + " -> " + str(a * b))