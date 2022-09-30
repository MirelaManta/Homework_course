# SESIUNEA 1
# 1.
# my_string = input('Introdu un string...')
# first_char = my_string[0]
# print(first_char)
# str_aslist = list(my_string)
# for i in range(1, len(str_aslist)-1):
#     if str_aslist[i].lower() == first_char.lower():
#         str_aslist[i] = first_char.upper()
# my_string = ''.join(str_aslist)
# print(my_string)
# print(my_string)

# my_str = input('Introdu un string...')
# first_char = my_str[0]
# print(my_str[0] + my_str[1: len(my_str) - 1].replace(first_char, first_char.upper()) + my_str[-1] )
#
#
# #2.
# user = input('user = ')
# password = input('password = ')
# dimens_pass = len(password)
# pass_to_asterisk = '*'
# for i in range(1, len(password)):
#     pass_to_asterisk += '*'
# print(f'Parola pentru {user} este {pass_to_asterisk} si are {dimens_pass} caractere.')

# user = input('user = ')
# password = input('password = ')
# dimens_pass = len(password)
# pass_to_asterisk = '*' * dimens_pass
# print(f'Parola pentru user {user} este {pass_to_asterisk} si are {dimens_pass} caractere.')


# SESIUNEA 2.
# # 1.
# string_test = input('Introdu un string..')
# assert string_test[0].casefold() == string_test[-1].casefold()  # ca un lower
#
# # 2.
# another_str = '0123456789'
# print(f'Numerele pare sunt {another_str[0::2]}.')
# print(f'Numerele impare sunt {another_str[1::2]}.')


# SESIUNEA 3/ 1.
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)  #nu va schimba nimic pentru ca nu pot exista duplicate
# 2.
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămână.')
else:
    print('Weekend nu este un subset al zilelor din săptămână.')

print(zile_sapt.difference(weekend))
print(zile_sapt.intersection(weekend))

