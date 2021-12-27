#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Demo klasse til brug i main.py
##

class Person:
    def __init__(self, navn):
        self.navn = navn

    def sig_hilsen(self):
        print("Hej mit navn er " + self.navn)