#If statements If statements If statements
"""
score = float(input("Score: "))
if score >= 90:
  print("Grade A")

elif score >= 80:
  print("Grade B")

elif score >= 70:
  print("Grade C")

elif score >= 60:
  print("Grade D")

else:
  print("You are fucked")
"""
"""
temperature = float(input("Temperature outside?: "))
if temperature > 35:
  print("Stay hydrated, it is hot out")
elif  temperature <= 25 and temperature >=18:
  print("It is nice out, get out of the house")
else:
  print("temperatures are dropping, bring a coat just in case")
"""
"""  
weight = float(input("Weight: "))
variable = input("(k)g or Pounds: ")
if variable.upper == "K":
  converted = weight / 0.45
  print("Weight in Pounds: " + str(converted))
else:
  converted = weight * 0.45
  print("Weight in Kilos: " + str(converted))
"""

#Lists Lists Lists
"""
list_1 = [1,2,3,4,5]
for i in list_1:
  print(i, end=" ")
   
list_1 = [1,2,3,4,5]
list_1.append(6)
list_1.remove (5)
list_1.insert(0,0)
list_1.pop(4)
list_1.reverse()
print(list_1)
List_1.clear
List_1.index
List_1.count
List_1.reverse
List_1.copy
list_2 = [20,30,40,50]
list_1.extend(list_2)
print(list_1)
"""
#List Comprehensions - concise way to create a list.
"""
square = []
for x in range (10):
  square.append(x**2)
print(square)
"""
"""
combs = []
for x in [1,2,3]:
 for y in [2,4,5,6]:
   if x != y:
     combs.append((x,y))
print(combs)
"""
"""
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
print(list(enumerate(seasons, start=1)))
"""
#Loops Loops Loops

"""
name = ["Edu", "Dudu", "Ed", "Eduardo"]
age = [23, 25, 29, 34]
for n, a in zip(name, age):
  print("{} is {} years old".format(n,a))
"""
"""
while True:
  print ("Who are you?")
  name = input()
  if name != "Edu":
    continue
  print("Hello Edu. What is your password? ")
  password = input ()
  if password == "Monkey":
    break
print("Access granted")
"""
"""
while True:
  try:
   x = float(input("What is x? "))
  except ValueError:
   print("x is not an integer")
  else:
   break
print(f"x is {x}")

"""
"""
while True:
  word = input("What is the magic word: ?")
  if word == "ed":
    print("You win") 
  else:
    print('Try again:')
"""
"""
i = 1
while i <= 5:
  print(i, end=" ")
  i = i + 1
"""
"""
count = 0
while count < 7:
  count += 1
  if count == 5:
    break
  print("you are an ass")
"""
"""
#random random random
import random
def runGame():
  "the game code"
  while True:
   print("Game menu")
   print("1) Start a new game")
   print("2) Quit")
   
   choice = input("Enter your choice")
   if choice == "1":
     runGame()
   elif choice == "2":
     break 
"""
#Functions Functions Functions
"""


def main ():
 student = get_student()
 print(f"{student[0]} from {student[1]}")
 
def get_student():
  name = input("Name: ")
  house = input("House: ")
  return (name, house)

if __name__ == "__main__":
 main() 
"""
 
"""
def main ():
  x = float(input("What is x? "))
  print("x squared is", square (x))
  
def square(n):
  return pow (n, 3)

main()
"""

"""
def math (x,y=10):
  return x ** y
result = math(3)
print(result)
"""

"""
def function (*args, **kwargs ): # args and kwargs will run as many args u want and different types
 print(args, kwargs)
 pass
function (10, 34, 45, 90, c = True, d = 10)
"""
"""
def function (x, y, z = 10):
 print(x + y * z)
 pass
function (4, 6, )
"""
"""
def multiply(x, y):
  print(f"You called the multiply of x,y with the values of x = {x} and y= {y}")
  print(f"the multiply of x*y = {x*y}")
multiply(4,8)
"""
"""
def square (x):
  return x*x
print(square(9))
"""  
"""
import random
magicnumber = random.randint(1,10)
while True:
 word = input("What is the magic number? ")
 if word == "quit":
   break

 try:
   playnumber = int(word)
 except ValueError:
   print("Try a different number without decimals")
   continue
    
 if playnumber == magicnumber:
  print('You got it right')
 elif playnumber < magicnumber:
  print("playnumber is lower")
 elif playnumber > magicnumber:
  print("Playnumber is higher")
  print("This is not the magic number, try again")
"""
"""
import random
numbers = random.choice (list(range(1, 61)))
print(numbers) 
""" 

"""

import random
numbers = random.randint(0, 61)
print(numbers)
"""
"""
import random

cards = ["jack", "queen", "king"]
random.shuffle (cards)
for card in cards:
  print(card)
"""
"""
from random import shuffle
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle (numbers)
print (numbers)

from random import sample
names =['Ed','Edu', 'Dudu', 'Eduardo']
single_sample= sample(names,3) 
print(single_sample)
"""
#Class Class Class
"""
class Person:
  def __init__(self,name):
    self.name = name
  
  def whoami(self):
    return "You are " + self.name

p1 = Person("Edu")
print(p1.whoami())
print(p1.name)
"""
"""
class human:
  def SayHello(self, name=None):
    if name != None:
      print("What's up", (name))
    else:
      print("Do I know you?")

object=human()
object.SayHello()
object.SayHello(" ")
"""   









