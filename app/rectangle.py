
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def get_area(self):
        if self.width > 0 and self.height > 0:
            return self.width*self.height
        raise Exception("It contains negative value")
    
    def get_perimeter(self):
        if self.width > 0 and self.height > 0:
            return (self.width+self.height)*2
        raise Exception("It contains negative value")