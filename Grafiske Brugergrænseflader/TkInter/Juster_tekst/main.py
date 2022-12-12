#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på hvordan tekst i labels kan justeres til venstre, højre, osv. 
# Bemærk at denne metode kun er nødvendig når pack anvendes.
##

import tkinter as tk

vindue = tk.Tk() # Opret det grundlæggende vindueselement

vindue.geometry("200x200") # Vinduesstørrelse

# Hvis teksten bare skal højre- eller venstrejusteres, kan parameteren "justify" anvendes.
# Bemærk: Justify gør intet hvis der kun er én linje tekst i labellet
label1 = tk.Label(vindue, text="Meget lang linje af\ntekst i et label", bg="red", justify=tk.RIGHT)
label1.pack(ipady=10)

# Hvis hele indholdet skal flyttes til højre eller venstre, kan det i stedet ske med "anchor".
# Anchor kan tage alle retninger på kompasset, såvel som midten: N, NE, NW, W, E, SW, S, SE, CENTER
label2 = tk.Label(vindue, text="Label 2", bg="green", anchor="w", width=20)
label2.pack(ipady=10)

# Hvis et label ikke defineres med en bredde, har anchor ingen effekt:
label3 = tk.Label(vindue, text="Label 2", bg="blue", anchor="w")
label3.pack(ipady=10)

vindue.mainloop() # Mainloop sørger for at vinduet åbner og forbliver åbent