#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på labels til tekst, og anvendelse af Pack
##

import tkinter as tk

vindue = tk.Tk() # Opret det grundlæggende vindueselement

vindue.geometry("200x200") # Vinduesstørrelse

# Et label skal have to parameter ved oprettelsen
# Første parameter er beholderen som labellet skal puttes ind i. 
# Parameteren "text" er det tekst der skal stå i labellet. 
label1 = tk.Label(vindue, text="Label 1")

# Pack er en geometry-manager, som sørger for at placere komponenter i vinduet.
# Hvis en komponent ikke bliver sendt omkring en geometry-manager som pack 
# (eller en af de andre), bliver den ikke vist.
# Det er ikke nødvendigt at sende parametre med ind i pack, 
# hvis man vil have komponenten centreret og vist på en linje alene.
label1.pack()

# Labellet kan også have parameterene bg for baggrundsfarve, 
# og fg for tekstfarve. 
label2 = tk.Label(vindue, text="Label 2", bg="blue", fg="orange")

# En komponent kan gives ekstra plads ved at fortælle pack hvor meget der skal tilføjes på x og y aksen,
# ved at anvende ipadx og ipady. 
# Bemærk: Det er ikke nødvendigt at angive begge værdier. Tallene skal være positive, og værdien (i pixels)
# tilføjes på begge sider af indholdet.
label2.pack(ipadx=20, ipady=5)

# Hvis en komponent skal placeres midt i det tilgængelige plads, kan det gøres ved at sende
# pack parameteren "expand" og sætte den til "true".
# Den vil så blive placeret midt i det plads der er tilbage når de andre komponenter er placeret.
label3 = tk.Label(vindue, text="Label 3", bg="green")
label3.pack(expand="true")

# En komponent kan placeres ved en af siderne (left, right, top, bottom) ved at benytte parameteren "side".
label4 = tk.Label(vindue, text="Label 4", bg="red")
label4.pack(side="bottom")


vindue.mainloop() # Mainloop sørger for at vinduet åbner og forbliver åbent