"""
Python Class Example - Car Class
This file demonstrates a comprehensive example of a Python class with various features.
"""


class Car:
    """
    A class representing a car with basic functionality.
    
    This class demonstrates:
    - Constructor with parameters
    - Instance variables and methods
    - Class variables
    - Special methods
    - Data validation
    """
    
    # Class variables (shared by all instances)
    wheels = 4
    fuel_types = ["Gasoline", "Diesel", "Electric", "Hybrid"]
    
    def __init__(self, make, model, year, color, fuel_type="Gasoline"):
        """
        Initialize a new Car instance.
        
        Args:
            make (str): The manufacturer of the car
            model (str): The model of the car
            year (int): The year the car was made
            color (str): The color of the car
            fuel_type (str): The type of fuel (default: "Gasoline")
        """
        # Input validation
        if not isinstance(year, int) or year < 1900 or year > 2030:
            raise ValueError("Year must be an integer between 1900 and 2030")
        
        if fuel_type not in self.fuel_types:
            raise ValueError(f"Fuel type must be one of: {', '.join(self.fuel_types)}")
        
        # Instance variables (unique to each object)
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type
        self.is_running = False
        self.speed = 0
        self.odometer = 0  # Miles driven
        self.fuel_level = 100  # Percentage
    
    def start_engine(self):
        """Start the car's engine."""
        if self.fuel_level <= 0:
            print(f"Cannot start {self.make} {self.model} - no fuel!")
            return False
        
        self.is_running = True
        print(f"The {self.year} {self.make} {self.model} engine is now running!")
        return True
    
    def stop_engine(self):
        """Stop the car's engine."""
        self.is_running = False
        self.speed = 0
        print(f"The {self.make} {self.model} engine has been turned off.")
    
    def accelerate(self, amount):
        """
        Increase the car's speed.
        
        Args:
            amount (int): Speed increase in mph
        """
        if not self.is_running:
            print("Can't accelerate - engine is not running!")
            return
        
        if self.fuel_level <= 0:
            print("Can't accelerate - no fuel!")
            self.stop_engine()
            return
        
        # Limit maximum speed
        max_speed = 120
        new_speed = min(self.speed + amount, max_speed)
        
        if new_speed == max_speed and self.speed < max_speed:
            print(f"Maximum speed of {max_speed} mph reached!")
        
        self.speed = new_speed
        self.fuel_level -= amount * 0.1  # Consume fuel based on acceleration
        self.fuel_level = max(0, self.fuel_level)  # Don't go below 0
        
        print(f"Accelerating! Current speed: {self.speed} mph (Fuel: {self.fuel_level:.1f}%)")
    
    def brake(self, amount):
        """
        Decrease the car's speed.
        
        Args:
            amount (int): Speed decrease in mph
        """
        self.speed = max(0, self.speed - amount)
        print(f"Braking! Current speed: {self.speed} mph")
    
    def drive(self, miles):
        """
        Drive the car for a specified distance.
        
        Args:
            miles (float): Distance to drive in miles
        """
        if not self.is_running:
            print("Can't drive - engine is not running!")
            return
        
        if self.fuel_level <= 0:
            print("Can't drive - no fuel!")
            return
        
        # Calculate fuel consumption (simplified)
        fuel_consumption = miles * 0.5  # 0.5% per mile
        
        if fuel_consumption > self.fuel_level:
            max_distance = self.fuel_level / 0.5
            print(f"Not enough fuel! Can only drive {max_distance:.1f} miles.")
            miles = max_distance
            fuel_consumption = self.fuel_level
        
        self.odometer += miles
        self.fuel_level -= fuel_consumption
        self.fuel_level = max(0, self.fuel_level)
        
        print(f"Drove {miles:.1f} miles. Total odometer: {self.odometer:.1f} miles")
        print(f"Fuel remaining: {self.fuel_level:.1f}%")
        
        if self.fuel_level <= 0:
            print("Out of fuel! Engine stopped.")
            self.stop_engine()
    
    def refuel(self, amount=100):
        """
        Refuel the car.
        
        Args:
            amount (float): Percentage to refuel (default: 100 for full tank)
        """
        old_level = self.fuel_level
        self.fuel_level = min(100, self.fuel_level + amount)
        added = self.fuel_level - old_level
        print(f"Refueled! Added {added:.1f}% fuel. Tank is now {self.fuel_level:.1f}% full.")
    
    def get_info(self):
        """Return detailed information about the car."""
        status = "Running" if self.is_running else "Stopped"
        return (f"{self.year} {self.make} {self.model} ({self.color})\n"
                f"Fuel Type: {self.fuel_type}\n"
                f"Status: {status}\n"
                f"Speed: {self.speed} mph\n"
                f"Odometer: {self.odometer:.1f} miles\n"
                f"Fuel Level: {self.fuel_level:.1f}%")
    
    def honk(self):
        """Make the car honk."""
        print(f"The {self.make} {self.model} says: BEEP BEEP!")
    
    # Special methods (dunder methods)
    def __str__(self):
        """String representation for end users."""
        return f"{self.year} {self.color} {self.make} {self.model}"
    
    def __repr__(self):
        """String representation for developers."""
        return (f"Car(make='{self.make}', model='{self.model}', "
                f"year={self.year}, color='{self.color}', fuel_type='{self.fuel_type}')")
    
    def __eq__(self, other):
        """Check if two cars are equal."""
        if not isinstance(other, Car):
            return False
        return (self.make == other.make and 
                self.model == other.model and 
                self.year == other.year)
    
    @classmethod
    def create_electric_car(cls, make, model, year, color):
        """Class method to create an electric car."""
        return cls(make, model, year, color, fuel_type="Electric")
    
    @staticmethod
    def compare_years(car1, car2):
        """Static method to compare the years of two cars."""
        return car1.year - car2.year


# Demonstration of the Car class
def main():
    """Demonstrate the Car class functionality."""
    print("=" * 50)
    print("PYTHON CAR CLASS DEMONSTRATION")
    print("=" * 50)
    
    # Creating car objects
    print("\n1. Creating Cars:")
    print("-" * 20)
    
    try:
        car1 = Car("Toyota", "Camry", 2022, "Blue", "Hybrid")
        car2 = Car("Honda", "Civic", 2021, "Red")
        car3 = Car.create_electric_car("Tesla", "Model 3", 2023, "White")
        
        print(f"Car 1: {car1}")
        print(f"Car 2: {car2}")
        print(f"Car 3: {car3}")
        
    except ValueError as e:
        print(f"Error creating car: {e}")
    
    print(f"\nAll cars have {Car.wheels} wheels")
    print(f"Available fuel types: {', '.join(Car.fuel_types)}")
    
    # Using car methods
    print("\n2. Car Operations:")
    print("-" * 20)
    
    # Start and drive car1
    car1.start_engine()
    car1.accelerate(30)
    car1.accelerate(20)
    car1.drive(50)
    car1.brake(15)
    car1.honk()
    
    print(f"\nCar 1 Info:\n{car1.get_info()}")
    
    # Try to use car2 without starting
    print(f"\n{car2} operations:")
    car2.accelerate(25)  # Should fail - engine not running
    car2.start_engine()
    car2.accelerate(40)
    car2.drive(100)
    
    # Refuel and continue
    car2.refuel(50)
    car2.drive(25)
    car2.stop_engine()
    
    print(f"\nCar 2 Info:\n{car2.get_info()}")
    
    # Demonstrate comparison
    print("\n3. Car Comparisons:")
    print("-" * 20)
    
    car4 = Car("Toyota", "Camry", 2022, "Silver", "Hybrid")
    print(f"Car 1 == Car 4: {car1 == car4}")  # Same make/model/year
    print(f"Car 1 == Car 2: {car1 == car2}")  # Different cars
    
    year_diff = Car.compare_years(car1, car2)
    print(f"Car 1 is {year_diff} year(s) newer than Car 2")
    
    # Demonstrate repr
    print(f"\nDeveloper representation of Car 3: {repr(car3)}")
    
    print("\n" + "=" * 50)
    print("DEMONSTRATION COMPLETE")
    print("=" * 50)


# Run the demonstration if this file is executed directly
if __name__ == "__main__":
    main()
