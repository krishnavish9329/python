#object oriented approches

# class Student:
#     name="anonymous"
#     #parameterized constructor
#     def __init__(self,fullName):
#         print("hello am constructor")
#         # print(self)
#         self.name=fullName
#     # defalut constructor
#     def __init_subclass__(cls) -> None:
#         pass

#     def p(self):
#         print(self.name)

# s1= Student("krishna")
# print(s1.name)
# s1.p()
# print(Student.name)


# prectice 1
class student:
    #Static methods
    @staticmethod
    def hello():
        print("hello everone ")
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
        print("ok")
    def avg(self):
        sum =0
        for i in self.mark:
            sum += i
        return ((sum)/3)
    
krishna = student("krishna",[96,85,75])

print(krishna.avg())
krishna.hello()


# class Number:
#    def sum(self):
#        return self.a + self.b

# num=Number()
# num.a=2
# num.b=8
# s=num.sum()
# print(s)

# class num:
#    def sum(self,a,b):
#        return a+b
   
# num=num()
# s=num.sum(4,7)
# print(s)

# class railwayform:
#    formType="railwayform"
#    def printData(self):
#        print(f"name is {self.name}")
#        print(f"train name is {self.train}")
       
# hello=railwayform()
# hello.name="radha"
# hello.train="rani"
# hello.printData()

#class attributes
# class Emplyee:
#    company="Google"
#    def getSelary(self):
#         print(f"salaery for this employee working in {self.company} is {self.Salary}")

# krishna=Emplyee()
# #sangam=Emplyee()
# #Emplyee.compainy="youtub" # change the class attributes
# #print(krishna.compainy)
# #krishna.selary=300
# #print(krishna.selary)
# #
# #print("sangam details:-")
# #print(sangam.compainy)
# #sangam.selary #Emplyee.selary(sangam)

# krishna.Salary=1000
# #krishna.getSelary()
# Emplyee.getSelary(krishna)

#static methor

# class Emplyee:
#     company="Google"
#     def getSelary(self):
#          print(f"salaery for this employee working in {self.company}is {self.Salary}")
#     @staticmethod
#     def greet():
#         print("Good morning")
# krishna=Emplyee()
# krishna.Salary=1222
# krishna.getSelary()
# Emplyee.getSelary(krishna)
# krishna.greet()

# class Employee:
#     company="google"

#     # def __init__(self):
#     #     print("employee is created")
        
#     def __init__(self,name,date,time):
#         print("employee is created")
#         print("employee name " + name)
#         print(f"employee is created \n employee name is {name} and {date} and {time} ")

#     def getSalary(self, signature):
#         print(f"salary for this employee working in {self.company} is {self.Salary}")
    
#     @staticmethod
#     def greet():
#         print("good morning")
    
#     @staticmethod
#     def time():
#         print("the time is --:-- \n")

# # krishna=Employee()
# krishna=Employee('krishna',22,5)
# krishna.Salary=2200
# krishna.getSalary(77)
# krishna.greet()