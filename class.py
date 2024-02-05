
class Car:
    def __init__(self, brand, tank_capacity, tank_current_capacity, current_gear, current_consumption, current_speed):
        self.brand = brand
        self.tank_capacity = tank_capacity
        self.tank_current_capacity = tank_current_capacity
        self.current_gear = current_gear
        self.current_consumption = current_consumption
        self.current_speed = current_speed


    def drive(self, distance):

        def status():
            print(
                "You are currently driving towards a destination. Your shifted gear is " + str(self.current_gear) +
                ", which makes your fuel consumption " + str(self.current_consumption) + " litres/km. On your current "
                "fuel capacity you will drive " + str(distance - remaining_distance) + " kilometers, and there will remain " +
                str(remaining_distance) + " kilometers to go.")

        i = int(input("Set here a designated gear."))
        self.shift_gear_up(i)
        remaining_distance = distance - self.tank_current_capacity / self.current_gear
        self.tank_current_capacity = 0
        status()

        while remaining_distance > 0:
            if self.tank_current_capacity == 0:
                self.refill()
                self.drive(remaining_distance)
            print("You have arrived to your destination!")
            break


    def shift_gear_up(self, desired_gear):
        if desired_gear < self.current_gear:
            self.shift_gear_down(desired_gear)

        self.current_gear += 1
        self.current_consumption += 1
        self.current_speed += 1
        print("Shifted one gear up. Current shifted gear is " + str(self.current_gear) + ". Current consumption is "
              + str(self.current_consumption) + " litre(s) per km")
        while self.current_gear < desired_gear:
            self.shift_gear_up(desired_gear)
            if self.current_gear > 5:
                print("There are only five gears in a car!!!")
                desired_gear = 5
                self.current_gear = 5
                self.current_consumption = 5
                self.current_speed = 5
                print("Shifted to " + str(self.current_gear) + ".")

    def shift_gear_down(self, desired_gear):
        if desired_gear > self.current_gear:
            print("Your current shifted gear is lower!")

        self.current_gear -= 1
        self.current_consumption -= 1
        self.current_speed -= 1
        print("Shifted one gear down. Current shifted gear is " + str(self.current_gear) + "."
              " Current consumption is " + str(self.current_consumption) + " litre(s) per km")
        while self.current_gear > desired_gear:
            self.shift_gear_down(desired_gear)
            if self.current_gear < 0:
                print("You cannot shift below zero! Zero is now shifted.")
                desired_gear = 0
                self.current_gear = 0
                self.current_consumption = 0
                self.current_speed = 0
                print("Shifted to " + str(self.current_gear) + ".")



    def refill(self):
        print("Your gas tank is empty. Slowing down a car to a zero.")
        self.shift_gear_down(0)
        print("Filling tank to its maximal capacity now.")
        self.tank_current_capacity = self.tank_capacity


car1 = Car("Audi", 60, 30, 0, 0, 0)

car1.drive(200)
