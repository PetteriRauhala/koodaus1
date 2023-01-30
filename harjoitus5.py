# Luokan luominen
class Auto:
    def __init__ (self, merkki, malli, rekisterinumero):
        self.merkki = merkki
        self.malli = malli
        self.rekisterinumero = rekisterinumero
        self.vuosi = None

    def __str__ (self) -> str:
        # Muotoillaan Auto-olio stringiksi

        # Muodostetaan ensin "vuosi"-muuttujaan -95  -tyylinen stringi
        
        #  Huom   Terniärioperaattori
        #          A if EHTo else B
        #        Valitsee arvon A jos EHTO on tosi, muuten arvon B

        vuosi = f" -{self.vuosi % 100}" if self.vuosi is not None else ""
        return f"Auto: {self.merkki} {self.malli}{vuosi} ({self.rekisterinumero})"


vw = Auto("VW", "Kupla", "AKU-313")
opel = Auto("Opel", "Kadet", "ABC-123")
volvo = Auto("Volvo", "240", "CBA-321")

# Atribuutteja voi asettaa myös luokan ulkopuolella
vw.vuosi = 1992
opel.vuosi = 1982
volvo.vuosi = 1995

print(vw)
print(opel)
print(volvo)
