#Define the area of a circle (radius squared x Pi)
def circle(radius):
	area_circle = (radius * radius) * 3.14
	print(area_circle)
	pass


def circle2(radius):
	area = (radius **2) * 3.14
	print(area)
	#return area #return doesn't work
	pass

#Define the area of a rectangle (width * height)
def rectangle(width,height):
	area = width * height
	print(area)
	#return area #return doesn't work

circle(2)
circle2(4)
rectangle(4,5)