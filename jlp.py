# coding: utf-8

import printer

import codecs
import sys
import locale


sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)


try:
    f = open(sys.argv[1], "r")
except IndexError:
    f = sys.stdin


for line in f:
    pretty_json = printer.format_json(line)

    print pretty_json


