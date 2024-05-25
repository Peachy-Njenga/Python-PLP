# Create a Python class named Person
class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        
person1 = Person("Jamie", 30, "Male")

person1.introduce()