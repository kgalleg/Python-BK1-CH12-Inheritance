# Practice: Custom Colors and Sounds

# Define 5 of your favorite vehicles
# Move all common properties in your vehicles to a new Vehicle class.
# Create an instance of each vehicle.
# Define a different value for each vehicle's properties.
# Create a drive() method in the Vehicle class.
# Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").
# Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.
# Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."
# Make your vehicle instances perform all three behaviors.

#example
# class Dog(Animal):

#   def __init__(self, breed):
#     self.breed = breed

# 5 cars

class Vehicle:

  def __init__(self, color, door_num, owner, max_occupancy_num):
    self.color= color
    self.door_num = door_num
    self.owner = owner
    self.max_occupancy_num= max_occupancy_num

  def drive(self):
    print(f"vrooooooooooom")

  def turn(self, direction):
        print(f"The vehicle turns {direction}")

  def stop (self):
    print (f"vehicle stopped")


class Tesla(Vehicle):
    def __init__(self):
        self.battery = ""

    def drive(self):
        # print(f"The Tesla makes this sounds keeeeeeeee")

        print(f"The {self.color} Tesla makes this sounds keeeeeeeee")

    def turn(self, direction):
        print(f"The Tesla turns {direction}")


class Rav4(Vehicle):
    def __init__(self):
        self.fuel=""

    def drive(self):
        print(f"The {self.color} Rav4 makes this sounds buuuuuuuuuu")

    def turn(self, direction):
        print(f"The Rav4 turns {direction}")

class Jeep(Vehicle):
    def __init__(self):
        self.speed = "very fast"

    def drive(self):
        print(f"The {self.color} Jeep makes this sounds hahaha")

    def turn(self, direction):
        print(f"The Jeep turns {direction}")


class Mustang(Vehicle):
    def __init__(self):
        self.trunk_size = "45 inches"

    def drive(self):
        print(f"The {self.color} Mustang makes this sounds hohohohoho")

    def turn(self, direction):
        print(f"The Mustang turns {direction}")


class BMW(Vehicle):
    def __init__(self):
        self.loved="everyone loves it"

    def drive(self):
        print(f"The {self.color} BMW makes this sounds siiiiiii")

    def turn(self, direction):
        print(f"The BMW turns {direction}")


electric_car = Tesla()
suv = Rav4()
green_suv= Jeep()
sporty_car = Mustang()
cool_car = BMW()

electric_car.color = "blue"
suv.color = "red"
green_suv.color = "purple"
sporty_car.color = "hot pink"
cool_car.color = "yellow"

electric_car.drive()
suv.drive()
green_suv.drive()
sporty_car.drive()
cool_car.drive()

electric_car.turn("right")
suv.turn("right")
green_suv.turn("right")
sporty_car.turn("right")
cool_car.turn("right")








