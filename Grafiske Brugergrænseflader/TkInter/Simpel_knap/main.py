#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på en knap og dens tilhørende event listener
##

import tkinter as tk

# Event listener til knappen.
# Hvad end der skal ske når der trykkes på knappen, defineres i denne funktion.
# Samme listener kan bruges til flere knapper.
def knap_klik():
    print("fisk")

vindue = tk.Tk() # Opret det grundlæggende vindueselement

vindue.geometry("200x100") # Sæt vinduets størrelse

# En knap skal bruge tre stykker information. 
# Første parameter er beholderen som knappen skal tilføjes til. Her "vindue". 
# Parameteren "text" er den tekst der skal stå på knappen. 
# Parameteren "command" er den funktion der skal kaldes når der trykkes på knappen. 
# Bemærk at funktionens navn skrives uden citationstegn og uden parentes til slut. 
knap = tk.Button(vindue, text="Udskriv fisk", command=knap_klik)

knap.pack() # Organiser indholdet i vinduet

vindue.mainloop() # Mainloop sørger for at vinduet åbner og forbliver åbent
