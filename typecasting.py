# Typecasting = one variable to another

#str
name = "Bro Code"

#int
age = 25

#float
gpa = 3.2

#bool
is_true = True

#truncates the decimal (3.2 becomes 3)
gpa = int(gpa)
print(gpa)

#changes number to float (25 becomes 25.0)
age = float(age)
print()

#changes age to a string (the result will be the same: 25)
#however it will not be a different data type, a string not a variable
age = str(age)

#result would be "251" and not 26
age += "1"

#boolean value is true when the variable is a string, but if the string is empty it is false
name = bool(name)
print(name)

#print(type(name))