"""import math

from check import print_rectangle_properties

class Rectangle:
    pass
    # TODO: Add code here

def main():
    pass
    # TODO: Add code here

if __name__ == "__main__":
    main()"""
#########################################################

import math
from check import print_rectangle_properties

class Rectangle:
    def __init__(self, width, height):
        self.width = float(width)  # Set the width property of the rectangle
        self.height = float(height)  # Set the height property of the rectangle
    
    def get_area(self):
        return self.width * self.height  # Calculate and return the area of the rectangle
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)  # Calculate and return the perimeter of the rectangle
    
    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)  # Calculate and return the diagonal of the rectangle
    
    def get_width(self):
        return self.width  # Return the width of the rectangle
    
    def get_height(self):
        return self.height  # Return the height of the rectangle

def main():
    rectangle1 = Rectangle(9.0, 12.0)  # Create a Rectangle object with width 9.0 and height 12.0
    print_rectangle_properties(rectangle1)  # Print the properties of rectangle1
    
    print()
    
    rectangle2 = Rectangle(17.0, 13.0)  # Create another Rectangle object with width 17.0 and height 13.0
    print_rectangle_properties(rectangle2)  # Print the properties of rectangle2

if __name__ == "__main__":
    main()
