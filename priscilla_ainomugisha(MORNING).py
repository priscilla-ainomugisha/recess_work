print("================================================================")
print("OPERATORS")
print("================================================================")
""""Logical NOT:'not'
-Assignment operators

"""

#Examples
#addition
x=50+45
print(x)
#subtraction
y=50-45
print(y)
#multiplication
z=50*45
print(z)
#Division
a=50/45
#Divide
b=50//3
print(b)
print(a)
#modulus
m=5%2
print(m)
#Exponention
n=20**5
print(m)
#Examples of comparison operators
#comparison operators
a=15
b=9

#greater than
if(a>b):
    print("a is greater than b")
    print(a>b)
#less than
if a<b:
    print("a is less than b")
    print(a<b)
#greater than or equal
if a>=b:
    print("a is greater than or equal to b")
    print(a>=b)
#less than or equal
if a<=b:
    print("a is less than or equal to b")
    print(a<=b)
#equal to
if a==b:
    print("a is equal to b")
    print(a==b)
#Not equal to
if a !=b: 
    print("a is not equal to b")
    print(a!=b)

    #Examples with LOGICAL OPERATORS
    a=True
    b=False
    #Logical AND
    print(a and b)

    #logical OR
    print(a or b)

    #Logical NOT
    print(not a)
    print(not b)
print("================================================================")
print("ASSIGNMENT operator")
print("================================================================")
#Assignment operators
#Compound assignment operators
a=5

#Add and Assign
a += 1
print(a)
#subtract and assign
b=5
b-=1
print(b)
#multiply and assign
c=4
c *=1
print (c)

#Divide and assign
d=10
d/=5
print (d)

#Modulus and assign#
e=13
e%=5
print (e)
#Exponential and assign
f=2
f**=4
print(f)
print("================================================================")
print("Membership operator")
print("================================================================")
#Membership asssignment operators
cars =['Jeep','Tesla','BMW','Rollsroyce']
if 'Jeep' in cars:
    print('Jeep is in the list')
    print('Tesla' in cars)
    print('Toyota' in cars)

#Identity operators
x=10
y=10
#is operator
print(x is y)
print(x is not y)
print(x==y)
print(x!=y)
print(x<y)
print(x<=y)

#List
z=[1,2,3,4,5,6,7,8,9,10,11,12]
w=[1,2,3,4,5,6,7,8,9,10,11,12]
print(z is not w)
print("================================================================")
print("BITWISE operator")
print("================================================================")
#Bitwise operator

#Bitwise operators are used to perform operations on individualbits on binary numbers 
#Bitwise AND(&):performs a bitwise and operation between the corresponding bits of two numbers
#Bitwise OR(|):performs a bitwise OR operation between the corresponding bits of two numbers
#Bitwise NOT(~):performs a bitwise NOT operation between the corresponding bits of two numbers#Bitwise XOR(^):performs a bitwise XOR operation between the corresponding bits of two numbers
#Bitwise left shift('<<):performs a bitwise left shift operation between the corresponding bits of two numbers
#Bitwise Rignht shift(>>):performs a bitwise right shift operation between the corresponding bits of two numbers

#Examples of bitwise operation
a=10 # 1010 in binary
b=20

#Bitwise And operations
result_and = a & b
print(result_and)
#Bitwise OR(|)
result_or = a | b
print(result_or)

result_xor = a ^ b
print(result_xor)

result_not = ~ b
print(result_not)

result_leftshift = a<<b
print(result_leftshift)

result_rightshift = a>>b
print(result_rightshift)




#Example and assignment
"""#Create a simple calculator function (add, subrtract,multiply,divide)
def add(a, b):
    return a+b
def subrtract(a, b):
    return a-b
def divide(a, b):
    return a/b
def multiply(a,b):
    return a*b

def main():
    print("Priscilla simple clculator")
    number1=float(input("Enter the first number"))
    number2=float(input("Enter the second number"))
    operator=float(input("Enter the operator'(+.-,*,/);")) 

    if operator=='+':
        result = add(number1,number2)
    elif operator=='-':
        result = subtract(number1,number2)
    elif operator=='*':
        result = multiply(number1,number2)
    elif operator=='/':
        result = divide(number1,number2)
    else:
        print ("Invalid operator")
        return
    print ("The result is :" + result)

if __name__ == "__main__":
  main()

print ("Addition:", add(a,b))
    print ("Subtraction:", subtract(a,b))
    print ("Division:", divide(a,b))
    print ("Multiplication:", multiply(a,b))"""
print("================================================================")
print("CALCULATOR")
print("================================================================")
#tkinter learn
#Assignment: create a simple calculator program  with a GUI interface.
#Make the title of the calculator program window with your name e.g Priscilla simple calculator
import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Priscilla's Simple Calculator")

# display box
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# number buttons
for i in range(1, 10):
    button = tk.Button(window, text=str(i), padx=20, pady=10, command=lambda i=i: button_click(i))
    button.grid(row=3 - (i-1)//3, column=(i-1)%3)

# extra buttons
button_0 = tk.Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0))
button_0.grid(row=4, column=0)
button_clear = tk.Button(window, text="C", padx=20, pady=10, command=button_clear)
button_clear.grid(row=4, column=1)
button_equal = tk.Button(window, text="=", padx=20, pady=10, command=button_equal)
button_equal.grid(row=4, column=2)

# operator buttons
button_add = tk.Button(window, text="+", padx=20, pady=10, command=lambda: button_click('+'))
button_add.grid(row=1, column=3)
button_subtract = tk.Button(window, text="-", padx=20, pady=10, command=lambda: button_click('-'))
button_subtract.grid(row=2, column=3)
button_multiply = tk.Button(window, text="*", padx=20, pady=10, command=lambda: button_click('*'))
button_multiply.grid(row=3, column=3)
button_divide = tk.Button(window, text="/", padx=20, pady=10, command=lambda: button_click('/'))
button_divide.grid(row=4, column=3)

# Start the main loop
window.mainloop()