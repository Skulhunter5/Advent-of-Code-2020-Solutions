# There is no solution yet

import re

with open("regulations", 'r') as file:
	lines = file.readlines()

graph = {}

for i in lines:
	color_primary = re.match('(.+?) bags', i).group(1)
	color_inside = re.findall('(\d+) (.+?) bag', i)
	if(len(color_inside) > 0):
		color_inside = list(list(zip(*color_inside))[1])
		graph[color_primary] = color_inside

colors = {}

def check(color):
	for j in graph[i]:
		if(j in colors):
			if(colors[j]):
				colors[i] = True
				continue
		else:
			check(j)
			if(colors[j]):
				colors[i] = True
				continue
	colors[i] = False

for i in graph:
	if(i in colors):
		continue
	check(i)

total = 0
for i in colors:
	if(colors[i]):
		total += 1
print(total)