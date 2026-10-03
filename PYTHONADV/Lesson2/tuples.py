#tuple -- data types
# []
# ()

words = ("spam","eggs","sausages")

print(words[0])
print(words[1])
print(words[2])
print(words)

# words[1] = "cheese"

empty_tuple = ()
print(empty_tuple)

person = ("Alice",30,"Engineer")

#Tuple unpacking
name,age,profession = person

print(name, "'s"," profession is", profession," and she is", age, "years old.")