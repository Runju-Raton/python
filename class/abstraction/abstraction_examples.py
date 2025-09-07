"""
Abstraction in Python - Comprehensive Examples
=============================================

This file demonstrates abstraction concepts with practical examples:
- Abstract Base Classes (ABC)
- Abstract methods and properties
- Template Method pattern
- Strategy pattern
- Real-world abstraction scenarios
"""

from abc import ABC, abstractmethod, abstractproperty
from typing import Protocol
import math


# =============================================================================
# 1. BASIC ABSTRACT BASE CLASS EXAMPLE
# =============================================================================

class Vehicle(ABC):
    """
    Abstract base class for all vehicles.
    Defines the common interface that all vehicles must implement.
    """
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._fuel_level = 100  # Start with full tank
    
    @abstractmethod
    def start_engine(self):
        """Abstract method - must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def stop_engine(self):
        """Abstract method - must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def get_max_speed(self):
        """Abstract method - return maximum speed."""
        pass
    
    @property
    @abstractmethod
    def fuel_type(self):
        """Abstract property - must be implemented by subclasses."""
        pass
    
    # Concrete methods (common to all vehicles)
    def get_info(self):
        """Concrete method available to all vehicles."""
        return f"{self.year} {self.make} {self.model}"
    
    def refuel(self, amount):
        """Concrete method for refueling."""
        self._fuel_level = min(100, self._fuel_level + amount)
        print(f"⛽ Refueled. Fuel level: {self._fuel_level}%")
    
    def get_fuel_level(self):
        """Concrete method to check fuel level."""
        return self._fuel_level
    
    def __str__(self):
        return f"{self.get_info()} ({self.fuel_type})"


class Car(Vehicle):
    """Concrete implementation of Vehicle for cars."""
    
    @property
    def fuel_type(self):
        return "Gasoline"
    
    def start_engine(self):
        print(f"🚗 {self.get_info()}: Engine started with key ignition")
        return True
    
    def stop_engine(self):
        print(f"🚗 {self.get_info()}: Engine stopped")
        return True
    
    def get_max_speed(self):
        return 180  # km/h
    
    def open_trunk(self):
        """Car-specific method."""
        print(f"🚗 {self.get_info()}: Trunk opened")


class Motorcycle(Vehicle):
    """Concrete implementation of Vehicle for motorcycles."""
    
    @property
    def fuel_type(self):
        return "Gasoline"
    
    def start_engine(self):
        print(f"🏍️ {self.get_info()}: Engine started with electric starter")
        return True
    
    def stop_engine(self):
        print(f"🏍️ {self.get_info()}: Engine stopped")
        return True
    
    def get_max_speed(self):
        return 250  # km/h
    
    def wheelie(self):
        """Motorcycle-specific method."""
        print(f"🏍️ {self.get_info()}: Performing a wheelie!")


class ElectricCar(Vehicle):
    """Concrete implementation of Vehicle for electric cars."""
    
    @property
    def fuel_type(self):
        return "Electric"
    
    def start_engine(self):
        print(f"⚡ {self.get_info()}: Electric motor started silently")
        return True
    
    def stop_engine(self):
        print(f"⚡ {self.get_info()}: Electric motor stopped")
        return True
    
    def get_max_speed(self):
        return 200  # km/h
    
    def charge_battery(self, hours):
        """Electric car specific method."""
        charge_gained = hours * 10  # 10% per hour
        self._fuel_level = min(100, self._fuel_level + charge_gained)
        print(f"⚡ Charged for {hours} hours. Battery level: {self._fuel_level}%")


# =============================================================================
# 2. PAYMENT SYSTEM ABSTRACTION
# =============================================================================

class PaymentProcessor(ABC):
    """
    Abstract base class for payment processing systems.
    Demonstrates abstraction in financial applications.
    """
    
    def __init__(self, merchant_id):
        self.merchant_id = merchant_id
        self._transaction_log = []
    
    @abstractmethod
    def validate_payment_details(self, payment_info):
        """Validate payment information - implementation varies by processor."""
        pass
    
    @abstractmethod
    def process_payment(self, amount, payment_info):
        """Process the actual payment - implementation varies by processor."""
        pass
    
    @abstractmethod
    def get_transaction_fee(self, amount):
        """Calculate transaction fee - varies by processor."""
        pass
    
    # Template method (uses abstract methods)
    def execute_payment(self, amount, payment_info):
        """
        Template method that defines the payment process flow.
        This is the same for all payment processors.
        """
        print(f"\n💳 Processing ${amount} payment...")
        
        # Step 1: Validate (implementation varies)
        if not self.validate_payment_details(payment_info):
            print("❌ Payment validation failed")
            return False
        
        # Step 2: Calculate fee (implementation varies)
        fee = self.get_transaction_fee(amount)
        total = amount + fee
        
        print(f"💰 Amount: ${amount}, Fee: ${fee}, Total: ${total}")
        
        # Step 3: Process (implementation varies)
        success = self.process_payment(total, payment_info)
        
        # Step 4: Log transaction (common for all)
        self._log_transaction(amount, fee, success, payment_info)
        
        return success
    
    def _log_transaction(self, amount, fee, success, payment_info):
        """Common logging method for all processors."""
        status = "SUCCESS" if success else "FAILED"
        log_entry = {
            'amount': amount,
            'fee': fee,
            'status': status,
            'payment_type': payment_info.get('type', 'unknown')
        }
        self._transaction_log.append(log_entry)
        print(f"📝 Transaction logged: {status}")
    
    def get_transaction_history(self):
        """Common method to get transaction history."""
        return self._transaction_log.copy()


class CreditCardProcessor(PaymentProcessor):
    """Concrete credit card payment processor."""
    
    def validate_payment_details(self, payment_info):
        """Credit card specific validation."""
        required_fields = ['card_number', 'expiry', 'cvv', 'cardholder_name']
        
        for field in required_fields:
            if field not in payment_info:
                print(f"❌ Missing required field: {field}")
                return False
        
        # Simplified validation
        card_number = payment_info['card_number']
        if len(card_number) not in [15, 16]:  # Amex or Visa/MC
            print("❌ Invalid card number length")
            return False
        
        print("✅ Credit card details validated")
        return True
    
    def process_payment(self, amount, payment_info):
        """Credit card specific processing."""
        print("💳 Connecting to credit card network...")
        print("💳 Processing credit card payment...")
        
        # Simulate processing (always succeeds in demo)
        print("✅ Credit card payment processed successfully")
        return True
    
    def get_transaction_fee(self, amount):
        """Credit card fee: 2.9% + $0.30"""
        return round(amount * 0.029 + 0.30, 2)


class PayPalProcessor(PaymentProcessor):
    """Concrete PayPal payment processor."""
    
    def validate_payment_details(self, payment_info):
        """PayPal specific validation."""
        if 'email' not in payment_info:
            print("❌ PayPal email required")
            return False
        
        email = payment_info['email']
        if '@' not in email:
            print("❌ Invalid PayPal email format")
            return False
        
        print("✅ PayPal details validated")
        return True
    
    def process_payment(self, amount, payment_info):
        """PayPal specific processing."""
        print("🌐 Connecting to PayPal API...")
        print("🌐 Processing PayPal payment...")
        
        # Simulate processing
        print("✅ PayPal payment processed successfully")
        return True
    
    def get_transaction_fee(self, amount):
        """PayPal fee: 3.49% + $0.49"""
        return round(amount * 0.0349 + 0.49, 2)


class CryptoProcessor(PaymentProcessor):
    """Concrete cryptocurrency payment processor."""
    
    def validate_payment_details(self, payment_info):
        """Cryptocurrency specific validation."""
        required_fields = ['wallet_address', 'currency_type']
        
        for field in required_fields:
            if field not in payment_info:
                print(f"❌ Missing required field: {field}")
                return False
        
        wallet = payment_info['wallet_address']
        if len(wallet) < 26:  # Simplified wallet validation
            print("❌ Invalid wallet address")
            return False
        
        print("✅ Cryptocurrency details validated")
        return True
    
    def process_payment(self, amount, payment_info):
        """Cryptocurrency specific processing."""
        currency = payment_info['currency_type']
        print(f"₿ Processing {currency} payment...")
        print("₿ Broadcasting to blockchain network...")
        
        # Simulate processing
        print("✅ Cryptocurrency payment processed successfully")
        return True
    
    def get_transaction_fee(self, amount):
        """Crypto fee: 1% flat rate"""
        return round(amount * 0.01, 2)


# =============================================================================
# 3. SHAPE ABSTRACTION WITH TEMPLATE METHOD
# =============================================================================

class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    Demonstrates template method pattern.
    """
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def calculate_area(self):
        """Abstract method to calculate area."""
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        """Abstract method to calculate perimeter."""
        pass
    
    # Template method
    def describe_shape(self):
        """
        Template method that uses abstract methods.
        Provides a consistent interface for describing shapes.
        """
        print(f"\n📐 Shape Analysis: {self.name}")
        print(f"   Area: {self.calculate_area():.2f}")
        print(f"   Perimeter: {self.calculate_perimeter():.2f}")
        print(f"   Type: {self.__class__.__name__}")
        
        # Additional analysis
        area = self.calculate_area()
        if area > 100:
            print("   Size: Large shape")
        elif area > 25:
            print("   Size: Medium shape")
        else:
            print("   Size: Small shape")
    
    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"


class Rectangle(Shape):
    """Concrete rectangle implementation."""
    
    def __init__(self, width, height):
        super().__init__(f"Rectangle {width}x{height}")
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Concrete circle implementation."""
    
    def __init__(self, radius):
        super().__init__(f"Circle r={radius}")
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    """Concrete triangle implementation."""
    
    def __init__(self, side_a, side_b, side_c):
        super().__init__(f"Triangle {side_a}-{side_b}-{side_c}")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def calculate_area(self):
        # Using Heron's formula
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    
    def calculate_perimeter(self):
        return self.side_a + self.side_b + self.side_c


# =============================================================================
# 4. NOTIFICATION SYSTEM ABSTRACTION
# =============================================================================

class NotificationSender(ABC):
    """
    Abstract base class for different notification methods.
    Demonstrates strategy pattern with abstraction.
    """
    
    @abstractmethod
    def send_notification(self, recipient, subject, message):
        """Send notification - implementation varies by type."""
        pass
    
    @abstractmethod
    def validate_recipient(self, recipient):
        """Validate recipient format - varies by notification type."""
        pass
    
    def notify(self, recipient, subject, message):
        """Template method for sending notifications."""
        print(f"\n📢 Preparing {self.__class__.__name__} notification...")
        
        if not self.validate_recipient(recipient):
            print("❌ Invalid recipient format")
            return False
        
        success = self.send_notification(recipient, subject, message)
        
        if success:
            print(f"✅ Notification sent successfully to {recipient}")
        else:
            print(f"❌ Failed to send notification to {recipient}")
        
        return success


class EmailSender(NotificationSender):
    """Concrete email notification sender."""
    
    def validate_recipient(self, recipient):
        """Email validation."""
        return '@' in recipient and '.' in recipient
    
    def send_notification(self, recipient, subject, message):
        """Email sending implementation."""
        print(f"📧 Sending email to: {recipient}")
        print(f"   Subject: {subject}")
        print(f"   Message: {message[:50]}...")
        
        # Simulate email sending
        return True


class SMSSender(NotificationSender):
    """Concrete SMS notification sender."""
    
    def validate_recipient(self, recipient):
        """Phone number validation."""
        return recipient.replace('+', '').replace('-', '').replace(' ', '').isdigit()
    
    def send_notification(self, recipient, subject, message):
        """SMS sending implementation."""
        print(f"📱 Sending SMS to: {recipient}")
        print(f"   Message: {subject}: {message[:100]}...")
        
        # Simulate SMS sending
        return True


class PushNotificationSender(NotificationSender):
    """Concrete push notification sender."""
    
    def validate_recipient(self, recipient):
        """Device token validation."""
        return len(recipient) > 20  # Simplified device token validation
    
    def send_notification(self, recipient, subject, message):
        """Push notification implementation."""
        print(f"📲 Sending push notification to device: {recipient[:20]}...")
        print(f"   Title: {subject}")
        print(f"   Body: {message[:80]}...")
        
        # Simulate push notification
        return True


# =============================================================================
# 5. PROTOCOL-BASED ABSTRACTION (Python 3.8+)
# =============================================================================

class Drawable(Protocol):
    """
    Protocol for drawable objects.
    Demonstrates structural typing (duck typing with type hints).
    """
    
    def draw(self) -> str:
        """Draw the object."""
        ...
    
    def get_color(self) -> str:
        """Get the object's color."""
        ...


class Square:
    """Square class that implements Drawable protocol."""
    
    def __init__(self, size, color="blue"):
        self.size = size
        self.color = color
    
    def draw(self) -> str:
        return f"Drawing a {self.color} square of size {self.size}"
    
    def get_color(self) -> str:
        return self.color


class Star:
    """Star class that implements Drawable protocol."""
    
    def __init__(self, points, color="yellow"):
        self.points = points
        self.color = color
    
    def draw(self) -> str:
        return f"Drawing a {self.color} {self.points}-pointed star"
    
    def get_color(self) -> str:
        return self.color


def render_drawable(drawable: Drawable):
    """Function that works with any Drawable object."""
    print(f"🎨 {drawable.draw()}")
    print(f"   Color: {drawable.get_color()}")


# =============================================================================
# DEMONSTRATION FUNCTIONS
# =============================================================================

def demonstrate_vehicle_abstraction():
    """Demonstrate basic abstraction with vehicles."""
    print("\n" + "="*60)
    print("VEHICLE ABSTRACTION DEMONSTRATION")
    print("="*60)
    
    # Cannot instantiate abstract class
    try:
        # vehicle = Vehicle("Generic", "Vehicle", 2023)  # This would fail
        pass
    except TypeError as e:
        print(f"❌ Cannot instantiate abstract class: {e}")
    
    # Create concrete vehicles
    car = Car("Toyota", "Camry", 2023)
    motorcycle = Motorcycle("Honda", "CBR", 2023)
    electric_car = ElectricCar("Tesla", "Model 3", 2023)
    
    vehicles = [car, motorcycle, electric_car]
    
    # Demonstrate polymorphism through common interface
    print(f"\n🚗 Vehicle Operations:")
    for vehicle in vehicles:
        print(f"\n{vehicle}")
        vehicle.start_engine()
        print(f"   Max Speed: {vehicle.get_max_speed()} km/h")
        print(f"   Fuel Level: {vehicle.get_fuel_level()}%")
        vehicle.stop_engine()
    
    # Demonstrate specific methods
    car.open_trunk()
    motorcycle.wheelie()
    electric_car.charge_battery(2)


def demonstrate_payment_abstraction():
    """Demonstrate abstraction in payment processing."""
    print("\n" + "="*60)
    print("PAYMENT PROCESSING ABSTRACTION DEMONSTRATION")
    print("="*60)
    
    # Create different payment processors
    credit_processor = CreditCardProcessor("MERCHANT_001")
    paypal_processor = PayPalProcessor("MERCHANT_002")
    crypto_processor = CryptoProcessor("MERCHANT_003")
    
    # Payment information for different methods
    credit_payment = {
        'type': 'credit_card',
        'card_number': '4532123456789012',
        'expiry': '12/25',
        'cvv': '123',
        'cardholder_name': 'John Doe'
    }
    
    paypal_payment = {
        'type': 'paypal',
        'email': 'john.doe@email.com'
    }
    
    crypto_payment = {
        'type': 'cryptocurrency',
        'wallet_address': '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa',
        'currency_type': 'Bitcoin'
    }
    
    processors = [
        (credit_processor, credit_payment),
        (paypal_processor, paypal_payment),
        (crypto_processor, crypto_payment)
    ]
    
    # Process payments using the same interface
    amount = 100.00
    for processor, payment_info in processors:
        processor.execute_payment(amount, payment_info)
    
    # Show transaction histories
    print(f"\n📊 Transaction Summaries:")
    for processor, _ in processors:
        history = processor.get_transaction_history()
        print(f"{processor.__class__.__name__}: {len(history)} transactions")


def demonstrate_shape_abstraction():
    """Demonstrate template method pattern with shapes."""
    print("\n" + "="*60)
    print("SHAPE ABSTRACTION DEMONSTRATION")
    print("="*60)
    
    # Create different shapes
    rectangle = Rectangle(10, 5)
    circle = Circle(7)
    triangle = Triangle(3, 4, 5)
    
    shapes = [rectangle, circle, triangle]
    
    # Use the same interface for all shapes
    for shape in shapes:
        shape.describe_shape()
    
    # Calculate total area
    total_area = sum(shape.calculate_area() for shape in shapes)
    print(f"\n📊 Total area of all shapes: {total_area:.2f}")


def demonstrate_notification_abstraction():
    """Demonstrate strategy pattern with notifications."""
    print("\n" + "="*60)
    print("NOTIFICATION SYSTEM ABSTRACTION DEMONSTRATION")
    print("="*60)
    
    # Create different notification senders
    email_sender = EmailSender()
    sms_sender = SMSSender()
    push_sender = PushNotificationSender()
    
    # Notification details
    recipients = [
        ("john@example.com", email_sender),
        ("+1-555-123-4567", sms_sender),
        ("device_token_abc123def456ghi789jkl012mno345pqr678", push_sender)
    ]
    
    subject = "Important Update"
    message = "Your account has been successfully updated with the new security features."
    
    # Send notifications using the same interface
    for recipient, sender in recipients:
        sender.notify(recipient, subject, message)


def demonstrate_protocol_abstraction():
    """Demonstrate protocol-based abstraction."""
    print("\n" + "="*60)
    print("PROTOCOL-BASED ABSTRACTION DEMONSTRATION")
    print("="*60)
    
    # Create objects that implement the Drawable protocol
    square = Square(5, "red")
    star = Star(6, "gold")
    
    drawables = [square, star]
    
    # Use the same interface for all drawable objects
    for drawable in drawables:
        render_drawable(drawable)


def main():
    """Main function to demonstrate all abstraction concepts."""
    print("🎭 ABSTRACTION IN PYTHON - COMPREHENSIVE DEMONSTRATION")
    print("=" * 70)
    
    demonstrate_vehicle_abstraction()
    demonstrate_payment_abstraction()
    demonstrate_shape_abstraction()
    demonstrate_notification_abstraction()
    demonstrate_protocol_abstraction()
    
    print("\n" + "="*70)
    print("📋 ABSTRACTION SUMMARY")
    print("="*70)
    print("✅ Hide Complexity: Abstract classes hide implementation details")
    print("✅ Common Interface: Same methods work on different objects")
    print("✅ Enforce Standards: Abstract methods must be implemented")
    print("✅ Template Methods: Common algorithms with varying implementations")
    print("✅ Polymorphism: Different objects, same interface")
    print("✅ Maintainability: Easy to add new implementations")
    
    print("\n🎯 Key Takeaways:")
    print("• Abstract base classes define contracts for subclasses")
    print("• Template methods provide consistent workflows")
    print("• Strategy pattern allows interchangeable implementations")
    print("• Protocols enable structural typing (duck typing)")
    print("• Abstraction simplifies complex systems")
    print("• Focus on 'what' rather than 'how'")


if __name__ == "__main__":
    main()
