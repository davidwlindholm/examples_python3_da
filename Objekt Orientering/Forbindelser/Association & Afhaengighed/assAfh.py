#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på forbindelserne "Association" og "Afhængighed"
#
# Da bilen kan være på 0..1 vej bruger vi en variabel.
# Vi har besluttet ikke at holde styr på hvor mange biler der er på vejen,
# derfor ingen liste i Vej.
##

class Vej:
    def __init__(self, navn, gpsKoordinater):
        self.navn = navn
        self.gpsKoodinater = gpsKoordinater

    def spaerVej(self):
        print("Vejen er lukket")
        #TODO: Luk vej

class Bil:
    #Variabel til vej, hvis vi bruger én.
    vej = None

    def __init__(self, model, maerke):
        self.model = model
        self.maerke = maerke
        self.hastighed = 0

    def startBil(self):
        print("Vroom")

    #Metoder til at oprette forbindelsen til den anden klasse
    def tilfoejVej(self, vej):
        self.vej = vej

    def forladVej(self):
        self.vej = None

    #Alternativ metode til at forbinde til vej - opret vejen selv.
    #Denne metode kan kun bruges fordi Vej ikke skal kende til Bil.
    def tilfoejVejMedData(self, navn, gpsKoodinater):
        self.vej = Vej(navn, gpsKoodinater)


#Test klasser
minVej = Vej("Fiskervej", [55.474597, 8.426153])
minBil = Bil("BMW", "M3")

minBil.tilfoejVej(minVej)
print(minBil.vej.navn)
minBil.forladVej()
