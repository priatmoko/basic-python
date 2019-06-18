class  Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print("This message is  inside the class")

point = Point(10, 20)
point.draw()      
point.x = 1000  
print(point.x)        