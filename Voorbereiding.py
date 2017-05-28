# import tkinter as tk
#
# root = tk.Tk()
#
# root.mainloop()
#
# print("Basic Programming - 2016")
# print("Week 1")
# opleiding = "NMCT"
# opleiding2 = "Deze cursus is onderdeel van de opleiding %s" % opleiding
# print("Welkom in {0} {1}".format(opleiding, opleiding2))
# # identiek
# print("Welkom in %s %s" % (opleiding, opleiding2))
# print("De hoofdstad van of {land} is {hoofdstad}".format(land="Belgie", hoofdstad="Brussel"))  # ToDo: hoe � afprinten?
#
# jaartal = 2016
# a, b = 1, 2
# print("a={0},b={1}".format(a, b))
#
# getal1, getal2, woord = 10, 12, "herfst"
#
# # Assignment Operators
# # enkele speciale zijn
# getal = 2
# getal **= 3
# print("resultaat van getal **= 3 is %s " % getal)
# getal //= 2
# print("resultaat van getal //= 3 is %0.0f " % getal)
#
# # rekenkundige bewerkingen
# c = a + b
# d = 3.14
# d = 3.14 + 1.875
# print("Constrante pi: {0}".format(d))
#
# input
#
# naam = input("Geen uw naam op: ")
# voornaam = input("Geef uw voornaam op: ")
# leeftijd = int(input("Wat is uw mentale leeftijd? "))
# leeftijd *= 2
# print("Welkom {1} {0} in {2}".format(voornaam, naam, opleiding))
# print("uw werkelijke leeftijd is {0}".format(leeftijd))
#
# # bmi-berekenen
# gewicht = float(input("Geef uw gewicht op (kg):"))
# lengte = float(input("Geef uw lengte op (m):"))
# bmi = gewicht / lengte ** 2
# print("Uw bmi is {0:.2f}".format(bmi))
#
# # Meer info op
# # http://www.python-course.eu/python3_formatted_output.php
#
#
#
# if (4 == 4):
#     print("Het antwoord is ")
#     print("True")
# else:
#     print("Het antwoord is ")
#     print("False")
#
#
#
# contactpersoon = "Walcarius Stijn"; opleiding ="NMCT"; jaartal=2016      #e-mail: stijn.walcarius@howest.be


# getalHex = 0xABD785
# getalBin = 0b101011
# getalOctal = 0o45275
# getalDec = 12541



getal1 = 0b1010101
getal2 = 0b1111001
som = getal1 + getal2
print("de som is {0:b}".format(som))