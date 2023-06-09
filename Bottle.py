class Bottle:
    def __init__(self,h,r,c):
        # default variable declaration
        self.height = h
        self.radius = r
        self.color = c

    def getHeight(self):
        return self.height

    def getRadius(self):
        return self.radius
        
    def getColor(self):
        return self.color

    def volume(self):
        return 3.14 * self.getHeight() * self.getRadius() **2

    def getdetails(self):
        return f"Height = {self.getHeight()}, Radius = {self.getRadius() }, color= {self.getColor()}"


class PlasticBottle(Bottle):
    def __init__(self,hei,rad,col,m,c):
        super().__init__(hei,rad,col)
        self.material = m
        self.cost = c

    def getMaterial(self):
        return self.material

    def area(self):
        s = 3.14 * super().getHeight() * super().getRadius()**2
        p= s*self.cost

        if p>300:
            p = p + p*0.15
            return p

        return p

    def printdetails(self):
        # return f"Height = {super().getHeight()}, Radius = {super().getRadius() }, color= {super().getColor()}, material = {self.getMaterial()}"
        return f"{super().getdetails()}, Material = {self.getMaterial()}"
    


def inputdetails():
    a = float(input("Enter height of bottle = "))
    b = float(input("Enter radius of bottle = "))
    c = input("Enter color of bottle = ")
    d = input("Enter material of bottle = ")
    e = float(input("Enter cost of bottle(per cm^2) = "))
    return a,b,c,d,e


def main():
    m,n,o,p,q = inputdetails()
    pb = PlasticBottle(m,n,o,p,q)
    print(pb.printdetails())
    print(pb.volume())
    print("Radius = ",pb.getRadius())
    print("Cost = ",pb.area())


if __name__ == '__main__':
    main()