shapes = open("static_transit/shapes.txt")
i = 0
pointsx = []
pointsy = []
truelines = []
for lines in shapes:
	if i!=0:
		xtemp = lines.split(',')[2]
		ytemp = lines.split(',')[3]
		if  xtemp not in pointsx:
			if ytemp not in pointsy:
				pointsx.append(xtemp)
				pointsy.append(ytemp)
				truelines.append(lines)
	else:
		truelines.append(lines)	

	i=i+1
newfile = open("static_transit/newshapes.txt",'w+')
for line in truelines:
	newfile.write(line)
newfile.close()