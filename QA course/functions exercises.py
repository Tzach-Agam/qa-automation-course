# 10.1:
# def max_num(a,b,c):
#     return max(a,b,c)
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# num3 = int(input("enter a number: "))
# print(max_num(num1, num2, num3))
# 10.2:
# def sum_f(lst):
#     lst = list(input("enter a list: "))
#     lst1 = []
#     for i in lst:
#         lst1.append(int(i))
#     return sum(lst1)
# result = sum_f(lst1)
# print(result)
# 10.3:
# def multy_list(lst):
#     sum_multy = 1
#     for i in range(len(lst)):
#         sum_multy *= lst[i]
#     return sum_multy
# print(multy_list([1, 2, 3, 4, 5]))
# 10.4:
# def str_1(string):
#     string = string[::-1]
#     return string
# print(str_1("tzach"))
# 10.5:
# def is_in_range(a, b, c):
#     if b <= a <= c:
#         return True
#     else:
#         return False
# print(is_in_range(4, 3, 5))
# 10.6:
# def low_up(string):
#     count_up = 0
#     count_low = 0
#     for i in string:
#         if i.isupper():
#             count_up += 1
#         if i.islower():
#             count_low += 1
#     print("the number of upper cases is: ", count_up)
#     print("the number of lower cases is: ", count_low)
# low_up("Tzach")
# 10.7:
# def del_duplicates(lst):
#     lst1 = []
#     for i in lst:
#         if i not in lst1:
#             lst1.append(i)
#     return lst1
# print(del_duplicates([1,1,1,2,3,4,3,5,6,7,8,10]))
# **************************
# def del_duplicates(lst):
#     for i in lst:
#         if lst.count(i) > 1:
#             lst.remove(i)
#     return lst
# print(del_duplicates([1,1,1,2,3,4,3,5,6,7,8,10]))
# 10.8:
# def is_prime(a):
#     for i in range(2,a):
#         if a % i == 0:
#             return "Not Prime"
#     else:
#         return "Prime"
# print(is_prime(3))
# 10.9:
# def sum_only_even(lst):
#     sum_even = 0
#     for i in lst:
#         if i % 2 == 0:
#             sum_even += i
#     return sum_even
# print(sum_only_even([1,2,3,4,5,6,7,8,9,10]))
# 10.10:
# def str_poly(string):
#     if " " in string:
#         string = string.replace(" ", "")
#     if string == string[::-1]:
#         return "POLINDROM"
#     else:
#         return "NOT POLINDROM"
# print(str_poly("mamam am"))
#
# def try_some_default(name = "tzach", age = 22, *args):
#     args[0] = 23
#     print(name, age, args[0])
# try_some_default("tzach", 22, "is awesome")

#external exercises1:
#1:
# def sum_3dig(num):
#     sum = 0
#     for i in num:
#         sum += int(i)
#     return sum
# num = input("enter a number: ")
# result = sum_3dig(num)
# print(result)
#2:
# num = int(input("enter a number: "))
# def num_is_3(a):
#     if 100 <= a <= 999:
#         return True
#     else:
#         return False
# result = num_is_3(num)
# if result == True:
#     print("good you enterd a valid number")
# else:
#     print("not goood! wrong number")
#3:
# def name_times(string, a):
#     for i in range(a):
#         print(string)
# name = input("enter a name: ")
# num = int(input("enter a num: "))
# name_times(name, num)
#4:
# def sum_num(a):
#     sum_all = 0
#     for i in range(1, a +1):
#         sum_all += i
#     return sum_all
# num = int(input("enter a number: "))
# result = sum_num(num)
# print(result)
#5:
# for i in range(5):
#     num = int(input("enter a number: "))
#     result = sum_num(num)
#     print("the summary of all numbers until this number is:", result)
#6:
# def num_between(a, b):
#     for i in range(a, b + 1):
#         print(i, end=" ")
# num1 = int(input("enter a number:" ))
# num2 = int(input("enter a number: "))
# num_between(1, 4)
#7:
# def max_num(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# def min_num(a, b):
#     if a < b:
#         return a
#     else:
#         return b
# num_between(min_num(num1, num2), max_num(num1, num2))
#8:
# def muly_num(a, b):
#     return a ** b
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# result = muly_num(num1, num2)
# print(result)
#9:
# def age_group(a):
#     if 0 <= a <= 18:
#         return "child"
#     elif 19 <= a <= 60:
#         return "adult"
#     elif 61 <= a <= 120:
#         return "senior"
#     else:
#         return "invalid age"
# age = int(input("enter an age: "))
# result = age_group(age)
# print(result)
#10:
# def passed_failed(grade):
#     if 70 <= grade <= 100:
#         return True
#     else:
#         return False
# for grade in range(5):
#     grade = int(input("enter a grade: "))
#     result = passed_failed(grade)
#     if result == True:
#         print("you passed!!")
#     else:
#         print("failed!!!")
#11:
# def between_even(lst):
#     for i in range(2, 41, 2):
#             lst.append(i)
# list1 = []
# between_even(list1)
# print(list1)
#12:
# import random
# def between_ran(lst):
#     for i in range(20):
#         ran = random.randint(1, 100)
#         lst.append(ran)
#     return lst
# lst1 = []
# lst1 = between_ran(lst1)
# print(lst1)
# num1 = int(input("enter a number: "))
# count = 0
# for i in lst1:
#     if num1 == i:
#         count +=1
# print(f"The number of times {num1} is in the list is {count}")

#13:
# def max_20(lst):
#     max_num = max(lst)
#     return lst.index(max_num)
# max_index = max_20(lst)
# print(max_index)
#14:
# def student_num(num):
#     lst = []
#     for i in range(num):
#         grade = int(input("enter a grade: "))
#         lst.append(grade)
#     return lst
# students_num = int(input("enter the number of students: "))
# all_grades = student_num(students_num)
# print(all_grades)
#15
# def avg_grade(lst):
#     sum_grades = 0
#     for grade in lst:
#         sum_grades += grade
#     return sum_grades / len(lst)
# average = avg_grade(all_grades)
# print(average)
#external exercises 2:
#1
# def lentgh(lst):
#     count = 0
#     for i in lst:
#         count += 1
#     return count
# print(lentgh([1, 2, 3]))
#2
# def count_num(lst, a):
#     count = 0
#     for i in lst:
#         if i == a:
#             count += 1
#     return count
# print(count_num([1,2,3,3],3))
#3
# def find_index(lst, a):
#     for i in range(len(lst)):
#         if lst[i] == a:
#             return i
# print(find_index([1,2,3,4],2))
#4
# def max_num(lst):
#     max_dig = 0
#     for i in range(len(lst)):
#         if lst[i] > max_dig:
#             max_dig = lst[i]
#     return max_dig
# print(max_num([1,2,3,4,10]))
#5************
# def turn_to_list(a):
#     lst = []
#     if type(a) == dict or type(a) == set or type(a) == tuple or type(a) == str:
#         for i in a:
#             lst.append(i)
#         return lst
#     else:
#         print("Error")
#         return None
# print(turn_to_list({1:20, 3:30, 4:50}))
#6********* not sure if this is correct the adress may be not the same!!
# def remove_value(lst, a):
#     lst1 = []
#     for i in lst:
#         if i != a:
#             lst1 += [i]
#     return lst1
# print(remove_value([1,2,6,6,5,6],6))
#7
# def keys(dict):
#     lst = []
#     for i in dict:
#         lst += [i]
#     return lst
# print(keys({1:10,2:20,3:30}))
#8
# def values(dict):
#     lst = []
#     for i in dict:
#         lst += [dict[i]]
#     return lst
# print(values({1:10,2:20,3:30}))
#9
# def items(dict):
#     lst = []
#     for i in dict:
#         lst += [(i,dict[i])]
#     return lst
# print(items({1:10,2:20,3:30}))
#10
# def set_fun(lst):
#     set1 = set()
#     for i in lst:
#         set1.add(i)
#     return set1
# print(set_fun([1,2,3,4,4,5,5,56,6,6,7]))



# def final_grade(exam, hw):
#     if exam >= 50 and hw - exam <= 25:
#         grade = 0.75 * exam + 0.25 * hw
#     else:
#         grade = exam
#     return int(grade)
# print(final_grade(90, 90))
# print(final_grade(90, 100))
# print(final_grade(50, 90))
# print(final_grade(60, 95))
# print(final_grade(90, 79.4))

def month_days(m):
    if m < 1 or m > 12:
        return -1
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    elif m == 2:
        return 28
print(month_days(13))
print(month_days(1))
print(month_days(6))
print(month_days(2))

































