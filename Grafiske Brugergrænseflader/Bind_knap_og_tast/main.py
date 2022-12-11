#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på hvordan en knap og en tast på tastaturet,
# kan anvende samme event listener
##

import tkinter as tk

# Event listener. Både bind og button kræver en funktion, men kun bind sender
# en parameter med i sit funktionskald. Det resulterer i en fejl, hvis funktionen
# ikke kan håndtere parameteren "event". 
# Samtidigt sender en button ingen parametre med, og kan derfor ikke kalde en funktion som kræver
# event. Altså skal event have en default værdi, så funktionen kan kaldes både med og uden parametren.
def goer_ting(event=None):
    print("Fisk")

vindue = tk.Tk() # Opret det grundlæggende vindueselement

vindue.geometry("200x200") # Vinduesstørrelse

knap_goer= tk.Button(vindue, text="Gør", command=goer_ting) # Aktiverer funktionen ved tryk på knappen
knap_goer.pack()

vindue.bind("<Key>", goer_ting) # Aktiverer funktionen ved tryk på alle taster


vindue.mainloop() # Mainloop sørger for at vinduet åbner og forbliver åbent