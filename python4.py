#functions    nothing but a block of code with defination 


def function_name():
  print("this is the body of function")

function_name()  # this is how to call a function

# you can pass params to a function

def show_what_is_passed(passed_value):
  print(passed_value)

show_what_is_passed(1)
show_what_is_passed('harshit')

# you can also assign a default value so if you dont assign
# any value it would take default one

def take_default_else_show(default_value = 'testing'):
  print(default_value)

take_default_else_show('showing passed val')
take_default_else_show()


# first if conditions

if 2 < 3 :
  print("right")

if 2 > 3:
  print("this will not prin")
else:
  print("false")

if 2 >3 :
  print("wrong")
elif 2 == 3:
  print("wronmg")    # if multiple if
else:
  print("this will run")


# function callback and return

def check(person):
  if int(person["age"]) > 18:
    return True
  else:
    return False
    
  
def studentinfo():
  person = {
    "name":"abhishek",
    "age":"19"
  }
  checkCondition = check(person) ### check the above function for defination

  if checkCondition  == True:
    print("eligible")
  else:
    print("not eligible")
  
studentinfo()