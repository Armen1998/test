import math

# 1. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a nested loop.
# Օգտագործելով ցիկլեր, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։

?


# 2. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a list comprehension.
# Օգտագործելով comprehension, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։

lst = [i ** 2 for i  in range(1,4)]
lst1 = [i ** 2 for i in range(4,7)]
lst2 = [i ** 2 for i in range(7,10)]

print(lst)
print(lst1)
print(lst2)


# 4. Count the number of 'b's in the given string. DO NOT use the count() method.
# Հաշվել տրված սթրինգում 'b'-երի քանակը։ Չօգտագործել count() մեթոդը։
nonsense = 'Blinking blindly, brainy Bob brings beautiful beer bottles beneath blue butterflies billowing brilliantly.'
# Count1 = 0
#
# lst = list(nonsense)
# for words in lst:
#   if 'b' in words:
#     Count1 += 1
#   if 'B' in words:
#     Count1 += 1
# print(Count1)

# 5. Write a program that will print the factorial of n.
# Գրել ծրագիր, որը կտպի n թվի ֆակտորիալը։

# WAY 1

# n = int(input('Enter your number:'))
# lst=[ i for i in  range(1,n)]
#
# result = math.prod(lst)
# print(result)

# WAY 2

# result = 1
# n = int(input('Enter your number:'))
# for i in range(1,n):
#   result *= i
#
# print(result)

