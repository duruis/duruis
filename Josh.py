"""
age = 18
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
"""

"""
income = int(input("What is your average monthly income? $ "))
credit = str(input("Does client have good credit score? "))
if income > 3000 and credit == "good":
  print("qualified")
else:
  print("review case")
"""
"""
for i in range(6):
  for b in range(5):
    print(f"[{i},{b}]")
"""
"""
count = 0
for number in range (1,10):
  if number % 2 == 0:
    count += 1
    print(number)
print(f"We have, {count} even numbers")
"""
"""
def greet (name):
  return f"what's up {name}"

first = greet("edu")
print(first)
"""
""" 
def multiply (*numbers):
  total = 1
  for number in numbers:
    total *= number
  return total
    
print(multiply(2,3,4,5))
"""
"""
def fizz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "not okay and okay"
    if input % 3 == 0:
        return "okay"

    if input % 5 == 0:
        return "maybe okay"


print(fizz(15))
"""
"""
numbers = [1,2,4,4,5,6,7]
first, second, *others = numbers 
print(first, *others)
"""
"""
items = [("edu", 30),
         ("dudu", 10),
         ("edu", 2),]
items.sort(key=lambda item:item[1])
print(items)
"""
"""
items = [
    ("edu", 30),
    ("dudu", 10),
    ("edu", 2),
]
# numbers = []
# for item in items:
#   numbers.append(item[1])
# print(numbers)

# or
number = list(map(lambda item:item[1], items))
print(number)
"""
