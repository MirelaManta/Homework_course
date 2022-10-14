from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    def __init__(self):
        self.pi = 3.14
        
    def descrie(self):
        print('Cel mai probabil am colturi.')
        
    @abstractmethod
    def aria(self):
        raise NotImplementedError


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    # def da_mi_latura(self):
    #     return self.__latura
    #
    # def seteaza_latura(self, lungimea_laturii):
    #     self.__latura = lungimea_laturii
    #
    # def sterge_latura(self):
    #     print('Am sters latura..')
    #     self.__latura = None

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: Latura are lungimea de {self.__latura} cm.')
        return self.__latura

    @latura.setter
    def latura(self, lungime_noua):
        print(f'Setter: Noua lungime a laturii: {lungime_noua} cm.')
        self.__latura = lungime_noua

    @latura.deleter
    def latura(self):
        print('Am sters lungimea laturii')
        self.__latura = None

    def aria(self):
        return f'Aria patratului cu latura de {self.__latura} este {self.__latura ** 2} cm2.'


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        FormaGeometrica.__init__(self)
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Cercul are raza cu lungimea {self.__raza} cm.')
        return self.__raza

    @raza.setter
    def raza(self, lungime_raza):
        print(f'Noua lungime a razei cercului este de: {lungime_raza} cm.')
        self.__raza = lungime_raza

    @raza.deleter
    def raza(self):
        print('Am sters lungimea razei..')
        self.__raza = None

    def aria(self):
        arie_cerc = self.pi * self.raza ** 2
        return f'Aria cercului cu raza de {self.__raza} este {arie_cerc}.'

    def descrie(self):
        print('Eu nu am colturi :(')


if __name__ == '__main__':
    # formageom  = FormaGeometrica()
    # formageom.descrie()
    patrat = Patrat(12)
    patrat.latura
    patrat.latura = 25
    del patrat.latura
    patrat.latura = 8
    print(patrat.aria())
    print('--------------------------')

    cerculet = Cerc(7)
    cerculet.raza
    cerculet.raza = 4
    del cerculet.raza
    cerculet.raza = 3
    print(cerculet.aria())
    cerculet.descrie()

    forme_geom = [patrat, cerculet]
    for forma_geometrice in forme_geom:
        forma_geometrice.descrie()

