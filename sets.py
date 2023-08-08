
Countries={"Uganda","kenya","Tanzania","Rwanda"}
print(Countries)

#DUPLICATES IN SETS 
#duplicates are ignored in sets
Countries={"Uganda","kenya","Tanzania","Rwanda","Rwanda","Rwanda","Rwanda","Rwanda"}
print(Countries)
print(len(Countries))

#DATATYPES
Countries={"Uganda","kenya","Tanzania","Rwanda"}
Country_codes={256,254,255,250}
print(type(Countries))

#Accessing items in a set
#Items can only be accesed sequentialy through a loop
for x in Countries:
    print(x)

#Add items to a set
Countries.add("SouthSudan")
print(Countries)

#ADD TWO SETS TOGETHER
#add elements from one set to another set
Countries.update(Country_codes)
print(Countries)

WestAfrica={"Nigeria","IvoryCoast","Ghana"}
Africa=Countries.union(WestAfrica)
print(Africa)