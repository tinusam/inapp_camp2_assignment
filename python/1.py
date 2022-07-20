from ast import Sub
from operator import sub
from statistics import multimode
import sys
import re
from time import process_time
"""
print ("Hello world")
#just printing the python version
just a
multiline comment
print(sys.version)



text = "{} is my country. All Indians are my brothers and sisters.".format('India')
print(text)

c = text.count('India')
print("Count of India in the text is {}".format(c))

myString = 'superman'
print(myString.endswith('man'))
print(myString.endswith('man',3))#start checking from index 3
print(myString.endswith('man',2,6))
print(myString.endswith(('man','ma'),2,6))


myString = "Good Morning"
print(myString.find('Mo'))
print(myString.find('Mo',3))
print(myString.find('Mo',3,7))
print(myString.index('M0o'))

#join() method to join items in a tuple with a separator
Separator = '*'
myTuple = ('h','e','l','l','o')
myNewString = Separator.join(myTuple)
print(myNewString)
print(myNewstring.lower())
print(myNewstring.upper())


#replace and split method
myString = "Hello World"
myString = myString.replace('o','i')
print(myString)
myStringSplit = myString.split(' ')
print(myStringSplit)


txt = "bits of paper, bits of paper"
x= re.findall("bi",txt)
print(x)

x= re.search("bi",txt)
print(x)

x= re.sub(" ","-",txt)
print(x)

#search using meta chars
txt ="hello world"
#find all lower case char between 'a' and 'm'
x=re.findall("[a-m]",txt)
print(x)


txt ="james bond is 007"
#find all the digits
x=re.findall("\d",txt)
print(x)

#look for a substr with j and have three char in b/w ends with s
x=re.findall("j...s",txt)
print(x)

#look for substr starting with'hello'
#using the metachar ^ and \A are same
txt = "hello world"
x=re.findall("^hello",txt)
print(x)

txt = "hello world"
x=re.findall("\Ahello",txt)
print(x)

#look for substr starting with 'world'
x=re.findall("world$",txt)
print(x)

#look for substr starting with 'wor'
x=re.findall("\wor",txt)
print(x)

#look if any word in the string starts with 'the'
txt="james watt invented the engine"
#look for substr starting with 'jam'
x=re.findall("\Ajam",txt)
print(x)

#using the metachar $
txt= "james watt invented sothe"
x=re.findall(r"the$",txt)
print(x)

#using the special sequence \b
txt= "james watt invented theso watt"
x=re.findall(r"\bthe",txt)
print(x)

#matching an email within a string using spcial sequence
mystring = "my email is tinu@tinu.com hope you will note it down"

#regular expression to match email
#check for non space chars before and  after '@'
regex='\S+@\S+'
x=re.findall(regex, mystring)
print(x)


#LIST AND LIST ACCESS OPTIONS
studentsAge = [18,39,23,13]
print(studentsAge)
print(studentsAge[2])#print the particular index
newStudentsAge=studentsAge[2:4]#starting from 2 till 4-1
print(newStudentsAge)
newStudentsAge=studentsAge[1:5:2]#starting from 1 till 5-1,every 2nd elemnts
print(newStudentsAge)
newStudentsAge=studentsAge[:3]#starting 0 index till 3-2 index
print(newStudentsAge)
newStudentsAge=studentsAge[::-1]#reverse the list
print(newStudentsAge)
newStudentsAge=studentsAge[-4]#reverse the list
print(newStudentsAge)

#append to add a value to the end of the list
studentsAge.append(16)

print(studentsAge)

#delete value from the list
del studentsAge[-1]
print(studentsAge)

#combine two list using extend()
studentsName =['Anu','Jobson','Tintu']
#studentsAge.extend(studentsName)
print(studentsAge)

#check if an item is in a list
print('Anu' in studentsName)

#get the no of items in the list
print(len(studentsName))

#reverse the contents 
studentsName.reverse()
print(studentsName)
studentsName.reverse()
print(studentsName)

#sort the list either alphabetically or numerically
studentsAge.sort()
print(studentsAge)

#list concatnation using + operator
print(studentsName+studentsName)
print(studentsName)

#list concatnation using * operator
print(studentsName*2)
print(studentsName)


#1) Sort the list in ascending orders and print the first element in the list
num=[14,11,32,67,34]
print(num)
num.sort()
print(num)
print(num[0])

#2) Python program to find second largest number in a list
Num1 = [34,87,12,34,67]
Num1.sort()
print(Num1)
print("Second largest number is:", sorted(Num1)[-2])

#3) Python program to print odd number & even numbers separately in a list of [1,2,3,4,5,6,7,8,9,10]
list=[1,2,3,4,5,6,7,8,9,10]
print(list)

even_list=[]
odd_list=[]
for i in range(len(list)):
  if(list[i]%2==0):
    even_list.append(list[i])
  else:
    odd_list.append(list[i])
print("Even Numbers List:", even_list)
print("Odd Numbers List:", odd_list)

#4. program for reversing a list
list1 = [34,76,12,34,87]
list1.reverse()
print(list1)

#5. program to print all odd numbers from 1-50
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
for num in range(start, end + 1):
     
    # checking condition
    if num % 2 != 0:
        print(num, end = " ")

        
#6.create a list that contains only Even numbers in given range
even_list = range(start, end + 1)[start%2::2]
 
for num in even_list:
    print(num, end = " ")

#7. program to count even and odd numbers in a list
list2 = [23,76,87,45,12,15,89]
  
odd = [num for num in list2 if num % 2 == 1]
odd_count = len(odd)
  
print("Even numbers in the list: ", len(list2) - odd_count)
print("Odd numbers in the list: ", odd_count)

#8. write a python program to remove zeros from an IP address
import re
IP = "107.07.123.5616"
string = re.sub('\.[0]*', '.', IP)
print(string)

 #. write a python program that matches a string that has an 'a' 
# followed by anything, ending in 'b'

y = 'a.*?b$'

str = 'aabb'
op = re.search(y, str)
print(op)

# 3. replace all occurrences of 6 with 'six' and 10 with 'ten' for the 
# given string 'They ate 6 apples and 10 bananas'

line = 'They ate 6 apples and 10 bananas'
output = re.sub('6','six', line)
output = re.sub('10', 'ten', output)
print(output)


#Tuples in Python
months = ("Jan","Feb","March")
print(months[0])
print(months[-1])
#months[0] = "test" will not work

#tuples methods in python
print(len(months))
print("Jan" in months)
print("January" in months)
#del months
print(months)
print(months+months)
print(months*3)

#dictionary in python
#dictionary declaration
#method 1
mystudents = {"Abhi":30, "Sibi":28, "Subi":"not updates"}
#method 2
mystudents = dict(Abhi=30, Sibi=28, Subi="not available" )
#method 3
mystudents = dict({"Abhi":30, "Sibi":28, "Subi":"not updates"})
print(mystudents["sibi"])
print(mystudents)





#Dictionary methods
print(mystudents.get("Subi"))#will return corressponding value
print(mystudents.items()) #will return dict items as array of tuples
print(mystudents.keys()) #return keys of the dict
print(mystudents.values()) #return values of the dict
print("Abhi" in mystudents) #return values of the dict
print(30 in mystudents.value())
print(len(mystudents))

mystudents2={"Abhi":31,"Binu":26}
mystudents.update(mystudents2)
print(mystudents)

mystudents.clear()
print(mystudents)


#set in python
#method 1
months={"jan","feb","mar"}
#method 2
months = set(["jan","feb","mar"])
print(months)
print(type(months))


#looping through elements in a set

for i in months:
    print(i)

 #declare an empty set
    days = set()
    #add values to set
    days.add("mon")
    days.add("tue")
    days.add("wed")

    for i in days:
      print(i)


myStudents2 = {"Abhi": 31, "Binu": 26}
mystudents.update(myStudents2)#join together dict by overwriting duplicate keys
print(mystudents)

myStudents.clear() #clear all values inside dict
print(mystudents)

del mystudents #delete dict along with variable
print(mystudents)


#Set in python

#method1
months = {"Jan","Feb","March"}
#method2 
months = set(["Jan","Feb","March"])

print(months)
print(type(months))

#looping thriugh elements in a set
for i in months:
    print(i)

#declare an empty set
days = set()
#add values to set
days.add("Mon") #insert single values
days.add("Tue")
days.add("Wed")
#looping thriugh elements in a set
for i in days:
    print(i)

days.update(["Thur","Fri"]) #insert multiple items
#looping thriugh elements in a set
for i in days:
    print(i)

#remove items from the set
#using discard() method, will remove item, not display error if item does not exist
days.discard("Thur")
for i in days:
    print(i)

#using remove() method, will remove item, will display error if item does not exist
days.remove("Thur")
#loop through items in set
for day in days:
    print(day)

days.clear()
print("cleared the set")
for day in days:
    print(day)


#set operations
months1 = {"Jan","Feb","Mar"}
months2 = set(["Mar","Apr","May"])
#union operation
months4 = months1 | months2
print(months4)
for month in months4:
    print(month)

#intersection operation
months4 = months1 & months2
print(months4)

#intersection update
months1 = {"Jan","Feb","Mar"}
months2 = {"Mar","Apr","May","Feb"}
months3 = {"Feb","Mar","Jun","Jul"}
#months1.intersection_update(months2,months3)
#print(months1)

#difference operation
months4 = months1 - months2
print(months4)

#symmetric difference 
#will retain all elements of set excluding the common ones
months4 = months1 ^ months2
months4 = months1.symmetric_difference(months2)
print(months4)



months1 = {"Jan","Feb","Mar","Apr","May","Jun"}
months2 = {"Mar","Apr","May","Feb"}
months3 = {"Feb","Mar","Jun","Jul"}
#set comparison operation
#checking if month1 is a superset of month2
print(months1 > months2)
#check if two sets are equalent(no of elements itself should be same)
print(months2 == months3)
#check if two sets are equal
print(months1 >= months2)
print(months1 <= months2)

#frozen set
months4frozen = frozenset({"nov","dec"})#immutable set
print(type(months4frozen))
print(months4frozen)
months4frozen.add("oct")#'forzenset' object has no attribute 


#input and output function in python
studName = input ("enter ur name:")
studAge = input("enter the age:")
print(studName)
print(type(studName))
print(studAge)
print(type(studAge))

#variations of print statement to include variables
print("The student name is ",studName,"and the age is ",studAge)
print("The student name is %s and the age is %s"%(studName,studAge))
print("The student name is {} and the age is {}".format(studName,studAge))


print('''hello world
how are u''')
#print a new line
print('hello world\nhow are u')
print('this is a backslah\\')
print('i am 5\'5\"tall')

#symmetric difference 
#will retain all elements of set excluding the common ones
months4 = months1 ^ months2
months4 = months1.symmetric_difference(months2)
print(months4)

#Set comparisons operation
months1 = {"Jan","Feb","Mar","Apr","May","Jun"}
months2 = {"Mar","Apr","May","Feb"}
months3 = {"Feb","Mar","Jun","Jul"}
#checking if months1 is a superset of months2
months1 > months2
print(months1 >months2)
print(months1 <months2)
#check if two sets are equal
print(months2 == months3)
#check if two sets are equal
print(months1 >= months2)
#check if two sets are equal as well as month2 is a superset of month1
print(months1 <= months2)

#frozen set
months4frozen = frozenset(["Nov","Dec"]) #immutable set
print(type(months4frozen))
print(months4frozen)

months4frozen.add("oct") #frozen set has no attribute

#input and output functions in python
studName = input("Please enter you name: ")
studAge = input("Please enter you age: ")
print(studName)
print(type(studName))
print(studAge)
print(type(studAge))

#variations of print statement to include variables
print("The student name is",studName, "and the age is",studAge)
print("The student name is %s and the age is %s" %(studName,studAge))
print("The student name is {} and the age is {}" .format(studName,studAge))

#print in multiple lines
print('''Hello World
How are you''')
#print a new line
print("Hello World\nHow are you")
print("This is a backslash\\")
print('I am 5\' 5\" tall')


#control flow ststement
#conditional statements
#if condition
userInputNo = input('Enter either 1 or 2:')
if(userInputNo == "1"):
    print("You entered 1")
    print("And you are number 1")
elif(userInputNo == "2"):
    print("You entered 2")
    print("Runner up. Keep it up!")
else:
    print("you did not enter 1 or 2")

#inline if statement
B=12
A=12 if B==10 else 13
print(A)

print("B is ten" if B==10 else "B is not 10")


#python match case statement example
#define a function
def http_status(status):
    match status:
      case 400:
        return "bad request"
      case 404:
        return"page not found"
      case _:
        return "unknown error occured"
#calling the function inside print statement
print(http_status(404))



#looping in python
#FOR loop to loop/iterate through a list in python
fruits = ['apples','oranges','banana','cherry']
for fruit in fruits:
  print (fruit)

#to display index using the enumerate method
for index, fruit in enumerate(fruits):
  print(index,fruit)

#tuse for loop to generate a series of numbers
#using the range function
for i in range(10):
  print(i)

#WHILE loop
counter = 5
while counter > 0:
  print ("Counter =", counter)
  counter = counter - 1

#break and continue statements
#break example
j = 0
for i in range(10):
  j= j +2
  print('i = ', i,'j = ', j)
  if j ==6:
    break
  print()

#continue example
j = 0
for i in range(10):
  j= j +2
  print('i = ', i,'j = ', j)
  if j ==6:
    continue
  print('continue j value is:',j)

  #try except (similar to try catch) in python
  try:
      answer =12/0
      print (answer)
  except:
      print("some friendly error")

    
#loop assignment
# 1) Print the list of number which are divisible by 5 and multiple of 8 between 2000 and 2500

numl=[]
for x in range(2000, 2500):
    if (x%5==0) and (x%8==0):
        numl.append(str(x))
print (','.join(numl))

#2) write a python program to create the multiplication table (from 1 to 10) of a number getting input from the user

n = int(input("Input a number: "))
# use for loop to iterate 10 times
for i in range(1,11):
   print(n,'x',i,'=',n*i)

#FUNCTION 
# FIND THE SUM OF TWO NUMBERS 
def findSum(a,b):
    sum=a+b
    return sum
print(findSum(2,3))

#python function 
#to find prime number
def checkIfPrime (numbertocheck):
  for x in range (2,numbertocheck):
    if(numbertocheck%x==0):
      return False
  return True
print(checkIfPrime (22))

#function returing multiple values
def calculations(a,b):
  add = a + b
  Sub = a - b
  mul = a * b
  div = a % b
  return(add,Sub,mul,div)

#calling the function
output = calculations(40,30)
print("Add result",output[0])
print("Sub result",output[1])
print("Mul result",output[2])
print("Div result",output[3])


#generator is a function that returns an iterator
#iterator is something that we can loop through using a looping statement
#function returing multiple values
def calculationsyield(a,b):
  add = a + b
  yield add
  Sub = a - b
  yield Sub
  mul = a * b
  yield mul
  div = a % b
  yield div
  return(add,Sub,mul,div)

#using a for loop we can loop through the returned value from the function
for value in calculationsyield(30,40):
  print(value)


#demonstrating variable scope
#declaring a global variable
message1 = "Just a global variable"

def myFunction():
    global message1 #enable modification of global  variable inside the function
    print("reached inside fuction")
    print(message1) #printing the global variable
    message2 = "its a local variable"
    print(message2)
    message1 = "just modifying the global variable"
    print(message1)#printing the global variable
myFunction() #calling the function
#print(message1)
#print(message2)

#demonstrate passing the arbitary list of arguments into the function
def make_pizza(size,*toppings): #arbitary list parameter is prefixed by *
    print(f"\nMaking a {size} -inch pizza with following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers')


def printme(str):
    "this prints a passed string into this function"
    print(str)
    return 

printme(str"test")



#passing arugment as required and keyword args
def printInfo(name, age):
    print("name", name)
    print("age", age)

  #calling with req arguments
printInfo("Tom",10)
#calling with keyword arguments
printInfo(age=10, name="Winne")
    
#Anonymous (lambda) function in python
#function definition is here
sum =lambda arg1, arg2: arg1 + arg2

#we can call sum as a function
print("value of total : ",sum(10,20))
print("value of total : ",sum(20,10))


#python fundamentals MODULES
import random
#calling function inside the module
print(random.randrange(1,10))

#OR

import random as r
print(r.randrange(1,20))

#OR

from random import randrange, randint
print(randrange(1,20))

#the random built in module
import random
print(random.random())
print(random.randint(5,20))
print(random.choice(["head","tail"]))

myshirtcolors=["blue","red","black","yellow","green"]
random.shuffle(myshirtcolors)
print(myshirtcolors)

random.seed(14)
print(random.random())


#time module in python
import time;
print(time.time()) #seconds part 1st jan 1970
print(time.localtime(time.time()))#get the multiple time value as a tuple
print(time.asctime(time.localtime(time.time())))

for i in range (0,10):
  print(i)
  time.sleep(1) #dlay the program execution by the specificed no of seconds


import datetime
print(datetime.datetime.now())#return the current datetime object

#creating custom datetime object
birthday = datetime.datetime (2022,7,20)
print(birthday)
birthday = datetime.datetime(2022,7,20,10,15,50)
print(birthday)


#
from datetime import datetime as dt

if dt(dt.now().year,dt.now().month,dt.now().day,9)<  dt.now().year,dt.now().month,dt.now().day,9 
print("working now")
else:
    print("shift completed")

import calendar

mycalendar = calendar.month(2022,7) #get calendar for a month
print(mycalendar)
mycalendar=calendar.prcal(2022) #get calendar for an year
print(mycalendar)

import math

#finding the exponential of a num,ber, then its absolute , then its log, then
#convert to the base of 10
number = 2e-7
print(math.log(math.fabs(number),10))

number = math.pow(4,2)#power
print (number)
number=math.floor(4.3)#round to the smallest digit
print(number)
number= math.ceil(4.3)#will round to the next digit
print(number)
number = math.fabs(-10)#return absolute value
print(number)
number = math.factorial(10)#factorial
print(number)
number = math.modf(3.14)#will return the int and fractional part
print(number)

#calling the custom module created
import prime

answer = prime.checkIfPrime(13)
print(answer)

"""

#rights of a function in python



def myfunction1():
  print("this is myfunction1")
myMyfunction = myfunction1
myfunction1()
myMyfunction()

def myfunction1():
  print("this is myfunction1")

def myfun2(receivedfn):
    receivedfn()
    receivedfn()
myfun2(myfunction1)


#returning a function from a function
def retuntoupperfn():
  return str.upper

upperref = retuntoupperfn()
print(upperref("hello world"))

#we can define a function inside another function

def outer():
  print("outer function")

  def firstInner():
    print("first inner function")

  def secondInner():
    print("second inner function")

  firstInner()
  secondInner()

outer()



#the inner function can acces the enclosing function variables

  
def myouter(mygreeting):
      print("this outer function says", mygreeting)

      def myfirstinnerfun():
        print("the first inner func says", mygreeting)
      return myfirstinnerfun

myouterfuncvariable =myouter("peace to the world")
myouterfuncvariable()