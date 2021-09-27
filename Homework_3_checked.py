"""IF, ELIF, ELSE"""

# 1. Enter your name, then find the sum of the ASCII values of the letters in your name. If that number is larger than
# 500, print "I've got a great name!", and "I've got a fancy name!" otherwise.
# Ներմուծեք ձեր անունը և գտեք անվան տառերի ASCII արժեքների գումարը։ Եթե թիվը մեծ է 500-ից, տպել "I've got a great
# name!", իսկ հակառակ դեպքում՝ "I've got a fancy name!"։

"""Լավ ա Արմեն ջան։ Կոդի ֆորմատավորումն էլ համարյա շատ լավ ա, բայց օրինակ հենց տակի տողում բացատները չկան 
օպերատորների ու թվերի արանքում։ Փորձի լուրջ ուշադրություն դարձնել դրան, գրագետ կոդը այդպես պիտի լինի։"""

# Name=(ord('A')+ord('r')+ord('m')+ord('e')+ord('n'))
#
# if Name>500:
#     print("I've got a great name!")
# else:
#     print("I've got a fancy name!")

# 2. Ask the user for a movie title. If the title starts with a capital letter, print "Great title!", otherwise print
# "Titles start with capital letters...". If the input starts with a special character [!, @, #, $, %, ^, &], print "I
# doubt that this is a title.".
# Պահանջել ներմուծել ֆիլմի վերնագիր։ Եթե վերնագիրը սկսվում է մեծատառով, տպել "Great title!", հակառակ դեպքում տպել
# "Titles start with capital letters..."։ Եթե ներմուծվածը սկսվում է [!, @, #, $, %, ^, &] նշաններով, տպել "I doubt that
# this is a title."․
# title=input('Enter movie title:')
#
# if title.istitle():
#     print("Great title!")
#
# elif title.startswith(('!', '@','#', '$', '%', '^', '&')):
#     print("I doubt that this is a title.")
#
# else:
#     print("Titles start with capital letters...")


# 3. Ask the user to input his/her age. If the user is older than 18, than tell them they're eligible to vote. If they
# are younger than 18, tell them how many years do they have to wait.
# Հարցրեք օգտատիրոջ տարիքը։ Եթե նա 18 տարեկանից մեծ է, նրան տեղյակ պահեք, որ կարող է քվեարկել։ Հակառակ դեպքում ասեք, թե
# քանի տարուց նա կկարողանա դա անել։
# age = int(input('how old are you?:'))
# if age >= 18:
#     print('you are eligible to vote')
# else:
#     print(f'you have to wait {18-age} years')


# 4. Write a program that will tell us whether a given year is a leap year or not.
# Գրել ծրագիր, որը կտեղեկացնի, թե տրված տարին նահանջ է, թե ոչ։

"""Էլի պայմաններ կան նահանջ տարի լինելու։ Օրինակ 1900-ը բաժանվում է 4-ի, բայց նահանջ չի։
Բոլոր պայմանները պսեվդոկոդով՝ 
if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)
"""
# x = range(0, 20000, 4)
# year = int(input('enter year:'))
#
# if year in x:
#     print('this year is a leap')
# else:
#     print('this year is not a leap')


# 5. Using 'random' module, generate a random number between -1000 and 1000. If the number is positive, print positive.
# If it's negative, print negative along with the absolute value of the number.
# Օգտագործելով random գրադարանը, գեներացնել [-1000,1000]-ը տիրույթում պատահական թիվ։ Եթե թիվը դրական է, տպել positive.
# Հակառակ դեպքում տպել negative և այդ թվի բացարձակ արժեքը։
import random
randnum  = random.randint(-1000, 1000)

if randnum > 0:
    print('positive')
else:
    print(f'negative {-randnum}')  # Բացարձակ արժեքը կարելի է ստանալ նաև abs() ֆունկցիայով