from fltk import *
from fonction import *

feny = 1000
fenx = feny * (16/9)
cree_fenetre(fenx,feny,frequence = 60)
cases(fenx)
j = 0
nb = 10
reste = 0
base = 21
alum = base
coup = 0

while True:
    efface_tout()
    alumettemodif(fenx, base, alum)
    imprim(fenx, alum)
    cases(fenx, nb)
    coup = 0

    ev = attend_ev()
    tev = type_ev(ev)
    if nb > 5 :
        reste = nb - 5
        nb = nb - reste

    if tev == 'ClicGauche':
        for i in range (1, nb + 1):
            if fenx * 0.8 - fenx * 0.03 < abscisse(ev) < fenx * 0.8 + fenx * 0.03 and  i * 2 * feny // 13 - fenx * 0.03 < ordonnee(ev) <  i * 2 * feny // 13 + fenx * 0.03:
                coup = i
                j += 1
        if reste > 0 : 
            nb = nb + reste
        for i in range (1 , nb - 4):
            if fenx * 0.9 - fenx * 0.03 < abscisse(ev) < fenx * 0.9 + fenx * 0.03 and  i * 2 * feny // 13 - fenx * 0.03 < ordonnee(ev) <  i * 2 * feny // 13 + fenx * 0.03:
                coup = i + 5
                j += 1
    if alum - coup >= 0 :
        alum = alum - coup
    if alum == 0:
        efface_tout()
        alumettemodif(fenx, base, alum)
        gagnant = str (1 + j % 2)
        chaine = "Le joueur " + gagnant +" gagne !"
        texte (fenx / 2, feny / 2,chaine = chaine, taille =int( fenx // 20), ancrage="center")
        attend_ev()
        alum = base
        j = 0
    if tev == 'Quitte':
        break   
    mise_a_jour() 