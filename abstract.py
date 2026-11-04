# #Abstract Methode

# from abc import ABC,abstractmethod

# class payment(ABC):  #parent abstract class
#     @abstractmethod
#     def pay(self,amount):
#         pass

# class CreditCard(payment):
#     def pay(self,amount):
#         print("Paid",amount,"using credit card")

# class cash(payment):
#     def pay(self,amount):
#         print("Paid",amount,"using cash")

# class UPI(payment):
#     def pay(self,amount):
#         print("Paid",amount,"using UPI")

# p1=UPI()
# p1.pay(1000)

# p2=CreditCard()
# p2.pay(2000)

# p3=cash()
# p3.pay(3000)

# from abc import ABC,abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def drive(self):
#        pass
# class Bike(Vehicle):
#     def drive(self):
#         print("Bike is moving")

# class Car(Vehicle):
#     def drive(self):
#         print("Car is moving")        

# class Bus(Vehicle):
#     def drive(self):
#         print("Bus is moving")     

# car=Car()
# bike=Bike()
# bus=Bus()
# car.drive()
# bike.drive()
# bus.drive()



# from abc import ABC, abstractmethod
# import math

# # Abstract Class
# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass


# # Circle Class
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius * self.radius


# # Rectangle Class
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# # Square Class
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side


# # Creating Objects
# c = Circle(35)
# r = Rectangle(12, 6)
# s = Square(4)

# # Display Areas
# print("Area of Circle =", round(c.area(), 2))
# print("Area of Rectangle =", r.area())
# print("Area of Square =", s.area())




# Excercise 2 

# Bank account


from abc import ABC, abstractmethod

# Abstract Class
class BankAccount(ABC):

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass


# Savings Account
class SavingsAccount(BankAccount):

    def deposit(self):
        print("Money deposited in Savings Account")

    def withdraw(self):
        print("Money withdrawn from Savings Account")


# Current Account
class CurrentAccount(BankAccount):

    def deposit(self):
        print("Money deposited in Current Account")

    def withdraw(self):
        print("Money withdrawn from Current Account")


# Creating Objects
s = SavingsAccount()
c = CurrentAccount()

# Calling Methods
s.deposit(1000)
s.withdraw(2000)

c.deposit(3000)
c.withdraw(4000)




#Notification System

# from abc import ABC, abstractmethod

# # Abstract Class
# class Notification(ABC):

#     @abstractmethod
#     def send(self):
#         pass


# # Email Notification
# class EmailNotification(Notification):

#     def send(self):
#         print("Sending Email Notification")


# # SMS Notification
# class SMSNotification(Notification):

#     def send(self):
#         print("Sending SMS Notification")


# # WhatsApp Notification
# class WhatsAppNotification(Notification):

#     def send(self):
#         print("Sending WhatsApp Notification")


# # Creating Objects
# e = EmailNotification()
# s = SMSNotification()
# w = WhatsAppNotification()

# # Calling Methods
# e.send()
# s.send()
# w.send()

# Institute Management

# from abc import ABC, abstractmethod

# # Abstract Class
# class Person(ABC):

#     @abstractmethod
#     def display_details(self):
#         pass


# # Student Class
# class Student(Person):

#     def display_details(self):
#         print("Student Name: Deepa")
#         print("Course: AIPA")


# # Teacher Class
# class Teacher(Person):

#     def display_details(self):
#         print("Teacher Name: Shailesh Yadav")
#         print("Subject: Python")


# # Principal Class
# class Principal(Person):

#     def display_details(self):
#         print("Principal Name: Ajay Pal Singh")
#         print("Institute: NSTI")


# # Creating Objects
# s = Student()
# t = Teacher()
# p = Principal()

# # Display Details
# s.display_details()
# t.display_details()
# p.display_details()




