import math
def circle_area(r) :
    area = math.pi * (r**2)
    return area
def circle_circumference(r):
    circumference = 2*math.pi*r
    return circumference

radius = int(input("Enter circle radius: "))
cArea = circle_area(radius)
cCircumFerence = circle_circumference(radius)
print("circle's circumference is %.2f"%cCircumFerence)
