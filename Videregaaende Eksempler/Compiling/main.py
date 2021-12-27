#!/usr/bin/env python

##
# © David Lindholm - me@davidlindholm.info
# License: GNU Affero General Public License v3.0
# Legal: https://www.gnu.org/licenses/agpl-3.0.en.html
##

##
# Demonstration af kald til python kompileren med specifikke filer.
# Dette sker normalt automatisk når et stykke kode kaldes flere gange.
# Formålet med dette er altså primært at spare tid de første gange
# programmet køres.
#
# Bemærk at koden stadig kræver Python for at køre, da det bliver kompilet
# til Python bytekode der skal fortolkes.
#
# Denne kode er funktionelt det samme som at køre kommandoen:
# python -m compileall demo.py
# i en terminal.
##

import py_compile

py_compile.compile('demo.py')
