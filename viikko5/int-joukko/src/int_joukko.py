KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        else:
            self.kapasiteetti = kapasiteetti
        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = []

    def kuuluu(self, n):
        return n in self.lukujono

    def mahtavuus(self):
        return len(self.lukujono)

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        if self.mahtavuus() >= self.kapasiteetti:
            self.kapasiteetti += self.kasvatuskoko
        self.lukujono.append(n)
        return True

    def poista(self, n):
        if self.kuuluu(n):
            self.lukujono.remove(n)
            return True
        return False

    def to_int_list(self):
        return self.lukujono

    @staticmethod
    def yhdiste(a, b):
        intjoukko = IntJoukko()
        for i in a.to_int_list():
            intjoukko.lisaa(i)
        for i in b.to_int_list():
            intjoukko.lisaa(i)
        return intjoukko

    @staticmethod
    def leikkaus(a, b):
        intjoukko = IntJoukko()
        for i in a.to_int_list():
            if b.kuuluu(i):
                intjoukko.lisaa(i)
        return intjoukko

    @staticmethod
    def erotus(a, b):
        intjoukko = IntJoukko()
        for i in a.to_int_list():
            if not b.kuuluu(i):
                intjoukko.lisaa(i)
        return intjoukko

    def __str__(self):
        if self.mahtavuus() == 0:
            return "{}"
        elif self.mahtavuus() == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in self.lukujono[0:-1]:
                tuotos = tuotos + str(i)
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[-1])
            tuotos = tuotos + "}"
            return tuotos