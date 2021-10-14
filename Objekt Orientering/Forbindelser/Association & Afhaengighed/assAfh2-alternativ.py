#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på forbindelserne "Association" og "Afhængighed"
#
# assAfh2 kan være svær at implementere hvis vi bruger en database,
# derfor kan man også vælge denne løsning med en manager
# Dette vil kræve et andet klassediagram
##



class Elev:
    def __init__(self, navn, studienr):
        self.navn = navn
        self.studienr = studienr

class Uddannelse:
    def __init__(self, navn, type, tid):
        self.navn = navn
        self.type = type
        self.tid = tid

class ElevUddannelse:
    def __init__(self, elev, uddannelse):
        self.elev = elev
        self.uddannelse = uddannelse

class UddannelsesManager:
    def __init__(self):
        self.uddannelser = []
        self.elever = []
        self.elevUddannelse = []

    def tilfoejUddannelse(self, navn, type, tid):
        nyUdd = Uddannelse(navn, type, tid)
        self.uddannelser.append(nyUdd)

    def tilfoejElev(self, navn, studienr, uddannelsesNavn):
        #Find uddannelse:
        udd = None
        for i in range(0, len(self.uddannelser)):
            if self.uddannelser[i].navn == uddannelsesNavn:
                udd = self.uddannelser[i]

        #Uddannelse fundet, så vi tilføjer elev
        if not udd == None:
            #Opret elev
            nyElev = Elev(navn, studienr)
            #Opret forbindelse
            elevUdd = ElevUddannelse(nyElev, udd)
            #Tilføj forbindelse til liste
            self.elevUddannelse.append(elevUdd)
