'''
1. if else ---> este o afirmatie ce tine de flow control, se executa blocul de cod 'if' daca conditia este True, iar
daca este falsa, se executa blocul de cod 'else'

2.
# '''
# import random
# x = int(input('x = '))
# y = int(input('y = '))
# z = int(input('z = '))
#
# if x>= 0:
#     print(f'{x} este un nr natural.')
# else:
#     print(f'{x} nu este nr natural.')
#
# # 3.
# if x < 0:
#     print(f'{x} este un nr negativ.')
# elif x > 0:
#     print(f'{x} este un nr pozitiv.')
# else:
#     print(f'{x} este neutru.')
#
# #4.
# if -2 < x < 13:
#     print(f'{x} este cuprins intre -2 si 13') # sau print(True)
# else:
#     print(f'{x} nu este cuprins intre -2 si 13') # print(False)
#
# #5.
# if x-y < 5:
#     print('Diferenta nr este mai mică decat 5')
# else:
#     print('Diferenta nr este mai mare decat 5')
#
# # 6.
# if not(5 < x < 27):
#     print(f'{x} nu e cuprins intre 5 si 27')
# else:
#     print(f'{x} este cuprins intre 5 si 27.' )
#
# # 7.
# if x == y:
#     print('Numerele sunt egale.')
# else:
#     print(f'Numarul mai mare este {max(x,y)}')
#
# # 8.
# if x == y == z:
#     print('Triunghiul este echilateral.')
# elif x == y != z or x != y == z or x == z != y:
#     print('Triunghiul este isoscel.')
# else:
#     print('Triunghiul este oarecare.')
#
# 9.
#
# letter = input('Choose a letter...')
# vocale = ['a', 'e', 'i', 'o', 'u', 'ă', 'î', 'â']
# if letter in vocale:
#     print('Este o vocala.')
# else:
#     print('Nu este o vocala.')
#
# # 10.
# nota = float(input('Nota = '))
# if nota >= 9:
#     nota = 'A'
#     print('Nota convertita este ' + nota)
# elif nota >= 8:
#     nota = 'B'
#     print('Nota convertita este ' + nota)
# elif nota >= 7:
#     nota = 'C'
#     print('Nota convertita este ' + nota)
# elif nota >= 6:
#     nota = 'D'
#     print('Nota convertita este ' + nota)
# elif nota >= 4:
#     nota = 'E'
#     print('Nota convertita este ' + nota)
# else:
#     nota = 'F'
#     print('Nota convertita este ' + nota)
#
# # OPȚIONALE 1.
# x = int(input('x = '))
# y = int(input('y = '))
# z = int(input('z = '))
#
# if len(str(x)) >= 4 and str(x).isnumeric():
#     print(f'{x} are minim 4 cifre.')
# else:
#     print(f'{x} nu are minim 4 cifre.')
# # 2.
# if len(str(x)) == 6 and str(x).isnumeric():
#     print(f'{x} are exact 6 cifre.')
# else:
#     print(f'{x} nu are exact 6 cifre.')
# # 3.
# if x % 2 == 0:
#     print(f'{x} este un nr par.')
# else:
#     print(f'{x} este un nr impar.')
#
# # 4.
# if x > y and x > z:
#     print(f'{x} este nr mai mare.')
# elif y > z and y > x:
#     print(f'{y} este nr mai mare.')
# elif z > x and z > y:
#     print(f'{z} este nr mai mare.')
# else:
#     print('Numerele sunt egale')
#
# # 5.
# # Suma unghiurilor unui triunghi este 180 grade.
# suma_ung = x + y + z
# if x > 0 and y > 0 and z > 0 :
#     if suma_ung == 180:
#         print('Acesta poate fi un triunghi valabil.')
#     else:
#         print('Triunghi invalid.')
# else:
#     print('Nu exista unghiuri cu valori negative.')

# 6.
coral_str = 'Coral is either the stupidest animal or the smartest rock'
if x > 0:
    coral_trimmed = coral_str[:-x]  #returneaza stringul de la inceput pana la indexul -x
    print(coral_trimmed)
else:
    coral_trimmed = coral_str[:x]
    print(coral_trimmed)

# 7.
coral_dubios = coral_str[:5] + coral_str[-5:]
print(coral_dubios)

# 8.
rock_index = coral_str.index('rock')
print(f'Indexul de start al cuvantului "rock" este {rock_index}.')
print(coral_str[:rock_index])

# Bonus
dice_roll = random.randrange(1,7)  # zarul are 6 fete
user_guess = int(input('Ghici ce fata a zarului cade..'))
if user_guess < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {user_guess} dar a fost {dice_roll}.')
elif user_guess > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {user_guess} dar a fost {dice_roll}.')
elif user_guess == dice_roll:
    print(f'Ai ghicit. Felicitări! Ai ales {user_guess} si zarul a fost {dice_roll}.')
