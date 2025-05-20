class Student:
    def __init__(self, name=None, age=None):
        if name is not None and age is not None:
            print(f"Constructor with name and age: Name = {name}, Age = {age}")
        elif name is not None:
            print(f"Constructor with only name: Name = {name}")
        else:
            print("Default constructor")

s1 = Student()
s2 = Student("Balaji")
s3 = Student("Jeeva", 25)
