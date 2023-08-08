#Exception handling
"""Exceptions are raised when the program is syntactically correct,
but the code results in an error. This error does not stop the execution
of the program, however, it changes the normal flow of the program. 
Syntax error is caused by the wrong syntax in the code. 
It leads to the termination of the program. 
"""
import datetime
participant=["Priscilla","Rachel","Alice","Bob"]
print(participant)
try:
    print("Enter Index of the user")
    choice = int(input())
    selected=participant[choice]

    print("Enter their year of entry")
    Year_of_Entry = datetime.datetime.strptime(input(), "%Y")
    Current_year = datetime.datetime.now().year 
    Time = Current_year - Year_of_Entry.year
    print(f"{selected} has been in this company for {Time} years") 

except IndexError:
    print("Error:Enter a valid index")
    exit()
except TypeError:
    print("Enter valid year")
    exit()
except Exception as e:
    print("Error has occured")
    exit()
finally:
    print("Success!")
   

"""print("================================================================")
# file hanndling
f = open("Hello.txt", "w") # This opens the file for writing and creates one if it doesn't exist

# Writing to the text file
# Writing to the text file
with open("Hello.txt", "w") as f:
    f.write("Hello there!\n")
    f.write("The month of May has come to an END, remember to set next month's goals \n")
    f.write("NEW MONTH \n")



# Appending the current month to the existing file

current_month = datetime.date.today().strftime("%B")
with open('Hello.txt', 'a') as f:
    f.write(f"The month of {current_month} has come to an END, remember to set next month's goals.\n")

# Reading and printing the file content
with open("Hello.txt", "r") as f:
    message = f.read()
    print(message)"""
