# Doelstelling labo 1
# gebruik van print
# gebruik van variabelen: int, string
# gebruik van int
# toekenning van waarden aan variabelen
# multiple assignment
# omzetting van string naar int
# eenvoudige rekenkundige bewerkingen met variabelen
# assignment operations
# print -> afronden op 2 decimalen


# print("Labo Basic Programming, \n\tLabo week 1 \n\t\tKennismaking met \"Python\", \n\t\tWerken met variabelen. \nLabo Basic Programming, \n\tLabo week 2")

# Oef: Maak telkens 2 variabelen (datatype integer) in bepaald formaat aan. print som af
getalHex1 = 0xABD785
getalHex2 = 0xECF5
som = getalHex1 + getalHex2
print("De som van getal {0:X} en getal {1:X} is {2:X}".format(getalHex1, getalHex2, som))
# analoog...
getalBin = 0b101011
getalOctal = 0o45275
getalDec = 12541

# Oef:  Vraag aan de gebruiker de basis en de hoogte van een driehoek op. Bereken nadien de opppervlakte en print deze nadien af.
# b = float(input("Geef de basis va de driehoek op : "))
# h = float(input("Geef de hoogte van de driehoek op : "))
# opp = b*h/2
# print("De oppervlakte bedraagt {0:.2f} ".format(opp))

# Oef: bepaal aantal dagen, uren, minuten, seconden op basis van een opgegeven aantal seconden
# time = int(input("Geef het aantal seconden op: "))
# day = time // (24 * 3600)
# time = time % (24 * 3600)
# hour = time // 3600
# time %= 3600
# minutes = time // 60
# time %= 60
# seconds = time
# print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

# Oef: vraag aan de gebruiker het aantal dagen, uren, minuten en seconden op. Bepaal het totale aantal seconden.
# days = int(input("Geef het aantal dagen op: ")) * 3600 * 24
# hours = int(input("Geef het aantal uren op: ")) * 3600
# minutes = int(input("Geef het aantal minuten op: ")) * 60
# seconds = int(input("Geef het aantal seconden op: "))
# time = days + hours + minutes + seconds
# print("Het totale aantal seconden bedraagt: ", time)


# print documentatie
# print(input.__doc__)
# print(print.__doc__)
# print(int.__doc__)

a = int(input("Geef een getal op: "))
n1 = int(a)
n2 = int(10*n1 + n1 )
n3 = int(100*n1 + n2)
som = n1 + n2 + n3
print("Het resultaat is: %d " % som)
