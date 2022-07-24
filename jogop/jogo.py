import random

# Criação dos valores das cartas, embaralhamento e separação em sub-arrays
cartas = list('AABBCCDDEEFFGGHH')
random.shuffle(cartas)
cartas = [cartas[:4],
         cartas[4:8],
         cartas[8:12],
         cartas[12:]]
tabuleiro = [list('*'*4) for i in range(4)]

def seleciona():
    # recebe 2 valores x e y pra indicar a posição dos pares
    a,b = map(int, input('? '))
    imprimeTabuleiro((a,b))
    # recebe 2 valores x e y pra indicar a posição dos pares
    x,y = map(int, input('? '))
    imprimeTabuleiro((a,b),(x,y))
    # Troca os asteristicos pelo valor das cartas
    if cartas[a][b] == cartas[x][y]:
        print('Formou par!')
        tabuleiro[a][b] = cartas[a][b]
        tabuleiro[x][y] = cartas[x][y]
    else:
        print('não formou par')
    # manter o loop do while na linha 47 ativo
    if any('*' in linha for linha in tabuleiro):
        return True
    
def imprimeTabuleiro(*tiles):
    for linha in range(len(cartas)):
        for coluna in range(len(cartas[0])):
            if (linha,coluna) in tiles:
                print(cartas[linha][coluna], end='', flush=True)
            else:
                print(tabuleiro[linha][coluna], end='', flush=True)
        print()

imprimeTabuleiro()

while seleciona():
    pass

