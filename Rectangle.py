import random
from Dot import Dot
from Road import Road
class SmallerRectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        
        self.width = width
        self.height = height
        self.dots=[]

class RectangleWithDots:
    def __init__(self,road:Road, rect_width=800, rect_height=1000,difficulty=1):
        # Rectangle coordinates and dimensions
        self.original_road=road
        self.road_height=road.height
        self.road_y=road.y
        self.rect_x = 0
        self.rect_y = 0
        self.rect_width = rect_width
        self.rect_height = rect_height

        # Number of random dots
        self.num_dots = 20*difficulty
        self.dot_radius = 15

        # List to store dot positions
        self.dots = [Dot(random.randint(self.rect_x, self.rect_x + self.rect_width),
                      random.randint(self.rect_y, self.rect_y + self.rect_height),name=m)
                     for m in range(self.num_dots)]

    def smallerRectangles(self) -> list:
        num_sub_rectangles = 1000
        sub_rectangle_height = (self.rect_height // num_sub_rectangles)

        # List to store sub-rectangle instances
        smaller_rectangles = []

        for i in range(num_sub_rectangles):  
            x = self.rect_x 
            y = self.rect_y+ i * sub_rectangle_height
            width = self.rect_width
            height = sub_rectangle_height * (i+1) 

            small = SmallerRectangle(x, y, width, height)

            smaller_rectangles.append(small)
        
        
        for i in range(len(smaller_rectangles)):
            for dot in self.dots:
                if smaller_rectangles[i].y<dot.y<=smaller_rectangles[i].height:
                    for m in range(0,self.original_road.max_height+self.original_road.height):
                        if i+m<len(smaller_rectangles):
                            smaller_rectangles[i+m].dots.append(Dot(dot.x,m,name=dot.name,new=False))
                           
                        
        return smaller_rectangles
                

       
    
    
    
    
    
