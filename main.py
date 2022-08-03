import doctest
from fonction import *

def nim(nb=21):
    L = []
    for i in range (21):
        L.append(i+1)
    return L

def marienbad(L = [7,5,3,1]):
    liste = [[],[],[],[]]
    for i in range (4):
        for j in range (L[i]):
            liste[i].append([j+1])
    return liste

def manchenim():
    alum = nim()
    chiffre = ["0","1","2","3","4","5","6","7","8","9"]
    joueur = 0
    while not vic(alum):
        coup = 4
        while coup <0 or coup>3:
            print ("\n",alum)
            coup = input("Retirer: \n1 \n2 \n3 \n")
            coup = coup.strip()
            if coup not in chiffre:
                coup = 0
                print ("invalid input")
            else:
                coup = int(coup)           
        if possible(alum, coup):
            retirer(alum, coup)
        joueur += 1
    if joueur % 2 == 1:
        print ("Le joueur 1 a gagné!")
    else:
        print ("Le joueur 2 a gagné!")
    return
    
def manchemarien():
    alum = marienbad()
    chiffre = ["0","1","2","3","4","5","6","7","8","9"]
    joueur = 0    
    while not vicmarien(alum):
        print(alum)
        coup = -1
        while coup < 0 or coup > 3:
            for i in range (len (alum)):
                print("\n","rangee",i,":",alum[i])
            row = -1
            while row < 0 or row > 3:
                row = input("Choissisez la rangee 0, 1, 2, 3\n")
                row = row.strip()
                if row not in chiffre:
                    row = -1
                    print("invalid row")
                else :
                    row = int(row)
            coup = input("Retirer: \n1 \n2 \n3 \n4 \n5 \n6 \n7\n")
            coup = coup.strip()
            if coup not in chiffre:
                coup = 0
                print ("invalid input")
            else:
                coup = int(coup)
            if possible(alum[row], coup):
                retirer(alum[row], coup)
            joueur += 1
    if joueur % 2 == 1:
        print ("Le joueur 1 a gagné!")
    else:
        print ("Le joueur 2 a gagné!")
    return
    