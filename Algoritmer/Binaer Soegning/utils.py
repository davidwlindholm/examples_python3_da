#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Klasse der sammenligner ord og returnerer det der kommer først
# alfabetisk. Anvendes for at undgå problemer med rækkefølgen af danske
# bogstaver i unicode.
##

class Comparator:
    def __init__(self):
        self.alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "æ", "ø", "å"]

    # Returnerer det af to ord der kommer først
    def kommerFoerst(self, ord1, ord2):
        # Samme ord to gange
        if ord1 == ord2:
            return ord1

        # Speciel situation til korte ord der er del af længere ord
        # F.eks. "hus" og "husk".
        if ord1 == ord2[0:len(ord1)]:
            return ord1
        elif ord2 == ord1[0:len(ord2)]:
            return ord2

        # Alle andre situationer
        for pos in range(0, len(ord1)): # Løb ord1 igennem
            if ord1[pos] != ord2[pos]: # Find første bogstav der ikke er det samme
                if self.alfabet.index(ord1[pos]) < self.alfabet.index(ord2[pos]): # Hvilket bogstav kommer først
                    return ord1
                else:
                    return ord2