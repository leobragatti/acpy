#! /usr/bin/env python
# coding:utf-8
import string

""" Exercicio 1 e 2 """
fox = 'The quick brown fox jumps over the lazy dog'
fox_letters = set(l.upper() for l in fox if l.isalpha())
#fox_letters = set(l.upper() for l in fox)
print len(fox_letters)

""" Exercicio 3 """
letters = set(string.ascii_uppercase)
print fox_letters == letters

""" Exercicio 4 """
jabuti = 'Um pequeno jabuti xereta viu dez cegonhas felizes'
jabuti_letras = set(l.upper() for l in jabuti if l.isalpha())
print len(jabuti_letras)
print letters != jabuti_letras
