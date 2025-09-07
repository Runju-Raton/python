# Encapsulation in Python - Complete Guide

## What is Encapsulation?

**Encapsulation** is one of the fundamental principles of Object-Oriented Programming (OOP). It refers to the bundling of data (attributes) and methods that operate on that data within a single unit (class), while restricting direct access to some of the object's components. This is a way of preventing accidental interference and misuse of the data.

## Key Concepts

### 1. Data Hiding
- Hide internal implementation details from the outside world
- Prevent direct access to sensitive data
- Control how data is accessed and modified

### 2. Access Control
Python uses naming conventions to indicate access levels:
- **Public**: `attribute` - Accessible from anywhere
- **Protected**: `_attribute` - Should only be accessed within the class and subclasses
- **Private**: `__attribute` - Should only be accessed within the class

### 3. Property Decorators
Use `@property`, `@setter`, and `@deleter` to control attribute access.

## Benefits of Encapsulation

1. **Data Protection**: Prevents unauthorized access and modification
2. **Code Maintainability**: Changes to internal implementation don't affect external code
3. **Validation**: Control how data is set and retrieved
4. **Debugging**: Easier to track where data is being modified
5. **Abstraction**: Hide complex implementation details

## Real-World Analogy

Think of encapsulation like a **car**:
- You interact with the car through its interface (steering wheel, pedals, gear shift)
- You don't directly manipulate the engine, transmission, or electrical systems
- The car's internal components are "encapsulated" and protected from direct access
- You can drive the car without knowing how the engine works internally

## Access Levels in Detail

### Public Attributes/Methods
```python
class Car:
    def __init__(self):
        self.brand = "Toyota"  # Public - can be accessed directly
    
    def start(self):  # Public method
        return "Car started"
```

### Protected Attributes/Methods
```python
class Car:
    def __init__(self):
        self._engine_type = "V6"  # Protected - intended for internal use
    
    def _check_engine(self):  # Protected method
        return "Engine OK"
```

### Private Attributes/Methods
```python
class Car:
    def __init__(self):
        self.__serial_number = "ABC123"  # Private - name mangled
    
    def __validate_key(self):  # Private method
        return True
```

## Property Decorators

Properties allow you to use methods like attributes:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """Getter method"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter method with validation"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        """Computed property"""
        return 3.14159 * self._radius ** 2
```

## When to Use Encapsulation

1. **Sensitive Data**: When you need to protect important data
2. **Data Validation**: When you need to validate input before setting attributes
3. **Computed Properties**: When attribute values need to be calculated
4. **API Design**: When you want to provide a clean interface to your class
5. **Future-proofing**: When you might need to change internal implementation later

## Best Practices

1. **Start with Public**: Make attributes public unless there's a reason not to
2. **Use Protected Wisely**: Use `_attribute` for internal implementation details
3. **Private When Necessary**: Use `__attribute` sparingly, mainly to prevent name conflicts
4. **Properties for Validation**: Use properties when you need to validate or compute values
5. **Document Access Levels**: Clearly document which attributes/methods are part of the public API

## Common Patterns

### 1. Getter/Setter Pattern
```python
class Temperature:
    def __init__(self):
        self._celsius = 0
    
    def get_celsius(self):
        return self._celsius
    
    def set_celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
```

### 2. Property Pattern (Pythonic)
```python
class Temperature:
    def __init__(self):
        self._celsius = 0
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
```

### 3. Read-Only Properties
```python
class Person:
    def __init__(self, name, birth_year):
        self._name = name
        self._birth_year = birth_year
    
    @property
    def name(self):
        return self._name  # Read-only, no setter
    
    @property
    def age(self):
        from datetime import datetime
        return datetime.now().year - self._birth_year
```

## Summary

Encapsulation is about:
- **Bundling** data and methods together
- **Controlling access** to object internals
- **Providing a clean interface** for object interaction
- **Protecting data integrity** through validation
- **Hiding implementation details** from external code

It's one of the most important principles for writing maintainable, robust Python code!
