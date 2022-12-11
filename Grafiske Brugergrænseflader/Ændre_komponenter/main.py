#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på ændring af komponenters tekst og tilstand
##

import tkinter as tk

def toggle_knap():
    knap_fisk["state"] = "normal" # Gør knap_fisk klikbar

def toggle_tekst():
    label.config(text="Hest") # Lav teksten på label om til "Hest"

vindue = tk.Tk() # Opret det grundlæggende vindueselement

vindue.geometry("200x200") # Vinduesstørrelse

knap_aktiver = tk.Button(vindue, text="Aktiver knap", command=toggle_knap)
knap_aktiver.pack()

knap_fisk = tk.Button(vindue, text="Skift dyr", command=toggle_tekst)
knap_fisk.pack(ipadx=12) # Justering for at gøre knapperne lige store
knap_fisk["state"] = "disable" # Knappen er ikke klikbar

label = tk.Label(vindue, text="Fisk")
label.pack(expand="true") # Brug resten af pladsen til dette label


vindue.mainloop() # Mainloop sørger for at vinduet åbner og forbliver åbent