# exercise 4.1
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# for i in range(num1+1,num2):
#     if i % 2 == 0:
#         print(i)
# exercise 4.2
# num = int(input("enter a number: "))
# for i in range(2,num):
#     if num % i == 0:
#         print("ths is not a primary number")
#         break
# else:
#     print("this is a primary number")
# exercise 4.3
# import random
# n = random.randint(1, 9)
# num = int(input("enter a number: "))
# while n != num:
#     if n > num:
#         print("the number tou guessed is lower")
#     elif n < num:
#         print("the number you guessed is higher")
#     num = int(input("enter a number: "))
# print("congrats! you guessed right")
# exersice 4.4
# import random
# count = 0
# num = int(input("enter a number between 1-100: "))
# ran = random.randint(1,100)
# while num != ran:
#     if num > ran:
#         massage = input("write higher: ")
#         count += 1
#     elif num < ran:
#         massage = input("write lower: ")
#         count += 1
#     num = int(input("enter a number between 1-100: "))
#     ran = random.randint(1, 100)
# massage = input("write exactly: ")
# print("counts until the exact number:",count)
# better one:
# import random
# count = 0
# left_border = 1
# right_border = 100
# num = int(input("enter a number between 1-100: "))
# ran = random.randint(1,100)
# massage = input(f"is {ran} higher, lower or exactly your number?")
# if massage == "exactly":
#     print("congrats! you guessed the right number")
# while num != ran:
#     if massage == "higher":
#         right_border = ran
#         ran = random.randint(left_border,right_border)
#         count += 1
#     elif massage == "lower":
#         left_border = ran
#         ran = random.randint(left_border, right_border)
#         count += 1
#     elif massage == "exactly":
#         break
#     num = int(input("enter a number between 1-100: "))
#     massage = input(f"is {ran} higher, lower or exactly your number?")
# print(f"congrats! you guessed the right number and it took you {count} guesses!! ")
# exercise 4.5
# nterms = int(input("How many terms? "))
# n1, n2 = 0, 1
# count = 0
# print("Fibonacci sequence:")
# while count < nterms:
#     print(n1)
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
#     count += 1
# exercise 4.6
# string = input("enter a string: ")
# char = input("enter a char: ")
# count = 0
# for i in string:
#     if i == char:
#         count += 1
# print(count)

####external (while):
# exercise 1
# num = int(input("enter a number with 3 digits: "))
# while 100 <= num <= 999:
#     sum = num // 100 + num % 10 + num // 10 % 10
#     print(sum)
#     num = int(input("enter a number with 3 digits: "))
# print("error")
#
# # exercise 2
# age = int(input("enter age: "))
# while 0<= age <=120:
#     if 0 <= age <= 18:
#         print("child")
#     elif 19 <= age <= 60:
#         print("adult")
#     elif 61 <= age <= 120:
#         print("senior")
#     age = int(input("enter age: "))
# print("the age you entered is not correct")

# exercise 3
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# while num1 % 2 == 0 and num2 % 2 == 0:
#     print(num1 + num2)
#     num1 = int(input("enter a number: "))
#     num2 = int(input("enter a number: "))
# print(num1 * num2)
#
# # # exercise 4
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# while num1 + num2 == 10:
#     num1 = int(input("enter a number: "))
#     num2 = int(input("enter a number: "))
# print("were done!")

# exercise 5
# num = int(input("enter a number between 10-99: "))
# while 10 <= num <= 99:
#     if num % 7 == 0 or num % 10 == 7 or num // 10 == 7:
#         print("cograts! you are lucky")
#     else:
#         print("not lucky number")
#     num = int(input("enter a number: "))
# print("wrong number!!")






