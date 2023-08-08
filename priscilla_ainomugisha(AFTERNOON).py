print("Exercise 1 ****************************************************************")
#EXERCISE 1
#No.1
Students=["Rachel","Amos","Harriet","bonny","linda"]
print(Students[1])
#No.2
Students[0]= "Alice"
print(Students)
#No.3
Students.append("Taniah")
#No.4
Students.insert(2,"Bathel")
print(Students)
#No.5
Students.remove(Students[3])
print(Students)
#No.6
print(Students[-1])
#No.7
Fruits=["Apple","banana","kiwi","grape","orange","peach","mango"]
print(Fruits [2:5])
#No.8
Countries=["Uganda","Kenya","tanzania","south_Sudan"]
New_countries=Countries.copy()
print(New_countries)
#No.9
for i in Countries:
    print(i)
 #No.10
Animals=["cow", "dog", "cat", "hen", "pig","elephant"]
Animals.sort()
print(Animals)
Animals.sort(reverse=True)
print(Animals)
#No.11
for animal in Animals:
   if 'a' in animal:
       print(animal)
print("Exercise 2****************************************************************")

#EXERCISE 2
#No.1 
x=("samsung", "iphone", "tecno", "redmi")
print(x[1])
#No.2
print(x[-2])
#No.3
x= [phone.replace("iphone", "itel") for phone in x]
z=tuple(x)
print(z)
#No.4
zlist = list(x)
zlist.append("huaweii")
zlist =tuple(zlist)
print(zlist)
#no.5
for phone in x:
    print(phone)
#no.6
zlist=list(x)
zlist.remove(zlist[0])
zlist=tuple(zlist)
print(zlist)
#no.7
cities =tuple(["kampala","mbarara","gulu","jinja"])
print(cities)
#no.8'
a,b,c,d = cities
print(a)
print(b)
print(c)
print(d)
#no.9
print(cities[1:4])
#No.10
tuple1=("Priscilla")
tuple2=("Ainomugisha")
fullname=tuple1 + tuple2
print(fullname)
#No.11
Colors =("red", "green", "blue")
multiple_colors=Colors*3
print(multiple_colors)

#No.12
#Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

count = thistuple.count(8)
print(count)
print("Exercise 3****************************************************************")

#EXERCISE 3
#SETS
#No.1
beverages =set(("water", "juice", "soda", "tea"))
print(beverages)

#No.2
beverages.add("milk")
beverages.add("yoghurt")
print(beverages)

#no.3
mySet ={"oven","kettle","microwave","refridgerator"}
if ("microwave" in mySet):
    print("microwave in set")
else:
     print("microwave is not there")

#no.4
mySet.remove("kettle")
print(mySet)

#no.5
for i in mySet:
    print (i)

#no.6
set1={1,2,3,4}
set2={5,6}
set1.update(set2)
print(set1)

#No.7
age={21}
name={"Priscilla"}
Details=age.union(name)
print(Details)
print("Exercise 4****************************************************************")
#EXERCISE 4
#1. Declare two variables, an integer and a string and use the correct method to concatenate 
x="Hey"
y=2
statement= x + str(y)
print(statement)

#2. Consider the example below;
txt = " Hello, Uganda! "
print(txt.strip)

#3. Write a python program to convert the value of ‘txt’ to uppercase.
print(txt.upper())

#4. Write a python program to replace character ‘U’ with ‘V’ in the string above.
new_txt=txt.replace('U','V')
print(new_txt)

#5. Using the code below, write a python program to return a range of characters in the 2nd
y = "I am proudly Ugandan"
chars=y[1:4]
print(chars)

#6. The piece of code below will give an error when output;
x = 'All "Data Scientists" are cool!'
print("corrected_String: " + x)
print("Exercise 5****************************************************************")
#EXERCISE 5
#no.1

Shoes = {
"brand" : "Nick",
"color" : "black",
"size" : 40
}
print(Shoes["size"])
#2. Write a python program to change the value “Nick” to “Adidas”
Shoes["brand"] = "Adidas"
print(Shoes)
#3. Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print(Shoes)
#4. Write a python program to return a list of all the keys in the dictionary above.
print(Shoes.keys())
#5. Write a python program to return a list of all the values in the dictionary above.
print(Shoes.values())
#6. Check if the key “size” exists in the dictionary above.
if "size" in Shoes.keys():
    print("size is in shoes")
else:
    print("No its not")
#7. Write a python program to loop through the dictionary above.
for i in Shoes:
    print(Shoes[i] )
#8. Write a python program to remove “color” from the dictionary.
Shoes.pop("color")
print(Shoes)
#9. Write a python program to empty the dictionary above.'
Shoes.clear()
print(Shoes)
#10. Write a dictionary of your choice and make a copy of it.
Fruits={
    1:"apple",
    2:"orange",
    3:"banana"
}
Fruits2=Fruits.copy()
print(Fruits2)
#11. Write a python program to show nested dictionaries
Programme={
    'courseunit1' : {
        'name':"python",
        'code': 345
    },
     'courseunit2' : {
        'name':"java",
        'code': 789
    },
    ' courseunit3' : {
        'name':"html",
        'code': 709
    }

}
print(Programme)
print(Programme['courseunit1']['name'])


