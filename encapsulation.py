# 02/11/2026
# class Employee:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self._salary = salary


#     def get_salary(self):
#         return self._salary

#     def inc_salary(self, amount):
#         if amount >0:
#             self._salary += amount
#             print("Salary updated")
#         else:
#             print("Invalid amount")

# emp=Employee("Shailesh",25,50000)
# print("Salary:",emp.get_salary())

# emp.inc_salary(8000)
# print("New Balance:",emp.get_salary())
# -------------------------------------------------------


# single inheritance

# class Animal():
#     def property(self):
#         print("Animal has 4 legs")

# class Dog(Animal):
#     def bark(self): 
#         print("Dog barks")

# d=Dog()
# d.bark()
# d.property()


# Multiple Inheritance

# class Father():
#     def skill1(self):
#         print("Driving")

# class Mother():
#     def skill2(self):
#         print("cooking")

# class child(Father, Mother):
#     def Qualities(self):
#         print("Inherited skill from parens:")
# x=child()
# x.Qualities()
# x.skill1()
# x.skill2()


#  multilevel inheritance

# class Grandfather():
#     def house(self):
#         print("Grandfather's house'")

# class father(Grandfather):
#     def bike(self):
#         print("Father's bike")

# class Son(Grandfather):
#     def laptop(self):
#         print("Son's laptop")

# class Grandson(father,Son):
#     def car(self):
#         print("Grandson's car")


# g=Grandson()
# g.house()
# g.bike()
# g.laptop()

