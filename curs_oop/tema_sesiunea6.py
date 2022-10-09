from math import pi
from datetime import date

class Cerc:
    #constructor
    def __init__(self, raza, culoare):
        # atribute, fields
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Culoarea cercului este {self.culoare}, iar raza lui este {self.raza}.')

    def arie_cerc(self):
        aria_cercului = pi * self.raza**2
        return f'Aria cercului este {aria_cercului}.'

    def diametru_cerc(self):
        diametru = 2 * self.raza
        return diametru

    def circumferinta_cerc(self):
        circumferinta = 2 * pi * self.raza
        return circumferinta


class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Dreptunghiul are lungimea de {self.lungime} cm, latimea de {self.latime} cm si culoarea {self.culoare}.')

    def arie_dreptunghi(self):
        return self.lungime * self.latime

    def perim_dreptunghi(self):
        return 2 * self.lungime + 2 * self.latime

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare



class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def nume_complet(self):
        return self.nume + ' ' + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        anual = self.salariu * 12
        return anual

    def marire_salariu(self, procent):
        salariu_nou = self.salariu * ((100 + procent)/100)
        return f'Pentru {self.nume_complet()}, salariu lunar dupa marirea cu {procent} % va fi de {salariu_nou}.'

    def descrie(self):
        return f'{self.nume_complet()} are salariul lunar de {self.salariu_lunar()} euro si salariul anual de ' \
               f'{self.salariu_anual()} euro.'



class Cont:
    def __init__(self, IBAN, titular_cont, sold):
        self.IBAN = IBAN
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        return f'{self.titular_cont} are in contul {self.IBAN} suma de {self.sold} lei.'

    def debitare_cont(self, suma):
        self.sold += suma
        print(f'Ati alimentat cu {suma} lei.')
        print(f'Acum aveti in cont {self.sold} lei.')

    def creditare_sold(self, suma):
        if suma <= self.sold:
            self.sold -= suma
            print(f'Ati cheltuit {suma} lei')
            print(f'V-au mai ramas {self.sold} lei.')
        else:
            print('Nu aveti suficienti bani in cont!')


class Factura:
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc
        self.serie = 'MTP'

    def afiseaza_seria(self):
        return self.serie

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pret(self, pret):
        self.pret_buc = pret

    def schimba_nume_prod(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        total = self.pret_buc * self.cantitate
        print(f'Factura seria {self.serie}, numar {self.numar}.')
        print(f'Data curenta: {date.today()}')
        print('Produs          | Cantitate       |  Pret/bucata    | TOTAL           ')
        print('-----------------------------------------------------------')
        str_prod = self.nume_produs
        while len(str_prod) < 15:
            str_prod += ' '
        str_c = str(self.cantitate)
        while len(str_c) < 15:
            str_c += ' '
        str_pr = str(self.pret_buc)
        while len(str_pr) < 15:
            str_pr += ' '
        str_t = str(total)
        while len(str_t) < 15:
            str_t += ' '
        print(f'{str_prod} | {str_c} | {str_pr} | {str_t}')



class Masina:
    def __init__(self, model, viteza_maxima):
        self.marca = 'Audi'
        self.model = model
        self.viteza_maxima = viteza_maxima
        self.viteza_actuala = 0
        self.culoare = 'gri'
        self.culori_disponibile = {'negru', 'albastru', 'rosu', 'argintiu', 'alb', 'turcoaz'}
        self.inmatriculata = False

    def descrie(self):
        print(f'Marca {self.marca}, model {self.model}')
        print(f'Poate ajunge de la {self.viteza_actuala} la {self.viteza_maxima} km/h.')
        print(f'Are culoarea initiala {self.culoare}.')
        print(f'Inmatriculata: {self.inmatriculata}')

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoare_noua):
        if culoare_noua in self.culori_disponibile:
            self.culoare = culoare_noua
        else:
            raise AttributeError('Culoare indisponibila!')

    def accelereaza(self, viteza):
        if viteza < self.viteza_actuala:
            raise ValueError('Viteza nu poate fi mai mica decat viteza de stationare!')
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
            print(f'Eaasy boy! Poti ajunge numai pana la {self.viteza_maxima} km/h')
        else:
            self.viteza_actuala = viteza

    def franeaza(self):
        self.viteza_actuala = 0




class ToDoList:
    def __init__(self):
        self.todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere
        return self.todo

    def finalizeaza_task(self, nume):
        self.todo.pop(nume)
        return self.todo

    def afiseaza_todo_list(self):
        return self.todo.keys()

    def afiseaza_detalii_suplimentare(self, nume_task):
        in_list = True
        if nume_task not in self.todo.keys():
            raspuns = input('Doriti sa adaugati task-ul in ToDo List? ')
            if raspuns == 'da':
                self.todo[nume_task] = input('Introdu detaliile pentru acest task..')
                return self.todo
            else:
                print('Bine, la revedere!')



if __name__ == '__main__':

    cerc1 = Cerc(5, 'albastru')
    cerc2 = Cerc(7, 'rosu')

    cerc1.descrie_cerc()
    cerc2.descrie_cerc()
    print(cerc1.arie_cerc())
    print(cerc2.arie_cerc())
    print(f'Cercul 1 are diametrul de {cerc1.diametru_cerc()} si circumferinta de {cerc1.circumferinta_cerc()}.')
    print(f'Cercul 2 are diametrul de {cerc2.diametru_cerc()} si circumferinta de {cerc2.circumferinta_cerc()}.')


    print('-------------------------------')

    D1 = Dreptunghi(6, 4, 'verde')
    D2 = Dreptunghi(8, 5, 'galben')
    D1.descrie()
    D2.descrie()
    print(f'Aria dreptunghiului 1 este: {D1.arie_dreptunghi()} cm2.')
    print(f'Aria dreptunghiului 2 este: {D2.arie_dreptunghi()} cm2.')
    print(f'Perimetrul dreptunghiului 1 este: {D1.perim_dreptunghi()} cm.')
    print(f'Perimetrul dreptunghiului 2 este: {D2.perim_dreptunghi()} cm.')
    print('Vom schimba culorile dreptunghiurilor.')
    D1.culoare = 'rosu'
    D2.culoare = 'portocaliu'
    D1.descrie()
    D2.descrie()

    print('----------------------------------')

    angajat1 = Angajat('Manta', 'Mirela', 3300)
    angajat2 = Angajat('Oprea', 'Tiberiu', 4500)

    print(angajat1.descrie())
    print(angajat2.descrie())
    print('Are loc o marire de salariu.')
    print(angajat1.marire_salariu(20))
    print(angajat2.marire_salariu(15))

    print('----------------------------------')

    cont1 = Cont('RO524623635MR', 'Manta Mirela', 15000)
    cont2 = Cont('R014566TI2022', 'Oprea Tiberiu', 26300)
    print(cont1.afisare_sold())
    cont1.debitare_cont(2500)
    cont1.creditare_sold(10000)
    print(cont2.afisare_sold())
    cont2.debitare_cont(3000)
    cont2.creditare_sold(15000)

    print('----------------------------------')
    fact1 = Factura(2345, 'Frigider', 20, 1200)
    fact2 = Factura(2346, 'Aspirator', 30, 750)


    fact1.genereaza_factura()
    print('\n')
    fact2.genereaza_factura()
    fact1.schimba_nume_prod('Televizor')
    fact1.schimba_pret(2500)
    fact1.genereaza_factura()
    fact2.schimba_cantitatea(35)
    fact2.schimba_nume_prod('Toaster')
    fact2.genereaza_factura()



    print('-----------------------------------------')
    masina1 = Masina('A8', 250)
    masina2 = Masina('Q7', 240)
    masina1.descrie()
    print('Inmatriculam masina...')
    masina1.inmatriculare()
    masina1.descrie()
    # masina1.accelereaza(-100)
    masina1.accelereaza(270)
    print('Las-o mai usor!')
    # masina1.vopseste('roz deschis')
    print('Vopsim masina..daca au ce culoare vreau eu..')
    masina1.vopseste('negru')
    print(f'Pentru Audi {masina1.model} noua culoare este {masina1.culoare}.')
    masina2.vopseste('turcoaz')
    masina2.accelereaza(180)
    print(f'Conduc masina Audi {masina2.model} cu {masina2.viteza_actuala} km/h.')
    print(f'In fata masinii apare un catel..franez..')
    masina2.franeaza()
    print(f'Acum masina {masina2.model} are viteza {masina2.viteza_actuala}.')
    print(f'Masina Audi {masina2.model} are acum culoarea {masina2.culoare}.')
    print(f'Pentru masina {masina1.model} statusul de inmatriculare este: {masina1.inmatriculata}')
    print('------------------------------------------------------')


    todo1 = ToDoList()
    print(todo1.adauga_task('Cumparaturi', 'Ia paine, iaurt, banane..'))
    print(todo1.adauga_task('Programari', 'La pensat: luni, 15:30'))
    print(todo1.finalizeaza_task('Cumparaturi'))
    print(todo1.adauga_task('Curatenie', 'Fa curat in bucatarie, baie si hol!'))
    print(todo1.afiseaza_todo_list())
    print(todo1.afiseaza_detalii_suplimentare('Plecari'))



