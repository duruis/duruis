
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
   
  
  





  

  
   

  
  
 
  







  
 
  


