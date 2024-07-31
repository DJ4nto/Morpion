import random

class bcolors:
    RRR = '\033[91m'
    GGG = '\033[92m'

symbol_player = "🔴"
symbol_bot = "❌"

print("Vous êtes les", symbol_player)
print("Le bot est les", symbol_bot)

table = [[0,0,0], [0,0,0], [0,0,0]]

def canwin(p):
    for i in range(3):
        for j in range(3):
            if table[i][j] == 0:
                table[i][j] = p
                if checkwin(p)[0] == 1:
                    table[i][j] = 0
                    return i, j
                else:
                    table[i][j] = 0
    return -1,-1


def playerinsert():
    b = 0
    while b == 0:
        ligne = int(input("Ligne (entre 1 et 3) : "))
        colonne = int(input("Colonne (entre 1 et 3) : "))
        if table[ligne - 1][colonne - 1] == 0:
            b = 1
        else:
            print("Cette case est déjà occupée")
    table[ligne - 1][colonne - 1] = symbol_player


def botinsert():
    v = 0
    if canwin(symbol_bot)[0] != -1:
        table[canwin(symbol_bot)[0]][canwin(symbol_bot)[1]] = symbol_bot
    elif canwin(symbol_player)[0] != -1:
        table[canwin(symbol_player)[0]][canwin(symbol_player)[1]] = symbol_bot
    else:
        while v == 0:
            ligne = random.randint(1,3)
            colonne = random.randint(1,3)
            if table[ligne - 1][colonne - 1] == 0:
                table[ligne - 1][colonne - 1] = symbol_bot
                v = 1


def affichage():
    for i in range(3):
      print("|", end = " ")
      for j in range(3):  
        if table[i][j] == 0:
          print("  ", end = " | ")
        else: 
          print(table[i][j], end = " | ")
      print()

def checkwin(p):
    for i in range(3):
        if table[i][0] == p and table[i][1] == p and table[i][2] == p:
            return 1, i + 1, 0, 0
    for i in range(3):
        if table[0][i] == p and table[1][i] == p and table[2][i] == p:
            return 1, 0, i + 1, 0
    if table[0][0] == p and table[1][1] == p and table[2][2] == p:
        return 1, 0, 0, 1
    if table[2][0] == p and table[1][1] == p and table[0][2] == p:
        return 1, 0, 0, 2
    return 0, 0, 0, 0


def checktie():
    for i in range(3):
        for j in range(3):
            if table[i][j] == 0:
                return 0
    return 1


x = 0
while x == 0:
    playerinsert()
    if checkwin(symbol_player)[0] == 1:
        affichage()

        if checkwin(symbol_player)[1] != 0:
            print("Ligne" + str(checkwin(1)[1]))
        if checkwin(symbol_player)[2] != 0:
            print("Colonne" + str(checkwin(1)[2]))
        if checkwin(symbol_player)[3] == 1:
            print("Diagonale 1")
        if checkwin(symbol_player)[3] == 2:
            print("Diagonale 2")

        print(bcolors.GGG + "Player Wins!")
        x = 1
        if input("Want replay? (Yes) ") != "Yes":
            break
        else:
            x = 0
            table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    if checktie() == 1:
        x = 1
        if input("There is a tie... Want replay? (Yes) ") != "Yes":
            break
        else:
            x = 0
            table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    botinsert()
    if checkwin(symbol_bot)[0] == 1:
        affichage()
        print(bcolors.RRR + "Bot Wins!")
        x = 1
        if input("Want replay? (Yes) ") != "Yes":
            break
        else:
            x = 0
            table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    affichage()
    if checktie() == 1:
        x = 1
        if input("There is a tie... Want replay? (Yes) ") != "Yes":
            break
        else:
            x = 0
            table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
