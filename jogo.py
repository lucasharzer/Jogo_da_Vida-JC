from tkinter import *
from time import sleep


# célula com coordenadas x, y
celula_qualquer = [[0 for row in range(-1, 41)] for col in range(-1, 41)]
celula_viva = [[0 for row in range(-1, 41)] for col in range(-1, 41)]
muda_de_estado = [[0 for row in range(-1, 41)] for col in range(-1, 41)]
# se for uma célula viva, passa a ser morta e se for uma célula morta, passa a ser viva.


# Estado Inicial
def Preenche():
    for y in range(-1, 41):
        for x in range(-1, 41):
            celula_viva[x][y] = 0
            muda_de_estado[x][y] = 0
            celula_qualquer[x][y] = tela.create_oval((x*10, y*10, x*10+10, y*10+10), outline="blue", fill="black")

            # Células vivas predefinidas:

            celula_viva[2][4] = 1
            celula_viva[3][5] = 1
            celula_viva[4][3] = 1
            celula_viva[4][4] = 1
            celula_viva[4][5] = 1
            celula_viva[4][7] = 1
            celula_viva[5][6] = 1
            celula_viva[5][8] = 1
            celula_viva[5][10] = 1
            celula_viva[7][5] = 1
            celula_viva[30][20] = 1
            celula_viva[30][21] = 1
            celula_viva[30][23] = 1
            celula_viva[29][19] = 1
            celula_viva[29][21] = 1
            celula_viva[29][24] = 1
            celula_viva[28][19] = 1
            celula_viva[28][22] = 1
            celula_viva[28][23] = 1
            celula_viva[20][20] = 1
            celula_viva[21][21] = 1
            celula_viva[20][21] = 1
            celula_viva[20][22] = 1
            celula_viva[19][22] = 1


# Quantidade de células vizinhas vivas, analisando cada uma das 8 células vizinhas
# v-1, n-1        v-1, n        v-1, n+1
# 
# v, n-1          (v, n)          v, n+1
# 
# v+1, n-1        v+1, n         v+1, n+1          
def Celula_vizinha(v, n):
    vizinhas_vivas = 0
    if celula_viva[v-1][n-1] == 1:
        vizinhas_vivas += 1        # vizinhas_vivas = vizinhas_vivas + 1
    if celula_viva[v-1][n] == 1:
        vizinhas_vivas += 1
    if celula_viva[v-1][n+1] == 1:
        vizinhas_vivas += 1
    if celula_viva[v][n-1] == 1:
        vizinhas_vivas += 1
    if celula_viva[v][n+1] == 1:
        vizinhas_vivas += 1
    if celula_viva[v+1][n-1] == 1:
        vizinhas_vivas += 1
    if celula_viva[v+1][n] == 1:
        vizinhas_vivas += 1
    if celula_viva[v+1][n+1] == 1:
        vizinhas_vivas += 1
    return vizinhas_vivas


def Regras():
    for y in range(0, 40):
        for x in range(0, 40):
            vizinhas_vivas = Celula_vizinha(x, y)
            # Primeira Regra
            if celula_viva[x][y] == 1 and vizinhas_vivas < 2:
                muda_de_estado[x][y] = 0
            # Segunda Regra
            if celula_viva[x][y] == 1 and vizinhas_vivas > 3:
                muda_de_estado[x][y] = 0
            # Terceira Regra
            if celula_viva[x][y] == 0 and vizinhas_vivas == 3:
                muda_de_estado[x][y] = 1
            # Quarta Regra
            if celula_viva[x][y] == 1 and (vizinhas_vivas == 2 or vizinhas_vivas == 3):
                muda_de_estado[x][y] = 1
    for y in range(0, 40):
        for x in range(0, 40):
            celula_viva[x][y] = muda_de_estado[x][y]


def Define_celula():
    for y in range(40):
        for x in range(40):
            if celula_viva[x][y] == 0:
                tela.itemconfig(celula_qualquer[x][y], fill="black")
            if celula_viva[x][y] == 1:
                tela.itemconfig(celula_qualquer[x][y], fill="green")

def Jogar():
    Regras()
    Define_celula()
    interface.after(800, Jogar)
    # atualizar a função jogar no intervalo de tempo em milisegundos


# Teste do jogo
print('\033[1;32mJogo Da Vida de John Conway\nCom células vivas predefinidas:\033[m')
sleep(3)
interface = Tk()
interface.title("Jogo da Vida de John Conway")
tela = Canvas(interface, width=400, height=400,highlightthickness=0, bd=1, bg='black')
tela.pack(expand=True)
Preenche()
Jogar()
interface.mainloop()