class Rectangle:
# define constructor with attributes: length and width 
    def __init__(self, length , width):
        self.length = length
        self.width = width

# Create Perimeter method
    def Perimeter(self):
        return 2*(self.length + self.width)

# Create area method
    def Area(self):
        return self.length*self.width   

# create display method
    def display(self):
        print("The length of rectangle is: ", self.length)
        print("The width of rectangle is: ", self.width)
        print("The perimeter of rectangle is: ", self.Perimeter())
        print("The area of rectangle is: ", self.Area())

class Cuboid(Rectangle):
    def __init__(self, length, width , height):
        Rectangle.__init__(self, length, width)
        self.height = height

# define Volume method
    def volume(self):
        return self.length*self.width*self.height

myRectangle = Rectangle(7 , 5) #create Rectangle object
myRectangle.display()  #calling the method on the object
print("----------------------------------")
myCuboid = Cuboid(7 , 5 , 2) #create a Cuboid object
print("the volume of myCuboid is: " , myCuboid.volume())


##############################
class Book:
    def __init__(self , Title , Author , Price):
        self.Title    =  Title
        self.Author   =  Author
        self.Price    =  Price
    

    def view(self ):
        return ("Book Title: " , self.Title ,  "Book Author: " , self.Author, "Book Price: " , self.Price)
    

MyBook = Book("Python Crash Course" , "Eric Matthes" , "23 $")          
print( MyBook.view())


###############


from math import pi
class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def perimeter (self):
        return  2 * pi * self.r


    def area (self):
        return  pi * self.r**2
    

    # form of the cercle equation 
    def formEquation (self, x, y):
        return (x-self.a)**2 + (y-self.b)**2 - self.r**2
    
    # method to test if given point blong to the circle or not 
    def test_belong (self, x, y):
        if (self.formEquation (x, y) == 0):
            print ("the point: (", x, y, ") belongs to the circle C")
        else:
            print ("the point: (", x, y, ") does not belong to the circle C")

class Cylinder(Circle):
    def __init__(self, a,b,r,h):
        Circle.__init__(self, a,b,r)
        self.h = h

# define Volume method
    def volume(self):
        return self.area()*self.h

# Creating of an instance object
C = Circle (1,2,1)

print ("the perimeter of the circle C is:", C.perimeter() )
print ("the area of circle C is:", C.area())
# we test if the point(1,1) belong to the circle or not
C.test_belong(1,1) 
# The output is:
#the perimeter of the circle C is: 6.283185307179586
#the area of circle C is: 3.141592653589793
#the point: ( 1 1 ) belongs to the circle C

Cyl = Cylinder(1,2,1,5)
print ("the volume of cylinder is:", Cyl.volume())

################################

class BankAccount:
    # create the constuctor with parameters: accountNumber, name and balance 
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        
    # create Deposit() method
    def Deposit(self , d ):
        self.balance = self.balance + d
    
    # create Withdrawal method
    def Withdrawal(self , w):
        if(self.balance < w):
            print("impossible operation! Insufficient balance !")
        else:
            self.balance = self.balance - w
    # create bankFees() method
    def bankFees(self):
        self.balance = (95/100)*self.balance
        
    # create display() method
    def display(self):
        print("Account Number : " , self.accountNumber)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.balance , " $")
        
# Testing the code :
newAccount = BankAccount(2178514584, "Albert" , 2700)
# Creating Withdrawal Test
newAccount.Withdrawal(300)
# Create deposit test
newAccount.Deposit(200)
# Display account informations
newAccount.display()
