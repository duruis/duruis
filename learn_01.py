
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
""""
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
""""  
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
'''
def main():
  print_square(3)
  
def print_square(n):
  for i in range(n):  
   print("#" * n)

main ()
'''
''
while True:
  try:
   x = float(input("What is x? "))
  except ValueError:
   print("x is not an integer")
  else:
   break
print(f"x is {x}")

  

  

  
   

  
  
 
  







  
 
  


