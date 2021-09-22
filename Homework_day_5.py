"""DATA STRUCTURES"""

# 1. Write a program to multiply all the items in a list.
# Գրել ծրագիր, որը կբազմապատկի լիստի բոլոր թվերը։

# lst=[5,4,2,1,3,12,3]
# result = 1
# for i in lst:
#  result *= i
#
# print(result)

# 2. Write a program to count the number of strings where the string length is 2 or more and the first and last
# character are same from a given list of strings.
# Գրել ծրագիր, որը կհաշվի լիստում եղած 2 կամ ավել երկարություն ունեցող լիստերի քանակը, որոնց առաջին և վերջին տառերը
# նույնն են։

# lst = [['hello', 'hi'], ['good', 'bad', 'nice'], ['like'], ['grow'], ['bob'], ['pick', 'up'], ['nice', 'brown']]
# result = 0
# for i in lst:
#  if len(i) >= 2 and i[0][0] == (i[len(i)-1][len(i[len(i)-1])-1]):
#   result += 1
# print(result)



# 3. Write a program that will remove duplicates from a list. DO NOT use set() method directly on the list.
# Գրել ծրագիր, որը կջնջի դուպլիկատները լիստից։ ՉՕԳՏԱԳՈՐԾԵԼ set() մեթոդը։
# lst = ['hello', 'how', 'are', 'you', 'my', 'friend', 'how', 'old', 'are', 'you']
#
# print(lst)
# for i in lst:
#  for j in lst:
#   if i == j:
#    lst.pop(lst.index(i))
#    print(lst)

#??
# 4. Create a list from 5 user inputs.
# Ստեղծել լիստ 5 ներմուծված թվերից
# lst = []
# x = input('Enter your first number:')
# y = input('Enter your second number:')
# z = input('Enter your third number:')
# q = input('Enter your fourth number:')
# w = input('Enter your fifth number:')
# lst.append(x)
# lst.append(y)
# lst.append(z)
# lst.append(q)
# lst.append(w)
# print(lst)
# 5. Write a program to print the given list after removing the 2nd, 4th and 5th elements.
# Գրել ծրագիր, որը կջնջի տրված լիստի 2-րդ, 4-րդ և 5-րդ էլեմենտները։

# lst = ['Rock', 'Pop', 'Metal','Hip-Hop', 'Rap']
# lst.pop(1)
# lst.pop(2)
# lst.pop(2)
# print(lst)
# 6. Given a list of ints, print True if the array contains a 2 next to a 2 somewhere.
# Գրել ծրագիր, որը կտպի True, եթե տրված լիստում ինչ-որ տեղ 2 թվին 2 է հաջորդում։

# lst = [4, 3, 53, 3, 12, 4, 3, 2, 5, 4, 2, 2, 1, 2, 4, 5, ]
#
# for i in range(len(lst)):
#  if lst[i] == 2 and lst[i+1] == 2:
#   print(True)


# 7. Given a list of ints, print True if every element is a 1 or a 4, and False otherwise.
# Գրել ծրագիր, որը կտպի True, եթե լիստի բոլոր էլեմենտները 1 կամ 4 են։ Հակառակ դեպքում տպել False:

# lst = [4, 1, 4, 4, 1, 4, 1, 4,]
# bool = True
# for i in lst:
#  if i != 4 and i != 1:
#   bool = False
#   break
#
# print(bool)




# 8. Ask for user input and add that input as a key into the dictionary. If the key exists, warn the user about it and
# do nothing. Assign some arbitrary value to it.
# Պահանջել ներմուծել բանալի և ավելացնել այդ բանալին dictionary-ի։ Եթե այն արդեն գոյություն ունի, տպել, որ բանալին արդեն
# կա և ոչինչ չանել։ Որպես արժեք տեղադրել պատահական օբյեկտ
# my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# key = input('Enter Key:')
#
# if key in my_dict:
#  print('key is already in Dictionary')
# else:
#  my_dict[key] = 'NewValue'
#
# print(my_dict)


# 9. Loop through the values of a dictionary and add them to a new list.
# Ցիկլի միջոցով ավելացնել dictionary—ի արժեքները նոր լիստի մեջ։
# my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# NewList= []
# for val in my_dict.values():
#  NewList.append(val)
# print(NewList)



# 10. Write a script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys.
# Գրել ծրագիր, որը կստեղծի և կտպի dictionary, որի բանալիները [1,15] թվերն են, իսկ արժեքները դրանց քառակուսիները։

# my_dict = {}
#
# for i in range(1,16):
#  x = i ** 2
#  my_dict[i] = x
#
# print(my_dict)