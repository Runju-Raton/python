"""
Polymorphism in Python - Comprehensive Examples
==============================================

This file demonstrates polymorphism concepts with practical examples:
- Duck typing and dynamic polymorphism
- Method overriding and inheritance-based polymorphism
- Operator overloading
- Abstract base classes with polymorphic behavior
- Design patterns using polymorphism
- Real-world polymorphic scenarios
"""

from abc import ABC, abstractmethod
import math
from typing import Protocol, List, Any
from datetime import datetime


# =============================================================================
# 1. DUCK TYPING - DYNAMIC POLYMORPHISM
# =============================================================================

class Duck:
    """Duck class for duck typing demonstration."""
    
    def __init__(self, name):
        self.name = name
    
    def fly(self):
        return f"{self.name} the duck flies in the sky!"
    
    def swim(self):
        return f"{self.name} the duck swims in the pond!"
    
    def make_sound(self):
        return f"{self.name} says: Quack! Quack!"


class Airplane:
    """Airplane class that can 'fly' like a duck."""
    
    def __init__(self, model):
        self.model = model
    
    def fly(self):
        return f"{self.model} airplane soars through the clouds!"
    
    def make_sound(self):
        return f"{self.model} makes: VROOOOOM!"


class Fish:
    """Fish class that can 'swim' like a duck."""
    
    def __init__(self, species):
        self.species = species
    
    def swim(self):
        return f"{self.species} fish swims gracefully underwater!"
    
    def make_sound(self):
        return f"{self.species} makes: Blub blub!"


class Robot:
    """Robot class that can do everything like a duck."""
    
    def __init__(self, model):
        self.model = model
    
    def fly(self):
        return f"{self.model} robot activates jet propulsion!"
    
    def swim(self):
        return f"{self.model} robot engages waterproof mode!"
    
    def make_sound(self):
        return f"{self.model} robot says: BEEP BOOP!"


def make_it_fly(flying_object):
    """Duck typing - works with any object that has a fly() method."""
    try:
        return flying_object.fly()
    except AttributeError:
        return f"{flying_object} cannot fly!"


def make_it_swim(swimming_object):
    """Duck typing - works with any object that has a swim() method."""
    try:
        return swimming_object.swim()
    except AttributeError:
        return f"{swimming_object} cannot swim!"


def make_sound(sound_maker):
    """Duck typing - works with any object that has a make_sound() method."""
    try:
        return sound_maker.make_sound()
    except AttributeError:
        return f"{sound_maker} is silent!"


# =============================================================================
# 2. METHOD OVERRIDING - INHERITANCE-BASED POLYMORPHISM
# =============================================================================

class Animal:
    """Base animal class for method overriding demonstration."""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self, food):
        """Base eating behavior."""
        return f"{self.name} the {self.species} eats {food}"
    
    def sleep(self):
        """Base sleeping behavior."""
        return f"{self.name} sleeps peacefully"
    
    def move(self):
        """Base movement - will be overridden by subclasses."""
        return f"{self.name} moves around"
    
    def make_sound(self):
        """Base sound - will be overridden by subclasses."""
        return f"{self.name} makes a sound"
    
    def get_info(self):
        """Get basic animal information."""
        return f"{self.name} is a {self.species}"
    
    def __str__(self):
        return f"{self.name} ({self.species})"


class Dog(Animal):
    """Dog class with overridden methods."""
    
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def move(self):
        """Override: Dog-specific movement."""
        return f"{self.name} runs on four legs, tail wagging!"
    
    def make_sound(self):
        """Override: Dog-specific sound."""
        return f"{self.name} barks: Woof! Woof!"
    
    def fetch(self, item):
        """Dog-specific behavior."""
        return f"{self.name} fetches the {item} and brings it back!"


class Cat(Animal):
    """Cat class with overridden methods."""
    
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def move(self):
        """Override: Cat-specific movement."""
        return f"{self.name} prowls silently on padded paws"
    
    def make_sound(self):
        """Override: Cat-specific sound."""
        return f"{self.name} meows: Meow! Purr..."
    
    def climb(self):
        """Cat-specific behavior."""
        return f"{self.name} gracefully climbs up high!"


class Bird(Animal):
    """Bird class with overridden methods."""
    
    def __init__(self, name, wingspan):
        super().__init__(name, "Bird")
        self.wingspan = wingspan
    
    def move(self):
        """Override: Bird-specific movement."""
        return f"{self.name} soars through the sky with {self.wingspan}cm wingspan!"
    
    def make_sound(self):
        """Override: Bird-specific sound."""
        return f"{self.name} chirps: Tweet tweet!"
    
    def fly_high(self):
        """Bird-specific behavior."""
        return f"{self.name} flies high above the clouds!"


class Fish(Animal):
    """Fish class with overridden methods."""
    
    def __init__(self, name, water_type):
        super().__init__(name, "Fish")
        self.water_type = water_type
    
    def move(self):
        """Override: Fish-specific movement."""
        return f"{self.name} swims gracefully through {self.water_type} water"
    
    def make_sound(self):
        """Override: Fish-specific sound."""
        return f"{self.name} makes bubbles: Blub blub..."
    
    def dive_deep(self):
        """Fish-specific behavior."""
        return f"{self.name} dives deep into the {self.water_type}!"


# =============================================================================
# 3. OPERATOR OVERLOADING - MATHEMATICAL POLYMORPHISM
# =============================================================================

class Vector2D:
    """2D Vector class demonstrating operator overloading."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Overload + operator for vector addition."""
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """Overload - operator for vector subtraction."""
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """Overload * operator for scalar multiplication."""
        if isinstance(scalar, (int, float)):
            return Vector2D(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __rmul__(self, scalar):
        """Right multiplication (scalar * vector)."""
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        """Overload / operator for scalar division."""
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Vector2D(self.x / scalar, self.y / scalar)
        return NotImplemented
    
    def __eq__(self, other):
        """Overload == operator for equality comparison."""
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False
    
    def __ne__(self, other):
        """Overload != operator for inequality comparison."""
        return not self.__eq__(other)
    
    def __abs__(self):
        """Overload abs() function to return vector magnitude."""
        return math.sqrt(self.x**2 + self.y**2)
    
    def __str__(self):
        """String representation for users."""
        return f"Vector2D({self.x}, {self.y})"
    
    def __repr__(self):
        """String representation for developers."""
        return f"Vector2D(x={self.x}, y={self.y})"
    
    def dot_product(self, other):
        """Calculate dot product with another vector."""
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        raise TypeError("Dot product requires another Vector2D")
    
    def magnitude(self):
        """Calculate vector magnitude."""
        return abs(self)
    
    def normalize(self):
        """Return normalized (unit) vector."""
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0)
        return self / mag


class Matrix2x2:
    """2x2 Matrix class demonstrating operator overloading."""
    
    def __init__(self, a, b, c, d):
        """Initialize matrix [[a, b], [c, d]]."""
        self.matrix = [[a, b], [c, d]]
    
    def __add__(self, other):
        """Matrix addition."""
        if isinstance(other, Matrix2x2):
            result = Matrix2x2(0, 0, 0, 0)
            for i in range(2):
                for j in range(2):
                    result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return result
        return NotImplemented
    
    def __mul__(self, other):
        """Matrix multiplication or scalar multiplication."""
        if isinstance(other, Matrix2x2):
            # Matrix multiplication
            a = self.matrix[0][0] * other.matrix[0][0] + self.matrix[0][1] * other.matrix[1][0]
            b = self.matrix[0][0] * other.matrix[0][1] + self.matrix[0][1] * other.matrix[1][1]
            c = self.matrix[1][0] * other.matrix[0][0] + self.matrix[1][1] * other.matrix[1][0]
            d = self.matrix[1][0] * other.matrix[0][1] + self.matrix[1][1] * other.matrix[1][1]
            return Matrix2x2(a, b, c, d)
        elif isinstance(other, (int, float)):
            # Scalar multiplication
            result = Matrix2x2(0, 0, 0, 0)
            for i in range(2):
                for j in range(2):
                    result.matrix[i][j] = self.matrix[i][j] * other
            return result
        return NotImplemented
    
    def __rmul__(self, scalar):
        """Right scalar multiplication."""
        return self.__mul__(scalar)
    
    def __str__(self):
        return f"Matrix2x2([[{self.matrix[0][0]}, {self.matrix[0][1]}], [{self.matrix[1][0]}, {self.matrix[1][1]}]])"
    
    def determinant(self):
        """Calculate matrix determinant."""
        return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]


# =============================================================================
# 4. ABSTRACT BASE CLASSES - FORMAL POLYMORPHISM
# =============================================================================

class Shape(ABC):
    """Abstract base class for all shapes."""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass
    
    def describe(self):
        """Common method for all shapes."""
        return (f"{self.name}:\n"
                f"  Area: {self.area():.2f}\n"
                f"  Perimeter: {self.perimeter():.2f}")
    
    def compare_area(self, other_shape):
        """Compare areas of two shapes."""
        if not isinstance(other_shape, Shape):
            raise TypeError("Can only compare with another Shape")
        
        self_area = self.area()
        other_area = other_shape.area()
        
        if self_area > other_area:
            return f"{self.name} is larger than {other_shape.name}"
        elif self_area < other_area:
            return f"{self.name} is smaller than {other_shape.name}"
        else:
            return f"{self.name} and {other_shape.name} have equal areas"
    
    def __str__(self):
        return self.name


class Rectangle(Shape):
    """Rectangle implementation of Shape."""
    
    def __init__(self, width, height):
        super().__init__(f"Rectangle({width}x{height})")
        self.width = width
        self.height = height
    
    def area(self):
        """Override: Calculate rectangle area."""
        return self.width * self.height
    
    def perimeter(self):
        """Override: Calculate rectangle perimeter."""
        return 2 * (self.width + self.height)
    
    def is_square(self):
        """Rectangle-specific method."""
        return self.width == self.height


class Circle(Shape):
    """Circle implementation of Shape."""
    
    def __init__(self, radius):
        super().__init__(f"Circle(r={radius})")
        self.radius = radius
    
    def area(self):
        """Override: Calculate circle area."""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Override: Calculate circle perimeter (circumference)."""
        return 2 * math.pi * self.radius
    
    def diameter(self):
        """Circle-specific method."""
        return 2 * self.radius


class Triangle(Shape):
    """Triangle implementation of Shape."""
    
    def __init__(self, side_a, side_b, side_c):
        super().__init__(f"Triangle({side_a},{side_b},{side_c})")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def area(self):
        """Override: Calculate triangle area using Heron's formula."""
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    
    def perimeter(self):
        """Override: Calculate triangle perimeter."""
        return self.side_a + self.side_b + self.side_c
    
    def is_equilateral(self):
        """Triangle-specific method."""
        return self.side_a == self.side_b == self.side_c
    
    def is_isosceles(self):
        """Triangle-specific method."""
        return (self.side_a == self.side_b or 
                self.side_b == self.side_c or 
                self.side_a == self.side_c)


# =============================================================================
# 5. PROTOCOL-BASED POLYMORPHISM (Python 3.8+)
# =============================================================================

class Drawable(Protocol):
    """Protocol for drawable objects."""
    
    def draw(self) -> str:
        """Draw the object."""
        ...
    
    def get_color(self) -> str:
        """Get the object's color."""
        ...


class Square:
    """Square class implementing Drawable protocol."""
    
    def __init__(self, size, color="blue"):
        self.size = size
        self.color = color
    
    def draw(self) -> str:
        """Implement draw method."""
        return f"Drawing a {self.color} square of size {self.size}"
    
    def get_color(self) -> str:
        """Implement get_color method."""
        return self.color
    
    def area(self):
        """Square-specific method."""
        return self.size ** 2


class Star:
    """Star class implementing Drawable protocol."""
    
    def __init__(self, points, color="yellow"):
        self.points = points
        self.color = color
    
    def draw(self) -> str:
        """Implement draw method."""
        return f"Drawing a {self.color} {self.points}-pointed star"
    
    def get_color(self) -> str:
        """Implement get_color method."""
        return self.color
    
    def twinkle(self):
        """Star-specific method."""
        return f"The {self.color} star twinkles brightly!"


def render_object(drawable: Drawable):
    """Function that works with any Drawable object."""
    print(f"🎨 {drawable.draw()}")
    print(f"   Color: {drawable.get_color()}")


# =============================================================================
# 6. DESIGN PATTERN: STRATEGY PATTERN WITH POLYMORPHISM
# =============================================================================

class PaymentStrategy(ABC):
    """Abstract strategy for payment processing."""
    
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        """Process payment of given amount."""
        pass
    
    @abstractmethod
    def get_fee(self, amount: float) -> float:
        """Calculate processing fee."""
        pass


class CreditCardPayment(PaymentStrategy):
    """Credit card payment strategy."""
    
    def __init__(self, card_number, cardholder_name):
        self.card_number = card_number[-4:]  # Store only last 4 digits
        self.cardholder_name = cardholder_name
    
    def process_payment(self, amount: float) -> str:
        """Process credit card payment."""
        return f"Processed ${amount:.2f} payment via Credit Card ending in {self.card_number}"
    
    def get_fee(self, amount: float) -> float:
        """Credit card fee: 2.9% + $0.30."""
        return amount * 0.029 + 0.30


class PayPalPayment(PaymentStrategy):
    """PayPal payment strategy."""
    
    def __init__(self, email):
        self.email = email
    
    def process_payment(self, amount: float) -> str:
        """Process PayPal payment."""
        return f"Processed ${amount:.2f} payment via PayPal ({self.email})"
    
    def get_fee(self, amount: float) -> float:
        """PayPal fee: 3.49% + $0.49."""
        return amount * 0.0349 + 0.49


class CryptoPayment(PaymentStrategy):
    """Cryptocurrency payment strategy."""
    
    def __init__(self, wallet_address, crypto_type):
        self.wallet_address = wallet_address[:10] + "..."  # Truncate for display
        self.crypto_type = crypto_type
    
    def process_payment(self, amount: float) -> str:
        """Process cryptocurrency payment."""
        return f"Processed ${amount:.2f} payment via {self.crypto_type} to {self.wallet_address}"
    
    def get_fee(self, amount: float) -> float:
        """Crypto fee: 1% flat rate."""
        return amount * 0.01


class PaymentProcessor:
    """Context class that uses payment strategies."""
    
    def __init__(self):
        self.strategy: PaymentStrategy = None
    
    def set_strategy(self, strategy: PaymentStrategy):
        """Set the payment strategy."""
        self.strategy = strategy
    
    def process_payment(self, amount: float) -> dict:
        """Process payment using current strategy."""
        if not self.strategy:
            raise ValueError("No payment strategy set")
        
        fee = self.strategy.get_fee(amount)
        total = amount + fee
        result = self.strategy.process_payment(amount)
        
        return {
            'amount': amount,
            'fee': fee,
            'total': total,
            'result': result,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


# =============================================================================
# DEMONSTRATION FUNCTIONS
# =============================================================================

def demonstrate_duck_typing():
    """Demonstrate duck typing polymorphism."""
    print("\n" + "="*60)
    print("DUCK TYPING POLYMORPHISM DEMONSTRATION")
    print("="*60)
    
    # Create objects with similar interfaces
    duck = Duck("Donald")
    airplane = Airplane("Boeing 747")
    fish = Fish("Salmon")
    robot = Robot("R2-D2")
    
    objects = [duck, airplane, fish, robot]
    
    # Test flying capability
    print(f"🛫 Flying Tests:")
    for obj in objects:
        result = make_it_fly(obj)
        print(f"   {result}")
    
    # Test swimming capability  
    print(f"\n🏊 Swimming Tests:")
    for obj in objects:
        result = make_it_swim(obj)
        print(f"   {result}")
    
    # Test sound making capability
    print(f"\n🔊 Sound Tests:")
    for obj in objects:
        result = make_sound(obj)
        print(f"   {result}")


def demonstrate_method_overriding():
    """Demonstrate method overriding polymorphism."""
    print("\n" + "="*60)
    print("METHOD OVERRIDING POLYMORPHISM DEMONSTRATION")
    print("="*60)
    
    # Create different animals
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Orange")
    bird = Bird("Tweety", 15)
    fish = Fish("Nemo", "salt")
    
    animals = [dog, cat, bird, fish]
    
    # Demonstrate polymorphic behavior
    print(f"🐾 Animal Behaviors (Same Method, Different Implementations):")
    for animal in animals:
        print(f"\n   {animal.get_info()}:")
        print(f"     Movement: {animal.move()}")
        print(f"     Sound: {animal.make_sound()}")
        print(f"     Eating: {animal.eat('food')}")
    
    # Demonstrate specific behaviors
    print(f"\n🎯 Specific Animal Behaviors:")
    print(f"   {dog.fetch('stick')}")
    print(f"   {cat.climb()}")
    print(f"   {bird.fly_high()}")
    print(f"   {fish.dive_deep()}")


def demonstrate_operator_overloading():
    """Demonstrate operator overloading polymorphism."""
    print("\n" + "="*60)
    print("OPERATOR OVERLOADING POLYMORPHISM DEMONSTRATION")
    print("="*60)
    
    # Vector operations
    print(f"📐 Vector Operations:")
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    
    print(f"   v1 = {v1}")
    print(f"   v2 = {v2}")
    print(f"   v1 + v2 = {v1 + v2}")
    print(f"   v1 - v2 = {v1 - v2}")
    print(f"   v1 * 2 = {v1 * 2}")
    print(f"   3 * v1 = {3 * v1}")
    print(f"   v1 / 2 = {v1 / 2}")
    print(f"   |v1| = {abs(v1):.2f}")
    print(f"   v1 == v2: {v1 == v2}")
    print(f"   v1 != v2: {v1 != v2}")
    print(f"   v1 · v2 = {v1.dot_product(v2)}")
    
    # Matrix operations
    print(f"\n🔢 Matrix Operations:")
    m1 = Matrix2x2(1, 2, 3, 4)
    m2 = Matrix2x2(2, 0, 1, 1)
    
    print(f"   m1 = {m1}")
    print(f"   m2 = {m2}")
    print(f"   m1 + m2 = {m1 + m2}")
    print(f"   m1 * m2 = {m1 * m2}")
    print(f"   m1 * 2 = {m1 * 2}")
    print(f"   det(m1) = {m1.determinant()}")


def demonstrate_abstract_polymorphism():
    """Demonstrate abstract base class polymorphism."""
    print("\n" + "="*60)
    print("ABSTRACT BASE CLASS POLYMORPHISM DEMONSTRATION")
    print("="*60)
    
    # Create different shapes
    rectangle = Rectangle(5, 3)
    circle = Circle(4)
    triangle = Triangle(3, 4, 5)
    
    shapes = [rectangle, circle, triangle]
    
    # Demonstrate polymorphic behavior
    print(f"📏 Shape Analysis (Same Interface, Different Implementations):")
    for shape in shapes:
        print(f"\n{shape.describe()}")
    
    # Demonstrate shape comparisons
    print(f"\n🔄 Shape Comparisons:")
    print(f"   {rectangle.compare_area(circle)}")
    print(f"   {circle.compare_area(triangle)}")
    
    # Demonstrate specific methods
    print(f"\n🎯 Shape-Specific Methods:")
    print(f"   Rectangle is square: {rectangle.is_square()}")
    print(f"   Circle diameter: {circle.diameter():.2f}")
    print(f"   Triangle is equilateral: {triangle.is_equilateral()}")
    print(f"   Triangle is isosceles: {triangle.is_isosceles()}")
    
    # Calculate total area
    total_area = sum(shape.area() for shape in shapes)
    print(f"\n📊 Total area of all shapes: {total_area:.2f}")


def demonstrate_protocol_polymorphism():
    """Demonstrate protocol-based polymorphism."""
    print("\n" + "="*60)
    print("PROTOCOL-BASED POLYMORPHISM DEMONSTRATION")
    print("="*60)
    
    # Create objects that implement Drawable protocol
    square = Square(5, "red")
    star = Star(8, "gold")
    
    drawables = [square, star]
    
    # Use polymorphically through protocol
    print(f"🎨 Drawing Objects (Protocol-Based Polymorphism):")
    for drawable in drawables:
        render_object(drawable)
        print()
    
    # Demonstrate specific methods
    print(f"🎯 Object-Specific Methods:")
    print(f"   Square area: {square.area()}")
    print(f"   Star twinkle: {star.twinkle()}")


def demonstrate_strategy_pattern():
    """Demonstrate strategy pattern with polymorphism."""
    print("\n" + "="*60)
    print("STRATEGY PATTERN POLYMORPHISM DEMONSTRATION")
    print("="*60)
    
    # Create payment processor
    processor = PaymentProcessor()
    
    # Create different payment strategies
    credit_card = CreditCardPayment("1234-5678-9012-3456", "John Doe")
    paypal = PayPalPayment("john@example.com")
    crypto = CryptoPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "Bitcoin")
    
    strategies = [
        ("Credit Card", credit_card),
        ("PayPal", paypal),
        ("Cryptocurrency", crypto)
    ]
    
    amount = 100.00
    
    print(f"💳 Processing ${amount} Payment with Different Strategies:")
    for strategy_name, strategy in strategies:
        processor.set_strategy(strategy)
        result = processor.process_payment(amount)
        
        print(f"\n   {strategy_name} Payment:")
        print(f"     Result: {result['result']}")
        print(f"     Amount: ${result['amount']:.2f}")
        print(f"     Fee: ${result['fee']:.2f}")
        print(f"     Total: ${result['total']:.2f}")
        print(f"     Time: {result['timestamp']}")


def main():
    """Main function to demonstrate all polymorphism concepts."""
    print("🎭 POLYMORPHISM IN PYTHON - COMPREHENSIVE DEMONSTRATION")
    print("=" * 70)
    
    demonstrate_duck_typing()
    demonstrate_method_overriding()
    demonstrate_operator_overloading()
    demonstrate_abstract_polymorphism()
    demonstrate_protocol_polymorphism()
    demonstrate_strategy_pattern()
    
    print("\n" + "="*70)
    print("📋 POLYMORPHISM SUMMARY")
    print("="*70)
    print("✅ Duck Typing: Objects used based on behavior, not type")
    print("✅ Method Overriding: Same method name, different implementations")
    print("✅ Operator Overloading: Custom behavior for operators")
    print("✅ Abstract Classes: Formal contracts for polymorphic behavior")
    print("✅ Protocols: Structural typing for polymorphism")
    print("✅ Design Patterns: Strategy, Template, and other patterns")
    
    print("\n🎯 Key Takeaways:")
    print("• Polymorphism enables 'one interface, many implementations'")
    print("• Python's duck typing provides natural polymorphism")
    print("• Method overriding allows customized behavior in subclasses")
    print("• Operator overloading makes custom classes behave like built-ins")
    print("• Abstract classes enforce polymorphic contracts")
    print("• Protocols enable structural polymorphism without inheritance")
    print("• Design patterns leverage polymorphism for flexible architectures")
    print("• Polymorphism promotes code reusability and maintainability")


if __name__ == "__main__":
    main()
