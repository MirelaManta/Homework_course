# 1.
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
lista_inversata = note_muzicale[::-1]
print(lista_inversata)
lista_inversata.reverse()
print('Dupa inversarea inversarii lista este: ', lista_inversata)

# 2.
print('"do" apare de ', note_muzicale.count('do'), ' ori."')

# 3.
list1 = [3, 1 , 0, 2]
list2 = [6, 5, 4]
lst_merged = list1 + list2
print(lst_merged)

list1.extend(list2)
print(list1)

# 4.
lst_sorted = sorted(list1)
print(lst_sorted)

# 5.
if len(lst_merged) == 0:           # sau empty = [] si comparare cu lista mea
    print('Lista este goala.')
else:
    print('Lista nu este goala.')

# 6/7.
lst_merged.clear()
if len(lst_merged) == 0:
    print('Lista este goala.')
else:
    print('Lista nu este goala.')

# 8.
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())
# 9.
print('Ana a luat nota ',dict1.get('Ana'),'.', sep='')
print('Gigel a luat nota ',dict1.get('Gigel'),'.', sep='' )
print('Dorel a luat nota ', dict1.get('Dorel'),'.', sep='')

# 10.
dict1['Dorel'] = 6
print('Dupa marire, nota lui Dorel este', dict1.get('Dorel'))

# 11.
dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1.keys())

# OPTIONALE
jucatori = ['Messi', 'Ronaldo', 'Neymar', 'Maradona', 'Hagi']
schimbari_efectuate = 0
schimbari_max = 3

jucator_de_schimbat = input('Spune ce jucator schimbam ')

if jucator_de_schimbat in jucatori:
    schimbari_efectuate += 1
    jucatori.remove(jucator_de_schimbat)
    jucator_de_adaugat = input('Spune ce jucator adaugam ')
    jucatori.append(jucator_de_adaugat)
    print(f'A iesit {jucator_de_schimbat}, a intrat {jucator_de_adaugat} , mai ai {schimbari_max - schimbari_efectuate} schimbari.')
else:
    print(f'Nu se poate efectua schimbarea deoarece jucatorul {jucator_de_schimbat} nu e in teren.')
    print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbari.')

print(jucatori)
