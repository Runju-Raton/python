"""
Python Objects Demonstration
============================

This file demonstrates various aspects of Python objects, including:
- Object creation and usage
- Object identity and comparison
- Object attributes and methods
- Object lifecycle
- Built-in vs custom objects
- Object introspection
- Object relationships
"""

import gc
from datetime import datetime


class Person:
    """A class representing a person - demonstrates basic object concepts."""
    
    # Class variable (shared by all instances)
    species = "Homo sapiens"
    population = 0
    
    def __init__(self, name, age, email=None):
        """Initialize a Person object."""
        # Instance variables (unique to each object)
        self.name = name
        self.age = age
        self.email = email
        self.created_at = datetime.now()
        self._id = id(self)  # Store object's memory address
        
        # Increment population when new person is created
        Person.population += 1
        print(f"✓ Person object created: {self.name} (ID: {self._id})")
    
    def introduce(self):
        """Method to introduce the person."""
        intro = f"Hi! I'm {self.name}, {self.age} years old."
        if self.email:
            intro += f" You can reach me at {self.email}"
        return intro
    
    def have_birthday(self):
        """Method to increment age."""
        self.age += 1
        print(f"🎂 {self.name} is now {self.age} years old!")
    
    def get_object_info(self):
        """Return detailed information about this object."""
        return {
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'created_at': self.created_at,
            'object_id': self._id,
            'memory_address': hex(id(self)),
            'class_name': self.__class__.__name__,
            'module': self.__module__
        }
    
    # Special methods (dunder methods)
    def __str__(self):
        """String representation for end users."""
        return f"{self.name} ({self.age} years old)"
    
    def __repr__(self):
        """String representation for developers."""
        return f"Person(name='{self.name}', age={self.age}, email='{self.email}')"
    
    def __eq__(self, other):
        """Check equality based on name and age."""
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False
    
    def __del__(self):
        """Called when object is about to be destroyed."""
        Person.population -= 1
        print(f"🗑️  Person object destroyed: {self.name}")


class BankAccount:
    """Demonstrates object state management and encapsulation."""
    
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance  # Protected attribute
        self._transaction_history = []
        print(f"💰 Bank account created for {owner} with ${initial_balance}")
    
    @property
    def balance(self):
        """Read-only access to balance."""
        return self._balance
    
    def deposit(self, amount):
        """Deposit money to the account."""
        if amount > 0:
            self._balance += amount
            self._transaction_history.append(f"Deposited ${amount}")
            print(f"💵 Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("❌ Deposit amount must be positive")
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                self._transaction_history.append(f"Withdrew ${amount}")
                print(f"💸 Withdrew ${amount}. New balance: ${self._balance}")
            else:
                print("❌ Insufficient funds")
        else:
            print("❌ Withdrawal amount must be positive")
    
    def get_transaction_history(self):
        """Return transaction history."""
        return self._transaction_history.copy()
    
    def __str__(self):
        return f"Account owner: {self.owner}, Balance: ${self._balance}"


class ObjectFactory:
    """Demonstrates factory pattern - objects creating other objects."""
    
    @staticmethod
    def create_person(person_type, **kwargs):
        """Factory method to create different types of person objects."""
        if person_type == "adult":
            return Person(kwargs.get('name', 'Unknown'), 
                         kwargs.get('age', 18), 
                         kwargs.get('email'))
        elif person_type == "child":
            return Person(kwargs.get('name', 'Kid'), 
                         kwargs.get('age', 8))
        else:
            return Person(kwargs.get('name', 'Person'), 
                         kwargs.get('age', 25))


def demonstrate_object_identity():
    """Demonstrate object identity concepts."""
    print("\n" + "="*50)
    print("OBJECT IDENTITY DEMONSTRATION")
    print("="*50)
    
    # Create objects
    person1 = Person("Alice", 30)
    person2 = Person("Bob", 25)
    person3 = Person("Alice", 30)  # Same data as person1
    person4 = person1  # Same object as person1
    
    print(f"\n🔍 Object Identity Analysis:")
    print(f"person1 ID: {id(person1)}")
    print(f"person2 ID: {id(person2)}")
    print(f"person3 ID: {id(person3)}")
    print(f"person4 ID: {id(person4)}")
    
    print(f"\n🔍 Identity Comparison (is):")
    print(f"person1 is person2: {person1 is person2}")  # False (different objects)
    print(f"person1 is person3: {person1 is person3}")  # False (different objects)
    print(f"person1 is person4: {person1 is person4}")  # True (same object)
    
    print(f"\n🔍 Equality Comparison (==):")
    print(f"person1 == person2: {person1 == person2}")  # False (different data)
    print(f"person1 == person3: {person1 == person3}")  # True (same data)
    print(f"person1 == person4: {person1 == person4}")  # True (same object)
    
    return person1, person2, person3, person4


def demonstrate_object_attributes():
    """Demonstrate different types of object attributes."""
    print("\n" + "="*50)
    print("OBJECT ATTRIBUTES DEMONSTRATION")
    print("="*50)
    
    person = Person("Charlie", 28, "charlie@email.com")
    
    print(f"📋 Instance Attributes:")
    print(f"  Name: {person.name}")
    print(f"  Age: {person.age}")
    print(f"  Email: {person.email}")
    
    print(f"\n📋 Class Attributes:")
    print(f"  Species: {person.species}")
    print(f"  Population: {Person.population}")
    
    # Modify attributes
    person.age = 29
    person.city = "New York"  # Dynamic attribute addition
    print(f"\n📝 Modified Attributes:")
    print(f"  Age: {person.age}")
    print(f"  City: {person.city}")
    
    return person


def demonstrate_object_methods():
    """Demonstrate object methods."""
    print("\n" + "="*50)
    print("OBJECT METHODS DEMONSTRATION")
    print("="*50)
    
    person = Person("Diana", 35, "diana@email.com")
    
    print(f"🗣️  Introduction: {person.introduce()}")
    
    person.have_birthday()
    
    print(f"📊 Object Information:")
    info = person.get_object_info()
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    return person


def demonstrate_built_in_objects():
    """Demonstrate that everything in Python is an object."""
    print("\n" + "="*50)
    print("BUILT-IN OBJECTS DEMONSTRATION")
    print("="*50)
    
    # Numbers are objects
    num = 42
    print(f"📊 Number object: {num}")
    print(f"   Type: {type(num)}")
    print(f"   Methods: {[m for m in dir(num) if not m.startswith('_')][:5]}...")
    
    # Strings are objects
    text = "Hello, World!"
    print(f"\n📝 String object: {text}")
    print(f"   Type: {type(text)}")
    print(f"   Length: {len(text)}")
    print(f"   Uppercase: {text.upper()}")
    
    # Lists are objects
    my_list = [1, 2, 3, 4, 5]
    print(f"\n📋 List object: {my_list}")
    print(f"   Type: {type(my_list)}")
    print(f"   ID: {id(my_list)}")
    my_list.append(6)
    print(f"   After append: {my_list}")
    
    # Functions are objects
    def sample_function():
        pass
    
    print(f"\n🔧 Function object: {sample_function}")
    print(f"   Type: {type(sample_function)}")
    print(f"   Name: {sample_function.__name__}")


def demonstrate_object_introspection():
    """Demonstrate object introspection techniques."""
    print("\n" + "="*50)
    print("OBJECT INTROSPECTION DEMONSTRATION")
    print("="*50)
    
    person = Person("Eve", 27)
    
    print(f"🔍 Object Introspection for: {person}")
    
    # Check object type
    print(f"\n📋 Type Information:")
    print(f"   Type: {type(person)}")
    print(f"   Is Person: {isinstance(person, Person)}")
    print(f"   Is object: {isinstance(person, object)}")
    
    # List attributes and methods
    print(f"\n📋 Attributes and Methods:")
    attributes = [attr for attr in dir(person) if not attr.startswith('_')]
    print(f"   Public attributes/methods: {attributes}")
    
    # Check for specific attributes
    print(f"\n📋 Attribute Checks:")
    print(f"   Has 'name': {hasattr(person, 'name')}")
    print(f"   Has 'salary': {hasattr(person, 'salary')}")
    
    # Get attribute safely
    name = getattr(person, 'name', 'Unknown')
    salary = getattr(person, 'salary', 'Not specified')
    print(f"   Name: {name}")
    print(f"   Salary: {salary}")
    
    # Object dictionary
    print(f"\n📋 Object Dictionary:")
    if hasattr(person, '__dict__'):
        for key, value in person.__dict__.items():
            print(f"   {key}: {value}")


def demonstrate_object_composition():
    """Demonstrate object composition - objects containing other objects."""
    print("\n" + "="*50)
    print("OBJECT COMPOSITION DEMONSTRATION")
    print("="*50)
    
    # Create person and bank account objects
    person = Person("Frank", 40, "frank@email.com")
    account = BankAccount(person.name, 1000)
    
    # Add bank account to person (composition)
    person.bank_account = account
    
    print(f"👤 Person: {person}")
    print(f"💰 Account: {person.bank_account}")
    
    # Use composed objects
    person.bank_account.deposit(500)
    person.bank_account.withdraw(200)
    
    print(f"\n📊 Transaction History:")
    for transaction in person.bank_account.get_transaction_history():
        print(f"   {transaction}")


def demonstrate_object_lifecycle():
    """Demonstrate object creation and destruction."""
    print("\n" + "="*50)
    print("OBJECT LIFECYCLE DEMONSTRATION")
    print("="*50)
    
    print(f"👥 Initial population: {Person.population}")
    
    # Create objects
    print(f"\n🆕 Creating objects:")
    people = []
    for i in range(3):
        person = Person(f"Person{i+1}", 20+i)
        people.append(person)
    
    print(f"👥 Current population: {Person.population}")
    
    # Delete objects
    print(f"\n🗑️  Deleting objects:")
    for person in people:
        del person
    
    # Force garbage collection
    gc.collect()
    
    print(f"👥 Final population: {Person.population}")


def demonstrate_factory_pattern():
    """Demonstrate factory pattern for object creation."""
    print("\n" + "="*50)
    print("FACTORY PATTERN DEMONSTRATION")
    print("="*50)
    
    # Use factory to create different types of objects
    adult = ObjectFactory.create_person("adult", name="John", age=25, email="john@email.com")
    child = ObjectFactory.create_person("child", name="Emma", age=10)
    default = ObjectFactory.create_person("default", name="Jane")
    
    print(f"👨 Adult: {adult.introduce()}")
    print(f"👶 Child: {child.introduce()}")
    print(f"👤 Default: {default.introduce()}")


def main():
    """Main function to run all object demonstrations."""
    print("🐍 PYTHON OBJECTS COMPREHENSIVE DEMONSTRATION 🐍")
    print("=" * 60)
    
    # Run all demonstrations
    person1, person2, person3, person4 = demonstrate_object_identity()
    person_attr = demonstrate_object_attributes()
    person_method = demonstrate_object_methods()
    demonstrate_built_in_objects()
    demonstrate_object_introspection()
    demonstrate_object_composition()
    demonstrate_factory_pattern()
    demonstrate_object_lifecycle()
    
    # Final summary
    print("\n" + "="*60)
    print("📊 SUMMARY")
    print("="*60)
    print(f"✓ Objects are instances of classes")
    print(f"✓ Each object has identity, type, and value")
    print(f"✓ Objects can have attributes (data) and methods (behavior)")
    print(f"✓ Everything in Python is an object")
    print(f"✓ Objects can be composed of other objects")
    print(f"✓ Objects have a lifecycle: creation → usage → destruction")
    print(f"✓ Python provides tools for object introspection")
    print(f"✓ Objects enable code reusability and organization")
    
    print(f"\n🎯 Final population count: {Person.population}")
    print("✨ Object demonstration completed!")


if __name__ == "__main__":
    main()
