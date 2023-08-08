from cgi import print_arguments


Animals=("cat","cow","hen","goat")
print(Animals)

#ALLOW FOR DUPLICATE VALUES
Animals=("cat","cow","cow","hen","Hen","goat","hen")
print(Animals)
print(len(Animals))

if len(Animals)==0:
    print("No Animals")
else:
    print("There are multiple animals")

#TUPLE SHOWING IFFERENT DATATYPES
Tuple1=("html","css","javascript")
Tuple2=(1,2,3,4,5,6,7,8,9,10)
print(type(Tuple1))
print(type(Tuple2))

#Finding datatype for elements in a turple using map()+type()
res=list(map(type,Tuple1))
print(str(res))
resi=list(map(type,Tuple2))
print(str(resi))

#HOW TO ACCESS TURPLES
Py=('spark','Python','pandas','pyspark','java')
result=Py[2]
result2=Py[-2]
print(result)
print(result2)

#ADD ITEMS TO A TUPLE
begin=(1,2,3)
last=(4,5,6)
#add two turples
numbers=begin +last
print(numbers)

#unpacking a turple
last=(1,2,3,*last)
print(last)

#add one element
list1=list(begin)
list1.append(12)
print(list1)

#using turple concatenation
lastlast=(1,)+begin
print(lastlast)


