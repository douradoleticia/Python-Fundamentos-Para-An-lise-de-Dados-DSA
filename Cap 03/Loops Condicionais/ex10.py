# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:49:41 2022

@author: letic
"""

contador = 0
frase = "É melhor, muito melhor, contentar-se com a realidade; \
    se ela não é tão brilhante como os sonhos, tem pelo menos a \
    vantagem de existir." 
for i in frase:
    if i == "r":
        contador += 1
print("Na frase do Machado, há", contador, "'r'.")