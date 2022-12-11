#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på hvordan et vindue sættes i fuldskærm
##

import tkinter as tk

fuldskaerm = False

def toggle_fuldskaerm():
    global fuldskaerm # Global variabel for at gemme vinduets tilstand
    fuldskaerm = not fuldskaerm # Skift boolean til det omvendte

    if fuldskaerm:
        vindue.attributes('-fullscreen', True) # Aktiver fuldskærm
    else:
        vindue.attributes('-fullscreen', False) # Deaktiver fuldskærm


vindue = tk.Tk() # Opret det grundlæggende vindueselement

vindue.geometry("200x200") # Vinduesstørrelse

knap_fuldskaerm = tk.Button(vindue, text="Toggle fuldskærm", command=toggle_fuldskaerm)
knap_fuldskaerm.pack()


vindue.mainloop() # Mainloop sørger for at vinduet åbner og forbliver åbent