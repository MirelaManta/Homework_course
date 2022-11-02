from math import pi

# 1.
def addition(x, y):
    return x+y

print(addition(8, 12))
print(addition(7, -17))


# 2.
def par_impar(a):
    if a % 2 == 0:
        return True
    else:
        return False

print(par_impar(7))
print(par_impar(12))


# 3.
def name_length(nume, prenume, nume_mijlociu):
    return len(nume + prenume + nume_mijlociu)

print(name_length('Manta', 'Mirela', 'Raluca'))
print(name_length('Oprea', 'Tiberiu', 'Alexandru'))


# 4.
def arie_dreptunghi(L, l):
    print('Aria dreptunghiului este: ')
    return L*l

print(arie_dreptunghi(7, 5))
print(arie_dreptunghi(10, 4))


# 5.
def arie_cerc(raza):
    aria = pi * raza**2
    return aria

print(arie_cerc(5))
print(arie_cerc(7))

# 6.


def find_char(x, given_str):
    if x.lower() in given_str:
        return True
    else:
        return False

print(find_char('.', 'Nu stiu ce string sa scriu aici.'))
print(find_char('U', 'Nu stiu ce string sa scriu aici.'))
print(find_char('M', 'Nu stiu ce string sa scriu aici.'))


# 7.
def lower_upper_count(str):
    c1 = 0
    c2 = 0 # tine de cate ori un caracter e lowercase
    for i in range(len(str)):
        if str[i] == ' ':
            continue
        if str[i].isupper():
            c1 +=1
        else:
            c2 +=1
    print(f'Nr de caractere upper case este {c1}.')
    print(f'Nr de caractere lower case este {c2}.')

print(len('CERUL are niste culori splendide IN ACEASTA seara.'.replace(' ', '')))
lower_upper_count('CERUL are niste culori splendide IN ACEASTA seara.')
lower_upper_count('CERUL ARE niste culori splendide in aceasta seara.')


# 8.
def positive_ones(lst):
    lst_pos = []
    for i in lst:
        if i > 0:
            lst_pos.append(i)
    return lst_pos

print(positive_ones([1, 5, -8, 12, -6]))
print(positive_ones([-9, 7, 5, -3, 1]))


# 9.
def compare(x, y):
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}.')
    elif x < y:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}.')
    else:
        print('Numerele sunt egale.')

compare(5, 9)
compare(7, -2)
compare(8, 8)


# 10.
def in_set(a, my_set):
    if a not in my_set:
        my_set.add(a)
        print('Am adaugat numarul nou in set.')
        return True
    else:
        print('Nu am adaugat numarul nou in set. Acesta exista deja.')
        return False

print(in_set(3, {2, 4, 7, 3, 9}))
print(in_set(6, {1, 2, 4, 7, 3}))


# varianta 2
def in_set2(b, my_set):
    gasit_b = False
    for elem in my_set:
        if elem == b:
            gasit_b = True

    if not gasit_b:
        my_set.add(b)
        print('Am adaugat numarul nou in set.')
        return True
    else:
        print('Nu am adaugat numarul nou in set. Acesta exista deja.')
        return False

print(in_set2(5, {2, 4, 7, 3, 9}))
print(in_set2(1, {1, 2, 4, 7, 3}))


# OPTIONALE
# 1. Functie care primeste o luna din an si returneaza cate zile are acea luna
# month = input('Doresc sa stiu nr de zile pt luna ...')
# def days_in_months(month):
#     days_months = {"Ianuarie": 31, "Februarie": 28, "Martie": 31, "Aprilie": 30,
#                    "Mai": 31, "Iunie": 30, "Iulie": 31, "August": 31, "Septembrie": 30,
#                    "Octombrie": 31, "Noiembrie": 30, "Decembrie": 31}
#
#     return days_months.get(month.capitalize())
# print(days_in_months(month))


# 2.
# Functie calculator care sa returneze 4 valori
def calculator(x, y):
    a, b, c, d = x+y, x-y, x*y, x/y
    print("Suma: ", a)
    print("Diferenta: ", b)
    print("Inmultirea: ", c)
    print("Impartirea: ", d)

calculator(5, 6)
calculator(-6, 12)


# 13.
def count_digit(lst):
    digitcount_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for digit in lst:
        if digit in digitcount_dict.keys():
           digitcount_dict[digit] += 1
        else:
            digitcount_dict[digit] = 1

    return digitcount_dict

print(count_digit([1, 1, 0, 5, 6, 8, 5]))
print(count_digit([2, 4, 2, 5, 3, 1, 4, 3, 7, 2, 0]))

# 14.


def val_max(a, b, c):
    val_maxima = max(a, b, c)
    print('Valoarea maxima este ')
    return val_maxima


def max_value(a, b, c):
    if a >= b and b >= c:
        max_val = a
    elif b >= c and c >= a:
        max_val = b
    else:
        max_val = c
    print('Max value is: ')
    return max_val


print(val_max(12, 5, 29))
print(val_max(5, 3, 9))

print(max_value(-8, 2, 4))
print(max_value(12, -9, 18))

# 15. Functie care sa primeasca un numar si sa returneze suma tuturor
# numerelor de la 0 la acel numar


def sum0_to_n(n):
    summ = n*(n+1)//2
    print(f'Suma primelor {n} numere naturale este: ')
    return summ

print(sum0_to_n(3))
print(sum0_to_n(12))


# BONUS
#16.Functie care primesete 2 liste de numere (numerele pot fi dublate). Returnati numerele comune


def common_items(list1, list2):
    common = set()
    for num in list1:
        if num in list2:
            common.add(num)
    print('Numerele comune din cele doua liste sunt: ')
    return common


print(common_items([1,1,2,3], [2, 2, 3, 4]))
print(common_items([2, 3, 5, 6, 5], [4, 5, 2, 1, 4]))


# 17.
def discount(price, percent):
    if percent < 100:
        new_price = price - (price * percent)/100
        return f'Noul tau pret este {new_price}.'
    elif percent == 100:
        return 'Felicitari! L-ai luat pe gratis. :))'
    else:
        return f'Reducerea ta de {percent} % este invalida!'


print(discount(100, 15))
print(discount(200, 100))
print(discount(500, 110))


# 18.
import datetime
import pytz


def date_time():
    x = datetime.datetime.now()
    print("Ora noastra curenta este: ")
    return x


def china_time():
    china_time_zone = pytz.timezone('Asia/Shanghai')
    china_time = datetime.datetime.now(china_time_zone)
    print('Ora Chinei este: ')
    return china_time

print(date_time())
print(china_time())
#for tz in pytz.all_timezones:
#    print(tz)

# 19.

from datetime import date


def days_till_birthday(event, birthday):
    today = date.today()
    till_bday = (birthday - today).days
    return f'Pana la {event} mai sunt {till_bday} zile.'

print(days_till_birthday('ziua mea', date(2022, 10, 18)))
print(days_till_birthday('Crăciun', date(2022, 12, 25)))

