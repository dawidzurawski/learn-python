#A stack is a LIFO data structure (Last in First Out)

array = []

print(array)

#append adds items to the stack
array.append('Coffee')
array.append('Pizza')
array.append('Steak')
array.append('Milk')

stack = []

#The pop method removes the last items from the stack first
firstItem = array.pop()
secondItem = array.pop()
thirdItem = array.pop()
fourthItem = array.pop()

stack.append(firstItem)
stack.append(secondItem)
stack.append(thirdItem)
stack.append(fourthItem)

print(stack)

#pop removes items from the stack
#stack.pop()

#print(stack)

#last item would be "Steak" because the "Milk" was already removed
#lastItem = stack.pop()
#print(lastItem)

#check the length of the stack and find at which index is "Pizza"
#position = len(stack) - stack.index("Pizza")

#result will be 1 because it is the second item
#print(position)

#if len(stack) == 0:
#    print("The array is empty")
#else:
#    print("The array is not empty")