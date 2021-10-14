#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på forbindelsen "Nedarvning"
##

class Person:
    def __init__(self, navn, telefon, email):
        self.navn = navn
        self.telefon = telefon
        self.email = email

    #Ligegyldig metode
    def erLevende(self):
        print("Jeg er levende")
        #TODO: Find ud af om personen er levende

class Elev(Person): #I parenteserne står navnet på den klasse vi nedarver fra
    def __init__(self, navn, telefon, email, studienr, uddannelse):
        # Send data til klasse vi nedarver fra:
        super().__init__(navn, telefon, email)
        #Opret vores egne variabler:
        self.studienr = studienr
        self.uddannelse = uddannelse

    #Ligegyldig metode
    def afslutUddannelse(self):
        print("Nu er jeg færdig")
        #TODO: Find ud af hvordan vi afslutter

#Test person-klasse:
minPerson = Person("Kurt", "12345678", "kurt@kurt.kurt")
minPerson.erLevende()
#Denne linje virker ikke da Person ikke er en Elev:
#print(minPerson.studienr)

#Test elev-klasse:
minElev = Elev("John", "87654321", "john@john.john", 125, "HTX")
minElev.afslutUddannelse()
#Denne linje virker, da en Elev er en Person:
minElev.erLevende()
