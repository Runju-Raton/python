"""
Inheritance in Python - Comprehensive Examples
=============================================

This file demonstrates inheritance concepts with practical examples:
- Single, multiple, multilevel, and hierarchical inheritance
- Method overriding and super() usage
- Method Resolution Order (MRO)
- Abstract base classes with inheritance
- Real-world inheritance scenarios
- Composition vs Inheritance examples
"""


# =============================================================================
# 1. SINGLE INHERITANCE - ANIMAL HIERARCHY
# =============================================================================

class Animal:
    """Base class representing all animals."""
    
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.energy = 100
        print(f"🐾 Animal created: {name} ({species})")
    
    def eat(self, food):
        """Basic eating behavior for all animals."""
        self.energy = min(100, self.energy + 20)
        print(f"🍽️ {self.name} ate {food}. Energy: {self.energy}")
    
    def sleep(self):
        """Basic sleeping behavior for all animals."""
        self.energy = min(100, self.energy + 30)
        print(f"😴 {self.name} is sleeping. Energy restored to: {self.energy}")
    
    def make_sound(self):
        """Generic sound - will be overridden by child classes."""
        return "Some animal sound"
    
    def get_info(self):
        """Get basic information about the animal."""
        return f"{self.name} is a {self.age}-year-old {self.species}"
    
    def __str__(self):
        return f"{self.name} ({self.species})"


class Dog(Animal):
    """Dog class inheriting from Animal."""
    
    def __init__(self, name, breed, age):
        # Call parent constructor
        super().__init__(name, "Dog", age)
        self.breed = breed
        self.loyalty = 100
        self.is_trained = False
    
    def make_sound(self):
        """Override parent method with dog-specific sound."""
        return "Woof! Woof!"
    
    def bark(self):
        """Dog-specific method."""
        sound = self.make_sound()
        print(f"🐕 {self.name} barks: {sound}")
        return sound
    
    def fetch(self, item):
        """Dog-specific behavior."""
        if self.energy < 20:
            print(f"🐕 {self.name} is too tired to fetch")
            return False
        
        self.energy -= 15
        print(f"🎾 {self.name} fetches the {item}!")
        return True
    
    def train(self, command):
        """Train the dog with a new command."""
        print(f"📚 Training {self.name} to {command}...")
        self.is_trained = True
        print(f"✅ {self.name} learned to {command}!")
    
    def get_info(self):
        """Override parent method with additional dog information."""
        base_info = super().get_info()  # Call parent method
        return f"{base_info} ({self.breed} breed, Loyalty: {self.loyalty}%)"


class Cat(Animal):
    """Cat class inheriting from Animal."""
    
    def __init__(self, name, color, age):
        super().__init__(name, "Cat", age)
        self.color = color
        self.independence = 80
        self.lives_remaining = 9
    
    def make_sound(self):
        """Override parent method with cat-specific sound."""
        return "Meow!"
    
    def meow(self):
        """Cat-specific method."""
        sound = self.make_sound()
        print(f"🐱 {self.name} meows: {sound}")
        return sound
    
    def climb(self, location):
        """Cat-specific behavior."""
        if self.energy < 10:
            print(f"🐱 {self.name} is too tired to climb")
            return False
        
        self.energy -= 10
        print(f"🌳 {self.name} climbs the {location}")
        return True
    
    def hunt(self, prey):
        """Cat-specific hunting behavior."""
        if self.energy < 25:
            print(f"🐱 {self.name} is too tired to hunt")
            return False
        
        self.energy -= 20
        print(f"🏹 {self.name} hunts {prey}")
        return True
    
    def get_info(self):
        """Override with cat-specific information."""
        base_info = super().get_info()
        return f"{base_info} ({self.color} colored, {self.lives_remaining} lives left)"


# =============================================================================
# 2. MULTILEVEL INHERITANCE - VEHICLE HIERARCHY
# =============================================================================

class Vehicle:
    """Base vehicle class."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
        self.fuel_level = 50
        print(f"🚗 Vehicle created: {year} {make} {model}")
    
    def start(self):
        """Start the vehicle."""
        self.is_running = True
        print(f"✅ {self.make} {self.model} started")
    
    def stop(self):
        """Stop the vehicle."""
        self.is_running = False
        print(f"⛔ {self.make} {self.model} stopped")
    
    def refuel(self, amount):
        """Refuel the vehicle."""
        self.fuel_level = min(100, self.fuel_level + amount)
        print(f"⛽ Refueled. Fuel level: {self.fuel_level}%")
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class MotorVehicle(Vehicle):
    """Motor vehicle - inherits from Vehicle."""
    
    def __init__(self, make, model, year, engine_type):
        super().__init__(make, model, year)
        self.engine_type = engine_type
        self.odometer = 0
    
    def drive(self, distance):
        """Drive the motor vehicle."""
        if not self.is_running:
            print(f"❌ Cannot drive. {self.make} {self.model} is not running.")
            return False
        
        if self.fuel_level < 10:
            print(f"❌ Not enough fuel to drive")
            return False
        
        self.odometer += distance
        fuel_consumed = distance * 0.1  # Simplified fuel consumption
        self.fuel_level = max(0, self.fuel_level - fuel_consumed)
        
        print(f"🛣️ Drove {distance} miles. Odometer: {self.odometer} miles")
        print(f"   Fuel remaining: {self.fuel_level:.1f}%")
        return True
    
    def get_engine_info(self):
        """Get engine information."""
        return f"{self.engine_type} engine"


class Car(MotorVehicle):
    """Car - inherits from MotorVehicle (multilevel inheritance)."""
    
    def __init__(self, make, model, year, engine_type, doors):
        super().__init__(make, model, year, engine_type)
        self.doors = doors
        self.passengers = 0
        self.max_passengers = 5 if doors == 4 else 2
    
    def add_passenger(self, count=1):
        """Add passengers to the car."""
        if self.passengers + count <= self.max_passengers:
            self.passengers += count
            print(f"👥 Added {count} passenger(s). Total: {self.passengers}")
            return True
        else:
            print(f"❌ Cannot add {count} passengers. Max capacity: {self.max_passengers}")
            return False
    
    def remove_passenger(self, count=1):
        """Remove passengers from the car."""
        if self.passengers >= count:
            self.passengers -= count
            print(f"👋 Removed {count} passenger(s). Total: {self.passengers}")
            return True
        else:
            print(f"❌ Cannot remove {count} passengers. Current: {self.passengers}")
            return False
    
    def honk(self):
        """Car-specific method."""
        print(f"📯 {self.make} {self.model} honks: BEEP BEEP!")
    
    def get_info(self):
        """Get comprehensive car information."""
        return (f"{super().__str__()} - {self.doors}-door car\n"
                f"   Engine: {self.get_engine_info()}\n"
                f"   Passengers: {self.passengers}/{self.max_passengers}\n"
                f"   Odometer: {self.odometer} miles\n"
                f"   Fuel: {self.fuel_level:.1f}%")


class Truck(MotorVehicle):
    """Truck - inherits from MotorVehicle."""
    
    def __init__(self, make, model, year, engine_type, cargo_capacity):
        super().__init__(make, model, year, engine_type)
        self.cargo_capacity = cargo_capacity
        self.current_cargo = 0
    
    def load_cargo(self, weight):
        """Load cargo into the truck."""
        if self.current_cargo + weight <= self.cargo_capacity:
            self.current_cargo += weight
            print(f"📦 Loaded {weight} lbs. Total cargo: {self.current_cargo} lbs")
            return True
        else:
            print(f"❌ Cannot load {weight} lbs. Capacity: {self.cargo_capacity} lbs")
            return False
    
    def unload_cargo(self, weight):
        """Unload cargo from the truck."""
        if self.current_cargo >= weight:
            self.current_cargo -= weight
            print(f"📤 Unloaded {weight} lbs. Remaining cargo: {self.current_cargo} lbs")
            return True
        else:
            print(f"❌ Cannot unload {weight} lbs. Current cargo: {self.current_cargo} lbs")
            return False
    
    def get_info(self):
        """Get comprehensive truck information."""
        return (f"{super().__str__()} - Truck\n"
                f"   Engine: {self.get_engine_info()}\n"
                f"   Cargo: {self.current_cargo}/{self.cargo_capacity} lbs\n"
                f"   Odometer: {self.odometer} miles\n"
                f"   Fuel: {self.fuel_level:.1f}%")


# =============================================================================
# 3. MULTIPLE INHERITANCE - MIXIN PATTERNS
# =============================================================================

class Flyable:
    """Mixin for objects that can fly."""
    
    def __init__(self):
        self.altitude = 0
        self.is_flying = False
    
    def take_off(self):
        """Take off into the air."""
        if not self.is_flying:
            self.is_flying = True
            self.altitude = 100
            print(f"✈️ Taking off! Altitude: {self.altitude} ft")
        else:
            print("❌ Already flying")
    
    def land(self):
        """Land on the ground."""
        if self.is_flying:
            self.is_flying = False
            self.altitude = 0
            print(f"🛬 Landing! Altitude: {self.altitude} ft")
        else:
            print("❌ Already on ground")
    
    def climb(self, feet):
        """Climb higher."""
        if self.is_flying:
            self.altitude += feet
            print(f"⬆️ Climbing! New altitude: {self.altitude} ft")
        else:
            print("❌ Cannot climb while on ground")


class Swimmable:
    """Mixin for objects that can swim."""
    
    def __init__(self):
        self.depth = 0
        self.is_swimming = False
    
    def dive(self, depth):
        """Dive underwater."""
        self.is_swimming = True
        self.depth = depth
        print(f"🏊 Diving! Depth: {self.depth} ft underwater")
    
    def surface(self):
        """Surface from underwater."""
        if self.is_swimming:
            self.depth = 0
            self.is_swimming = False
            print(f"🌊 Surfacing! Back at water surface")
        else:
            print("❌ Not currently swimming")
    
    def swim(self, distance):
        """Swim a distance."""
        print(f"🏊 Swimming {distance} meters")


class Bird(Animal, Flyable):
    """Bird class with multiple inheritance."""
    
    def __init__(self, name, species, age, wing_span):
        Animal.__init__(self, name, species, age)  # Initialize Animal
        Flyable.__init__(self)  # Initialize Flyable
        self.wing_span = wing_span
    
    def make_sound(self):
        """Override Animal's make_sound method."""
        return "Tweet! Chirp!"
    
    def flap_wings(self):
        """Bird-specific method."""
        print(f"🕊️ {self.name} flaps its wings ({self.wing_span} inch wingspan)")
    
    def get_info(self):
        """Override with bird-specific information."""
        base_info = super().get_info()
        flying_status = "flying" if self.is_flying else "on ground"
        return f"{base_info} (wingspan: {self.wing_span} inches, {flying_status})"


class Duck(Animal, Flyable, Swimmable):
    """Duck class demonstrating multiple inheritance from multiple sources."""
    
    def __init__(self, name, age, color):
        Animal.__init__(self, name, "Duck", age)
        Flyable.__init__(self)
        Swimmable.__init__(self)
        self.color = color
    
    def make_sound(self):
        """Override Animal's make_sound method."""
        return "Quack! Quack!"
    
    def quack(self):
        """Duck-specific method."""
        sound = self.make_sound()
        print(f"🦆 {self.name} quacks: {sound}")
    
    def paddle(self):
        """Duck-specific swimming method."""
        print(f"🦆 {self.name} paddles in the water")
    
    def get_info(self):
        """Get comprehensive duck information."""
        base_info = super().get_info()
        status = []
        if self.is_flying:
            status.append(f"flying at {self.altitude} ft")
        if self.is_swimming:
            status.append(f"swimming at {self.depth} ft depth")
        if not status:
            status.append("on land")
        
        return f"{base_info} ({self.color} colored, {', '.join(status)})"


# =============================================================================
# 4. HIERARCHICAL INHERITANCE - EMPLOYEE SYSTEM
# =============================================================================

class Employee:
    """Base employee class."""
    
    company_name = "TechCorp Inc."
    
    def __init__(self, name, employee_id, department, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.base_salary = base_salary
        self.years_of_service = 0
        print(f"👔 Employee hired: {name} (ID: {employee_id})")
    
    def work(self, hours):
        """Basic work method."""
        print(f"💼 {self.name} worked {hours} hours")
        return hours
    
    def get_annual_salary(self):
        """Calculate annual salary."""
        return self.base_salary
    
    def promote(self, salary_increase):
        """Promote employee with salary increase."""
        self.base_salary += salary_increase
        print(f"🎉 {self.name} promoted! New salary: ${self.base_salary:,}")
    
    def get_info(self):
        """Get employee information."""
        return (f"Employee: {self.name} (ID: {self.employee_id})\n"
                f"Department: {self.department}\n"
                f"Base Salary: ${self.base_salary:,}\n"
                f"Years of Service: {self.years_of_service}")
    
    def __str__(self):
        return f"{self.name} ({self.employee_id}) - {self.department}"


class Developer(Employee):
    """Developer class inheriting from Employee."""
    
    def __init__(self, name, employee_id, base_salary, programming_languages):
        super().__init__(name, employee_id, "Development", base_salary)
        self.programming_languages = programming_languages
        self.projects_completed = 0
        self.bugs_fixed = 0
    
    def code(self, language, hours):
        """Developer-specific work method."""
        if language not in self.programming_languages:
            print(f"❌ {self.name} doesn't know {language}")
            return False
        
        self.work(hours)  # Call parent work method
        print(f"💻 {self.name} coded in {language} for {hours} hours")
        return True
    
    def fix_bug(self):
        """Fix a bug."""
        self.bugs_fixed += 1
        print(f"🐛 {self.name} fixed a bug! Total bugs fixed: {self.bugs_fixed}")
    
    def complete_project(self):
        """Complete a project."""
        self.projects_completed += 1
        print(f"🎯 {self.name} completed a project! Total: {self.projects_completed}")
    
    def learn_language(self, language):
        """Learn a new programming language."""
        if language not in self.programming_languages:
            self.programming_languages.append(language)
            print(f"📚 {self.name} learned {language}!")
        else:
            print(f"❌ {self.name} already knows {language}")
    
    def get_info(self):
        """Override with developer-specific information."""
        base_info = super().get_info()
        return (f"{base_info}\n"
                f"Languages: {', '.join(self.programming_languages)}\n"
                f"Projects Completed: {self.projects_completed}\n"
                f"Bugs Fixed: {self.bugs_fixed}")


class Manager(Employee):
    """Manager class inheriting from Employee."""
    
    def __init__(self, name, employee_id, base_salary, team_size):
        super().__init__(name, employee_id, "Management", base_salary)
        self.team_size = team_size
        self.meetings_held = 0
        self.decisions_made = 0
    
    def hold_meeting(self, topic, duration):
        """Hold a meeting."""
        self.meetings_held += 1
        self.work(duration)  # Call parent work method
        print(f"👥 {self.name} held a {duration}-hour meeting about {topic}")
        print(f"   Total meetings held: {self.meetings_held}")
    
    def make_decision(self, decision):
        """Make a management decision."""
        self.decisions_made += 1
        print(f"⚖️ {self.name} decided: {decision}")
        print(f"   Total decisions made: {self.decisions_made}")
    
    def get_annual_salary(self):
        """Override salary calculation with management bonus."""
        base_salary = super().get_annual_salary()
        management_bonus = self.team_size * 1000  # $1000 per team member
        return base_salary + management_bonus
    
    def get_info(self):
        """Override with manager-specific information."""
        base_info = super().get_info()
        annual_salary = self.get_annual_salary()
        return (f"{base_info}\n"
                f"Team Size: {self.team_size}\n"
                f"Meetings Held: {self.meetings_held}\n"
                f"Decisions Made: {self.decisions_made}\n"
                f"Annual Salary: ${annual_salary:,}")


class SalesRepresentative(Employee):
    """Sales representative class inheriting from Employee."""
    
    def __init__(self, name, employee_id, base_salary, commission_rate):
        super().__init__(name, employee_id, "Sales", base_salary)
        self.commission_rate = commission_rate  # Percentage
        self.sales_made = 0
        self.total_sales_amount = 0
    
    def make_sale(self, amount):
        """Make a sale."""
        self.sales_made += 1
        self.total_sales_amount += amount
        commission = amount * (self.commission_rate / 100)
        
        print(f"💰 {self.name} made a ${amount:,} sale!")
        print(f"   Commission earned: ${commission:,.2f}")
        print(f"   Total sales: {self.sales_made}, Total amount: ${self.total_sales_amount:,}")
        
        return commission
    
    def get_annual_salary(self):
        """Override salary calculation with commission."""
        base_salary = super().get_annual_salary()
        annual_commission = self.total_sales_amount * (self.commission_rate / 100)
        return base_salary + annual_commission
    
    def get_info(self):
        """Override with sales rep-specific information."""
        base_info = super().get_info()
        annual_salary = self.get_annual_salary()
        return (f"{base_info}\n"
                f"Commission Rate: {self.commission_rate}%\n"
                f"Sales Made: {self.sales_made}\n"
                f"Total Sales Amount: ${self.total_sales_amount:,}\n"
                f"Annual Salary (with commission): ${annual_salary:,.2f}")


# =============================================================================
# 5. METHOD RESOLUTION ORDER (MRO) DEMONSTRATION
# =============================================================================

class A:
    def method(self):
        print("Method from class A")
        return "A"


class B(A):
    def method(self):
        print("Method from class B")
        result = super().method()  # Call parent method
        return f"B->{result}"


class C(A):
    def method(self):
        print("Method from class C")
        result = super().method()  # Call parent method
        return f"C->{result}"


class D(B, C):
    def method(self):
        print("Method from class D")
        result = super().method()  # Follows MRO
        return f"D->{result}"


class E(C, B):  # Different order
    def method(self):
        print("Method from class E")
        result = super().method()  # Follows different MRO
        return f"E->{result}"


# =============================================================================
# DEMONSTRATION FUNCTIONS
# =============================================================================

def demonstrate_single_inheritance():
    """Demonstrate single inheritance with animals."""
    print("\n" + "="*60)
    print("SINGLE INHERITANCE DEMONSTRATION")
    print("="*60)
    
    # Create animals
    dog = Dog("Buddy", "Golden Retriever", 3)
    cat = Cat("Whiskers", "Orange", 2)
    
    # Use inherited methods
    print(f"\n🐕 Dog Activities:")
    print(f"   {dog.get_info()}")
    dog.eat("dog food")
    dog.bark()
    dog.fetch("ball")
    dog.train("sit")
    dog.sleep()
    
    print(f"\n🐱 Cat Activities:")
    print(f"   {cat.get_info()}")
    cat.eat("fish")
    cat.meow()
    cat.climb("tree")
    cat.hunt("mouse")
    
    # Demonstrate polymorphism
    print(f"\n🔄 Polymorphism Demo:")
    animals = [dog, cat]
    for animal in animals:
        print(f"   {animal.name} says: {animal.make_sound()}")


def demonstrate_multilevel_inheritance():
    """Demonstrate multilevel inheritance with vehicles."""
    print("\n" + "="*60)
    print("MULTILEVEL INHERITANCE DEMONSTRATION")
    print("="*60)
    
    # Create vehicles
    car = Car("Toyota", "Camry", 2023, "V6", 4)
    truck = Truck("Ford", "F-150", 2022, "V8", 2000)
    
    # Car operations
    print(f"\n🚗 Car Operations:")
    car.start()
    car.add_passenger(3)
    car.drive(50)
    car.honk()
    print(f"\n{car.get_info()}")
    
    # Truck operations
    print(f"\n🚛 Truck Operations:")
    truck.start()
    truck.load_cargo(500)
    truck.drive(30)
    truck.unload_cargo(200)
    print(f"\n{truck.get_info()}")


def demonstrate_multiple_inheritance():
    """Demonstrate multiple inheritance with flying and swimming animals."""
    print("\n" + "="*60)
    print("MULTIPLE INHERITANCE DEMONSTRATION")
    print("="*60)
    
    # Create bird and duck
    eagle = Bird("Eagle", "Bald Eagle", 5, 84)
    duck = Duck("Donald", 3, "white")
    
    # Eagle operations
    print(f"\n🦅 Eagle Operations:")
    print(f"   {eagle.get_info()}")
    eagle.flap_wings()
    eagle.take_off()
    eagle.climb(200)
    eagle.eat("fish")
    eagle.land()
    
    # Duck operations (multiple capabilities)
    print(f"\n🦆 Duck Operations:")
    print(f"   {duck.get_info()}")
    duck.quack()
    duck.take_off()  # From Flyable
    print(f"   {duck.get_info()}")
    duck.land()
    duck.dive(5)     # From Swimmable
    duck.paddle()
    duck.surface()
    print(f"   Final status: {duck.get_info()}")


def demonstrate_hierarchical_inheritance():
    """Demonstrate hierarchical inheritance with employees."""
    print("\n" + "="*60)
    print("HIERARCHICAL INHERITANCE DEMONSTRATION")
    print("="*60)
    
    # Create different types of employees
    developer = Developer("Alice Johnson", "DEV001", 80000, ["Python", "JavaScript", "SQL"])
    manager = Manager("Bob Smith", "MGR001", 100000, 8)
    sales_rep = SalesRepresentative("Carol Davis", "SAL001", 50000, 5)
    
    # Developer activities
    print(f"\n👩‍💻 Developer Activities:")
    developer.code("Python", 8)
    developer.fix_bug()
    developer.complete_project()
    developer.learn_language("Rust")
    developer.promote(10000)
    print(f"\n{developer.get_info()}")
    
    # Manager activities
    print(f"\n👨‍💼 Manager Activities:")
    manager.hold_meeting("Sprint Planning", 2)
    manager.make_decision("Approve new feature")
    manager.promote(15000)
    print(f"\n{manager.get_info()}")
    
    # Sales representative activities
    print(f"\n👩‍💼 Sales Representative Activities:")
    sales_rep.make_sale(25000)
    sales_rep.make_sale(15000)
    sales_rep.promote(5000)
    print(f"\n{sales_rep.get_info()}")


def demonstrate_method_resolution_order():
    """Demonstrate Method Resolution Order (MRO)."""
    print("\n" + "="*60)
    print("METHOD RESOLUTION ORDER (MRO) DEMONSTRATION")
    print("="*60)
    
    # Show MRO for different classes
    print(f"📋 Method Resolution Order:")
    print(f"   D.mro(): {[cls.__name__ for cls in D.mro()]}")
    print(f"   E.mro(): {[cls.__name__ for cls in E.mro()]}")
    
    # Create instances and call methods
    d = D()
    e = E()
    
    print(f"\n🔄 Calling d.method() (D inherits B, C):")
    result_d = d.method()
    print(f"   Result: {result_d}")
    
    print(f"\n🔄 Calling e.method() (E inherits C, B):")
    result_e = e.method()
    print(f"   Result: {result_e}")


def demonstrate_composition_vs_inheritance():
    """Demonstrate when to use composition vs inheritance."""
    print("\n" + "="*60)
    print("COMPOSITION VS INHERITANCE COMPARISON")
    print("="*60)
    
    # Inheritance example (is-a relationship)
    print(f"🔗 INHERITANCE Example (IS-A relationship):")
    dog = Dog("Rex", "German Shepherd", 4)
    print(f"   A Dog IS-A Animal: {isinstance(dog, Animal)}")
    print(f"   Dog can use Animal methods: {dog.get_info()}")
    
    # Composition example (has-a relationship)
    print(f"\n🧩 COMPOSITION Example (HAS-A relationship):")
    
    class Engine:
        def __init__(self, horsepower):
            self.horsepower = horsepower
        
        def start(self):
            return f"Engine with {self.horsepower}HP started"
    
    class CompositionCar:
        def __init__(self, make, model):
            self.make = make
            self.model = model
            self.engine = Engine(300)  # Car HAS-A Engine
        
        def start(self):
            return f"{self.make} {self.model}: {self.engine.start()}"
    
    comp_car = CompositionCar("BMW", "X5")
    print(f"   A Car HAS-A Engine: {hasattr(comp_car, 'engine')}")
    print(f"   Car uses Engine: {comp_car.start()}")
    
    print(f"\n💡 Guidelines:")
    print(f"   • Use INHERITANCE for IS-A relationships (Dog is-a Animal)")
    print(f"   • Use COMPOSITION for HAS-A relationships (Car has-a Engine)")
    print(f"   • Favor composition over inheritance when possible")


def main():
    """Main function to demonstrate all inheritance concepts."""
    print("🧬 INHERITANCE IN PYTHON - COMPREHENSIVE DEMONSTRATION")
    print("=" * 70)
    
    demonstrate_single_inheritance()
    demonstrate_multilevel_inheritance()
    demonstrate_multiple_inheritance()
    demonstrate_hierarchical_inheritance()
    demonstrate_method_resolution_order()
    demonstrate_composition_vs_inheritance()
    
    print("\n" + "="*70)
    print("📋 INHERITANCE SUMMARY")
    print("="*70)
    print("✅ Code Reuse: Child classes inherit parent functionality")
    print("✅ Extensibility: Easy to add new features through inheritance")
    print("✅ Polymorphism: Same interface, different implementations")
    print("✅ Method Overriding: Child classes can customize parent behavior")
    print("✅ super(): Properly call parent class methods")
    print("✅ MRO: Python uses C3 linearization for method resolution")
    
    print("\n🎯 Key Takeaways:")
    print("• Single inheritance: One parent class")
    print("• Multiple inheritance: Multiple parent classes (use carefully)")
    print("• Multilevel inheritance: Chain of inheritance")
    print("• Hierarchical inheritance: Multiple children from one parent")
    print("• Use super() to call parent methods properly")
    print("• Understand MRO for multiple inheritance")
    print("• Favor composition over inheritance when appropriate")
    print("• Inheritance models 'is-a' relationships")


if __name__ == "__main__":
    main()
