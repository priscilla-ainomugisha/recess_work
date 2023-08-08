#works when one wants to combine a string to a number
#we need to us ethe format() method
#the format() takes the passed arguments,formats them and places
#them in the string where the place holders{} are.
age = 21
name="My name is Priscilla and Iam {}"

print(name.format(age))
#the format() method can take multiple arguments and place them in respective placeholders

name="Priscilla"
DOB=2002
place_of_birth="kampala"

details="My name is {}, born on {},in {}"
print(details.format(name,DOB,place_of_birth))