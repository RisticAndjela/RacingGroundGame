class Bump:
    def __init__(self,dot,road):
        self.height=50
        self.width=5
        self.x=dot.x * road.x /250
        self.y=dot.y * road.y /600
        self.madeOf=dot
        self.color=(100,0,0)