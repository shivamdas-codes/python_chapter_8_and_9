# using delete keyword to delete an attribute of a class:
class student:

    def __init__(self,name):
        self.name = name

s1 = student("shivam")
print(s1.name)
del s1.name
# print(s1.name)  # This will raise an AttributeError since name has been deleted