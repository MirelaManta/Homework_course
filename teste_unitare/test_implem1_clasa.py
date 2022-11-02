import unittest
from implem1_clasa import Dreptunghi


class TesteDreptunghi(unittest.TestCase):
    def setUp(self):
        self.lungime1 = 7
        self.latime1 = 5
        self.culoare1 = 'roz'
        self.lungime2 = 8
        self.latime2 = 6
        self.culoare2 = 'verde'
        self.d1 = Dreptunghi(self.lungime1, self.latime1, self.culoare1)
        self.d2 = Dreptunghi(self.lungime2, self.latime2, self.culoare2)

    def test_descriere(self):
        self.assertEqual(self.d1.descrie(),
                         f'Dreptunghiul are lungimea de {self.lungime1} cm, latimea de {self.latime1} cm si culoarea {self.culoare1}.')

        self.assertEqual(self.d2.descrie(), f'Dreptunghiul are lungimea de {self.lungime2} cm, latimea de {self.latime2} cm si culoarea {self.culoare2}.')


    def test_arie(self):
        self.assertTrue(self.d1.arie_dreptunghi() == 35)
        self.assertNotEqual(self.d1.arie_dreptunghi(), 50)
        self.assertFalse(self.d2.arie_dreptunghi() != 48)

    def test_perimetru(self):
        self.assertEqual(self.d1.perim_dreptunghi(), 24)
        self.assertTrue(self.d2.perim_dreptunghi() == 28)

    def test_culoare(self):
        self.d1.schimba_culoarea('portocaliu')
        self.d2.schimba_culoarea('negru')
        self.assertTrue(self.d1.culoare == 'portocaliu')
        self.assertEqual(self.d2.culoare, 'negru', 'expected color: negru')


if __name__ == '__main__':
    unittest.main()
