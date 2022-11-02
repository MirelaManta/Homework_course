from abc import ABC, abstractmethod


class FormaGeom(ABC):

    @abstractmethod
    def arie(self):
        pass

    @abstractmethod
    def perimetru(self):
        pass

class Patrat(FormaGeom):
    def __init__(self, latura):
        self.latura = latura

    def arie(self):
        return self.latura * self.latura

    def perimetru(self):
        return self.latura * 4


class Dreptunghi(FormaGeom):
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def arie(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2 * self.lungime + 2 * self.latime


class Cerc(FormaGeom):
    def __init__(self, raza):
        self.raza = raza
        self.pi = 3.14

    def arie(self):
        return self.pi * pow(self.raza, 2)

    def perimetru(self):
        return 2 * self.pi * self.raza
