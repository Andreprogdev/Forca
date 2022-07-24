import imp
import random
from gotoxy import gotoxy
from termcolor import colored

cartas = list('AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZaabbccddeeff')
random.shuffle(cartas)
tabuleiro = open("tabuleiroteste.txt")
tabuleiro = tabuleiro.read()

def seleciona():
    x1,y1 = map(int, input('informe a coord X e Y:'))
    
    x2,y2 = map(int, input('informe a coord X e Y:'))

def removePeca(int1,int2,int3,int4,int5,int6,int7,int8):
    novoTabuleiro1 = "    ".join([tabuleiro[:int1],tabuleiro[int5:]])
    novoTabuleiro2 = "    ".join([novoTabuleiro1[:int2],novoTabuleiro1[int6:]])
    novoTabuleiro3 = "    ".join([novoTabuleiro2[:int3],novoTabuleiro2[int7:]])
    novoTabuleiro4 = "    ".join([novoTabuleiro3[:int4],novoTabuleiro3[int8:]])
    print(novoTabuleiro4.format(*cartas))

def colorePeca(x,y):
    variax = 5 *  (x-1)
    variay = 235 * (y-1)
    i,j,k,l = variax + 60 + variay , variax + 125 + variay, variax + 190 + 1 * (x-1)+variay, variax + 263 + variay
    m,n,o,p = i + 4,j + 4,k + 5,l + 4
    
    novoTabuleiro1 = colored(tabuleiro[i:m], "red").join([tabuleiro[:i],tabuleiro[m:]])
    novoTabuleiro2 = colored(novoTabuleiro1[j:n], "red").join([novoTabuleiro1[:j],novoTabuleiro1[n:]])
    novoTabuleiro3 = colored(novoTabuleiro2[k:o], "red").join([novoTabuleiro2[:k],novoTabuleiro2[o:]])
    novoTabuleiro4 = colored(novoTabuleiro3[l:p], "red").join([novoTabuleiro3[:l],novoTabuleiro3[p:]])
    print(novoTabuleiro4.format(*cartas))
   