#Variables are containers where you can store values (boolean, string, integers, floats)

#Strings - characters
first_name = "Dawid"
food = "pizza"
email = "dawid@gmail.com"

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

#Integers - whole numbers
age = 18
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} of students")

#Float - numbers with decimals
price = 10.99

print(f"The price is $10.99")

#Boolean - true or false
is_student = False
for_sale = True
is_online = True

print(f"Are you a student: {is_student}")

if is_student:
  print("You are a student")
else:
  print("You are not a student")

if for_sale:
  print("That item is for sale")
else:
  print("That item is for sale")

if is_online:
  print("That item is for online sale")
else:
  print("That item is for online sale")