import random

# 1.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for ind in range(len(masini)):
    print(f'Masina mea preferata este {masini[ind]}.')

for masina in masini:
    print(f'Masina mea preferata este {masina}')

i=0
while i < len(masini):
    print(f'Masina mea preferata este {masini[i]}')
    i +=1

#2.
for i in range(len(masini)):
    for j in range(1, len(masini)-1):
        masini[j] = masini[j].upper()
print(masini)

# 3.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == "Mercedes":
        print('Am gasit masina dorita de dvs.')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam.')

# 4.
for masina in masini:
    if masina == "Trabant" or masina =='Lastun':
        continue
    print(f'S-ar putea sa va placa masina {masina}.')

# 5.
masini_vechi = []
for i in range(len(masini)):
    if masini[i] == 'Trabant' or masini[i] == 'Lastun':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

# 6.
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
# 6.
print('Masinile pe care le puteti cumpara si pretul lor, sunt: ')
for model in pret_masini:    # model = the key
    if pret_masini[model] < 15000:
        print(model, '->', pret_masini[model])

print('Masinile pe care le puteti cumpara sunt: ')
for masina_pret in pret_masini.items():
    if masina_pret[1] < 15000:
        print(masina_pret)

#7.
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
count = 0
for i in range(len(numere)):
    if numere[i] == 3:
        print('Am gasit un 3!')
        count +=1
print(f'Cifra 3 apare in total de {count} ori.')

#8.
suma = 0
for i in range(len(numere)):
    suma = suma + i
print(f'Suma numerelor din lista este: {suma}.')

#9.
nr_max = 0
for i in range(len(numere)):
    if numere[i] > nr_max:
        nr_max = numere[i]
        print(f'Nr maxim curent este: {numere[i]}')
    else:
        print('Am gasit deja nr maxim!')
print(f'Cel mai mare nr din lista este: {nr_max}')

# 10.
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(len(numere)):
    if numere[i] > 0 or numere[i] < 0:
        numere[i] = - numere[i]
print(numere)

# 11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)

    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)

print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)

# 12.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(alte_numere)):
    for j in range(i+1, len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            temp = alte_numere[i]
            alte_numere[i] = alte_numere[j]
            alte_numere[j] = temp

print(alte_numere)

# 13.
numar_secret = random.randrange(1,30)
n_am_ghicit = True

while n_am_ghicit:
    numar_ghicit= int(input('Alege un nr '))
    if numar_ghicit < numar_secret:
        print('Nr secret e mai mare.')
    elif numar_ghicit > numar_secret:
        print('Nr secret e mai mic.')
    else:
        print('Felicitari! Ai ghicit!')
        n_am_ghicit = False

# 14.
chosen_num = int(input('Alege un nr de la tastatura '))

for i in range(chosen_num + 1):
    for j in range(i):
        print(i, end= '')
    print('\n')

#. 15.
tastatura_telefon = [      # i = 0, 1, 2, 3
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f' Cifra curenta este {tastatura_telefon[i][j]}.')
