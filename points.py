import math

#Stores list of points and the distance between any two points
class PointGrid:
	def __init__(self, points):
		self.point_list = [];
		for point in points:
			self.point_list.append((point[0],point[1]))
		self.dists = []
		for i in range(len(points)-1):
			self.dists.append([])
			for j in range(i+1, len(points)):
				x_diff = points[i][0] - points[j][0]
				y_diff = points[i][1] - points[j][1]
				dist = math.sqrt(math.pow(x_diff,2) + math.pow(y_diff,2))
				self.dists[i].append(dist)

	def pdist(self, p1, p2):
		print(p1)
		print(p2)
		if p1 < p2:
			return self.dists[p1][p2-p1-1]
		elif p1 > p2:
			return self.dists[p2][p1-p2-1]
		else:
			return 0
		
	def printRoutes(self):
		

p1 = PointGrid([(0,0),(0,12),(10,0),(10,12),(4,7)])
print(p1.pdist(1,2))
