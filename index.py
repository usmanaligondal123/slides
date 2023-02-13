print("hello world")

#variable declaration and sum 
number_1=23
number_2=32
sum=number_1+number_2
print(sum)
#type casting nd cheking data type
a="31"
print(type(a))
#input from user
my_name=input("enter my name:")
#strings nd string slicing
user_name="aneela siddique"
print(user_name)
sl=user_name[:9]
print(sl)
#functions of string
length=len(user_name)
print(length)
bol=user_name.endswith("que")
print(bol)
#lists and tupples
fruits=["apple","banana","mango",32]
print(fruits)
id=fruits[1:]
print(id)
list_2=[1,3,7,5,6,8,2,9]
print(list_2)
list_2.sort()
print(list_2)
list_2.reverse()
print(list_2)
list_2.append(0)
print(list_2)
list_2.insert(4,7)
print(list_2)
tuple_1=(1,2,3,7,1)
print(tuple_1)
numbers=tuple_1.count(1)
print(numbers)
#dictionary
result={"name":"eisha","marks":23}
print(result)
print(result.items())
print(result.keys())
#sets
thisset = {"apple", "banana", "cherry"}
print(thisset)
#length of sets
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#conditinal expressions
a = 33
b = 200
if b > a:
  print("b is greater than a")
  
age=23
if age > 20:
    print("it is true")
elif age > 50:
    print ("it is my age")
else:
    print("it is wrong")
#loops
#while loop
i = 1
while i < 10:
  print(i)
  i += 1
# for loop 
fruits = ["apple", "mango","grapes","cherry"]
for x in fruits:
  print(x)
 #break 
fruit = ["mango","grapes","cherry"]
for x in fruit:
  print(x)
  if x == "grapes":
    break
#continue
veg = ["potato", "pee","tomato", "carrot"]
for x in veg:
  if x == "tomato":
    continue
  print(x)
