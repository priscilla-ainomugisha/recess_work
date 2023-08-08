#data dictionaries are used to store data values in(key:value) pairs
#Dictioneries are orders, changeable and do not allow duplicates
#Dictionaries can have items of any datatype
mydict={
    "phone":"iphone",
    "model":"Iphone14",
    "year":2023
}
print(mydict)

#length of the data dictionary
print(len(mydict))
#data type
print(type(mydict))
#Access Dictionary items
z=mydict["year"]
print(z)

y=mydict.get("model")
print(y)

w=mydict.keys()
print(w)


##EXERCISES##

#Exercise one:use the values() method to return a list of all values in the dictionary
print(mydict.values())
#Exercise two:check if the value does exist in your dictionary
value = 'iphone'

if value in mydict.values():
    print(f"Yes, Value: '{value}' exists in dictionary")
else:
    print(f"No, Value: '{value}' does not exists in dictionary")
#Exercise three: Give an example on how to change dictionary items, how to update
# Adding a new key value pair
mydict.update({'version': "pro"})
print(mydict)
mydict.update({'model': "Iphone15"})
print(mydict)
#Exercise four: Give an example on how to add dictionary items,How to remove dictionary items
mydict['storage'] = 128
print(mydict)
#removing a dictionary item
key_to_be_deleted = 'version'
mydict.pop(key_to_be_deleted)
print(mydict)
#exercise five:an example on how to loop through a dictionary and how to nest dictionaries
    # Iterate over the dictionary using for loop
for key in mydict:
    value = mydict[key]
    print(key, " :: ", value)
    #Netsed dictionaries
    # A Nested dictionary i.e. dictionaty of dictionaries
students = {
            'ID 1':    {'Name': 'Shaun', 'Age': 25, 'City': 'Mukono'},
            'ID 2':    {'Name': 'Aiko', 'Age': 21, 'City': 'Kampala'},
            'ID 3':    {'Name': 'Angella', 'Age': 20, 'City': 'Kabong'},
            'ID 4':    {'Name': 'kasumba', 'Age': 23, 'City': {'perm': 'Tokyo',
                                                             'current': 'London'}},
            }

def nested_dict_values_iterator(dict_obj):
    ''' This function accepts a nested dictionary as argument
        and iterate over all values of nested dictionaries
    '''
    # Iterate over all values of given dictionary
    for value in dict_obj.values():
        # Check if value is of dict type
        if isinstance(value, dict):
            # If value is dict then iterate over all its values
            for v in  nested_dict_values_iterator(value):
                yield v
        else:
            # If value is not dict type then yield the value
            yield value


#Loop through all nested dictionary values
for value in nested_dict_values_iterator(students):
    print(value)