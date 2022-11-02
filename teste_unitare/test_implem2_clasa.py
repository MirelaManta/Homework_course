import unittest
from implem2_clasa import Angajat

class TestAngajat(unittest.TestCase):

    def setUp(self):
        self.nume1 = 'Manta'
        self.prenume1 = 'Mirela'
        self.salariu1 = 3300
        self.nume2 = 'Tiberiu'
        self.prenume2 = 'Oprea'
        self.salariu2 = 4500
        self.angajat1 = Angajat(self.nume1, self.prenume1, self.salariu1)
        self.angajat2 = Angajat(self.nume2, self.prenume2, self.salariu2)

    def test_nume_complet(self):
        self.assertEqual(self.angajat1.nume_complet(), self.angajat1.nume + ' ' + self.angajat1.prenume)
        self.assertTrue(self.angajat2.nume_complet() == self.angajat2.nume + ' ' + self.angajat2.prenume)

    def test_sal_lunar(self):
        self.assertEqual(self.angajat1.salariu_lunar(), self.angajat1.salariu)
        self.assertTrue(self.angajat2.salariu_lunar() == self.angajat2.salariu_lunar())

    def test_sal_anual(self):
        self.assertEqual(self.angajat1.salariu_anual(), self.angajat1.salariu * 12)
        self.assertTrue(self.angajat2.salariu_anual() == self.angajat2.salariu * 12)

    def test_marire_sal(self):
        salariu_angajat1 = self.angajat1.salariu
        salariu_angajat2 = self.angajat2.salariu
        self.angajat1.marire_salariu(12)
        self.angajat2.marire_salariu(20)

        self.assertEqual(self.angajat1.salariu, round(salariu_angajat1 * ((100 + 12)/100), 1))
        self.assertEqual(self.angajat2.salariu, round(salariu_angajat2 * ((100 + 20)/100), 1))


    def test_descriere(self):
        self.assertEqual(self.angajat1.descrie(), f'{self.angajat1.nume_complet()} are salariul lunar de {self.angajat1.salariu_lunar()} euro si salariul anual de ' \
               f'{self.angajat1.salariu_anual()} euro.')
        self.assertTrue(self.angajat2.descrie() == f'{self.angajat2.nume_complet()} are salariul lunar de {self.angajat2.salariu_lunar()} euro si salariul anual de ' \
               f'{self.angajat2.salariu_anual()} euro.')
