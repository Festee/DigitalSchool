grades = {
    ("John","Math"):5,
    ("Alice","Biology"):4,
    ("Bob","Physics"):4,
    ("Eve","Music"):5,
    ("John","English"):4,
}

john_math = grades[("John","Math")]
print("John's grade in math is :", john_math)

grades[("Bob","Math")] = 3
print(grades)

keys = list(grades.keys())
print(keys)
