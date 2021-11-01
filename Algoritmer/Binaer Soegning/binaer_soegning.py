#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på implementation af binær søgning
##

import math
from utils import Comparator

# Bemærk: Sorterede lister
talliste = [-4, 0, 1, 5, 23]
ordliste = ["dild", "fisk", "gnu", "hest", "mug"]

findTal = 23
findOrd = "sky"

# Søgning i tallisten
startPos = 0
slutPos = len(talliste) - 1

fundet = False
while startPos <= slutPos:
    midtPos = math.floor((slutPos + startPos) / 2) # Nedrunding for at sikre heltal

    if findTal == talliste[midtPos]: # Tal fundet
        print("Tal fundet")
        fundet = True
        break
    elif findTal < talliste[midtPos]: # Tal er mindre end midten
        slutPos = midtPos - 1
    else: # Tal er større end midten
        startPos = midtPos + 1
if not fundet:
    print("Tal ikke fundet")

# Søgning i ordlisten
comparator = Comparator() # Bruges til alfabetisk sammenligning af ord
startPos = 0
slutPos = len(ordliste) - 1
midtPos = None

fundet = False
while startPos <= slutPos:
    midtPos = math.floor((slutPos + startPos) / 2) # Nedrunding for at sikre heltal

    if findOrd == ordliste[midtPos]:
        print("Ord fundet")
        fundet = True
        break
    elif findOrd == comparator.kommerFoerst(findOrd, ordliste[midtPos]): # Essentielt findord < ordliste[midtPos]
        slutPos = midtPos - 1
    else:
        startPos = midtPos + 1
if not fundet:
    print("Ord ikke fundet")