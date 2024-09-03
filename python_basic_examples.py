# Defining a function with default arguments and type hints
def greet(name: str = "world", times: int = 1) -> None:
    """Print a greeting a specified number of times."""
    for _ in range(times):
        print(f"Hello, {name}!")

greet("Alice", 3)



# Lambda function to square a number
square = lambda x: x * x
print(square(5))  # Output: 25

# List comprehension with a lambda function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]



# Mutable vs Immutable examples
immutable_tuple = (1, 2, 3)
mutable_list = [1, 2, 3]

# Attempting to change elements
# immutable_tuple[1] = 4  # This will raise a TypeError

mutable_list[1] = 4  # This is allowed
print(mutable_list)  # Output: [1, 4, 3]



# Conditional Statements and Loops
def process_numbers(numbers: list[int]) -> list[int]:
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num ** 2)  # Square even numbers
        elif num % 2 != 0:
            continue  # Skip odd numbers
    return result

print(process_numbers([1, 2, 3, 4, 5]))  # Output: [4, 16]



# Custom Exception
class CustomError(Exception):
    pass

def risky_division(a: int, b: int) -> float:
    try:
        if b == 0:
            raise CustomError("Division by zero is not allowed.")
        return a / b
    except CustomError as e:
        print(e)
        return float('inf')  # Return infinity as a placeholder

print(risky_division(10, 2))  # Output: 5.0
print(risky_division(10, 0))  # Output: Division by zero is not allowed. \n inf



# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, file!\n")
    file.write("This is a sample text.")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)  # Output: Hello, file! \n This is a sample text.



# Json
import json

# Convert a dictionary to JSON string
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
json_string = json.dumps(data)
print(json_string)  # Output: {"name": "Alice", "age": 30, "city": "New York"}

# Convert JSON string back to a dictionary
parsed_data = json.loads(json_string)
print(parsed_data)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}



# Inheritance
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError("Subclasses must implement this method.")

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says Meow!"

animals = [Dog("Rex"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())  # Output: Rex says Woof! \n Whiskers says Meow!






# ABC
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Abstract method to calculate the area of the shape."""
        pass

    def description(self) -> str:
        """Concrete method to return a description of the shape."""
        return f"This is a {self.__class__.__name__}."

# Note: We cannot instantiate the Shape class directly because it has an abstract method.

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.width * self.height

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)

shapes = [circle, rectangle]
for shape in shapes:
    print(f"{shape.description()} Area: {shape.area()}")

