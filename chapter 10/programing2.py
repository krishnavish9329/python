
# class Student:
#     def __init__(self,name):
#         self.name = name

# s1= Student("krishna")
# print(s1.name)
# del s1 
# print(s1.name)


#private(linke) Attributes


# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass #private Attribute(__(name of veriable))
#     def reset_pass(self, acc_new_pass):
#         print(self.__acc_pass)
#         self.__acc_pass=acc_new_pass
#     def __hello(self):
#         print("hello  name  enter the details")
#     def welcome(self):
#         self.__hello()

    
# a1=Account(1234,"abc")
# a1.welcome()
# print(a1.acc_no)
# a1.reset_pass(123)
# a1.reset_pass('a')
# a1.reset_pass('a')


# a2=Account("1234","abc")
# print(a2.acc_no)



#inheritance 

#single interitance


# class Car:
#     color="black"
#     @staticmethod
#     def start():
#         print("car started")
#     @staticmethod
#     def stop():
#         print("car stopped :")    
# class ToyptaCar(Car):
#     def __init__(self,barnd):
#         self.band = barnd


# car1 = ToyptaCar("fortuner")
#car1 = Fortuner("EV")

# print(car1.name)
# print(car1.color)
# print(car1.start())


#multi-level inheritance 

# class Car:
#     @staticmethod
#     def start():
#         print("car started")
#     @staticmethod
#     def stop():
#         print("car stopped :")    
# class ToyptaCar(Car):
#     def __init__(self,barnd):
#         self.band = barnd
    
# class Fortuner(ToyptaCar):
#     def __init__(self,type):
#         self.type=type

# car1 = Fortuner("EV")


# print(car1.type)
# print(car1.start())


#multipale inheritance

# class A:
#     varA ="welcome to class A"


# class B:
#     varB ="welcome to class B"

# class C (A,B):
#     varC ="welcome to class C"

# c1=C()

# print(c1.varA)
# print(c1.varB)
# print(c1.varC)


#super mrthod


# class Car:
#     def __init__(self,type):
#         self.type=type

#     @staticmethod
#     def start():
#         print("car started")
#     @staticmethod
#     def stop():
#         print("car stopped :")    
# class ToyptaCar(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         super().stop()
#         self.name = name

# car1 = ToyptaCar("fortuner","EV")
# print(car1.name)
# print(car1.type)
# print(car1.start())


# #classMethod


# class person:
#     name="anonymous"
#     # def chnageName(self,name):
#     #     # self.name=name
#     #     person.name=name #1st method of class method
#     #     self.__class__.name=name #2st method of class method

#     @classmethod
#     def chnageName(cls,name):
#         cls.name=name

# p1=person()
# p1.chnageName("krishna")

# print(p1.name)
# print(person.name)


#propety method

# class student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem = chem
#         self.math=math
#     @property
#     def percentage(self):
#         return str((self.phy+ self.chem +self.math)/3)+"%"
# stu1= student(89,97,99)
# print(stu1.percentage)
# stu1.phy=86
# print(stu1.phy)
# print(stu1.percentage)



#polymorphism

class str:
    def __init__(self,name):
        self.name=name

    def __add__(self,s2):
        return self.name+" "+s2.name
s1=str("krishna")
s2=str("vishwakarma")

s3=s1+s2
print(s3)

