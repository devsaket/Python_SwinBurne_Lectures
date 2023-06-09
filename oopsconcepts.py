# oops Concept : object oriented paradigms (Concepts)

# Object - Real life objects 
#                  |
#      |----------------------------------------|
#  (physical property)state            functional (behaviour)
#    data members                       member functions
#      variables                            functions/ definitions

#############  CONCEPT OF CLASS
# class = blueprint of a real life object
# object = instance of a class


# class Bottle:
#     def __init__(self,h,r,c):
#         # default variable declaration
#         self.height = h
#         self.radius = r
#         self.color = c

#     def getHeight(self):
#         return self.height

#     def getRadius(self):
#         return self.radius
        
#     def getColor(self):
#         return self.color

#     def volume(self):
#         return 3.14 * self.getHeight() * self.getRadius() **2

#     def getdetails(self):
#         return f"Height = {self.getHeight()}, Radius = {self.getRadius() }, color= {self.getColor()}"

    

# def inputdetails():
#     a = int(input("Enter height of bottle = "))
#     b = int(input("Enter radius of bottle = "))
#     c = input("Enter color of bottle = ")
#     return a,b,c

# def main():
#     p,q,r  = inputdetails()
#     coke = Bottle(p,q,r)
#     print(coke.getdetails())
#     print(coke.volume())

#     print("-"*10)
#     p,q,r  = inputdetails()
#     pepsi = Bottle(p,q,r)
#     print(pepsi.getdetails())
#     print(pepsi.volume())


# # main() validator
# if __name__ == '__main__':
#     main()





class Rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def perimeter(self):
        return 2*(self.length+self.width)

    def area(self):
        return self.length * self.width


r = Rectangle(4,5)
print(r.perimeter())

