# Luokan luominen
class Auto:
    def __init__ (self, merkki, malli, rekisterinumero):
        self.merkki = merkki
        self.malli = malli
        self.rekisterinumero = rekisterinumero

    def __str__ (self) -> str:
        # Merkkijonoja voi yhdistää plus-merkillä
        teksti =   "Auto: " + self.merkki + " " + self.malli + " (" + self.rekisterinumero + ") "

        # Sama f-stringillä
        teksti = f"Auto: {self.merkki} {self.malli} ({self.rekisterinumero})"
        
        return teksti


auto1 = Auto("VW", "Kupla", "AKU-313")
auto2 = Auto("Opel", "Kadet", "ABC-123")
auto3 = Auto("Volvo", "240", "CBA-321")

print(auto1)
print(auto2)
print(auto3)
