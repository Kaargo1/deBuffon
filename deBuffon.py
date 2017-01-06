import math, random

class Needle:
	def __init__(self, length, pos, angle):
		self.length = length
		#central position of needle
		self.pos = pos
		self.angle = angle
		#end points of needle
		self.a = [0, 0]
		self.b = [0, 0]
		#calculats end points of needle
		self.a[0] = self.pos[0] + (self.length/2)*math.cos(self.angle)
		self.a[1] = self.pos[1] + (self.length/2)*math.sin(math.radians(self.angle))
		self.b[0] = self.pos[0] - (self.length/2)*math.cos(self.angle)
		self.b[1] = self.a[1] - self.length*math.sin(math.radians(self.angle))


needles = []

boardWidth = 21
boardHeight = 30

def calculate():

	for i in range(16):
		needles.append(Needle(6.5, [random.uniform(0, boardWidth), random.uniform(0, boardHeight)], random.randrange(180)))
	lines = [29.7-needles[0].length*x for x in range(7)]
	t = 0
	for needle in needles:
		for line in lines:
			if needle.b[1] <= line <= needle.a[1]:
				t += 1
	
	return (len(needles)*2)/t


listOfTests = []
testedTests = []
for j in range(100):
	for i in range(100):
		listOfTests.append(calculate())
	#average
	testedTests.append(sum(listOfTests)/len(listOfTests))

#prints average of all previous averages
print(sum(testedTests)/len(testedTests))
