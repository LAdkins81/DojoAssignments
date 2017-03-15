#specify the following attributes: price, speed, fuel, mileage.
# If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.
class Car (object):
    def __init__(self, price, speed, fuel, mileage, tax=0.12):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax

# Create six different instances of the class Car.
# In the class have a method called display_all() that returns all the information about the car as a string.
# In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.
    def display_all(self):
        if self.price > 10000:
            self.tax = "0.15"
        print "Price: ", self.price
        print "Speed: ", self.speed
        print "Fuel: ", self.fuel
        print "Mileage: ", self.mileage
        print "Tax: ", self.tax

firstcar = Car(2000, "55mph", "Full", "22mpg")
firstcar.display_all()

seccar = Car(15000, "75mph", "Half Full", "30mpg")
seccar.display_all()

thircar = Car(150000, "45mph", "Empty", "40mpg")
thircar.display_all()

fourcar = Car(6000, "100mph", "Mostly Full", "25mpg")
fourcar.display_all()

fifthcar = Car(3000, "15mph", "Mostly Empty", "35mpg")
fifthcar.display_all()

sixthcar = Car(60000, "80mph", "Empty", "50mpg")
sixthcar.display_all()
