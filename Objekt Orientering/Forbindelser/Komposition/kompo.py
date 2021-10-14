#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på forbindelsen "Komposition"
##

class Side:
    def __init__(self, sidetal, indhold):
        self.sidetal = sidetal
        self.indhold = indhold

class Bog:
    def __init__(self, titel, forfatter, sider, owner):
        self.titel = titel
        self.forfatter = forfatter
        self.sider = sider
        self.owner = owner

    def tilfoejSide(self, sidetal, indhold):
        nySide = Side(sidetal, indhold)
        self.sider.append(nySide)

    def fjernSide(self, side):
        self.sider.remove(side)

        #Check om vi selv skal slettes:
        if len(self.sider) == 0:
            self.owner.sletBog(self)

#Klassen BogManager holder styr på bøgerne
class BogManager:
    def __init__(self):
        self.boeger = []

    def tilfoejBog(self, titel, forfatter, sider):
        nyBog = Bog(titel, forfatter, sider, self)
        self.boeger.append(nyBog)

    def sletBog(self, bog):
        self.boeger.remove(bog)
