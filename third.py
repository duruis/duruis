"""
b_year = int(input("What is your year of birth? "))
age = 2024 - b_year
print(age)
"""
"""
first = ("Edu")
last = ("monkey")
print(f"{first} is the coolest dude and his last name is {last}")
"""
"""
course = ("Python for beginners")
print(f"{course.replace("Python", "sex")}")
"""
"""
price_house = float(input("What is the price of the house? "))
good_bad_credit = input("Do you have good or bad credit? ").lower()
if good_bad_credit == "good":
  print(f"total_downpayment", {price_house * 0.1})
elif good_bad_credit == "bad":
 print("total_downpayment",   {price_house * 0.2})
print("Thanks for your business")
"""
"""
price = 100000
good_credit = False
if good_credit:
  down_payment = price * 0.1
else:
  down_payment = price * 0.2
  print(f"Down payment: " ${down_payment})
print("Thanks for your business")
"""
"""
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
  guess = int(input("Guess: "))
  guess_count += 1
  if guess == secret_number:
   print("You won")
   break
else:
  print("Sorry, you failed")
"""
"""
prices = [10,20,30,40]
for i in prices:
 print(f"You own me {sum(prices)}")
 break
"""
"""
list = [5,2,5,2,2]
for number in list:
  print("x" * number)
#or
list = [5,2,5,2,2]
for number in list:
  output= ""
  for first in range(number):
     output += "x"
  print(output)
"""
"""
matrix = [
[1, 2 , 3],
[4, 5, 6],
[7, 8, 9]
]
matrix [1] [0:3] = [10, 20, 30]
print(matrix) 
"""
"""
numbers = (1,2,4,3,5,6,7,1,2,3,7,8,9,5,3,2,1,4,5,6)
no_duplicates = list(set(numbers))
print(no_duplicates)
"""
"""
numbers = (0,1,3,4,5)
x,t,r,e,t = numbers
print((r*t)/e)
"""
"""
contact = {"name": "Edu",
  "age": "30",
  "phone": "10204",
  "city": "Nashive",
    }
print(contact ["age"])
"""
"""
phone = input("What is your fucking phone number bitch? ")
digital={"1": "one", "2": "two", "3": "three"}
for i in phone:
 print(digital.get(i), end=" ")
"""

  
  
  


  






        
    
    
    

  
  
  
  
   
