# some operations on data types
#- - - - -- - - - string operations

name = 'abhishek kakkar'
name1 = ['abhishek','kakkar'] # len(name1) will be 2

print(len(name)) # length of string or name or list
print(name.upper()) # upper case
print(name.replace('a', '1'))


line = 'length of abhishek 8'

if "abhishek" in line:
  print("abhishek is there")

if "abhishek" not in line:
  print("this will not run") # this statement will not run as there is "not" in condition



# - - -- - - - - list operationsa

alphabets = ["a","b","c","d"]
numz = [1,2,3,4]

print(alphabets[2])
print(numz[1:])   # this will display all values from 2 to end of list

alphabets.append("e")        # insert value at last
print(alphabets,"added e")
alphabets.pop()             # remove item from end
numz.pop(0)                 # remove at specific place
print(numz)
print(alphabets,"removed e")
alphabets.insert(1, "B")     # this list will be ["a","B","b".....] so on
print(alphabets)

counter = [1,2,3,3,1,1]
print(counter.count(1))   # value is 3




#-- -- -- - - dict or object

person = {
  "tshirt":"unknown",
  "gender":"male",
  "name":"abhishek",
  "married": False,
}

for i in person:
  print(i,person[i])
print('--------------------')
for key,value in person.items():
  print(key,value)

#getting all keys and values separately
keysPerson = person.keys()
valuesPerson = person.values()

print(keysPerson,valuesPerson)