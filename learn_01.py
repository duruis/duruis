
# Immutable = you cannot change once you definite it 
# str; int; float; bool; bytes; tuple


# Muttable = you can change them
 # list []; set; dict
 
'''x = [i for i in range (10)]
y = [i for i in range (10) if i % 2 == 0]
print(x + y)

def function (x, y, z = 10):
 print(x + y * z)
 pass
function (4, 6, )

# args and kwargs will run as many args u want and different types
def function (*args, **kwargs ): 
 print(args, kwargs)
 pass
function (10, 34, 45, 90, c = true, d = 10)

# using * and ** 
def function ( a, b, c= True, d= False):
  print(a, b, c, d)
  pass
function (*[1, 2], **{"c":  "cool", "d": "nice"})
'''
'''
name = input ("What's your name? ")
print("Hello " + name)'''
"""
bday = input("When is your birthday year? ") 
age = 2024 - int(bday)
print(age)
"""
"""
First = float(input("First: "))
Second = float(input("Second: "))
Sum = First + Second
print("Sum:", + Sum)
"""
"""
animal = (1223, 1223, 1234, 2323, 3445, 4323, 23, 23, )
print(animal.count(23))
"""
"""
animal = 230
print(animal <= 240 and animal > 210)
"""
"""
temperature = float(input("Temperature: " ))
if temperature > 20 and temperature <= 35:
 print("Lets stay home, and have sex")
 print("Enjoy the day, smoke weed, have sex again lol")

print("Done")
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
"""
i = 1
while i <= 5:
  print(i)
  i = i + 1
"""
"""
#list of names
names_list = ["Edu", "Ed", "ed", "Du", "Dudu", "Eduardo"]
#Function
def find_name(name, names_list):
  if name in names_list: 
    return f"{name} is in the list."
  else:
    return f"{name} is not listed."
 
#Input= name to find 
name_to_find = input ("Enter the name you want to find: ")

#Result
result = find_name(name_to_find, names_list)
print(result)
"""
"""
numbers = [2, 4, 6, 8, 10]
for item in numbers:
  print(item)
"""
"""
numbers = range (0, 60, 2)
for i in numbers:
  print(i)
"""
"""  
color = input("What is your favorite color: ?")
print(f"I also love {color}")

"""
"""
print("What is your name? ")
name = input()
print ("It is nice to meet you, {}" .format (name)) 

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
for i in [ 1, 2, 3, 4, 5, 6, 7, 8, 9, ]:
  if i == 11:
    break
else:
  print("only executed no item in the list in equal to 3")
"""
"""
name = ["Edu", "Dudu", "Ed", "Eduardo"]
age = [23, 25, 29, 34]
for n, a in zip(name, age):
  print("{} is {} years old".format(n,a))
"""
"""
print ("Hello world\nIt is been a freaking beautiful journey\nThanks God for another beautiful day")
"""
"""
def add(x, y):
 return x + y
result = add(23, 77)
print(result)

"""
"""
x = float(input("What is x? "))
y = float(input("What is y? "))
print(f"{x + y: ,}")
"""
"""
x = float(input("What is x? "))
y = float(input("What is y? "))
print(round(x / y, 2))
"""
"""
def hello(to="World"):
   print("hello,", to)
   
hello()
name = input("What is your name? ")
hello (name)
"""
"""
def main ():
  x = float(input("What is x? "))
  print("x squared is", square (x))
  
def square(n):
  return pow (n, 2)

main()
"""
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
def main ():
  x = float(input("What is x? "))
  if is_even(x):
    print("Even")
  else:
    print("Odd")
def is_even (n):
    return n % 2 == 0
     
main ()
"""
"""
name = input("What is your name? ")
match name:
  case "Edu" | "Ed" | "Dudu":
    print ("Pira")
  case "Mel" | "Me" | "Meme":
    print("Recife")
  """
"""  
i = 5
while i != 0:
  print("meow")
  i = i - 1
"""
"""
for i in range (20):
  print ("meow")
  """
"""
print ("meow\n" * 3, end="")  
  """
""" 
while True:
  n = int(input("What is n? "))
  if n > 0:
     break
for _ in range(n):
  print("meow")
"""
"""
students = ["Edu", "Dudu", "Ed", ]
for i in range(len(students)):
  print(i + 1, students[i])
  
"""
"""
animals = [
  {"ID": "PUSP", "YEAR": "TF", "SEX": "M"},
  {"ID": "PUSP", "YEAR": "TT", "SEX": "F"},
  {"ID": "PUSP", "YEAR": "TTT", "SEX": "M"},
]  
for individual in animals:
 print(individual ["ID"], individual ["YEAR"], individual ["SEX"], sep=(", "))
"""
"""
def main ():
 print_row(4)
  
def print_row (width):
  print("?" * width)
  
main()
"""
"""
def main():
  print_square(3)
  
def print_square(n):
  for i in range(n):  
   print("#" * n)

main ()
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
import random
numbers = random.choice (list(range(61)))
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
import statistics
print(statistics.mean ([10, 20]))
"""
"""
import sys
if len(sys.argv) < 2:
   print ("Too few arguments")
elif len(sys.argv) > 2:
  print ("Too many arguments")
else:
 print("What's up? My name is", sys.argv[1])
"""
"""
def main():
  hello("world")
  goodbye("world")
  
def hello(name):
  print(f"hello, {name}")
  
def goodbye(name):
  print(f"goodbye, {name}")

if __name__ == "__main__":
 main ()

# continue ...create a new file

import sys
from learn_01 import hello
if len(sys.argv) == 2:
   hello (sys.argv [1])

"""
"""
def main ():
  x = float(input("What is x? "))
  print("x square is ", square(x))
  
def square(n):
  return n * n

if __name__ == "__main__":
 main ()
 
#in a new file

from learn_01 import square

def test_positive():
  assert square(2) == 4
  assert square(3) == 9

def test_negative():
  assert square(-2) == 4
  assert square(-3) == 9

def test_zero():
  assert square(0) == 0
"""
"""
name = input("What is your name? ")
with open("names.txt", "a") as file:
 file.write(f"{name}\n")

with open("names.txt", "r") as file:
  for line in file:
    print("hello,", line.rstrip())

"""
"""
names = []
with open("names.txt") as file:
  for line in file:
    names.append(line.rstrip())
for name in sorted(names):
 print(f"hello, {name}") 

"""
"""
with open ("names.txt") as file:
   for line in file:
     name, location = line.rstrip().split(",")
     print(f"{name} is in {location}")
"""
"""
#to read and sort through the csv file
 import csv
 names = []
 with open ("names.txt") as file:
   reader = csv.DictReader(file)
   for name , location in reader:
     names.append({"name":name, "location":location})

 print(f"{name} is in {location}")
"""
"""
import csv
name = input("What is your name? ")
home = input("Where is your home? ")

with open("students.csv", "a") as file:
  writer = csv.DictWriter(file, fieldnames=["name", "home"])
  writer.writerow({"name": name, "home": home})
  
"""
"""

import sys
from PIL import Image
novo = []

for arg in sys.argv[1:]:
  image = Image.open(arg)
  novo.append(image)
  
novo[0].save(
  "new_file.gif", save_all=True, append_novo=[novo[1]], duration=100, loop=0) 

"""
"""
email = input("What is your email?").strip()

if "a" in email and  "." in email: 
  print("Valid")
else:
  print("Invalid")   
  
"""
"""
import re
name = input("What is your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
  name = matches.group(1) + " " + matches.group(2)
  print(f"hello, {name}")

"""


  
"""
name = input("Name: ?")
house = input("House: ?")
print(f"{name} from {house}")
"""
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
'''
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Pira", "Recife", "Olimpia"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


def main():
    student = get_student()
    print(student)


if __name__ == "__main__":
    main()
'''


