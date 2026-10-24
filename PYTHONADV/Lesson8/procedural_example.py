#Example of procedural programmin in Python
#OOP - Object oriented programming
#Polimorfizmi, trashegimia, enkapsulimi, abstraksioni, klasa, objekti

def calculate_area(length,width):
    return length*width

def calculate_perimetri(length,width):
    return 2*(length+width)

length =5
width=3

area = calculate_area(length,width)
perimeter = calculate_perimetri(length,width)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
