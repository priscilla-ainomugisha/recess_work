#regular expression
"""



""" 
# Matching and searching
# regex re.match(), re.search(), re.findall()

## Example 1 -Demonstrating regex | Match first word,group words,whole numbers
"""import re #module for regulaar expreession

text="hello , my name is Priscilla. Iam a 3rd year software Engineering student"

# Matching the first word
match = re.search(r"\b\w+\b", text)

if match:
    print("Match:",match.group())

# Matching numbers
matches = re.findall(r"\d+", text)
print("Matches:",matches)

## Example 2 -Validate email format for login screen
import re

def validate_email(email):
    pattern = r'^[\w\d+\.\-]+@[\w\.]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return "Invalid email"

email1="ainomugisha.priscilla@gmail.com"
email2="ainomugisha.priscilla@gmailcom"

print(validate_email(email1))
print(validate_email(email2))

# Generators and Iterators
# yield generator
# Iterator '__iter__' gen 
def factorial(n):
 if n == 0: 
   yield 1
 else: 
  # yield n * factorial(n-1)
   fact =1
   for i in range(1,n+1):
     fact *=i 
     yield fact
# Printing factorial of a number
for i in range(1,10):
   print(factorial(i))

##Example 3
def squares():
  for i in range(1,10):
    yield i **2
# create an iterator object that yoelds square numbers from 1 to 10

squares_iterator = squares()

# print the first 5 squares of numbers from 1 to 10
for i in range(5):
  print(next(squares_iterator))"""

# Decorators @my_decorator
# Decorators in Python allow you to modify the behaviour of the functions
# without directly changing their source code
def my_decorator(func):
  def inner():
    print("This is the decorator ")
    func()
  return inner()


@my_decorator
def outer_decorator():
  print("This is the decorator ")

outer_decorator()