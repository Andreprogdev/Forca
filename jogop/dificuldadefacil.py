import csv
import numpy as np
from termcolor import colored 
with open("cartas6x6.csv", newline='') as file:
    result_list = list(csv.reader(file))
    cartas = np.array(result_list)

def seleciona():
    x1,y1 = map(int, input("Informe as coords X e Y: "))
    imprimeTabuleiro(cartas)
    imprimeTabuleiro(colorePeca(x1,y1))

def imprimeTabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            print(tabuleiro[i][j], end="")
        print("\n")   

def colorePeca(x,y):
   cartas[x][y] = colored(cartas[x][y], "blue")
   return cartas
seleciona()