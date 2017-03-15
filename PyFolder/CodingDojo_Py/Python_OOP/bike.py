class Bike (object):
    def __init__(self):
        self.price = '$15'
        self.max_speed = '32 mph'
        self.miles = 0

    def display_info(self):
        price = self.price
        max_speed = self.max_speed
        print price
        print max_speed
        #have this method display the bike's price, maximum speed, and the total miles.
    def ride(self, times):
        print "riding..."
        self.formiles = times * 10
        print self.formiles
         #have it display "Riding" on the screen and increase the total miles ridden by 10
    def reverse(self, times):
        print "reversing..."
        if self.miles > 0:
            self.revmiles = self.miles - 5
            print self.revmiles
        #have it display "Reversing" on the screen and decrease the total miles ridden by 5...

#Have the first instance ride three times, reverse once and have it displayInfo().
rb = Bike()
rb.ride(3)
rb.reverse(1)
rb.display_info()
#Have the second instance ride twice, reverse twice and have it displayInfo().
blueb = Bike()
blueb.ride(2)
blueb.reverse(2)
blueb.price = '$44'
blueb.max_speed ='28mph'
blueb.display_info()
#Have the third instance reverse three times and displayInfo().
yellowb = Bike()
yellowb.reverse(3)
yellowb.display_info()
#What would you do to prevent the instance from having negative miles?
