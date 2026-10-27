# que 1

# i = 1
# while i <= 100:
#     print(i)
#     i += 1
# print("Lp ended")

# que 2

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
# print("Lp ended")

# # que 3 
# n = int(input("enter the number : "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1
 
# quest 4 
# n = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx < len(n):
#     print(n[idx])
# #     idx += 1

# quest 5
# t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# i = 0
# x = 36
# while i < len(t):
#     if (t[i] == x):
#         print("NUMBER FUNDS AT INDEX ", i)
#     else:
#         print("finding...............")
#     i += 1

# t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# i = 0
# x = 36
# while i < len(t):
#     if (t[i] == x):
#         print("NUMBER FUNDS AT INDEX ", i)
#         break
#     else:
#         print("finding...............")
#     i += 1

#print these element using fr lp
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for val in list:
#     print (val)


# list = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 25
# idx = 0
# for val in list:
#     if (val == x):
#         print("ur values n 25 find at : ", idx)
#     idx += 1

# n = int(input("enter the number : "))
# fact = 1 
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print("fact is : ", fact)

# n = int(input("enter a number : "))
# fact = 1
# i = 1
# for i in range(1, n+1):
#     fact *= i
# print("factorial of is : ", fact)

# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","a")
# f.write("\nso guys this is our next file ")
# f.close()

# # import os
# # os.remove("demo.txt")

# with open("sample.txt", "w") as f:
#     f.write("hii everone\nwe are learning file I/O\nusing java.\nI like programming in java.

# def check_for_word():
#     word = "learning"
#     with open("sample.txt",'r') as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("found")
#         else:
#             print("not found")
# check_for_word()

# count = 0
# with open("sample.txt", "r") as f:
#     data = f.read()
#     nums = data.split(",")
#     for i in nums:
#         if(int(i) % 2 == 0):
#             count += 1
# print(count)    

#constructer in python 

# #creating a class 
# class student:
# #if we are not passing any argument in consrtructer then it is called default constructer 
#     def __init__():
#         pass

# # >>>>>>>>> Parameterized constructer <<<<<<<<<<<   
#     def __init__(self, name , age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#         print("Adding newe student data in our database >>>>>>>>")

# #here we are creating our first object 
# s1 = student("chandan joshi", 21, "Dwarahat")
# print(s1.name, s1.age, s1.address)

# #here we are creating our second object
# s2 = student("Gokul singh chuhan", 21, "Rudrapur")
# print(s2.name, s2.age, s2.address)

#create students class that takes name and marks of 3 sub as arguments in cnstructer 
#then create a method to print the average 

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks 

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hiii", self.name, "Your avg marks is :", sum/3)

# s1 = student("Chandan Joshi", [98, 84, 97])
# s1.get_avg()

#Create accunt class with 2 attributes - Balance & accunt number 
#create methods for debit, credit , and printing the balance

#creating a class
# class account:                                           
#     def __init__(self, bal, acc):                   
#         self.balance = bal
#         self.account_number = acc

# #Debit
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was Debited.")
#         print("Total Balance: ", self.get_balance())

# #credit
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited.")
#         print("Total Balance: ", self.get_balance())

# #printing account balance 
#     def get_balance(self):
#         return self.balance
    
# #creting an object 
# acc1 = account(20000, 263653)
# acc1.debit(1000)   # Electricity Bill
# acc1.credit(600)   # Interest
# acc1.credit(40000) # Salary credited
# acc1.debit(5000)   # Monthly Rent

# # private keyword 
# class account:                                           
#     def __init__(self, bal, acc_no, acc_pass):                   
#         self.balance = bal
#         self.account_no = acc_no
#         self.__account_password = acc_pass #private keyword 
# acc1 = account(45000, 263653, 123123)
# print(acc1.balance)
# print(acc1.account_no)
# print(acc1.__account_password) #here we get error in this line 


#Inheritance
# class car:
#     @staticmethod
#     def start():
#         print("Car started........!")
#     @staticmethod
#     def stop():
#         print("car stoped.........!")

# class Toyota(car):
#     def __init__(self, name):
#         self.name = name

# # Multi-level Inheritance

# class fortuner(Toyota):
#     def __init__(self, type):
#         self.type = type

# car3 = fortuner("Diesel......")
# car1 = Toyota("Fortuner......")
# car2 = Toyota("Hycross.......")

# print(car3.type)
# print(car1.name)
# print(car2.name)
# print(car1.start())
# print(car1.stop())
# print(car2.start())
# print(car2.stop())

#Multiple Inheritance
# class a:
#     vara = "hii guys "

# class b:
#     varb = "i am learning python series from apna college. "

# class c(a, b):
#     varc = "And i am right now, in my learning face and one day i will become an ai/ml and data science engineer.....!"

# c1 = c()

# print(c1.vara)
# print(c1.varb)
# print(c1.varc)

# #class method 
# class person :
#     name = "anonymous"
#     @classmethod
#     def changename(cls, name):
#         cls.name = name
# p1 = person()
# p1.changename("chandan joshi")
# print(p1.name)
# print(person.name)

# #property method 
# class student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"

# stu1 = student(98, 89, 97)
# print(stu1.percentage)

# stu1.phy = 87
# print(stu1.percentage)

 #polymorphism operator overloading
# class complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img 
#     def shownumber(self):
#         print(self.real, "i +", self.img, "j")
#     def __add__(num1, num2):
#         newreal = num1.real + num2.real
#         newimg = num2.img + num2.img
#         return complex(newreal, newimg)
#     def __sub__(num1, num2):
#         newreal = num1.real - num2.real
#         newimg = num2.img - num2.img
#         return complex(newreal, newimg)
#     def __mul__(num1, num2):
#         newreal = num1.real * num2.real
#         newimg = num2.img * num2.img
#         return complex(newreal, newimg)
    
# num1 = complex(9, 8)
# num1.shownumber()

# num2 = complex(5, 3)
# num2.shownumber()

# class complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
#     def shownumber(self):
#         print(self.real, "i+", self.img, "j")
#     def __add__(num1, num2):
#         newreal = num1.real + num2.real
#         newimg = num1.img + num2.img
#         return complex(newreal, newimg)
# num1 = complex(5, 6)
# num1.shownumber()
# num2 = complex(3, 5)
# num2.shownumber()
# num3 = num1 + num2 
# num3.shownumber()


# # Guess the number game 
# import random
# target = random.randint(1, 100)
# while True:
#     userchoice = input("Guess the number or QUIT the game  : ")
#     if (userchoice == "Q"):
#         break
#     userchoice = int(userchoice)
#     if (userchoice == target):
#         print("Congrets, Correct guess !!!!!!")
#         break
#     elif(userchoice < target):
#         print("Think Biger Number.....!")
#     else:
#         print("This time you choose big number......!")

# print("!________________Game Over________________!")


# #random password genrator by using loop
# import random
# import string
# pass_len = 12
# charvalues = string.ascii_letters + string.digits + string.punctuation
# password = ""
# for i in range(pass_len):
#     password += random.choice(charvalues)
# print("your password is : ", password)


# #random password genrator by using loop
# import random
# import string
# pass_len = 12
# charvalues = string.ascii_letters + string.digits + string.punctuation
# result = "".join([random.choice(charvalues) for i in range(pass_len)])
# print("your password is : ", result)

#Import libraries and packages listed above
import pandas as pd
import numpy as np

# Load dataset into dataframe
df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')
print("done")