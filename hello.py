
from itertools import combinations
print('Hello World!')
# consola de output ---> Run
# consola de experimentare---> Python Console

'''
comentariu multiple lines
cand facem mai multe mentiuni
''' ''' bagat in print il poate interpreta ca pe un string pe mai multe linii
'''

# This is a exercise to determine all posible combinations of two numbers, from a given list

def combos_oftwo(my_list):
    combos = list(combinations(my_list, 2))
    print(f'Toate combinatiile posibile de 2 nr sunt: {combos}')
    sum_oftwo = 0
    for combo in combos:
        sum_oftwo = sum(combo)
        print(f'O suma este {sum_oftwo}')
#
#
my_list = [2, 7, 5, 9, 3, 2, 8]
combos_oftwo(my_list)
print('Acestea sunt toate sumele posibile. Cred.')
#
