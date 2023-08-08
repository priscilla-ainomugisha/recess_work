#Exercise 1
#demonstarte using inheritance to calculate area and perimeter of a circle and rectangle 
#use shape as the base class
"""import math

class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculating the area and perimeter
circle_area = circle.calculate_area()
circle_perimeter = circle.calculate_perimeter()

rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()

# Printing the results
print("Circle Area:", circle_area)
print("Circle Perimeter:", circle_perimeter)
print("Rectangle Area:", rectangle_area)
print("Rectangle Perimeter:", rectangle_perimeter)

#Example 3'
#multiple inheritance
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name}is eating..")

class Flyable:
    def fly(self):
        print(f"{self.name}is flying...")
    
class Bird(Animal,Flyable):
    def __init__(self, name,wingse):
        super().__init__(name)
        self.species = species

    def display_info(self):
        super().display_info()
        print(f"Species: {self.species}")
        print(f"Name: {self.name}")

#Create a bird object
my_bird = Bird("pigeon","bird")

#invoke the bird methods
print(my_bird.display_info())
my_bird.eat()
my_bird.fly()

# Method Overriding
class Animal:
    def make_sound(self):
        print("Animal is making as ound")

class Dog(Animal):
    def make_sound(self):
        print("Dog is barking")
    
class Cat(Animal):
    def make_sound(self):
        print("Cat is meowing")
def make_animal_sound(animal):
    animal.make_sound()

#create objects
animal = Animal()
dog = Dog()
cat =Cat()

#Calling make_animal_sound function
make_animal_sound(animal)
make_animal_sound(dog)
make_animal_sound(cat)

#Polymorphism
#It allows you too write code that can work with different types of objects

#Method overriding
#Method overloading allows a class to have multiple metods with the same name but
#different parameters

# Exercise 2
#Demonstrate abstraction using calculating area of a circle and rectangle 
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

circle = Circle(5)
print("Area of the circle:", circle.area())

rectangle = Rectangle(4, 6)
print("Area of the rectangle:", rectangle.area())"""
print("================================================================")
print("ASSIGNMENT")

import tkinter as tk

class ReceiptGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Receipt Generator")

        self.items = []
        self.prices = []

        # Product details
        self.p1_name, self.p1_price = "Bread", 4500
        self.p2_name, self.p2_price = "Milk", 1700
        self.p3_name, self.p3_price = "Eggs", 6500

        # Receipt Header
        self.company_name = "Mega Standard Supermarket"
        self.company_address = "Old taxi Park"
        self.company_city = "Kampala, Uganda"

        # Receipt Footer
        self.message = "Goods once sold cannot be returned\nThanks for shopping with Mega Standard Supermarket!\n"

        self.header_label = tk.Label(root, text=self.get_header(), justify=tk.CENTER)
        self.header_label.pack()

        self.line_label = tk.Label(root, text="-" * 50, justify=tk.CENTER)
        self.line_label.pack()

        self.items_label = tk.Label(root, text="\tProduct Name\tProduct Price")
        self.items_label.pack()

        self.add_product(self.p1_name, self.p1_price)
        self.add_product(self.p2_name, self.p2_price)
        self.add_product(self.p3_name, self.p3_price)

        self.line_label = tk.Label(root, text="=" * 50, justify=tk.CENTER)
        self.line_label.pack()

        self.total_label = tk.Label(root, text=self.get_total(), justify=tk.CENTER)
        self.total_label.pack()

        self.line_label = tk.Label(root, text="=" * 50, justify=tk.CENTER)
        self.line_label.pack()

        self.footer_label = tk.Label(root, text=self.message, justify=tk.CENTER)
        self.footer_label.pack()

        self.line_label = tk.Label(root, text="*" * 50, justify=tk.CENTER)
        self.line_label.pack()

    def get_header(self):
        header = f"\t\t{self.company_name.title()}\n"
        header += f"\t\t{self.company_address}\n"
        header += f"\t\t{self.company_city}"
        return header

    def add_product(self, name, price):
        self.items.append(name)
        self.prices.append(price)

        product_label = tk.Label(self.root, text=f"\t{name.title()}\t\tUGX{price}")
        product_label.pack()

    def get_total(self):
        total_price = sum(self.prices)
        total = f"\t\t\tTotal\n"
        total += f"\t\t\tUGX{total_price}"
        return total

if __name__ == "__main__":
    root = tk.Tk()
    app = ReceiptGenerator(root)
    root.mainloop()
