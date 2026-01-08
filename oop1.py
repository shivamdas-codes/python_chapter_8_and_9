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