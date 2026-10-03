#create a list of names
names = ["Alice","Bob","Charlie","David"]

#Iterate in the names list and print every name
for name in names:
    print(name)

#################################################

sentence = "Hello, World!"

for character in sentence:
    if character.isalpha(): #Check if the character is a letter
        print(character)

#################################################

for number in range(1,6):
    print(number)

#################################################

numbers = [12,45,6,72,21,8,94,57]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
print("The maximum value in the list is: ",maximum)

#num:12   maximum:12
#num:45    max:45
#num:6    max:45
#num:72   max:72
