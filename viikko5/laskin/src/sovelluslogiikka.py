class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = []

    def miinus(self, arvo):
        self.edellinen.append(self.tulos)
        self.tulos -= arvo

    def plus(self, arvo):
        self.edellinen.append(self.tulos)
        self.tulos += arvo

    def nollaa(self):
        self.edellinen.append(self.tulos)
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.edellinen.append(self.tulos)
        self.tulos = arvo

    def kumoa(self):
        self.tulos = self.edellinen.pop()

class Summa:
    def __init__(self, sovellus: Sovelluslogiikka, lue_syote):
        self.sovellus = sovellus
        self.lue_syote = lue_syote
        self.syote = 0

    def suorita(self):
        self.syote = int(self.lue_syote())
        self.sovellus.plus(self.syote)

    def kumoa(self):
        self.sovellus.miinus(self.syote)
        self.syote = 0

class Erotus:
    def __init__(self, sovellus: Sovelluslogiikka, lue_syote):
        self.sovellus = sovellus
        self.lue_syote = lue_syote
        self.syote = 0

    def suorita(self):
        self.syote = int(self.lue_syote())
        self.sovellus.miinus(self.syote)

    def kumoa(self):
        self.sovellus.plus(self.syote)
        self.syote = 0

class Nollaus:
    def __init__(self, sovellus: Sovelluslogiikka, lue_syote):
        self.sovellus = sovellus
        self.lue_syote = lue_syote
        self.syote = 0

    def suorita(self):
        self.syote = self.lue_syote()
        self.sovellus.nollaa()

    def kumoa(self):
        self.sovellus.aseta_arvo(self.edellinen)
        self.edellinen = 0

class Kumoa:
    def __init__(self, sovellus: Sovelluslogiikka, lue_syote):
        self.sovellus = sovellus
        self.lue_syote = lue_syote

    def suorita(self):
        self.sovellus.kumoa()
