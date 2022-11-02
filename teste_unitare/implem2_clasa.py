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
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.salariu = round(self.salariu * ((100 + procent)/100), 1)
        print (f'Pentru {self.nume_complet()}, salariu lunar dupa marirea cu {procent} % va fi de {self.salariu}.')

    def descrie(self):
        return f'{self.nume_complet()} are salariul lunar de {self.salariu_lunar()} euro si salariul anual de ' \
               f'{self.salariu_anual()} euro.'


if __name__ == '__main__':
    angajat1 = Angajat('Manta', 'Mirela', 3300)
    angajat2 = Angajat('Oprea', 'Tiberiu', 4500)

    print(angajat1.descrie())
    print(angajat2.descrie())
    print('Are loc o marire de salariu.')
    print(angajat1.marire_salariu(20))
    print(angajat2.marire_salariu(15))
