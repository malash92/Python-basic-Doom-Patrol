#1 Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

#2 Create a child class Bus that will inherit all the variables and methods of the Vehicle class and will have seating_capacity own method

class Bus(Vehicle):
    def __init__(self, max_speed, miliage, seating_capacity):
        Vehicle.__init__(self, max_speed ,miliage)
        self.seating_capacity = seating_capacity

#3 Determine which class a given Bus object belongs to (Check type of an object) ??????????????????

bus_11 = Bus(100, 200, 30)

print(type(bus_11))

#4 Create an instance of Bus named school_bus and determine if school_bus is also an instance of the Vehicle class

school_bus = Bus(90, 100, 30)

print(isinstance(school_bus, Vehicle))

#5  Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.nember_of_students = number_of_students

#6 Create a new class SchoolBus that will inherit all the methods from School and Bus and will have its own - bus_school_color

class School_Bus(School, Bus):
    def __init__(self,  get_school,number_of_students, max_speed, miliage, seating_capacity, bus_school_colour):
        School.__init__(self, get_school, number_of_students)
        Bus.__init__(max_speed, miliage, seating_capacity)
        self.bus_school_colour = bus_school_colour

#7 Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
#make a tuple of it and by using for call their action using the same method.
#Magic methods:

class Bear:
    def __init__(self, make_sound):
        self.make_sound = make_sound

    def pr_make_sound(self):
        print(f"I shout: {self.make_sound}")
class Wolf:
    def __init__(self, make_sound):
        self.make_sound = make_sound

    def pr_make_sound(self):
        print(f"I shout: {self.make_sound}")

bear = Bear(make_sound="rrr")
wolf = Wolf(make_sound="auu")

animals = (bear, wolf)

for animal in animals:
    animal.pr_make_sound()

