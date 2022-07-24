import random
import numpy as np 
cartas = list('AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZaabbccddeeff')
cartas = random.shuffle(cartas)
tabuleiro = []
for i in range(8):
    for j in range(8):
        tabuleiro[i][j] = "----\n|  |\n|{}|\n----"

print(tabuleiro.format(*cartas))