class Bike (object):
    def __init__(self, price, max_speed, miles=0):
        self.price = "$15"
        self.max_speed = "25mph"
        self.miles = miles

    def display_info(self):
        print "Price: ", self.price
        print "Speed: ", self.max_speed
        #have this method display the bike's price, maximum speed, and the total miles.
    def ride(self):
        print "riding..."
        self.miles * 10
        print self
         #have it display "Riding" on the screen and increase the total miles ridden by 10
    def reverse(self):
        print "reversing..."
        if self.miles > 0:
            self.miles - 5
            print self
        #have it display "Reversing" on the screen and decrease the total miles ridden by 5...

#Have the first instance ride three times, reverse once and have it displayInfo().
rb = Bike('$15', "25mph")
rb.ride().ride().ride().reverse().display_info()
#Have the second instance ride twice, reverse twice and have it displayInfo().
blueb = Bike()
blueb.price = '$44'
blueb.max_speed ='28mph'
blueb.ride().ride.reverse().display_info()
#Have the third instance reverse three times and displayInfo().
yellowb = Bike()
yellowb.reverse().reverse().reverse().display_info()
#What would you do to prevent the instance from having negative miles?
