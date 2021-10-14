#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på forbindelsen "Aggregering"
##

class Biografsal:
    def __init__(self, nummer, antalSaeder):
        self.nummer = nummer
        self.antalSaeder = antalSaeder

    def startFilm(self):
        pass
        #TODO: Start film

class Biograf:
    def __init__(self, navn, adresse):
        self.navn = navn
        self.adresse = adresse
        self.biografsale = []

    def tilfoejSal(self, biografsal):
        self.biografsale.append(biografsal)

    def harFilm(self, film):
        pass
        #TODO: har film
