file = open("res/expense report", 'r')
lines = file.readlines()

for a in lines:
	for b in lines:
		for c in lines:
			a = int(a)
			b = int(b)
			c = int(c)
			if(a == b | b == c | a == c):
				continue
			if(a + b + c == 2020):
				print(str(a) + ":" + str(b) + ":" + str(c) + " -> " + str(a * b * c))