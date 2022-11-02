class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare
    def descrie(self):
        return f'Dreptunghiul are lungimea de {self.lungime} cm, latimea de {self.latime} cm si culoarea {self.culoare}.'

    def arie_dreptunghi(self):
        return self.lungime * self.latime

    def perim_dreptunghi(self):
        return 2 * self.lungime + 2 * self.latime

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


if __name__ == '__main__':
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
