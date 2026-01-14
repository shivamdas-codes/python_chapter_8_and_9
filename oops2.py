# # DELETE KEYWORD to delete an attribute of a class:
# class student:

#     def __init__(self,name):
#         self.name = name

# s1 = student("shivam")
# print(s1.name)
# del s1.name
# # print(s1.name)  # This will raise an AttributeError since name has been deleted



# #PRIVATE METHOD:
# # without private attribute:
# class account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass

# a1 = account("12345","abcd")
# print(a1.acc_no)
# print(a1.acc_pass)
# # in this case it will print the number and password of the account which is wrong because the private method is not implemented


# # with private attribute:
# class account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass  # Private attribute

#     def reset(self):
#         print(self.acc_no)

# a1 = account("12345","abcd")
# print(a1.acc_no)
# print(a1.reset())
# print(a1.acc_pass)
# # in this case it will print the number and password of the account which is wrong because the private method is not implemented




# INHERITANCE example:
# single level inheritance
class car:  #base class
    color = "black"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class bmwmodel(car):    #single inheritance
    def __init__(self,model):
        self.model = model

b1 = bmwmodel("X5")
print(b1.color)
print(b1.model)
b1.start()

    
# multi-level inheritance     
class car:  #base class
    color = "black"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class bmwmodel(car):    #multi inheritance
    def __init__(self,name):
        self.model = name

class bmw_factory1(bmwmodel):   #multilevel inheritance
    def __init__(self,model,price):
        self.model = model
        self.price = price

b1 = bmw_factory1("X5",5000000)
print(b1.color)
print(b1.model)
print(b1.price)
b1.start()


