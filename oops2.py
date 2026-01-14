# # DELETE KEYWORD to delete an attribute of a class:
# class student:

#     def __init__(self,name):
#         self.name = name

# s1 = student("shivam")
# print(s1.name)
# del s1.name
# # print(s1.name)  # This will raise an AttributeError since name has been deleted



#PRIVATE METHOD:
# without private attribute:
class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass

a1 = account("12345","abcd")
print(a1.acc_no)
print(a1.acc_pass)
# in this case it will print the number and password of the account which is wrong because the private method is not implemented


# with private attribute:
class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # Private attribute

    def reset(self):
        print(self.acc_no)

a1 = account("12345","abcd")
print(a1.acc_no)
print(a1.reset())
print(a1.acc_pass)
# in this case it will print the number and password of the account which is wrong because the private method is not implemented

