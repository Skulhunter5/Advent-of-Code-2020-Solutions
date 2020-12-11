with open("data", 'r') as file:
	nums = list(map(int, file.readlines()))

i = 25
while(i < len(nums)):
	done = False
	for j in range(i):
		for k in range(i):
			if(nums[j] == nums[k]):
				continue
			if(nums[j] + nums[k] == nums[i]):
				done = True
				break
		if(done):
			break
	if(not done):
		print(nums[i])
		break
	i += 1