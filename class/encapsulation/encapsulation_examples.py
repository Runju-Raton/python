"""
Encapsulation in Python - Comprehensive Examples
===============================================

This file demonstrates encapsulation concepts with practical examples:
- Public, protected, and private attributes
- Property decorators for controlled access
- Data validation and protection
- Real-world encapsulation scenarios
"""

from datetime import datetime
import re


class BankAccount:
    """
    Comprehensive example of encapsulation in a banking system.
    Demonstrates data protection, validation, and controlled access.
    """
    
    # Class variable (public)
    bank_name = "SecureBank"
    
    def __init__(self, account_holder, initial_balance=0, account_type="Savings"):
        # Public attributes (can be accessed directly)
        self.account_holder = account_holder
        self.account_type = account_type
        self.created_at = datetime.now()
        
        # Protected attributes (intended for internal use, indicated by single underscore)
        self._account_number = self._generate_account_number()
        self._transaction_history = []
        
        # Private attributes (name mangled, indicated by double underscore)
        self.__balance = 0
        self.__pin = None
        self.__is_frozen = False
        
        # Initialize balance through property to ensure validation
        self.balance = initial_balance
        
        print(f"✅ Account created for {account_holder}")
        print(f"   Account Number: {self._account_number}")
        print(f"   Initial Balance: ${self.__balance}")
    
    def _generate_account_number(self):
        """
        Protected method to generate account number.
        Should only be used internally by the class.
        """
        import random
        return f"ACC{random.randint(100000, 999999)}"
    
    def __validate_amount(self, amount):
        """
        Private method to validate monetary amounts.
        Only accessible within this class.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return True
    
    # Property for balance - provides controlled access
    @property
    def balance(self):
        """
        Getter for balance - allows read access.
        This is the public interface for accessing balance.
        """
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        """
        Setter for balance with validation.
        Ensures only valid amounts can be set.
        """
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount
        self._log_transaction(f"Balance set to ${amount}")
    
    # Property for account number (read-only)
    @property
    def account_number(self):
        """
        Read-only access to account number.
        No setter provided, so it cannot be modified externally.
        """
        return self._account_number
    
    # Property for PIN with validation
    @property
    def pin(self):
        """
        PIN property - only returns masked version for security.
        """
        return "****" if self.__pin else "Not Set"
    
    @pin.setter
    def pin(self, value):
        """
        PIN setter with validation.
        Ensures PIN meets security requirements.
        """
        if not isinstance(value, str):
            raise TypeError("PIN must be a string")
        
        if len(value) != 4 or not value.isdigit():
            raise ValueError("PIN must be exactly 4 digits")
        
        self.__pin = value
        self._log_transaction("PIN updated")
        print("🔐 PIN successfully set")
    
    def _log_transaction(self, transaction):
        """
        Protected method to log transactions.
        Used internally by other methods.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._transaction_history.append(f"{timestamp}: {transaction}")
    
    def deposit(self, amount):
        """
        Public method to deposit money.
        Uses private validation and protected logging.
        """
        if self.__is_frozen:
            raise Exception("Account is frozen")
        
        self.__validate_amount(amount)
        self.__balance += amount
        self._log_transaction(f"Deposited ${amount}")
        
        print(f"💰 Deposited ${amount}. New balance: ${self.__balance}")
        return self.__balance
    
    def withdraw(self, amount):
        """
        Public method to withdraw money.
        Includes validation and balance checking.
        """
        if self.__is_frozen:
            raise Exception("Account is frozen")
        
        self.__validate_amount(amount)
        
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        
        self.__balance -= amount
        self._log_transaction(f"Withdrew ${amount}")
        
        print(f"💸 Withdrew ${amount}. New balance: ${self.__balance}")
        return self.__balance
    
    def transfer(self, amount, target_account):
        """
        Public method to transfer money to another account.
        """
        if self.__is_frozen:
            raise Exception("Account is frozen")
        
        # Withdraw from this account
        self.withdraw(amount)
        
        # Deposit to target account
        target_account.deposit(amount)
        
        self._log_transaction(f"Transferred ${amount} to {target_account.account_number}")
        print(f"💸➡️💰 Transferred ${amount} to account {target_account.account_number}")
    
    def freeze_account(self, admin_pin="ADMIN123"):
        """
        Public method to freeze account (admin function).
        """
        if admin_pin != "ADMIN123":
            raise ValueError("Invalid admin credentials")
        
        self.__is_frozen = True
        self._log_transaction("Account frozen")
        print("🧊 Account has been frozen")
    
    def unfreeze_account(self, admin_pin="ADMIN123"):
        """
        Public method to unfreeze account (admin function).
        """
        if admin_pin != "ADMIN123":
            raise ValueError("Invalid admin credentials")
        
        self.__is_frozen = False
        self._log_transaction("Account unfrozen")
        print("🔓 Account has been unfrozen")
    
    def get_transaction_history(self, pin=None):
        """
        Public method to get transaction history.
        Requires PIN for security.
        """
        if pin != self.__pin:
            raise ValueError("Invalid PIN")
        
        return self._transaction_history.copy()  # Return copy to prevent external modification
    
    def get_account_info(self):
        """
        Public method to get basic account information.
        Excludes sensitive data.
        """
        return {
            'holder': self.account_holder,
            'account_number': self._account_number,
            'account_type': self.account_type,
            'balance': self.__balance,
            'created_at': self.created_at.strftime("%Y-%m-%d"),
            'is_frozen': self.__is_frozen
        }
    
    def __str__(self):
        """Public interface for string representation."""
        status = "🧊 FROZEN" if self.__is_frozen else "✅ ACTIVE"
        return f"BankAccount({self.account_holder}, {self._account_number}, ${self.__balance}) - {status}"
    
    def __repr__(self):
        """Developer representation."""
        return f"BankAccount(account_holder='{self.account_holder}', initial_balance={self.__balance})"


class Student:
    """
    Example demonstrating encapsulation in an educational context.
    Shows how to protect student data and provide controlled access.
    """
    
    def __init__(self, name, student_id, email):
        # Public attributes
        self.name = name
        self.enrollment_date = datetime.now()
        
        # Protected attributes
        self._student_id = student_id
        self._email = email
        
        # Private attributes
        self.__grades = {}
        self.__gpa = 0.0
        self.__is_active = True
        
        print(f"📚 Student enrolled: {name} (ID: {student_id})")
    
    @property
    def student_id(self):
        """Read-only student ID."""
        return self._student_id
    
    @property
    def email(self):
        """Email property with validation."""
        return self._email
    
    @email.setter
    def email(self, value):
        """Email setter with validation."""
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, value):
            raise ValueError("Invalid email format")
        self._email = value
        print(f"✉️ Email updated to: {value}")
    
    @property
    def gpa(self):
        """Read-only GPA calculation."""
        return self.__gpa
    
    @property
    def is_active(self):
        """Read-only active status."""
        return self.__is_active
    
    def add_grade(self, subject, grade):
        """
        Public method to add grades with validation.
        """
        if not self.__is_active:
            raise Exception("Cannot add grades to inactive student")
        
        if not isinstance(grade, (int, float)):
            raise TypeError("Grade must be a number")
        
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100")
        
        self.__grades[subject] = grade
        self.__calculate_gpa()
        
        print(f"📊 Grade added: {subject} = {grade}")
        print(f"📈 Updated GPA: {self.__gpa:.2f}")
    
    def __calculate_gpa(self):
        """
        Private method to calculate GPA.
        Only called internally when grades change.
        """
        if not self.__grades:
            self.__gpa = 0.0
            return
        
        total_points = sum(self.__grades.values())
        self.__gpa = total_points / len(self.__grades)
    
    def get_grades(self, requesting_user_type="student"):
        """
        Get grades with different access levels based on user type.
        """
        if requesting_user_type == "student":
            # Students see their grades and GPA
            return {
                'grades': self.__grades.copy(),
                'gpa': self.__gpa
            }
        elif requesting_user_type == "teacher":
            # Teachers see detailed breakdown
            return {
                'student_id': self._student_id,
                'grades': self.__grades.copy(),
                'gpa': self.__gpa,
                'total_subjects': len(self.__grades)
            }
        else:
            raise ValueError("Unauthorized access")
    
    def deactivate_student(self, admin_reason=""):
        """
        Deactivate student account (admin function).
        """
        self.__is_active = False
        print(f"🚫 Student {self.name} has been deactivated")
        if admin_reason:
            print(f"   Reason: {admin_reason}")
    
    def __str__(self):
        status = "✅ ACTIVE" if self.__is_active else "🚫 INACTIVE"
        return f"Student({self.name}, ID: {self._student_id}, GPA: {self.__gpa:.2f}) - {status}"


class TemperatureSensor:
    """
    Example of encapsulation in IoT/sensor context.
    Demonstrates data validation and computed properties.
    """
    
    def __init__(self, sensor_id, location):
        self.sensor_id = sensor_id
        self.location = location
        
        # Protected attributes
        self._calibration_offset = 0.0
        self._last_reading_time = None
        
        # Private attributes
        self.__raw_celsius = 20.0  # Default room temperature
        self.__is_calibrated = False
        self.__error_count = 0
        
        print(f"🌡️ Temperature sensor initialized: {sensor_id} at {location}")
    
    @property
    def celsius(self):
        """Get temperature in Celsius with calibration applied."""
        return self.__raw_celsius + self._calibration_offset
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("Temperature must be a number")
        
        # Reasonable temperature range check (-100°C to 200°C)
        if not (-100 <= value <= 200):
            self.__error_count += 1
            raise ValueError("Temperature out of reasonable range (-100°C to 200°C)")
        
        self.__raw_celsius = value
        self._last_reading_time = datetime.now()
        print(f"🌡️ Temperature reading: {self.celsius:.1f}°C")
    
    @property
    def fahrenheit(self):
        """Computed property: Celsius to Fahrenheit conversion."""
        return (self.celsius * 9/5) + 32
    
    @property
    def kelvin(self):
        """Computed property: Celsius to Kelvin conversion."""
        return self.celsius + 273.15
    
    @property
    def last_reading_time(self):
        """Read-only access to last reading time."""
        return self._last_reading_time
    
    @property
    def error_count(self):
        """Read-only access to error count."""
        return self.__error_count
    
    def calibrate(self, known_temperature, admin_key="CALIBRATE"):
        """
        Calibrate the sensor against a known temperature.
        """
        if admin_key != "CALIBRATE":
            raise ValueError("Invalid calibration key")
        
        current_reading = self.__raw_celsius
        self._calibration_offset = known_temperature - current_reading
        self.__is_calibrated = True
        
        print(f"🔧 Sensor calibrated. Offset: {self._calibration_offset:.2f}°C")
    
    def get_sensor_status(self):
        """Get comprehensive sensor status."""
        return {
            'sensor_id': self.sensor_id,
            'location': self.location,
            'current_celsius': self.celsius,
            'current_fahrenheit': self.fahrenheit,
            'current_kelvin': self.kelvin,
            'is_calibrated': self.__is_calibrated,
            'error_count': self.__error_count,
            'last_reading': self._last_reading_time
        }


def demonstrate_public_protected_private():
    """Demonstrate different access levels."""
    print("\n" + "="*60)
    print("PUBLIC, PROTECTED, PRIVATE ACCESS DEMONSTRATION")
    print("="*60)
    
    account = BankAccount("Alice Johnson", 1000)
    
    # PUBLIC ACCESS (✅ Works)
    print(f"\n📋 PUBLIC ACCESS:")
    print(f"   Account Holder: {account.account_holder}")  # Public attribute
    print(f"   Bank Name: {account.bank_name}")            # Class attribute
    print(f"   Balance: ${account.balance}")               # Public property
    
    # PROTECTED ACCESS (⚠️ Works but shouldn't be used externally)
    print(f"\n⚠️ PROTECTED ACCESS (not recommended):")
    print(f"   Account Number: {account._account_number}")      # Protected attribute
    print(f"   Transaction History Length: {len(account._transaction_history)}")  # Protected attribute
    
    # PRIVATE ACCESS (❌ Won't work as expected)
    print(f"\n❌ PRIVATE ACCESS (demonstrates name mangling):")
    try:
        print(f"   Direct __balance access: {account.__balance}")  # This will fail
    except AttributeError as e:
        print(f"   Error: {e}")
    
    # Private access through name mangling (not recommended)
    try:
        mangled_name = f"_BankAccount__balance"
        private_balance = getattr(account, mangled_name)
        print(f"   Name-mangled access: ${private_balance}")
    except AttributeError:
        print("   Name-mangled access also failed")


def demonstrate_properties():
    """Demonstrate property decorators for controlled access."""
    print("\n" + "="*60)
    print("PROPERTY DECORATORS DEMONSTRATION")
    print("="*60)
    
    account = BankAccount("Bob Smith", 500)
    
    # Property getter
    print(f"💰 Balance (via property): ${account.balance}")
    
    # Property setter with validation
    try:
        account.balance = 1500  # Valid
        print(f"✅ Balance updated to: ${account.balance}")
    except ValueError as e:
        print(f"❌ Error: {e}")
    
    try:
        account.balance = -100  # Invalid
    except ValueError as e:
        print(f"❌ Validation error: {e}")
    
    # Read-only property
    print(f"🔢 Account Number (read-only): {account.account_number}")
    
    # PIN property with masking
    print(f"🔐 PIN status: {account.pin}")
    account.pin = "1234"
    print(f"🔐 PIN after setting: {account.pin}")


def demonstrate_data_validation():
    """Demonstrate data validation through encapsulation."""
    print("\n" + "="*60)
    print("DATA VALIDATION DEMONSTRATION")
    print("="*60)
    
    # Create student with validation
    student = Student("Emma Wilson", "STU001", "emma@university.edu")
    
    # Valid operations
    student.add_grade("Mathematics", 95)
    student.add_grade("Physics", 88)
    student.add_grade("Chemistry", 92)
    
    # Invalid grade attempt
    try:
        student.add_grade("Biology", 150)  # Invalid grade
    except ValueError as e:
        print(f"❌ Validation error: {e}")
    
    # Email validation
    try:
        student.email = "invalid-email"
    except ValueError as e:
        print(f"❌ Email validation error: {e}")
    
    student.email = "emma.wilson@university.edu"  # Valid email
    
    print(f"📊 Final student info: {student}")


def demonstrate_computed_properties():
    """Demonstrate computed properties."""
    print("\n" + "="*60)
    print("COMPUTED PROPERTIES DEMONSTRATION")
    print("="*60)
    
    sensor = TemperatureSensor("TEMP001", "Living Room")
    
    # Set temperature and see computed properties
    sensor.celsius = 25.0
    
    print(f"🌡️ Temperature Readings:")
    print(f"   Celsius: {sensor.celsius:.1f}°C")
    print(f"   Fahrenheit: {sensor.fahrenheit:.1f}°F")
    print(f"   Kelvin: {sensor.kelvin:.1f}K")
    
    # Calibrate sensor
    sensor.calibrate(24.5)  # Assume actual temperature is 24.5°C
    
    print(f"\n🔧 After Calibration:")
    print(f"   Celsius: {sensor.celsius:.1f}°C")
    print(f"   Fahrenheit: {sensor.fahrenheit:.1f}°F")
    print(f"   Kelvin: {sensor.kelvin:.1f}K")


def demonstrate_secure_operations():
    """Demonstrate secure operations using encapsulation."""
    print("\n" + "="*60)
    print("SECURE OPERATIONS DEMONSTRATION")
    print("="*60)
    
    # Create two bank accounts
    account1 = BankAccount("Alice", 1000)
    account2 = BankAccount("Bob", 500)
    
    # Set PINs
    account1.pin = "1234"
    account2.pin = "5678"
    
    # Perform secure operations
    account1.deposit(200)
    account1.transfer(150, account2)
    
    # Try to access transaction history with wrong PIN
    try:
        history = account1.get_transaction_history("0000")  # Wrong PIN
    except ValueError as e:
        print(f"🔒 Security error: {e}")
    
    # Access with correct PIN
    history = account1.get_transaction_history("1234")
    print(f"\n📜 Transaction History (last 3):")
    for transaction in history[-3:]:
        print(f"   {transaction}")


def main():
    """Main function to demonstrate all encapsulation concepts."""
    print("🔒 ENCAPSULATION IN PYTHON - COMPREHENSIVE DEMONSTRATION")
    print("=" * 70)
    
    demonstrate_public_protected_private()
    demonstrate_properties()
    demonstrate_data_validation()
    demonstrate_computed_properties()
    demonstrate_secure_operations()
    
    print("\n" + "="*70)
    print("📋 ENCAPSULATION SUMMARY")
    print("="*70)
    print("✅ Data Protection: Private attributes prevent unauthorized access")
    print("✅ Validation: Properties ensure data integrity")
    print("✅ Controlled Access: Methods provide secure interfaces")
    print("✅ Clean API: Public methods hide implementation complexity")
    print("✅ Maintainability: Internal changes don't break external code")
    print("✅ Security: Sensitive operations require proper authentication")
    
    print("\n🎯 Key Takeaways:")
    print("• Use public attributes/methods for the class interface")
    print("• Use protected (_attribute) for internal implementation details")
    print("• Use private (__attribute) for sensitive data and name conflict prevention")
    print("• Properties provide Pythonic access control")
    print("• Validation should happen at the boundaries (setters, methods)")
    print("• Encapsulation makes code more robust, secure, and maintainable")


if __name__ == "__main__":
    main()
