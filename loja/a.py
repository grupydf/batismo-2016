#! /usr/bin/python3
# coding: utf-8
arquivo = open('produtos.csv', 'r')
produtos = csv.DictReader(arquivo, delimiter=";")
for pro in produtos:
    print (pro)
