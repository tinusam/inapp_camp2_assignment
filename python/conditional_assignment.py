#conditional statement exercise
userInputMonth = input('Enter the Date of Birth month:')
if(userInputMonth == "1"):
    print("Garnet")
    print("People born in january are bold and alert")
elif(userInputMonth == "2"):
    print("Amethyst")
    print("People born in february are lucky and loyal")
elif(userInputMonth == "2"):
    print("Amethyst")
    print("People born in february are lucky and loyal")
elif(userInputMonth == "3"):
    print("Aquamarine")
    print("People born in March are naughty and genius")
elif(userInputMonth == "4"):
    print("Diamond")
    print("People born in April are caring and strong")
elif(userInputMonth == "5"):
    print("Emerald")
    print("People born in May are loving and practical")
elif(userInputMonth == "6"):
    print("Alexandrite")
    print("People born in June are romantic and curious")
elif(userInputMonth == "7"):
    print("Ruby")
    print("People born in July are adventurous and honest ")
elif(userInputMonth == "8"):
    print("Peridot")
    print("People born in August are active and hardworking")
elif(userInputMonth == "9"):
    print("Sapphire")
    print("People born in September are sensitive and pretty")
elif(userInputMonth == "10"):
    print("Tourmaline")
    print("People born in October are stylish and friendly")
elif(userInputMonth == "11"):
    print("Citrine")
    print("People born in November are nice and creative")
elif(userInputMonth == "12"):
    print("Zircon")
    print("People born in December are confident and freedom loving")



else:
    print("you did not enter Date of Birth")

def birthstone(userInputMonth):
    match userInputMonth:
        case '1':
            return 'Birthstone is Garnet\nPeople born in January are bold and alert'
        case '2':
            return 'Brithstone is Amethyst\nPeople born in February are lucky and loyal'
        case '3':
            return 'Brithstone is Aquamarine\nPeople born in March are naughty and genius'
        case '4':
            return 'Brithstone is Diamond\nPeople born in April are caring and strong'
        case '5':
            return 'Brithstone is Emerald\nPeople born in May are loving and pratical'
        case '6':
            return 'Brithstone is Alexandrite\nPeople born in June are romantic and curious.'
        case '7':
            return 'Brithstone is Ruby\nPeople born in July are adventurous and honest'
        case '8':
            return 'Brithstone is Peridot\nPeople born in August are active and hardworking'
        case '9':
            return 'Brithstone is Sapphire\nPeople born in September are sensitive and pretty'
        case '10':
            return 'Brithstone is Tourmaline\nPeople born in October are stylish and friendly'
        case '11':
            return 'Brithstone is Citrine\nPeople born in November are nice and creative'
        case '12':
            return 'Brithstone is Zircon\nPeople born in December are confident and freedom loving'
        case _:
            return 'Wrong month no'

print(birthstone(userInputMonth))




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