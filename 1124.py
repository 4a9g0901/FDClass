'''
class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
    def __str__ (self):
        return f"Name = {self.name}\n Agr ={self.age}"

test1 = Person("Lee", 20)
print(test1)

test2 = Person("May", 123)
print(test2.__dict__)

'''

class Students:

    def __init__(self, subjects, grades):
        self.subjects = subjects
        self.grades = grades
    
    def __str__(self):
        return f"subjects = {self.subjects }\ngrades = {self.grades} "    

class StudentName:

    def __init__(self) :
        self.Charlie = Students("Math", 60)        
        self.Mary = Students("English", 80)  
        self.Brian = Students("Science", 59)      
        self.Ken = Students("Operating System",100)

students_info = StudentName()

print(students_info.Charlie)
print(students_info.Mary)
print(students_info.Brian)
print(students_info.Ken)
    
    