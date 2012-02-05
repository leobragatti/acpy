#! /usr/bin/env python
# coding:utf-8

mulheres = ['Mariana', 'Ana', 'Paula']
homens = ['Pedro', 'Juca', 'Tom', 'Joaquim']

""" Exercicio 1 """
filtro = [homem for homem in homens if len(homem) <= 4]
print filtro

""" Exercicio 2 """
tupla = [(homem[0], homem) for homem in homens]
print tupla

""" Exercicio 3 """
dicionario = dict([{homem[0], homem} for homem in homens])
print dicionario

""" Exercicio 4 """
associacao = zip(mulheres, homens)
print associacao

""" Exercicio 5 """
danca = [(mulher, homem) for mulher in mulheres for homem in homens]
print danca

""" Exercicio 6 """
dancaFiltro = [(mulher, homem) for mulher in mulheres if len(mulher)<=4 for homem in homens if len(homem)<=4]
print dancaFiltro
