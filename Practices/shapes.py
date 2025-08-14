class Shape:
	width = 5
	height = 5
	printChar = '*'

	def printRow(self, i):
		raise NotImplementedError("Will be implemented by children extending this class")

	def print(self):
		for i in range(self.height):
			self.printRow(i)


class Square(Shape):
	def printRow(self, i):
		print(self.printChar * self.width)

class Triangle(Shape):
    def printRow(self, i):
       # print(i)
        print(self.printChar * (i + 1))

class Triangle1(Shape):
    height = 5
    width = 2 * height
    def printRow(self, i):
       # print('i',i)
        triangleWidth = i* 2 + 1
       # print('triangleWidth',triangleWidth)
       # print (self.width - triangleWidth)
       # print((self.width - triangleWidth)/2)
        padding = int( (self.width - triangleWidth) / 2 )
        #print('padding',padding)
        print( '' *padding  + self.printChar * triangleWidth )



# Test
print("Square:")
square = Square()
square.print()

print("\nTriangle:")
triangle = Triangle()
triangle.print()

print("\nTriangle1:")
triangle1 = Triangle1()
triangle1.print()

