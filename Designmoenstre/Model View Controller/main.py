#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på Model View Controller designmønstret.
##

import time
import os

#### MODEL ####
class FileIO:
    def loadFil(self, navn):
        loadedFil = Fil()
        loadedFil.navn = navn
        loadedFil.sidstGemt = time.time()
        loadedFil.data = ""

        file = open(navn, "r")
        content = file.readlines()
        for line in content:
            loadedFil.data += line
            loadedFil.data += "\n"

        return loadedFil

    def gemFil(self, fil):
        gemtFil = open(fil.navn, "w")
        gemtFil.write(fil.data)
        gemtFil.close()

    def isFile(self, navn):
        return os.path.isfile(navn)

class Fil:
    navn = None
    data = None
    sidstGemt = None


#### CONTROLLER ####
class DataManager:
    def __init__(self):
        self.fileio = FileIO()

    def laesFil(self, navn):
        if self._checkData(navn):
            file = self.fileio.loadFil(navn)
            return file.data

    def skrivFil(self, navn, data):
        if self._checkData(navn, data):
            file = Fil()
            file.data = data
            file.navn = navn
            file.sidstGemt = time.time()
            self.fileio.gemFil(file)

    def _checkData(self, filnavn, fildata = None):
        erOkay = True
        if filnavn == "" or filnavn is None:
            erOkay = False
        if fildata != None and fildata == "":
            erOkay = False
        if fildata == None and not self.fileio.isFile(filnavn):
            erOkay = False
        return erOkay


#### VIEW ####
class MainUI:
    def __init__(self):
        self.dataManager = DataManager()
        self.mainMenu()

    def mainMenu(self):
        print("---- Velkommen til tekst editor ----")
        print("Vælg mulighed:\n[1] Læs fil\n[2] Skriv til fil\n[3] Exit")
        valg = input("")
        self.handleInput(valg)

    def handleInput(self, valg):
        if valg == "1":
            self.loadMenu()
        elif valg == "2":
            self.gemMenu()
        elif valg == "3":
            exit(0)
        else:
            print("Ukendt kommando")
            self.mainMenu()

    def gemMenu(self):
        print("------------------------")
        navn = input("Filnavn:")
        data = input("Data der skal gemmes:")
        self.dataManager.skrivFil(navn, data)
        self.mainMenu()

    def loadMenu(self):
        print("------------------------")
        navn = input("Filename:")
        print(self.dataManager.laesFil(navn))
        self.mainMenu()


# Test code
ui = MainUI()
