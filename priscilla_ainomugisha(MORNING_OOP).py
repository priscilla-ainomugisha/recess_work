#Day 4 -Object Oriented programming in python

#Key concepts in OOP:
"""
1.Class
2.Object
3.Encapsulation
4.Inheritance
5.Polymorphism
6.Abstractions
"""

print("============================================================")
print("CLASS")
print("============================================================")
#A class is a blue print for creating objects
#Example 1: Car
print("Class:Car")
class Car:
    def __init__(self, make, model,year):
        self.make = make
        self.model= model
        self.year = year
    
    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")

my_car =Car("Toyota","Corola",2022)#Creating object
print("Make:", my_car.make)
print("Model:", my_car.model)
print("Year:", str(my_car.year))
my_car.start_engine()
my_car.stop_engine()
print("______________________________________________________________________")
print("Class:Bank Account")

#Example 2: Bank Account
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
            self.balance=amount

    def withdraw(self,amount):
            if self.balance>= amount:
                self.balance -=amount
            else:
                print("Insufficient funds to withdraw")
            
    def display_balance(self):
            print("Account number:" , self.account_number)
            print("Balance:" , self.balance)

#Create a bank account object
my_account=BankAccount("123456789",1000)

#Perform operations on the bank account object
my_account.display_balance()#Output Account Number:123456789, balance 1000
my_account.deposit(500)
my_account.withdraw(100)
my_account.display_balance()#Output Account Number:123456789, balance 1300

#Example 4:Rectangle
print("______________________________________________________________________")
print("Class:Rectangle")
class Rectangle:
     def __init__(self,length,width):
          self.length = length
          self.width = width
     def calculate_area(self):
          return self.length*self.width
     def calculate_perimeter(self):
          return 2 * (self.length+self.width)
#create a Rectangle
my_rectangle=Rectangle(15,5)
print(my_rectangle.length)
print(my_rectangle.width)
#Calculate and display the area and perimeter
print(my_rectangle.calculate_area())
print(my_rectangle.calculate_perimeter())

#Example 3:Student
print("______________________________________________________________________")
print("Class:Student")

class Student:
     # create a consructor
     def __init__(self,name,year,course):
          self.name = name
          self.year = year
          self.course = course
    # create methods
     def display_details(self):
          print("Name: ", self.name)
          print("Year: ", self.year)
          print("Course: ", self.course)
        
# Create a Student
my_student = Student("Priscilla","Year 3","Software Engineering")

# Diplay student details
my_student.display_details()

# Example 5:Cirle 
print("______________________________________________________________________")
print("Class:Person")
# Object

class Person:
     def __init__(self,name,age):
          self.name = name
          self.age = age
     def greet(self):
          print("Hello,my name is: ", self.name)
          print("Iam", self.age, "years old")
#Create a peron objecy
my_person1 = Person("Jeff",35)
my_person2 = Person("Steve",20)

# access the person obeject atributes
print(my_person1.name)
print(my_person2.age)
print(my_person2.name)
print(my_person2.age)
#invoke methods
my_person1.greet()
my_person2.greet()

# Exercise 1:Calculate area and perimeter of triangle
print("______________________________________________________________________")
print("Class:Triangle")

class Triangle:
     def __init__(self,base,height,hypotunese):
          self.base = base
          self.height = height
          self.hypotunese = hypotunese
     def calculate_area(self):
          return 0.5*self.height*self.base
     def calculate_perimeter(self):
          return self.height + self.base + self.hypotunese
     
#Create a triangle
my_triangle = Triangle(1,3,2)
my_triangle2 = Triangle(3,3,3)

print(my_triangle.calculate_area())
print(my_triangle2.calculate_perimeter())

# Exercise 2:calculate and display employee bonus(15%) of salary (employee1:150000, employee2:230000)
print("______________________________________________________________________")
print("Class:Bonus")

class Employee_bonus:
     def __init__(self,name,salary):
          self.name = name
          self.salary = salary
     def bonus(self,salary):
          return (0.15 )*self.salary
        
     
    
#creating objects
employee1 = Employee_bonus("Zam",150000)
employee2 = Employee_bonus("zhun",230000)

print(employee1.name)
print(employee1.salary)
print(employee1.bonus(150000))
print(employee2.name)
print(employee2.salary)
print(employee2.bonus(230000))
print("============================================================")
print("ENCAPSULATION")
print("============================================================")
# main goal of encapsulation
"""
1. To hide the implementation of details of objects
2. to protect the object from changes
3. To protect the object from external changes
4. code organisation and modularity
"""
#Example with bank account
print("Class:Bank Account")
class BankAccount:
    def __init__(self,_account_number,_balance):
        self._account_number = _account_number#Encapsulates the account number
        self._balance = _balance

    def deposit(self,amount):
            self._balance +=amount # Encapsulates the deposit

    def withdraw(self,amount):
            if self._balance>= amount:
                self._balance -=amount
            else:
                print("Insufficient funds to withdraw")
            
    def display_balance(self):
            print("Account number:" , self._account_number)
            print("Balance:" , self._balance)
#create a bank object
my_account = BankAccount("123456789",1000)

#Access the object and modify encapsulated attributes indirectly
print(my_account._account_number)
print(my_account._balance)
my_account.deposit(500)
print(my_account._balance)
my_account.withdraw(100)
print(my_account._balance)

#Exercise 2: Convert temperature(37) from celcius to fahrenheit
print("______________________________________________________________________")

print("Temperature Exercise")
class TemperatureConverter:
    def __init__(self,_temperature):
        self._temperature = _temperature
    def to_celcius(self):
       return (self._temperature*9/5) + 32
    

my_temperature = TemperatureConverter(37)
print(my_temperature)
print(my_temperature.to_celcius())

"""Assignment :Show encapsulation with employee information to give a pay increment 
(salary with employee information to new salary e.g from 850000 to 1000000)"""
print("______________________________________________________________________")

print("Salary Increment Exercise")
class Employee:
    def __init__(self, name,salary):
        self._name = name
        self._salary = salary
     
    def get_name(self):
        return self._name
    def get_salary(self):
         return self._salary
    def set_salary(self,new_salary):
         self._salary = new_salary
    def apply_increment(self,increment_amount):
         self._salary += increment_amount

my_employee = Employee("Priscilla",200000)

print("Employee name:", my_employee.get_name())
print("Current salary:", my_employee.get_salary())

#Incrementing the salary
increment_amount =1000000
if (my_employee._salary < 500000):
    my_employee.apply_increment(increment_amount)
else:
     my_employee._salary = my_employee._salary
#Getting the incremented salary
print("New slary: ", my_employee.get_salary())
