# Parit pikanäpppäimet
# VSCoden komentopaletti     Control+Shift+P
# Rivien kommentointi        Ctrl + ' (Windows)
#                            Ctrl + Shift + 7 (Linux)
# Ohjelma pysäyttäminen      Ctrl + C

# Tee koodi, joka kysyy viisi nimeä ja laittaa ne listaan nimeltä "nimet"

nimet = []

# Vaihtoehto 1
nimi = input("Anna nimi: ")
nimet.append(nimi)
nimi = input("Anna nimi: ")
nimet.append(nimi)
nimi = input("Anna nimi: ")
nimet.append(nimi)
nimi = input("Anna nimi: ")
nimet.append(nimi)
nimi = input("Anna nimi: ")
nimet.append(nimi)

 # Vaihtoehto 2
for i in range(1, 6):
     nimi = input("Anna nimi: " + str(i) + ": ")
     nimet.append(nimi)
 
 # Vaihtoehto 3
while True:
     nimi = input("Anna nimi: ")
     nimet.append(nimi)
     if len(nimet) >= 5:
         break

 # Vaihtoehto 4
while len(nimet) < 5:
    nimi = input("Anna nimi: ")
    nimet.append(nimi)


# Viimeisenä tulosta nimet
print(nimet)
