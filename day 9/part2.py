with open("data", 'r') as file:
	nums = list(map(int, file.readlines()))

goal = 248131121

i = 0
while(i < len(nums)):
	currentTotal = 0
	j = 0
	while(currentTotal < goal):
		currentTotal += nums[i + j]
		j += 1
	if(j == 1):
		continue
	if(currentTotal == goal):
		j -= 1
		largest = 0
		smallest = 100000 * 100000
		for k in range(j + 1):
			idx = i + k
			if(nums[idx] > largest):
				largest = nums[idx]
			elif(nums[idx] < smallest):
				smallest = nums[idx]
		print(smallest + largest)
		break
	i += 1