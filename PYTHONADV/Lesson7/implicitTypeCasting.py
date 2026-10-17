#Example 1
from pyexpat.errors import messages

x = 32 #integer
y = 5.3 #float

result = x + y
print(result, " of type ", type(result))

age = 25

message = " I am " + str(age) + " years old"
print(message)

a=5
b="3"

result1 = a*int(b)
print(result1, " of type ", type(result1))


