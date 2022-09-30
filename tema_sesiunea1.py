# o variabilă este o cutiuță în care punem valori
cat_name = 'Dusty'
varsta = 12
salariu = 10000.50
cloudy = True
print(type(cat_name))
print(type(varsta))
print(type(salariu))
print(type(cloudy))

salariu = round(salariu)
print(f'Acum salariul este de tipul {type(salariu)}')

print(f'Numele pisicii mele este {cat_name}.')
print(f'Sora mea are varsta de {varsta} ani.')
print(f'Mi-ar placea sa am un salariu de minim {salariu} lei.')
print('Afara {este_nor} este innorat.'.format(este_nor='este' if cloudy else 'Nu este.'))
# 6.
nume = input('Introdu numele tau ')
prenume = input('Introdu prenumele tau ')
print(f'Numele complet are {len(nume + prenume)} caractere.')
#
# # 7.
Lungimea = int(input('Latimea = '))
Latimea = int(input('Latimea = '))
Aria = Lungimea * Latimea
print(f'Aria dreptunghiului este {Aria}.')

# 8/9 ????
given_str = 'Coral is either the stupidest animal or the smartest rock'
print(given_str.split().count('the')) # Doar 'the' ca si cuvant solo
#sau
str_asList = given_str.split()
contor = 0
for i in range(0, len(str_asList)):
    if str_asList[i] == 'the':
        contor += 1
print(f'"The" apare de {contor} ori in acel string.')
print(given_str.count('the'))   #include si 'the' din 'either'


# 10.
given_str = 'Coral is either the stupidest animal or the smartest rock'
# given_str = '1234'---> de test
assert given_str.isdigit() # ---> AssertionError

# OPȚIONALE 1.
str_imp = input('Introdu aici stringul...')
middle_char = len(str_imp)//2  # aflu ce index are caracterul din mijloc
print(str_imp[middle_char])

# 2.
rhyme = input('Baga un string din doua cuvinte')
cuv1 = rhyme.split(' ')[0]
cuv2 = rhyme.split(' ')[1]
print(cuv1 +'\n'+ cuv2)  #printeaza cuvintele pe linii diferite

print(input('Baga un string din doua cuvinte ').split())
#nu stiu sa le si salvez si sa si printez pe o singura linie

