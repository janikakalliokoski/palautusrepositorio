from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._maara = 0
        self._hinta = 0
        self._ostoskori = []
        self._tuotteet_korissa = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return self._maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2

    def hinta(self):
        return self._hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if self._tuotteet_korissa.get(lisattava.nimi()) is None:
            self._tuotteet_korissa[lisattava.nimi()] = Ostos(lisattava)
            self._ostoskori.append(self._tuotteet_korissa[lisattava.nimi()])
        else:
            self._tuotteet_korissa[lisattava.nimi()].muuta_lukumaaraa(1)
        self._maara += 1
        self._hinta += lisattava.hinta()


    def poista_tuote(self, poistettava: Tuote):
        self._maara -= 1
        self._tuotteet_korissa[poistettava.nimi()].muuta_lukumaaraa(-1)
        if self._tuotteet_korissa[poistettava.nimi()].lukumaara() == 0:
            self._ostoskori.remove(self._tuotteet_korissa[poistettava.nimi()])
            del self._tuotteet_korissa[poistettava.nimi()]

    def tyhjenna(self):
        self._tuotteet_korissa = {}
        self._ostoskori = []
        self._maara = 0
        self._hinta = 0

    def ostokset(self):
        return self._ostoskori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
