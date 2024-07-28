#Dictionary Dictionary Dictionary
"""
tel= {"ed": 3475, "edu": 3745, "dudu": 2049, "eduar": 2847}
tel["jo"] = 2103
del tel ["ed"]
print(tel)
"""
#looping 
"""
knights = {"galand": "the pure", "robin": "the brave"}
for k, w, in knights.items():
  print(k,w)
"""
"""
questions = ["name", "quest", "favorite color"]
answer = ["lancelot", "the holy grail", "blue"]
for q,a in zip(questions, answer):
  print("What is your: {0} It is {1}".format(q,a))
"""
#using set to eliminate duplicates
"""
basket = ["apple", "orange", "apple", "papaia", "carrots"]
for f in sorted(set(basket)):
  print(f) 
"""

   
 