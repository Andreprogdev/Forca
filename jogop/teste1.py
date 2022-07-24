import random
from termcolor import colored



# sorteia o tabuleiro 
cartas = list('AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZaabbccddeeff')
random.shuffle(cartas)
tabuleiro = open("tabuleiroteste.txt")
tabuleiro = tabuleiro.read()

def seleciona():
    print(tabuleiro.format(*cartas))
    x1,y1 = map(int, input('informe a coord X e Y:'))
    select1 = colorePeca(x1,y1,tabuleiro)
    print(select1.format(*cartas))
    x2,y2 = map(int, input('informe a coord X e Y:'))
    select2 = colorePeca2(x2,y2,select1,)
    print(select2.format(*cartas))
# pega o valor da peça pra saber onde remover

# troca o desenho das peças por espaço em branco e printa o tabuleiro
def removePeca(x,y):
    variax = 5 *  (x-1)
    variay = 235 * (y-1)
    inicio = [variax + 60 + variay , variax + 116 + variay, variax + 172 + 1 * (x-1)+variay, variax + 235 + variay]
    fim = [inicio[0] + 4,inicio[1] + 4,inicio[2] + 5,inicio[3] + 4]
    
    novoTabuleiro1 = "    ".join([tabuleiro[:inicio[0]],tabuleiro[fim[0]:]])
    novoTabuleiro2 = "    ".join([novoTabuleiro1[:inicio[1]],novoTabuleiro1[fim[1]:]])
    novoTabuleiro3 = "    ".join([novoTabuleiro2[:inicio[2]],novoTabuleiro2[fim[2]:]])
    novoTabuleiro4 = "    ".join([novoTabuleiro3[:inicio[3]],novoTabuleiro3[fim[3]:]])
    print(novoTabuleiro4.format(*cartas))

def colorePeca(x,y,tabuleiro,*cor):
    variax = 5 *  (x-1)
    variay = 235 * (y-1)
    inicio = [variax + 60 + variay , variax + 125 + variay, variax + 190 + 1 * (x-1)+variay, variax + 263 + variay]
    if cor == 1:
        for i in range(len(inicio)):
            inicio[i] -= 43

    fim = [inicio[0] + 4,inicio[1] + 4,inicio[2] + 5,inicio[3] + 4]
    novoTabuleiro1 = colored(tabuleiro[inicio[0]:fim[0]], "red").join([tabuleiro[:inicio[0]],tabuleiro[fim[0]:]])
    novoTabuleiro2 = colored(novoTabuleiro1[inicio[1]:fim[1]], "red").join([novoTabuleiro1[:inicio[1]],novoTabuleiro1[fim[1]:]])
    novoTabuleiro3 = colored(novoTabuleiro2[inicio[2]:fim[2]], "red").join([novoTabuleiro2[:inicio[2]],novoTabuleiro2[fim[2]:]])
    novoTabuleiro4 = colored(novoTabuleiro3[inicio[3]:fim[3]], "red").join([novoTabuleiro3[:inicio[3]],novoTabuleiro3[fim[3]:]])
    return novoTabuleiro4
def colorePeca2(x,y,tabuleiro):
    variax = 5 *  (x-1)
    variay = 235 * (y-1)
    inicio = [variax + 68 + variay , variax + 143 + variay, variax + 217 + 1 * (x-1)+variay, variax + 299 + variay,]
    fim = [inicio[0] + 4,inicio[1] + 4,inicio[2] + 5,inicio[3] + 4]
    novoTabuleiro1 = colored(tabuleiro[inicio[0]:fim[0]], "red").join([tabuleiro[:inicio[0]],tabuleiro[fim[0]:]])
    novoTabuleiro2 = colored(novoTabuleiro1[inicio[1]:fim[1]], "red").join([novoTabuleiro1[:inicio[1]],novoTabuleiro1[fim[1]:]])
    novoTabuleiro3 = colored(novoTabuleiro2[inicio[2]:fim[2]], "red").join([novoTabuleiro2[:inicio[2]],novoTabuleiro2[fim[2]:]])
    novoTabuleiro4 = colored(novoTabuleiro3[inicio[3]:fim[3]], "red").join([novoTabuleiro3[:inicio[3]],novoTabuleiro3[fim[3]:]])
    return novoTabuleiro4.format(*cartas)
   
seleciona()

print("--/|  |/| A |/--")