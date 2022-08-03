import fltk
import fonction

fenx = 1080
feny = fenx /(16/9)

fltk.cree_fenetre(fenx, feny, frequence=60)

fonction.Nom_du_jeux(fenx)
fltk.attente(1)
fonction.AST(fenx)
fltk.attend_ev()
fltk.efface_tout()
fonction.Nom_du_jeux_deux(fenx)
fonction.menuprin(fenx)
Play = True
Retoursel = False
Marien = False
Nim = False
Retournim = False
Parametre = True
Retour = False
Playnim = False
Normal = False
Misere = False
Resol1 = False
Resol2 = False
Choix = False
Rejouer = False
Quitte = True
Credit = True
nbalum = 21
nbcoups = 3

while True:
    ev = fltk.donne_ev()
    tev = fltk.type_ev(ev) 
    moity = feny/2
    moitx = fenx/2   
    cranx = fenx/80
    crany = feny/80    
    longpar, hautpar = fltk.taille_texte("Parametre", "Calibri", int((cranx*3)))
    longplay, hautplay = fltk.taille_texte("Jouer", "Calibri", int((cranx*3))) 
    longmarien, hautmarien  = fltk.taille_texte("Jeux de Marienbad", "Calibri", int((cranx*5))) 
    longnim, hautnim = fltk.taille_texte("Jeux de Nim", "Calibri", int((cranx*5))) 
    longret, hautret = fltk.taille_texte("Retour", "Calibri", int((cranx*5))) 
    longplaynim, hautplaynim = fltk.taille_texte("Play", "Calibri", int((cranx*5)))
    longretour, hautretour = fltk.taille_texte("Retour", "Calibri", int((cranx*1)))
    longMal, hautMal = fltk.taille_texte("Normal","Calibri",int((cranx*1.5)))
    longmis, hautmis = fltk.taille_texte("Misere","Calibri",int((cranx*1.5)))
    longresol1, hautresol1 = fltk.taille_texte("Résolution: 1280x720", "Calibri", int((cranx*1.5)))
    longresol2, hautresol2 = fltk.taille_texte("Résolution: 1920x1080", "Calibri", int((cranx*1.5)))
    longquitte, hautquitte = fltk.taille_texte("Quitter", "Calibri",int((cranx*3)))
    longcredit, hautcredit = fltk.taille_texte("Crédit","Calibri",int((cranx*3)))

    if tev == 'ClicGauche':      
        if Play :
            if moitx - longplay//2 - cranx < fltk.abscisse(ev) < moitx + longplay//2 + cranx and (feny/1.7) - crany*11 - hautplay//2< fltk.ordonnee(ev) < (feny/1.7) - crany*9 + hautplay//2:           
                fltk.efface_tout()
                fonction.fennim(fenx)
                fonction.fenmarienbad(fenx)
                fonction.retour(fenx)
                Play = False
                Retoursel = False
                Marien = True
                Nim = True
                Retournim = False
                Parametre = False
                Retour = True
                Playnim = False
                Normal = False
                Misere = False
                continue
        if Parametre :
            if moitx - longpar//2 - cranx < fltk.abscisse(ev)< moitx + longpar//2 + cranx and (feny/2.2) + crany*9 - hautpar//2 < fltk.ordonnee(ev)< (feny/2.2) + crany*11 + hautpar//2:
                fltk.efface_tout()
                fonction.reglage_taille_fenetre(fenx)
                fonction.retour(fenx)
                Play = False
                Retoursel = False
                Marien = False
                Nim = False
                Retournim = False
                Parametre = False
                Retour = True
                Playnim = False
                Normal = False
                Misere = False
                Resol1 = True
                Resol2 = True
                Choix = False
                continue
        if Resol1:
            if (fenx/2) - longresol1//2 - cranx*2 < fltk.abscisse(ev) < (fenx/2) + longresol1//2 + cranx*2 and (feny/30) + crany*28 - hautresol1//2 < fltk.ordonnee(ev) < (feny/30) + crany*32 + hautresol1//2:
                fltk.ferme_fenetre()
                fenx = 1280
                feny = fenx /(16/9)
                fltk.cree_fenetre(fenx, feny)
                fonction.reglage_taille_fenetre(fenx)
                fonction.retour(fenx)
                Resol1 = False
                Resol2 = True
                continue
        if Resol2:
            if (fenx/2) - longresol2//2 - cranx*2 < fltk.abscisse(ev) < (fenx/2) + longresol2//2 + cranx*2 and (feny/5) + crany*28 - hautresol2//2 < fltk.ordonnee(ev) < (feny/5) + crany*32 + hautresol2//2:
                fltk.ferme_fenetre()
                fenx = 1920
                feny = fenx /(16/9)
                fltk.cree_fenetre(fenx, feny)
                fonction.reglage_taille_fenetre(fenx)
                fonction.retour(fenx)
                Resol1= True
                Resol2= False
                continue    
        if Retour :
            if moitx - longret//2 - cranx*2 < fltk.abscisse(ev)< moitx + longret//2 + cranx*2 and  moity + crany*28 - hautret//2 <fltk.ordonnee(ev)<moity + crany*32 + hautret//2:
                fltk.efface_tout()
                fonction.menuprin(fenx)
                Play = True
                Retoursel = False
                Marien = False
                Nim = False
                Retournim = False
                Parametre = True
                Retour = False
                Playnim = False
                Normal = False
                Misere = False
                Resol1 = False
                Resol2 = False
                continue
        if Nim :
            if moitx - longnim//2 - cranx*2 <fltk.abscisse(ev)< moitx + longnim//2 + cranx*2 and moity - crany*12 - hautnim//2 <fltk.ordonnee(ev)< moity - crany*8 + hautnim//2:
                fltk.efface_tout()
                fonction.suitenim(fenx)
                fonction.nombre_alumette_nim(fenx)
                fonction.nombre_de_coup(fenx)
                fonction.playnim(fenx)
                fonction.bouton_Normal(fenx)
                fonction.bouton_Misere(fenx)
                fonction.retour(fenx)
                Play = False
                Retoursel = True
                Marien = False
                Nim = False
                Retournim = False
                Parametre = False
                Retour = False
                Playnim = True
                Normal = True
                Misere = True
                Choix = True
                continue
        if Credit :
            if moitx - longcredit//2 - cranx <fltk.abscisse(ev)< moitx + longcredit//2 + cranx and (feny/1.215) - crany*11 - hautcredit//2 <fltk.ordonnee(ev)< (feny/1.215) - crany*9 + hautcredit//2 :
                fltk.efface_tout()
                fonction.retour(fenx)
                Play = False
                Retoursel = True
                Marien = False
                Nim = False
                Retournim = False
                Parametre = False
                Retour = False
                Playnim = False
                Normal = False
                Misere = False
                Choix = True
                continue 
        if Choix:
            if fenx * 0.7 - fenx * 0.03 < fltk.abscisse(ev) < fenx * 0.7 + fenx * 0.03 and  2 * feny // 5.5 - fenx * 0.03 < fltk.ordonnee(ev) < 2 * feny // 5.5 + fenx * 0.03:
                if nbalum > 4:
                    nbalum -= 1
                fltk.efface("Nb_alum")
                fonction.nombre_alumette_nim(fenx,5.5,0.8,nbalum)
            if fenx * 0.9 - fenx * 0.03 < fltk.abscisse(ev) < fenx * 0.9 + fenx * 0.03 and  2 * feny // 5.5 - fenx * 0.03 < fltk.ordonnee(ev) < 2 * feny // 5.5 + fenx * 0.03:
                if nbalum < 42:
                    nbalum += 1
                fltk.efface("Nb_alum")
                fonction.nombre_alumette_nim(fenx,5.5,0.8,nbalum)
            if fenx * 0.7 - fenx * 0.03 < fltk.abscisse(ev) < fenx * 0.7 + fenx * 0.03 and  2 * feny // 3.8 - fenx * 0.03 < fltk.ordonnee(ev) < 2 * feny // 3.8 + fenx * 0.03:
                if nbcoups > 1 :
                    nbcoups -= 1
                fltk.efface("Nb_coup")
                fonction.nombre_de_coup(fenx, 3.8, 0.8, nbcoups)
            if fenx * 0.9 - fenx * 0.03 < fltk.abscisse(ev) < fenx * 0.9 + fenx * 0.03 and  2 * feny // 3.8 - fenx * 0.03 < fltk.ordonnee(ev) < 2 * feny // 3.8 + fenx * 0.03:
                if nbcoups < 10:
                    nbcoups += 1
                fltk.efface("Nb_coup")
                fonction.nombre_de_coup(fenx, 3.8, 0.8, nbcoups)    
            if (fenx/1.4) - longMal//2 - cranx*2 < fltk.abscisse(ev) < (fenx/1.4) + longMal//2 + cranx*2 and (feny/3) + crany*28 - hautMal//2 < fltk.ordonnee(ev) < (feny/3) + crany*32 + hautMal//2:
                fonction.bouton_Normalselect(fenx)
                fonction.bouton_Misere(fenx)
                Normal = True
                Misere = False      
            if (fenx/1.15) - longmis//2 - cranx*2 < fltk.abscisse(ev) < (fenx/1.15) + longmis//2 + cranx*2 and (feny/3) + crany*28 - hautmis//2 < fltk.ordonnee(ev) < (feny/3) + crany*32 + hautmis//2:
                fonction.bouton_Misereselect(fenx)
                fonction.bouton_Normal(fenx)
                Normal = False
                Misere = True
        if Playnim :
            if Normal:
                if moitx - longplaynim //2 - cranx*2 <fltk.abscisse(ev)< moitx + longplaynim//2 + cranx*2 and (feny/3.7) - crany*12 - hautplaynim//2 <fltk.ordonnee(ev)< (feny/3.7) - crany*8 + hautplaynim//2 :
                    fltk.efface_tout()
                    fonction.jeu_nim(fenx, nbalum, nbcoups)
                    Play = False
                    Retoursel = False
                    Marien = False
                    Nim = False
                    Retournim = True
                    Parametre = False
                    Retour = False
                    Playnim = False
                    Normal = True
                    Misere = False
                    Choix = False
                    continue
                if tev =='Quitte':
                    break
            if Misere:
                if moitx - longplaynim //2 - cranx*2 <fltk.abscisse(ev)< moitx + longplaynim//2 + cranx*2 and (feny/1.7) - crany*12 - hautplaynim//2 <fltk.ordonnee(ev)< (feny/1.7) - crany*8 + hautplaynim//2 :
                    fltk.efface_tout()
                    fonction.jeu_nim(fenx, nbalum, nbcoups, False)
                    fonction.retourjeu(fenx)
                    Play = False
                    Retoursel = False
                    Marien = False
                    Nim = False
                    Retournim = True
                    Parametre = False
                    Retour = False
                    Playnim = False
                    Normal = False
                    Misere = True
                    Choix = False
                    continue
        if Marien :
            if moitx - longmarien//2 - cranx*2 <fltk.abscisse(ev)< moitx + longmarien//2 + cranx*2 and moity + crany*8 - hautmarien//2 <fltk.ordonnee(ev)< moity + crany*12 + hautmarien//2:
                fltk.ferme_fenetre()
                fonction.manchemarien()
                continue
        if Retoursel :
            if moitx - longret//2 - cranx*5 <fltk.abscisse(ev) <(moitx + longret//2 + cranx*5) and  moity + crany*28 - hautret//2 <fltk.ordonnee(ev)< moity + crany*32 + hautret//2:
                fltk.efface_tout()
                fonction.menuprin(fenx)
                Play = True
                Retoursel = False
                Marien = False
                Nim = False
                Retournim = False
                Parametre = True
                Retour = False
                Playnim = False
                Normal = False
                Misere = False
                Resol1 = False
                Resol2 = False
                continue
        if Retournim :
            if (fenx/10) - longretour//2 - cranx*2 <fltk.abscisse(ev)< (fenx/10) + longretour//2 + cranx*2 and (feny/1.9) + crany*28 - longretour//2 <fltk.ordonnee(ev)< (feny/1.9) + crany*32 + longretour//2 :
                fltk.efface_tout()
                fonction.suitenim(fenx)
                fonction.nombre_alumette_nim(fenx,5.5,0.8,nbalum)
                fonction.nombre_de_coup(fenx, 3.8, 0.8, nbcoups)
                fonction.playnim(fenx)
                fonction.bouton_Normal(fenx)
                fonction.bouton_Misere(fenx)
                fonction.retour(fenx)
                Play = False
                Retoursel = True
                Marien = False
                Nim = False
                Retournim = False
                Parametre = False
                Retour = False
                Playnim = True
                Normal = True
                Misere = True
                Choix = True
                continue
        if Quitte :
            if moitx - longquitte//2 - cranx <fltk.abscisse(ev)< moitx + longquitte//2 + cranx and (feny/1.065) - crany*11 - hautquitte//2 <fltk.ordonnee(ev)< (feny/1.065) - crany*9 + hautquitte//2 :
                break
    if tev == 'Quitte':
        break
    fltk.mise_a_jour()
fltk.ferme_fenetre()