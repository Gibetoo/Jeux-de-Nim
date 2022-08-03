import fltk
#==============================================================================
#                                 Fonction du Jeux
#==============================================================================

def nim(nb=21):
    L = []
    for i in range (21):
        L.append(i+1)
    return L

def marienbad(L = [7,5,3,1]):
    liste = [[],[],[],[]]
    for i in range (4):
        for j in range (L[i]):
            liste[i].append(j+1)
    return liste


def possible(alum, coup):
    """
    Regarde si le coup du joueur est possible
    
    :Paramètre alum: Nombre d'alumette
    :Paramètre coup: Nombre de coup 
    :Type: int

    >>> possible([0,0,0],1)
    True
    >>> possible([0,0],3)
    False
    """
    if len(alum) < coup:
        return False
    return True

def retirer(alum, coup):
    """
    Retire le nombre d'alumette choisie par le joueur
    
    :Paramètre alum: Nombre d'alumette
    :Paramètre coup: Nombre de coup 
    :Type: int

    >>> coup([0,0,0],2)
    [0]
    """
    if possible(alum, coup):
        for i in range(coup):
            alum.pop()
    return 

def vic(alum):
    """
    renvoie True si le joueur a gagné
    
    :Paramètre alum: Nombre d'alumette
    :Type: bool
    >>> vic([])
    True
    """
    if len(alum):
        return False
    return True

def vicmarien(alum):
    for i in range (len(alum)):
        if alum[i]:
            return False
    return True

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

#==============================================================================
#                                 Fonction Graphique
#==============================================================================

def alumette(fenx,nb = 21):
    """
    Creation du nombre d'alumette necessaire pour le jeu de Nim
    
    :Paramètre fenx: Taille de fenêtre
    :Paramètre nb: Nombre d'alumette à afficher (défaut: 21)
    :Type: int
    """
    feny = fenx / (16/9)
    fenx = fenx * 0.7
    ray = feny * (1/100)
    debx = fenx / nb
  
    deby = feny * (3/8) + ray * 1.2
    for i in range (1, nb + 1):

        fltk.cercle(debx * i, deby , ray*1.5, remplissage="brown", epaisseur=1)
        fltk.rectangle(debx * i - ray, deby + ray*1.2, debx * i + ray, 
                       deby + ray*23, remplissage="bisque")
    return

def alumettemodif(fenx, alum, nb = 21):
    """
    Modifie le nombre d'alumette
    
    :Paramètre fenx: Taille de fenêtre
    :Type: int
    """
    feny = fenx / (16/9)
    fenx = fenx * 0.7
    ray = feny * (1/100)
    debx = fenx / alum
  
    deby = feny * (3/8) + ray * 1.2
    for i in range (1,nb + 1):

      fltk.cercle(debx * i, deby , ray*1.5, remplissage="brown", epaisseur=1)
      fltk.rectangle(debx * i - ray, deby + ray*1.2, debx * i + ray, 
                     deby + ray*23, remplissage="bisque")
    return


def alumarienbad(fenx, L = [7,5,3,1]):
    """
    Creation du nombre d'alumette necessaire au Marienbad
    
    :Paramètre fenx: Taille de fenêtre
    :Type: int
    """
    feny = fenx / (16/9)
    fenx = fenx * 0.7
    height = feny / (len(L)*2 + 1)
    ray = height/25
    
    for i in range(len(L)):
        for y in range (L[i]):
            debx = fenx / L[0]
            fltk.cercle(debx*(y+1), height * (i*2+1)-20 , ray*2.25, 
                        remplissage="brown", epaisseur=1)
            fltk.rectangle(debx * (y+1) - ray*1.75, 
                           height * (i*2+1) + ray*1.7 -20, 
                           debx * (y+1) + ray*1.75, 
                           height * (i*2+1)+ ray*33.5 -20,remplissage="bisque")
    return
  

def fenplay(fenx) :
    """
    Bouton Play du menu principal
    
    :Paramètre fenx: Taille de fenêtre
    :Type: int
    """
    feny = fenx / (16/9)
    moity = feny/1.7
    moitx = fenx/2
    cranx = fenx/80
    crany = feny/80
    chaine = "Jouer"
    police = "Calibri"
    taille = int((cranx*3))
    fltk.texte(moitx, moity - crany*10 , chaine,
          police=police, taille=taille, couleur="black",
          ancrage='center')
    
    longueur, hauteur = fltk.taille_texte(chaine, police, taille)
    fltk.rectangle(moitx - longueur//2 - cranx,moity - crany*11 - hauteur//2,
                   moitx + longueur//2 + cranx, moity - crany*9 + hauteur//2,
                   couleur="black", epaisseur = fenx/(fenx/2))
    

def menuprin(fenx) : 
    """
    Menu principal avec bouton Play et Parametre
    
    :Paramètre fenx: Taille de fenêtre
    :Type: int
    """
    feny = fenx / (16/9)
    moity = feny/2.2
    moitx = fenx/2
    cranx = fenx/80
    crany = feny/80
    chaine = "Parametre"
    police = "Calibri"
    taille = int((cranx*3))
    fltk.texte(moitx, moity + crany*10 , chaine,
          police=police, taille=taille, couleur="black",
          ancrage='center')
    
    longueur, hauteur = fltk.taille_texte(chaine, police, taille)
    fltk.rectangle(moitx - longueur//2 - cranx, moity + crany*9 - hauteur//2,
                   moitx + longueur//2 + cranx,moity + crany*11 + hauteur//2,
                   couleur="black",  epaisseur = fenx/(fenx/2))
    fenplay(fenx)
    Nom_du_jeux_deux(fenx)
    credit(fenx)
    quitte(fenx)
    
def fennim(fenx) : 
    """
    Bouton du Jeu de Nim
    
    :Paramètre fenx: Taille de fenêtre
    :Type: int
    """
    feny = fenx / (16/9)
    moity = feny/2
    moitx = fenx/2
    cranx = fenx/80
    crany = feny/80
    chaine = "Jeux de Nim"
    police = "Calibri"
    taille = int((cranx*5))
    fltk.texte(moitx, moity - crany*10 , chaine,
          police=police, taille=taille, couleur="black",
          ancrage='center')
    
    longueur, hauteur = fltk.taille_texte(chaine, police, taille)
    fltk.rectangle(moitx - longueur//2 - cranx*2,moity - crany*12 - hauteur//2,
                   moitx + longueur//2 + cranx*2, moity - crany*8 + hauteur//2,
                   couleur="black", epaisseur = fenx/(fenx/3))
    

def fenmarienbad(fenx) : 
    """
    Bouton du jeu Marienbad
    
    :Paramètre fenx: Taille de fenêtre
    :Type: int
    """
    feny = fenx / (16/9)
    moity = feny/2
    moitx = fenx/2
    cranx = fenx/80
    crany = feny/80
    chaine = "Jeux de Marienbad"
    police = "Calibri"
    taille = int((cranx*5))
    fltk.texte(moitx, moity + crany*10 , chaine,
          police=police, taille=taille, couleur="black",
          ancrage='center')
    
    longueur, hauteur = fltk.taille_texte(chaine, police, taille)
    fltk.rectangle(moitx - longueur//2 - cranx*2, moity + crany*8 - hauteur//2,
                   moitx + longueur//2 + cranx*2,moity + crany*12 + hauteur//2,
                   couleur="black",  epaisseur = fenx/(fenx/3))
    
    
def retour(fenx) : 
    """
    Bouton retour
    
    :Paramètre fenx: Taille de fenêtre
    :Type: int
    """
    feny = fenx / (16/9)
    moity = feny/2
    moitx = fenx/2
    cranx = fenx/80
    crany = feny/80
    chaine = "Retour"
    police = "Calibri"
    taille = int((cranx*1.5))
    fltk.texte(moitx, moity + crany*30 , chaine,
          police=police, taille=taille, couleur="black",
          ancrage='center')
    
    longueur, hauteur = fltk.taille_texte(chaine, police, taille)
    fltk.rectangle(moitx - longueur//2 - cranx*2, moity + crany*28 - hauteur//2,
              moitx + longueur//2 + cranx*2,moity + crany*32 + hauteur//2,
              couleur="black",  epaisseur = fenx/(fenx/2))

def retourjeu(fenx) : 
    """
    Second bouton retour utilisé en cours de partie
    
    :Paramètre fenx: Taille de fenêtre
    :Type: int
    """
    feny = fenx / (16/9)
    moity = feny/2
    moitx = fenx/10
    cranx = fenx/80
    crany = feny/80
    chaine = "Retour"
    police = "Calibri"
    taille = int((cranx*1.5))
    fltk.texte(moitx, moity + crany*30 , chaine,
          police=police, taille=taille, couleur="black",
          ancrage='center')
    
    longueur, hauteur = fltk.taille_texte(chaine, police, taille)
    fltk.rectangle(moitx - longueur//2 - cranx*2,moity + crany*28 - hauteur//2,
              moitx + longueur//2 + cranx*2,moity + crany*32 + hauteur//2,
              couleur="black",  epaisseur = fenx/(fenx/2))


def suitenim(fenx) : 
    """
    Page réglage du Jeu de Nim
    
    :Paramètre fenx: Taille de fenêtre
    :Type: int
    """
    feny = fenx / (16/9)
    moity = feny/2
    moitx = fenx/3
    cranx = fenx/80
    crany = feny/80
    fltk.texte(moitx, moity - crany*10 , "Nombre d'alumette :",
          police="Calibri", taille=int((cranx*2)), couleur="black",
          ancrage='center')
    
    moity = feny/1.5
    moitx = fenx/3
    fltk.texte(moitx, moity - crany*10 , "Nombre de coup possible:",
          police="Calibri", taille=int((cranx*2)), couleur="black",
          ancrage='center')
    
    moity = feny / 1.2
    moitx = fenx/3
    fltk.texte(moitx, moity - crany*10 , "Mode Normal ou Misère :",
          police="Calibri", taille=int((cranx*2)), couleur="black",
          ancrage='center')

def playnim(fenx):
    """
    Bouton Play du Jeu de Nim. Sert à lancer le jeu
    
    :Paramètre fenx: Taille de fenêtre
    :Type: int
    """
    feny = fenx / (16/9)
    moity = feny/3.7
    moitx = fenx/2
    cranx = fenx/80
    crany = feny/80
    chaine = "Play"
    police = "Calibri"
    taille = int((cranx*5))
    fltk.texte(moitx, moity - crany*10 , chaine,
          police=police, taille=taille, couleur="black",
          ancrage='center')

def Nom_du_jeux(fenx):
    
    feny = fenx / (16/9)
    moity = feny/1.8
    moitx = fenx/2
    cranx = fenx/80
    crany = feny/80
    chaine = "Jeux de Nim"
    police = "Calibri"
    taille = int((cranx*5))
    fltk.texte(moitx, moity - crany*10 , chaine,
          police=police, taille=taille, couleur="black",
          ancrage='center')

def Nom_du_jeux_deux(fenx):
    
    feny = fenx / (16/9)
    moity = feny/2.6
    moitx = fenx/2
    cranx = fenx/80
    crany = feny/80
    chaine = "Jeux de Nim"
    police = "Calibri"
    taille = int((cranx*5))
    fltk.texte(moitx, moity - crany*10 , chaine,
          police=police, taille=taille, couleur="black",
          ancrage='center')

def AST(fenx):
    feny = fenx / (16/9)
    moity = feny/1.2
    moitx = fenx/2
    cranx = fenx/80
    crany = feny/80
    chaine = "Appuyer sur une touche pour commencer"
    police = "Calibri"
    taille = int((cranx*2))
    fltk.texte(moitx, moity - crany*10 , chaine,
          police=police, taille=taille, couleur="black",
          ancrage='center')

def credit(fenx):
    feny = fenx / (16/9)
    moity = feny/1.215
    moitx = fenx/2
    cranx = fenx/80
    crany = feny/80
    chaine = "Crédit"
    police = "Calibri"
    taille = int((cranx*3))
    fltk.texte(moitx, moity - crany*10 , chaine,
          police=police, taille=taille, couleur="black",
          ancrage='center')

    longueur, hauteur = fltk.taille_texte(chaine, police, taille)
    fltk.rectangle(moitx - longueur//2 - cranx,moity - crany*11 - hauteur//2,
                   moitx + longueur//2 + cranx, moity - crany*9 + hauteur//2,
                   couleur="black", epaisseur = fenx/(fenx/2))

def quitte(fenx):
    feny = fenx/(16/9)
    moity = feny/1.065
    moitx = fenx/2
    cranx = fenx/80
    crany = feny/80
    chaine = "Quitter"
    police = "Calibri"
    taille = int((cranx*3))
    fltk.texte(moitx, moity - crany*10 , chaine,
          police=police, taille=taille, couleur="black",
          ancrage='center')

    longueur, hauteur = fltk.taille_texte(chaine, police, taille)
    fltk.rectangle(moitx - longueur//2 - cranx,moity - crany*11 - hauteur//2,
                   moitx + longueur//2 + cranx, moity - crany*9 + hauteur//2,
                   couleur="black", epaisseur = fenx/(fenx/2))

def cases (fenx,nb = 3):
    """
    Création du nombre de bouton necessaire pour jouer au Jeu de Nim
    Utilisation: Retirer le nombre d'alumette que le joueur désir
    
    :Paramètre fenx: Taille de fenêtre
    :Paramètre nb: Nombre de case (défaut: 3)
    :Type: int
    """
    feny = int( fenx / (16/9))
    chaine = "1"
    police = "Calibri"
    taille = feny // 14
    reste = 0

    if nb > 5 :
        reste = nb - 5
        nb = nb - reste
    for i in range (1 , nb + 1):
        chaine = str(i)
        fltk.texte(fenx * 0.8,i * 2 * feny // 13, chaine,
                police="Calibri", couleur="black",
                ancrage='center', taille = taille )

        longueur, hauteur = fltk.taille_texte(chaine, police, taille)
        fltk.rectangle(fenx * 0.8 - fenx * 0.03 , i * 2 * feny // 13 - fenx * 0.03,
                fenx * 0.8 + fenx * 0.03, i * 2 * feny // 13 + fenx * 0.03,
                couleur="black", epaisseur = fenx // 333)
    if reste > 0 : 
        nb = nb + reste
    if nb > 5:
        for i in range (1 , nb - 4):
            chaine = str(i+5)
            fltk.texte(fenx * 0.9, i * 2 *feny // 13, chaine,
                    police="Calibri", couleur="black",
                    ancrage='center', taille = taille )

            longueur, hauteur = fltk.taille_texte(chaine, police, taille)
            fltk.rectangle(fenx * 0.9 - fenx * 0.03 , 
                           i * 2 * feny // 13 - fenx * 0.03,
                           fenx * 0.9 + fenx * 0.03, 
                           i * 2 * feny // 13 + fenx * 0.03,couleur="black", 
                           epaisseur = fenx // 333)


def imprim(fenx, alum):
    feny = fenx * (16/9)
    fltk.texte ((fenx * 0.7) / 2, feny / 15,chaine = str(alum), 
                taille =int( fenx / 16.66), ancrage="center")
    return

def bouton_plus(fenx,h=5.5,l=0.7):
    """
    Création du bouton "+"
    Utilisation: Augmenter le nombre d'alumette ou de coup 
    
    :Paramètre fenx: Taille de fenêtre
    :Type: int
    """
    feny = int( fenx / (16/9))
    chaine = '+'
    police="Calibri"
    taille = feny // 14
    fltk.texte(fenx * l, 2 * feny // h, chaine,
            police="Calibri", couleur="black",
            ancrage='center', taille = taille )
    
    longueur, hauteur = fltk.taille_texte(chaine, police, taille)
    fltk.rectangle(fenx * l - fenx * 0.03 , 2 * feny // h - fenx * 0.03,
            fenx * l + fenx * 0.03, 2 * feny // h + fenx * 0.03,
            couleur="black", epaisseur = fenx/(fenx/2))

def bouton_moins(fenx,h=5.5,l=0.9):
    """
    Création du bouton "-"
    Utilisation: Diminue le nombre d'alumette ou de coup
    
    :Paramètre fenx: Taille de fenêtre
    :Type: int
    """
    feny = int( fenx / (16/9))
    chaine = '-'
    police="Calibri"
    taille = feny // 14
    fltk.texte(fenx * l, 2 * feny // h, chaine,
            police="Calibri", couleur="black",
            ancrage='center', taille = taille )
    
    longueur, hauteur = fltk.taille_texte(chaine, police, taille)
    fltk.rectangle(fenx * l - fenx * 0.03 , 2 * feny // h - fenx * 0.03,
            fenx * l + fenx * 0.03, 2 * feny // h + fenx * 0.03,
            couleur="black", epaisseur = fenx/(fenx/2))


def nombre_alumette_nim(fenx,h=5.5,l=0.8,nb=21):
    """
    Affiche le nombre d'alumette configurer par le joueur
    
    :Paramètre fenx: Taille de fenêtre
    :Paramètre nb: Nombre d'alumette (défaut: 21)
    :Type: int
    """
    feny = int( fenx / (16/9))
    police="Calibri"
    taille = feny // 14
    fltk.texte(fenx * l, 2 * feny // h, str(nb),
            police="Calibri", couleur="black",
            ancrage='center', taille = taille, tag = "Nb_alum")

    longueur, hauteur = fltk.taille_texte(str(nb), police, taille)
    fltk.rectangle(fenx * l - fenx * 0.03 , 2 * feny // h - fenx * 0.03,
              fenx * l + fenx * 0.03, 2 * feny // h + fenx * 0.03,
              couleur="black", epaisseur = fenx/(fenx/2))
    bouton_moins(fenx,5.5,0.7)
    bouton_plus(fenx,5.5, 0.9)
    
def nombre_de_coup(fenx,h=3.8,l=0.8, nb=3):
    """
    Affiche le nombre de coup configurer par le joueur
    
    :Paramètre fenx: Taille de fenêtre
    :Paramètre nb: Nombre de coup (défaut: 3)
    :Type: int

    """
    feny = int( fenx / (16/9))
    police="Calibri"
    taille = feny // 14
    fltk.texte(fenx * l, 2 * feny // h, str(nb),
            police="Calibri", couleur="black",
            ancrage='center', taille = taille, tag="Nb_coup" )

    longueur, hauteur = fltk.taille_texte(str(nb), police, taille)
    fltk.rectangle(fenx * l - fenx * 0.03 , 2 * feny // h - fenx * 0.03,
              fenx * l + fenx * 0.03, 2 * feny // h + fenx * 0.03,
              couleur="black", epaisseur = fenx/(fenx/2))
    bouton_moins(fenx,3.8,0.7)
    bouton_plus(fenx,3.8,0.9)

def jeu_nim(fenx, base , nb,mode = True):
    """
    Jeu de Nim
    
    :Paramètre fenx: Taille de fenêtre
    :Paramètre base: Nombre d'alumette
    :Paramètre nb: Nombre de cases(nombre de coup)
    :Paramètre mode: Mode de jeu (défaut:'True'= Normal et 'False'= Misère)
    :Type: int et bool
    """
    feny = fenx/(16/9)
    cases(fenx)
    j = 0
    reste = 0
    alum = base
    coup = 0
    
    
    while True:
        fltk.efface_tout()
        alumettemodif(fenx, base, alum)
        imprim(fenx, alum)
        cases(fenx, nb)
        coup = 0

        ev = fltk.attend_ev()
        tev = fltk.type_ev(ev)
        if nb > 5 :
            reste = nb - 5
            nb = nb - reste

        if tev == 'ClicGauche':
            for i in range (1, nb + 1):
                if fenx * 0.8 - fenx * 0.03 < fltk.abscisse(ev) < fenx * 0.8 + fenx * 0.03 and  i * 2 * feny // 13 - fenx * 0.03 < fltk.ordonnee(ev) <  i * 2 * feny // 13 + fenx * 0.03:
                    coup = i
                    j += 1
        if reste > 0 : 
            nb = nb + reste
            for i in range (1 , nb - 4):
                if fenx * 0.9 - fenx * 0.03 < fltk.abscisse(ev) < fenx * 0.9 + fenx * 0.03 and  i * 2 * feny // 13 - fenx * 0.03 < fltk.ordonnee(ev) <  i * 2 * feny // 13 + fenx * 0.03:
                    coup = i + 5
                    j += 1
        if alum - coup >= 0 :
            alum = alum - coup
        if alum == 0:
            if mode:
                fltk.efface_tout()
                alumettemodif(fenx, base, alum)
                gagnant = str (1 + j % 2)
                chaine = "Le joueur " + gagnant +" gagne !"
                fltk.texte (fenx / 2, feny / 2,chaine = chaine,
                       taille =int( fenx // 20), ancrage="center")
                alum = base
                j = 0
                break
            else:
                fltk.efface_tout()
                alumettemodif(fenx, base, alum)
                gagnant = str (1 + j % 2)
                chaine = "Le joueur " + gagnant +" Perd !"
                fltk.texte (fenx / 2, feny / 2,chaine = chaine, 
                       taille =int( fenx // 20), ancrage="center")
                alum = base
                j = 0
                break   
        fltk.mise_a_jour() 
    retourjeu(fenx)

def bouton_Normal(fenx):
    """
    Création du bouton du mode Normal
    
    :Paramètre: Taille de fenêtre
    :Type: int
    """
    feny = fenx / (16/9)
    moity = feny/3
    moitx = fenx/1.4
    cranx = fenx/80
    crany = feny/80
    chaine = "Normal"
    police = "Calibri"
    taille = int((cranx*1.5))
    fltk.texte(moitx, moity + crany*30 , chaine,
          police=police, taille=taille, couleur="black",
          ancrage='center')
    
    longueur, hauteur = fltk.taille_texte(chaine, police, taille)
    fltk.rectangle(moitx - longueur//2 - cranx*2,moity + crany*28 - hauteur//2,
              moitx + longueur//2 + cranx*2,moity + crany*32 + hauteur//2,
              couleur="black",  epaisseur = fenx/(fenx/2))

def bouton_Normalselect(fenx):
    """
    Affiche le bouton Normal séléctioné si le joueur clique dessus
    
    :Paramètre: Taille de fenêtre
    :Type: int
    """
    feny = fenx / (16/9)
    moity = feny/3
    moitx = fenx/1.4
    cranx = fenx/80
    crany = feny/80
    chaine = "Normal"
    police = "Calibri"
    taille = int((cranx*1.5))
    fltk.texte(moitx, moity + crany*30 , chaine,
          police=police, taille=taille, couleur="black",
          ancrage='center')
    
    longueur, hauteur = fltk.taille_texte(chaine, police, taille)
    fltk.rectangle(moitx - longueur//2 - cranx*2,moity + crany*28 - hauteur//2,
              moitx + longueur//2 + cranx*2,moity + crany*32 + hauteur//2,
              couleur="red",  epaisseur = fenx/(fenx/2))

def bouton_Misere(fenx):
    """
    Création du bouton du mode Misère
    
    :Paramètre: Taille de fenêtre
    :Type: int
    """
    feny = fenx / (16/9)
    moity = feny/3
    moitx = fenx/1.15
    cranx = fenx/80
    crany = feny/80
    chaine = "Misere"
    police = "Calibri"
    taille = int((cranx*1.5))
    fltk.texte(moitx, moity + crany*30 , chaine,
          police=police, taille=taille, couleur="black",
          ancrage='center')
    
    longueur, hauteur = fltk.taille_texte(chaine, police, taille)
    fltk.rectangle(moitx - longueur//2 - cranx*2,moity + crany*28 - hauteur//2,
              moitx + longueur//2 + cranx*2,
              moity + crany*32 + hauteur//2,couleur="black",
              epaisseur = fenx/(fenx/2))
    
def bouton_Misereselect(fenx):
    """
    Affiche le bouton Misère séléctioné si le joueur clique dessus
    
    :Paramètre: Taille de fenêtre
    :Type: int
    """
    feny = fenx / (16/9)
    moity = feny/3
    moitx = fenx/1.15
    cranx = fenx/80
    crany = feny/80
    chaine = "Misere"
    police = "Calibri"
    taille = int((cranx*1.5))
    fltk.texte(moitx, moity + crany*30 , chaine,
          police=police, taille=taille, couleur="black",
          ancrage='center')
    
    longueur, hauteur = fltk.taille_texte(chaine, police, taille)
    fltk.rectangle(moitx - longueur//2 - cranx*2,moity + crany*28 - hauteur//2,
              moitx + longueur//2 + cranx*2,moity + crany*32 + hauteur//2,
              couleur="red",  epaisseur = fenx/(fenx/2))


def reglage_taille_fenetre(fenx):
    """
    Affiche le menu du réglage des définition dans le menu Paramètre
    :Paramètre: Taille fenêtre
    :Type: int
    """
    feny = fenx / (16/9)
    moity = feny/30
    moitx = fenx/2
    cranx = fenx/80
    crany = feny/80
    fltk.texte(moitx, moity + crany*30 , "Résolution: 1280x720",
          police="Calibri", taille= int((cranx*1.5)), couleur="black",
          ancrage='center')
        
    longueur, hauteur = fltk.taille_texte("Résolution: 1280x720", "Calibri",
                                     int((cranx*1.5)))
    fltk.rectangle(moitx - longueur//2 - cranx*2,moity + crany*28 - hauteur//2,
              moitx + longueur//2 + cranx*2,moity + crany*32 + hauteur//2,
              couleur="red",  epaisseur = fenx/(fenx/2))
    moity = feny/5
    moitx = fenx/2
    fltk.texte(moitx, moity + crany*30 , "Résolution: 1920x1080",
          police="Calibri", taille= int((cranx*1.5)), couleur="black",
          ancrage='center')

    longueur, hauteur = fltk.taille_texte("Résolution: 1920x1080", "Calibri",
                                     int((cranx*1.5)))
    fltk.rectangle(moitx - longueur//2 - cranx*2,moity + crany*28 - hauteur//2,
              moitx + longueur//2 + cranx*2,moity + crany*32 + hauteur//2,
              couleur="red",  epaisseur = fenx/(fenx/2))