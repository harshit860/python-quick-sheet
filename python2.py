# Different data types how we can store data in combination

a = 5           # Integer 
A = 6           # case sensitive a and A are different values
y = "John"      # String
dec = 12.50     # float or decimal
valid = True     # boolean |  yes or no | true or false
fruits = ['mango','banana','apple']    # List or famously called array in other langugae mostly
vegetables = ("carrot", "potato", "onion")   # tuple value cant be changed
counter = range(100) # range  0 to 99
user = {
  "name": "Harshit",
  "age": "25",
  "gender": "Male"
} # dict | object in  other languages | key val pair

# printing the above
print(fruits)
print(vegetables)
print(counter)
print(user)

# to access particular values 

print(fruits[0]) # mango
print(vegetables[1]) # potato
print(user["name"])
print(user.get("age"))

harshitAge = user.get("age")     # you can access the object with the help of this method
user.update({"age": 26})
print('harshits age is ' + harshitAge)
print('harshits age is ' + str(user["age"]))

## ---------- looping 

for i in range(0,10):
  print(i)

# fruits = ['mango','banana','apple']  using the fruits example
for i in fruits:   
  print(i)

check = 1
while check < 5:
  print(check,' ->check value')
  check += 1 # or check += 1


# fruits = ['mango','banana','apple']  using the fruits example
count = 0
while count < len(fruits):
  print('check count value', count)
  print(fruits[count])
  count = count + 1  # or count += 1


