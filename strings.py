#strings
p='Hello world!'
r="Hello there too"
q="""Iam offering BSSE year three currently doing recess 
in python, datascience and django"""
print(q)

#Strings as arrays
a="Aternoon"
print(a[0])

#Exercise one:use the len()functionto determine the length of your string
length = len(p)
print(length)
#Exercise two:Give an example of using a for loop in a string
for char in r:
    print(char)
#Exercise three:Give an example of slicing in strings
# Slice from index 0 to 5 (exclusive)
substring1 = p[0:5]
print(substring1)
# Slice from index 5 to the end of the string
substring2 = p[5:]
print(substring2)
