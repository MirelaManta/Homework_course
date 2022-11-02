import unittest
from forma_geom import Patrat, Dreptunghi, Cerc


class TestePatrat(unittest.TestCase):
    def setUp(self):
        self.latura1 = 6
        self.latura2 = 8
        self.patrat1 = Patrat(self.latura1)
        self.patrat2 = Patrat(self.latura2)

    def test_arie_P(self):
        arie_patrat1 = self.patrat1.latura * self.patrat1.latura
        arie_patrat2 = self.patrat2.latura * self.patrat2.latura
        self.assertEqual(self.patrat1.arie(), arie_patrat1)
        self.assertEqual(self.patrat2.arie(), arie_patrat2)

    def test_perimetru_P(self):
        perim1 = self.patrat1.latura * 4
        perim2 = self.patrat2.latura * 4
        self.assertTrue(self.patrat1.perimetru() == perim1)
        self.assertTrue(self.patrat2.perimetru() == perim2)


class TesteDreptunghi(unittest.TestCase):
    def setUp(self):
        self.lungime = 9
        self.latime = 5
        self.dreptunghi = Dreptunghi(self.lungime, self.latime)

    def test_arie_D(self):
        arie = self.dreptunghi.lungime * self.dreptunghi.latime
        self.assertEqual(self.dreptunghi.arie(), arie)

    def test_perimetru_D(self):
        perimetru_dr = 2 * self.dreptunghi.lungime + 2 * self.dreptunghi.latime
        self.assertEqual(self.dreptunghi.perimetru(), perimetru_dr)


class TesteCerc(unittest.TestCase):
    def setUp(self):
        self.raza1 = 6
        self.raza2 = 3
        self.pi = 3.14
        self.cerc1 = Cerc(self.raza1)
        self.cerc2 = Cerc(self.raza2)


    def test_arie_C(self):
        arie_cerc1 = self.pi * pow(self.cerc1.raza, 2)
        arie_cerc2 = self.pi * pow(self.cerc2.raza, 2)
        self.assertEqual(self.cerc1.arie(), arie_cerc1)
        self.assertTrue(self.cerc2.arie() == arie_cerc2)

    def test_perimetru_C(self):
        perim_cerc1 = 2 * self.pi * self.cerc1.raza
        perim_cerc2 = 2 * self.pi * self.cerc2.raza
        self.assertEqual(self.cerc1.perimetru(), perim_cerc1)
        self.assertTrue(self.cerc2.perimetru() == perim_cerc2)

if __name__ == '__main__':
    unittest.main
