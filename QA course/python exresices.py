#external (while-for basics)
#exercise 1:
# sum = 0
# len = 0
# for i in range(6):
#     num = int(input("enter a number: "))
#     sum += num
#     len += 1
# avrage = sum / len
# print(avrage)
#exersice 2:
# sum = 0
# len = 0
# for i in range(6):
#     num = int(input("enter a number: "))
#     if num % 2 == 0:
#         sum += num
#         len += 1
# average = sum / len
# print(average)
#exercise 3:
# for i in range(10,100):
#     if i % 10 == 7:
#         print(i)
# #exercise 4:
# sum = 0
# for i in range(10,100):
#     if i % 10 == 0:
#         sum += i
# print(sum)
#exercise 5:
# grade_num = int(input("enter how many grades there are: "))
# sum_passed = 0
# len_passed = 0
# for i in range(grade_num):
#     grade = int(input("enter grade: "))
#     if 0 <= grade <= 100:
#         if grade >= 60:
#             sum_passed += grade
#             len_passed += 1
# average = sum_passed / len_passed
# print("the averge score of those who passed is: ",average)
#exercise 6:
# grade_num = int(input("enter how many grades there are: "))
# sum_pass = 0
# len_pass = 0
# sum_failed = 0
# len_failed = 0
# for i in range(grade_num):
#     grade = int(input("enter grade: "))
#     if 0 <= grade <= 100:
#         if grade >= 60:
#             sum_pass += grade
#             len_pass += 1
#         elif grade < 60:
#             sum_failed += grade
#             len_failed += 1
# average_pass = sum_pass / len_pass
# average_failed = sum_failed / len_failed
# print("the average grade of those who passed is: ",average_pass)
# print("the average grade of those who failed is: ",average_failed)
#exercise 7:
# sum = 0
# for i in range(5):
#     num = int(input("enter a number: "))
#     right_digit = num % 10
#     sum += right_digit
# print(sum)
#exercise 8:
# num = int(input("enter a number: "))
# for i in range(1,num):
#     if i % 5 == 0:
#         print(i)
#exercise 9:
# num = int(input("enter a number: "))
# for i in range(2,num + 1,2):
#      print(i)
#exercise 10:
# count = 0
# num = int(input("enter a number: "))
# while num != 0:
#     if num != 0:
#         if num % 3 == 0 or num % 7 == 0:
#             count += 1
#     num = int(input("enter a number: "))
# print("the number of numbers that divide 3 or 7 is:", count)
#external (while-for advenced)
#1
# grade_max = 0
# sum_grade = 0
# count = 0
# grade = int(input("enter grade: "))
# while 0 <= grade <= 100:
#     if grade > grade_max:
#         grade_max = grade
#     sum_grade += grade
#     count += 1
#     grade = int(input("enter grade: "))
# print("the highest grade is: ",grade_max)
# average = sum_grade / count
# print("the average grade is: ",average)
# difference = grade_max - average
# print("the difference between highest grade and average is: ",difference)
#2
# passward = int(input("enter passward: "))
# for i in range(5):
#     veri_passward = int(input("enter verification: "))
#     if veri_passward == passward:
#         print("verification successful!!")
#         break
#     elif veri_passward != passward:
#         print("verification failed!!")
#         continue
# else:
#     print("too many tries!! failed!!!")
#3
# sum = 0
# num = (input("enter a number: "))
# for i in num:
#     sum += int(i)
# print(sum)
#4
# num = int(input("enter a number: "))
# for i in range(2,num):
#     if num % i == 0:
#         print("this is not a prime number!!!")
#         break
# else:
#     print("this is a prime number!!!")
#5
# count = 0
# num = input("enter a number: ")
# for i in num:
#     count +=1
# print(count)
#6
# num = int(input("enter a number: "))
# min_num = num
# while num != 0:
#     if num > 0:
#         if num < min_num:
#             min_num = num
#     num = int(input("enter a number: "))
# print(min_num)
#7
# num = input("enter a number: ")
# for i in num:
#     print(i)
#     break
#8
# lst = []
# for i in range(7):
#     num = int(input("enter a number: "))
#     lst = lst + [num]
# print(lst)
# max = 0
# for i in lst:
#     if i > max:
#         max = i
# print(f"the serial number of the highest value is: {lst.index(max) + 1}")
#9
# num = input("enter a number: ")
# num = num[::-1]
# print(num)
# print(int(num) * 2)
#10
num1 = int(input("enter a number: "))
num2 = int(input("enter a number: " ))
while num1 < num2:
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))
num2_in_num1 = 0
count = 0
while num2_in_num1 <= num1 - num2:
    num2_in_num1 += num2
    count += 1
print("the division of num1 in num2 is: ", count)
module = num1
while module >= num2:
    module -= num2
print("the leftover of the division of num1 in num2 is: ", module)