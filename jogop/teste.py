import random
from termcolor import colored

cartas = list('AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZaabbccddeeff')
random.shuffle(cartas)
tabuleiro = open("tabuleiroteste.txt")
tabuleiro = tabuleiro.read()

def colorePeca2(x,y):
    variax = 5 *  (x-1)
    variay = 235 * (y-1)
    inicio = [variax + 104 + variay , variax + 169 + variay, variax + 234 + 1 * (x-1)+variay, variax + 307 + variay,]
    fim = [inicio[0] + 4,inicio[1] + 4,inicio[2] + 5,inicio[3] + 4]
    novoTabuleiro1 = colored(tabuleiro[inicio[0]:fim[0]], "red").join([tabuleiro[:inicio[0]],tabuleiro[fim[0]:]])
    novoTabuleiro2 = colored(novoTabuleiro1[inicio[1]:fim[1]], "red").join([novoTabuleiro1[:inicio[1]],novoTabuleiro1[fim[1]:]])
    novoTabuleiro3 = colored(novoTabuleiro2[inicio[2]:fim[2]], "red").join([novoTabuleiro2[:inicio[2]],novoTabuleiro2[fim[2]:]])
    novoTabuleiro4 = colored(novoTabuleiro3[inicio[3]:fim[3]], "red").join([novoTabuleiro3[:inicio[3]],novoTabuleiro3[fim[3]:]])
    return novoTabuleiro4.format(*cartas)
def seleciona():
    print(tabuleiro.format(*cartas))
    x1,y1 = map(int, input('informe a coord X e Y:'))
    select1 = tabuleiro.replace(tabuleiro,colorePeca(x1,y1))
    print(select1.format(*cartas))
    x2,y2 = map(int, input('informe a coord X e Y:'))
    select2 = tabuleiro.replace(tabuleiro,colorePeca(x2,y2)).replace(tabuleiro,colorePeca(x1,y1))
    print(select2.format(*cartas))
print((len(tabuleiro.format(*cartas))))
print((len(colorePeca(1,1))))