def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

def add(a, b, c=0):
    return a + b + c

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
    def fetch(self, item):
        return f"{self.name} fetched the {item}!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def subtract(a, b):
    return a - b
