# example 1:
class student():
    name = "shivam das"

s1 = student()
print(s1.name)
s2 = student()
print(s2.name)
# basically both s1 and s2 are different objects of same class student but both have same attribute name as it is defined in the class once.


# example 2:
class car():
    color = "blue"
    brand = "BMW"

c1 = car()
print(c1.color)
print(c1.brand)



# example 3: (IMPORTANT)
class student:
    college_name = "avanthi institutes"
    name = "anonymous"  #class attr...........this is used in case any student name is not provided

    def __init__(self):
        pass
    # it is a default constructor
    # if we dont write any constructor then python provides a default constructor
    
    def __init__(self,name,marks):  # constructor with parameters
        self.name = name    #obj attr
        self.marks = marks
        print("adding new data to datebase")
    # it is a parameterized constructor

s1 = student("shivam",95)
print(s1.name,s1.marks)
print(student.college_name)

s2 = student("shreya",98)
print(s2.name,s2.marks)
print(student.college_name)
