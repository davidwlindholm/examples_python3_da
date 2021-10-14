#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på forbindelserne "Association" og "Afhængighed"
#
# Da en elev kan have flere uddannelser bruger vi en liste
# Vi er også interesseret i hvor mange elever der går på hvilke uddannelser,
# så derfor har uddannelse også en liste
##


class Elev:
    def __init__(self):
        pass
        #Init er tom, så dumme programmører ikke instantierer elev direkte

    #Underscore (_) indikerer til andre at de ikke skal kalde denne metode
    def _nyElev(self, navn, studienr, uddannelse):
        self.navn = navn
        self.studienr = studienr
        #Opret liste af uddannelser eleven går på
        self.uddannelser = []
        self.uddannelser.append(uddannelse)

    def erBestaaet(self, uddannelsesNavn):
        #Løb elevens uddannelser igennem og led efter uddannelsen
        for i in range(0, len(self.uddannelser)):
            if self.uddannelser[i].navn == uddannelsesNavn:
                print("Nu er jeg bestået:", uddannelsesNavn)
                self.uddannelser.pop(i)
                break

class Uddannelse:
    def __init__(self, navn, type, tid):
        self.navn = navn
        self.type = type
        self.tid = tid
        self.elever = []

    def startUndervisning(self):
        if len(self.elever) > 0:
            print("Så starter undervisningen")

    def tilfoejElev(self, elev):
        self.elever.append(elev)

    def opretNyElev(self, navn, studienr):
        nyElev = Elev() #Opret elev
        nyElev._nyElev(navn, studienr, self) #Fyld elev med data
        self.elever.append(nyElev) #Tilføj elev til liste
        return nyElev #Returner til brug i lister

#Test klasser
minUddannelse1 = Uddannelse("HTX", "Gymnasie", "3 år")
minUddannelse2 = Uddannelse("Elektronikkursus", "Aftenskole", "6 mdr")

#Opret og tilføj elev til første uddannelse
minElev = minUddannelse1.opretNyElev("Kurt", 12345)
#Tilføj elev til andre uddannelser:
minUddannelse2.tilfoejElev(minElev)
