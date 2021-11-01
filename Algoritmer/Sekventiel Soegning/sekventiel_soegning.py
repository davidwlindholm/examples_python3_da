#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Eksempel på sekventiel søgning
##

talliste = [1, 0, -4, 23, 5]
ordliste = ["fisk", "hest", "gnu", "mug", "dild"]

findTal = 5
findOrd = "sky"

# Søgning i tallisten
fundet = False
for tal in talliste:
    if findTal == tal:
        print("Tal fundet")
        fundet = True
        break
if not fundet:
    print("Tal ikke fundet")

# Søgning i ordlisten
fundet = False
for ord in ordliste:
    if findOrd == ord:
        print("Ord fundet")
        fundet = True
        break
if not fundet:
    print("Ord ikke fundet")