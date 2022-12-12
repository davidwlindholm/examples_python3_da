#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på hvordan man kan evaluere input mens der skrives.
##

import tkinter as tk

# Funktion til evaluering af hvert tastetryk i inputfeltet
def tjek_input(tekst):
    if "fisk".startswith(tekst): # Starter ordet fisk med det indtastede? (f, fi, fis, fisk)
        return True # Inputtet er tilladt
    else:
        return False # Inputter er ikke tilladt da det ikke er en del af ordet "fisk"


vindue = tk.Tk()
vindue.title("Skriv \"fisk\"")
vindue.geometry("300x200")

inputfelt = tk.Entry(vindue) # inputfelt
inputfelt.pack(ipadx=10, ipady=10)
reg_tjek_input = vindue.register(tjek_input) # Registrer kontrolfunktionen, så den gemmes som en tekststreng

inputfelt.config(validate="key", validatecommand=(reg_tjek_input, "%P")) # Ved hvert tryk på en tast, evaluer om inputtet er tilladt

vindue.mainloop()