# exerecise 5.1:
# list = []
# n = int(input("enter number og elements is list: "))
# for i in range(0,n):
#     ele = int(input("enter element: "))
#     list.append(ele)
# print(max(list))
# print(min(list))
# print(sum(list)/len(list))
# exeresice 5.2:
# str = input("enter a long string: ")
# str = str[::-1]
# print(str)
# exersice 5.3:
# import random
# lst = []
# n = 10
# for i in range(n):
#     ran = random.randint(0,10)
#     lst.append(ran)
# print(lst)
# exerecise 5.4:
# lst1 = []
# n = int(input("enter how many elements you want: "))
# for i in range(n):
#     ele = int(input("enter element: "))
#     lst1.append(ele)
# lst2 = []
# m = int(input("enter how many elements you want: "))
# for i in range(m):
#     ele = int(input("enter element: "))
#     lst2.append(ele)
# lst3 = lst1 + lst2
# print(lst3)
# print(len(lst3))

# exersice 5.5:
# lst_failed = []
# lst_passed = []
# n = int(input("enter how many grades there are: "))
# count_failed = 0
# count_passed = 0
# for i in range(n):
#     grade = int(input("enter grade: "))
#     if 1 <= grade <= 60:
#         lst_failed += [grade]
#         count_failed += 1
#     elif 60 < grade <=100:
#         lst_passed += [grade]
#         count_passed += 1
# print("failed= ",count_failed,"the failed grades: ",lst_failed)
# print("passed= ",count_passed,"the passed grades: ",lst_passed)
# exercise 5.6:
# lst = []
# for i in range(1,11):
#     lst.append(i)
# print(lst)
# lst1 = lst[7:]
# print(lst1[::-1])
# print(lst[1::2])
# print((lst[::2]))
# lst_new = lst
# num1 = int(input("enter number: "))
# lst_new[4] = num1
# num2 = int(input("enter a number: "))
# lst_new[5] = num2
# num3 = int(input("enter a number: "))
# lst_new.append(num3)
# print(lst_new)
# lst_double = lst * 2
# print(lst_double)
# lst_firstlast = []
# lst_firstlast.append(lst[0])
# lst_firstlast.append(lst[-1])
# print(lst_firstlast)

#external exercises (list)
#1
# from random import randint
# lst = []
# for i in range(9):
#     num = randint(1,100)
#     lst += [num]
# print(lst)
# 2 ///for exercises 2:11
# lst = []
# for i in range(1,11):
#     lst += [i]
# print(lst)
#3
# lst_last3 = lst[7:]
# print(lst_last3)
# #4
# lst_back = lst[::-1]
# print(lst_back)
# #5
# lst_even = lst[1::2]
# print(lst_even)
# #6
# lst_first5 = lst[:4]
# print(lst_first5)
# #7
# lst_odd = lst[::2]
# print(lst_odd)
#8
# num = int(input("enter a number: "))
# lst[7:] = [num]
# print(lst)
#9
# num = int(input("enter a number: "))
# lst[-3:] = [num]
# print(lst)
#10
# lst_removed = []
# for num in lst:
#     if num % 3 == 0:
#         lst_removed += [num]
#         lst.remove(num)
# print(lst)
# lst += lst_removed
# print(lst)
#11
# lst = [1,1] + lst[2:]
# print(lst)
# for i in range(len(lst)-2):
#     lst[i + 2] = lst[i] + lst[i + 1]
# print(lst)
# #12
# lst_word = []
# str = input("enter a string: ")
# for i in str:
#     if i == " ":
#         continue
#     lst_word += [i]
# for i in lst_word:
#     if lst_word.count(i) > 1:
#         lst = lst_word.remove(i)
# print(lst_word)
#13
# import random
# lst = []
# for i in range(20):
#     num = random.randint(1,100)
#     lst += [num]
# print(lst)
# user_num = int(input("enter a number: "))
# while user_num in lst:
#     lst.remove(user_num)
# print(lst)
#14
# num = int(input("enter a number: "))
# lst = []
# for i in range(1, num + 1):
#     if num % i == 0:
#         lst += [i]
# print(lst)
#15
# fib_len = int(input("how many numbers in the fibonachi sequence?"))
# num1 = 0
# num2 = 1
# count = 0
# lstf = [num1, num2]
# while count < fib_len:
#     lstf += [num1]
#     sum_num = num1 + num2
#     num1 = num2
#     num2 = sum_num
#     count += 1
# print(lstf)
#16
# import random
# lst = []
# for i in range(10):
#     num = random.randint(1,10)
#     lst.append(num)
# print(lst)
# for i in lst:
#     if lst.count(i) > 1:
#         lst.remove(i)
# print(lst)
#17
# import random
# lst1 = [random.randint(1,100) for i in range(1,10)]
# lst2 = [random.randint(1,100) for i in range(1,10)]
# print(lst1)
# print(lst2)
# for i in lst1:
#     if i in lst2:
#         print("there is 1 common member in the lists")
#         break
# else:
#     print("no common members")
#18
# lst = [input("enter a word: ") for i in range(5)]
# print(lst)
# count = 0
# for i in lst:
#     if len(i) >= 4 and i[0] == i[-1]:
#         count += 1
# print("the number of words where the number of letters is 4 ot more and the first and last letters are the same is: ", count)
#19
# import random
# lst = [random.randint(1,10) for i in range(10)]
# print(lst)
# count = 0
# for i in lst:
#     count = lst.count(i)
#     print(f"{i} is in the list {count} times")
#20
# import random
# lst = [random.randint(1,10) for i in range(10)]
# print(lst)
# num = int(input("enter a number: "))
# count = 0
# for i in lst:
#     if i != num:
#         count += 1
#         continue
#     elif i == num:
#         count +=1
#         print("num is in index: ", count - 1)
#         break
# else:
#     print("sorry! the number you chose is not in the list")
#21
# import random
# string = ""
# for i in range(4):
#     ran = str(random.randint(0, 9))
#     while ran in string:
#         ran = str(random.randint(1,9))
#     string += ran
# print("Hello player! are you ready for a game?")
# print("You need to guess a 4 digits number and we will tell you if you guessed the correct number.")
# print("bools means you found a digit, hits means you found the digit in the exact spot!\nNow let us begin!")
# guess = input("Please enter a 4 digits number: ")
# bools = 0
# hits = 0
# while guess != string:
#     for i in guess:
#         if i in string:
#             bools += 1
#     for i in range(len(guess)):
#         if guess[i] == string[i]:
#             hits += 1
#             # we can delete bools -= 1 but then the number of bools will contain hits
#             bools -= 1
#     print(f"Your bools are: {bools} and hits are: {hits}")
#     guess = input("Enter another guess: ")
#     bools = 0
#     hits = 0
# else:
#     print(f"Congrats! The number you've entered is correct and it was {string}!")
#22
# import random
# words_list = ["king", "queen", "prince", "lion", "zebra", "elephant", "horse", "dog", "cat", "school",
#               "paper", "desk", "key", "champion", "rock", "book", "head", "hands", "leg", "mountain",
#               "grass", "house", "pencil", "rain", "fall", "summer", "winter", "spain", "france", "italy"]
# print("Hello player! Are you ready for a game?\nThis is the number of words you need to guess:")
# ran_word = random.choice(words_list)
# ran_word_split = list(ran_word)
# word_len = []
# for i in ran_word_split:
#     word_len += "_"
# print(" ".join(word_len))
# print("you have 8 trials!")
# guess = input("please enter a letter you think is in the word: ")
# count = 0
# while count < 8:
#     for i in range(len(ran_word_split)):
#         if guess == ran_word_split[i]:
#             word_len[i] = guess
#     print(" ".join(word_len))
#     count += 1
#     if word_len == ran_word_split:
#         print("congrats!! youve guessed the right number!!!")
#         break
#     guess = input("please enter a letter you think is in the word: ")
# else:
#     print("sorry! you didn't guess in 8 trials!")

#tuples:
##exercise 6.1:
# t = (1, 2, 3)
# (a, b, c) = t
# print(a, b, c)
# exercise 6.2:
# t = ("a", "b", "c", "d", "e")
#2
# str = t[0] + t[1] + t[2] + t[3] + t[4]
# print(str)
# 1
# str = ""
# for i in t:
#     str += i
# print(str)
##exercise 6.3:
# tuple_info = ("name: tzach agam", 5776565, 22, 0, "none")
# print("the clients personal info: ", tuple_info)
# print("the clients personal info: ")
# for i in tuple_info:
#     print(i)
# exercise 6.4:
# import random
# lst = []
# for i in range(1,10):
#     lst += [random.randint(1,100)]
# print(lst)
# tup = tuple(lst)
# print(tup)
# num = int(input("enter a number: "))
# lst.append(num)
# print(lst)
# tup2 = tuple(lst)
# print(tup2)
#dictionary:
# 7.1:
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}
# dic_new = {}
# dic_new.update(dic1)
# dic_new.update(dic2)
# dic_new.update(dic3)
# print(dic_new)
# 7.2:
# print(dic_new)
# if 1 in dic_new:
#     print("1 is found")
# 7.3:
# dict = {1:10, 2:20, 3:30, 4:40, 5:50}
# dict = {value:key for key, value in dict.items()}
# print(dict)
# 7.4:
# num = int(input("enter a number: "))
# di = {}
# for i in range(num):
#     di.update({i:i*i})
# print(di)
# 7.5:
# di = {1:10, 2:20, 3:30, 4:40, 5:50}
# sum = 0
# for i in di:
#     sum += di[i]
# print(sum)
# 7.6:
# di = {1:10, 2:20, 3:30, 4:40, 5:50}
# num = int(input("enter a number: "))
# del di[num]
# print(di)
# 7.7
# di = {1:10, 2:20, 3:30, 4:40, 5:50, 6:50}
# result = {}
# for key,value in di.items():
#     if value not in result.values():
#         result[key] = value
# print(result)
# #7.8:
# names = ["gadi", "yonit", "toni", "gali", "shimi"]
# grades = [80, 90, 60, 50, 20]
# di = {}
# for key in names:
#     for value in grades:
#         di[key] = value
#         grades.remove(value)
#         break
# print(di)
# 8.1:
# set1 = {1, 3, 6, 5,7, 0}
# set2 = {3, 6, 5, 1, 7,9}
# set3 = set()
# set3.update(set1)
# set3.update(set2)
# print(set3)
# set3.remove(6)
# print(set3)
# print(f"max set3: {max(set3)}, min set3: {min(set3)}, len set3: {len(set3)}")
# set4 = set()
# set4.update(set3)
# set4.add(4)
# print(set4)
# set1.clear()
# set2.clear()
# print(f"set1: {set1}, set2: {set2}")

