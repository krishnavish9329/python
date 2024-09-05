# class Employee: #base class
#     company="google"
#     def showDetails(self):
#         print("this is an employee")

# class programmer(Employee): #derive class
#     language="python"
#     def getLanguage(self):
#         print("the language is "+self.language)
#     def showDetails(self):
#         print("this is an programmer") #overwrit function 

# p=programmer()
# p.showDetails()
# p.getLanguage()
# print(p.company)

# class Employee:
#     company="visa"
#     eCode=120
# class freelancer:
#     company="fiverr"
#     level=0

#     def upgradeLevel(self):
#         self.level=self.level+1

# class programmer(Employee,freelancer):
#     name ="rohit"
# p=programmer()
# p.upgradeLevel()
# print(p.level)
# print(p.eCode)


class person:
    country="india"
    def takeBreath(self):
        print("iam breathing ...")
class Employee(person):
    company="honda"

    def getsalary(self):
        print(f"salary is {self.alary}")
    
    def takeBreath(self):
        print("i am an employee so i am luckily breeathing ...")

class prorammer(Employee):
    company="fiver"
    def getsalary(self):
        print("no salary to programmer ")

p=person()
e=Employee()
print(e.company)
pr=prorammer()
pr.takeBreath()
print(pr.company)
print(pr.country)
#e.getsalary()
