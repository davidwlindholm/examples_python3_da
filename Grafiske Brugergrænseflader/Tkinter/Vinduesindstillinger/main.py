#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på indstillingerne for et vindue i Tkinter
##

import tkinter as tk

vindue = tk.Tk() # Opret det grundlæggende vindueselement

# Giv vinduet en titel
vindue.title("Fisk")

# Giv vinduet en størrelse og en placering på skærmen.
# Formatet er geometry("højde x bredde")
# Koordinatsystemet starter fra skærmens øverste venstre hjørne. 
# Hvilket vil sige at Y-aksen vender nedad, mens X-aksen er som altid.
vindue.geometry('250x300')

# Beslut om vinduet skal kunne trækkes større eller mindre.
# Metoden tager to booleans, for henholdsvist højden og bredden: resizable(højde, bredde)
vindue.resizable(False, False)

# Sørg for at vinduet altid vises øverst
# Bemærk: Brug sparsomt, til vigtige vinduer
vindue.attributes("-topmost", 1)


#vindue.attributes("-fullscreen", 1)
vindue.wm_state('zoomed')

vindue.mainloop() # Mainloop sørger for at vinduet åbner og forbliver åbent