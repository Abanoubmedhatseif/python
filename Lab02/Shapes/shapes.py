class Shape():
    def __init__(this, name, color):
        this.name = name
        this._color = color

    def get_color(this):
        return this._color

    def set_color(this, color):
        this._color = color
        
    def calculate_area(this):
        pass
    
class Circle(Shape):
    def calculate_area(this):
        print("this is circle area")
        
class Square(Shape):
    def calculate_area(this):
        print("this is square area")
        
class Rectangle(Shape):
    def __init__(this, color, length, width):
        super().__init__("Rectangle", color)
        this.length = length
        this.width = width
    
    def calculate_area(this):
        return  this.length*this.width
        


