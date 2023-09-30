# #exresice 2.1
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# city = input("Enter your city: ")
# print("your name is:",name,"\nyour age is:",age,"\nyour city is:",city)
# #exrecise 2.2
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# city = input("Enter your city: ")
# print("your name is %s, your age is %d, your city is %s" %(name,age,city))
# #exrecise 2.3 ******** need guidence here
# all_info = input("Enter all your address info: ")
# lst = all_info.split(" ")
# print(lst)
# for i in lst:
#     print(i)
# #exrecise 2.4 ************* need guidence here
# string = input("enter a string: ")
# print(len(string))
# print(string[2:7])
# print(string.split(" ")[0]*3)
# print(str.title(string))

# external exercises:
#1
# word = input("enter a word: ")
# new_word = ""
# for i in word:
#     if i != "a" and i != "A":
#         new_word += i
# print(new_word)
#2
# string = input("enter a string: ")
# lengh = len(string)
# new_string = ""
# for i in range(lengh):
#     new_string = string[0] + string[lengh -1]
#     print(new_string)
#3
# word = input("enter a word: ")
# letter = input("enter a letter: ")
# for i in range(len(word) - 1):
#     if word[i] == letter:
#         print(i)
#         break
# else:
#     print("-1")
#4
# word = input("enter a word: ")
# count = 0
# for i in word:
#     count += 1
# print("The length of the word is:", count)
#5
# word = input("enter a word: ")
# letter = input("enter a letter: ")
# count = 0
# for i in word:
#     if i == letter:
#         count += 1
# print("The number of tines the letter is in the word is:", count)
#6
# word = input("enter a word: ")
# print(word[0].upper() + word[1:])
#7
# word = input("enter a word: ")
# new_word = ""
# for i in word:
#     new_word += i * 2
# print(new_word)
#8 need guidence here
# word = input("enter a word: ")
# new_word = ""
# for i in word:
#     if word.count(i) > 1:
#         new_word += i
# print(new_word)
#9
# word1 = input("enter a word: ")
# word2 = input("enter a word: ")
# string = ""
# for i in word1:
#     if i in word2 and i not in string:
#         string += i
# print(len(string))
# 10
# import random
# name = input("Enter a name: ")
# passward = ""
# for i in range(len(name)):
#     passward += random.choice(name)
# print(passward)
# 11
# sentence = input("enter a sentence: ")
# word = input("enter a word: ")
# lst_sentence = sentence.split()
# lst_times = []
# for i in range(len(lst_sentence)):
#     if word == lst_sentence[i]:
#         lst_times += [i]
# print(lst_times)
# 12
# sentence = input("Enter a sentence: ")
# first option:
# cap_sentence = sentence.title()
# print(cap_sentence)
# seconf option:
# sentence = input("Enter a sentence: ")
# lst_sentence = sentence.split()
# new_sentence = ""
# for i in lst_sentence:
#     new_sentence += i.capitalize() + " "
# print(new_sentence)
# 13:
# sentence = input("enter a sentence: ")
# word = input("enter a word: ")
# new_sentence = ""
# for i in sentence:
#     if i == word:
#         new_sentence += i.capitalize()
#     else:
#         new_sentence += i
# print(sentence)
# print(new_sentence)




