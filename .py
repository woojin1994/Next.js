def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Dog(Animal):
    def speak(self):
        return "Woof!"

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
