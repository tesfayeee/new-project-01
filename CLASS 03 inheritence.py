class shape: # it doesnot have any  attributes 
    def  area(): #it s avoid / placeholder/empty method [ creared to make the overrideing purpose ]
        pass
#   the first subclas inheritis from shape class 

class Circle(shape):

    def __init__(self,radius):
        self.radius = radius   #assigned the value of lenth radius parametrieas to the self.radius atributes
        # override the parent Method
    def area(self):
        return 3.14 * self.radius * self.radius 
    
# the 2nd subclass inheritence from the shape class
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        # override the parent Method
    def area (self): # culculate the area of rectangule
            return self.length * self.width
    

def calculate_area(shape): #accept object as parameters
 return shape.area()
Circle_Pobject = Circle(15)
Rectangle_objects = rectangle(28,15)

print("------------circle area-------------")

print(calculate_area(Circle_Pobject))

print("------------circle area-------------")

print(calculate_area(Rectangle_objects))





#YAADANNOO KOO (CODE ERRORS  "ai"checker)



# class shape: 
#     def area(self):  # Add 'self' for instance method
#         pass  # Placholder for overriding

# class Circle(shape):    
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):  # Add 'self' for instance method
#         return 3.14 * self.radius * self.radius 

# class Rectangle(shape):  # Move Rectangle class out of Circle
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):  # Add 'self' for instance method
#         return self.length * self.width

# def calculate_area(shape):  # Accept object as parameter
#     return shape.area()

# # Create objects of Circle and Rectangle
# circle_object = Circle(15)
# rectangle_object = Rectangle(28, 15)

# # Print results
# print("------------ Circle Area -------------")
# print(calculate_area(circle_object))

# print("------------ Rectangle Area -------------")
# print(calculate_area(rectangle_object))