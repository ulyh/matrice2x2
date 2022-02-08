#-------------------------------------------------------------------------------
# Name:        module1
# Author:      h
# Created:     26/05/2021
#-------------------------------------------------------------------------------
# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter.font import BOLD
import numpy as np


#--- Programme principal -------------------------------------------------------
def determinant(tab):
    """ Retourne le déterminant d'une matrice 2x2(liste)"""
    if len(tab) == 2 and len(tab[0]) == 2:
        det = tab[0][0] * tab[1][1] - tab[1][0] * tab[0][1]
    else:
        det = 0

    return det

def inverse_matrice(tab):
    """Retourne l'inverse de la matrice 2x2 (array) """
    d = determinant(tab)
    if determinant(tab) != 0:
        # Transposition des valeurs
        tmp = tab[0][0]
        tab[0][0] = tab [1][1]
        tab[1][1] = tmp

        #
        tab[0][1] *= -1
        tab[1][0] *= -1

        mati = []
        for ligne in tab:
            matj = []
            for element in ligne:
                coordonnee = element*(1/d)
                if coordonnee == int(coordonnee):
                    matj.append(int(coordonnee))
                else:
                    matj.append(round(coordonnee, 2))

            mati.append(matj)
        return mati
    else:
        return "opération impossible"

def calcul():

    # définir les variables globales
    global textA, textB, textdet

    matA = textA.get("0.0", "end")      # récupère une chaîne de caractères
    textB.delete("0.0", "end")          # efface l'entrée B
    textdet.delete("0.0", "end")


    matA = matA.split()             # filtre la case vide du str

    for index, i in enumerate(matA):
        matA[index] = int(i)        # convertir str en int

    # saisie récupérée dans une liste de listes
    lA = []
    for i, a in enumerate(matA):
        if i % 2 == 0:
            slA = []
            slA.append(a)
        else:
            slA0.append(a)
            lA.append(slA0)
        slA0 = slA

    # donne la dimension de la matrice
    matriceA = np.array(lA)             # transforme la liste de listes en array
                                          # .shape seulement pour array

    # calcul de l'inverse A^-1
    invA = inverse_matrice(matriceA)

    # A^-1 convertie en str
    str_invA = str(invA)

    # nettoyage de la chaîne de caractères
    str_invA = str_invA.replace("], [", "\n")       # indice Gilles

    for i in range(5):
        str_invA = str_invA.replace("[[,]]"[i], "")

    # affichage en front de A^-1
    textB.insert("0.0", str_invA)

    # colcul du déterminant de la matrice A
    det = determinant(matriceA)

    # affichage du déterminant
    textdet.insert("0.0", det)

def main():
    fenetre = Tk()
    fenetre.geometry("470x200")
    fenetre.title("Inversion matricielle de dimension 2")
    fenetre.config(bg='blanched almond')

    global textA, textB, textdet

    # libellé
    titre_label = Label(fenetre, text="Calcul de la matrice inverse de A", bg='blanched almond', fg='royal blue', font=('Arial', 13, BOLD))
    textA_label = Label(fenetre, text="A =", fg="blue", bg='blanched almond')
    parentheseA = Label(fenetre, text="", fg="blue", bg='blanched almond')
    textB_label = Label(fenetre, text="B =", fg="blue", bg='blanched almond')
    parentheseB = Label(fenetre, text="", fg="blue", bg='blanched almond')

    textdet_label = Label(fenetre, text="det = ", fg="blue", bg='blanched almond')

    # Saisie matrice A
    textA = Text(fenetre, width=9, heigh=3, bg="blanched almond", font=(None, 17))
    textB = Text(fenetre, width=9, heigh=3, bg="blanched almond", font=(None, 17))
    textdet = Text(fenetre, width=3, heigh=2, bg="royal blue", font=(None, 17))

    # Bouton calcul
    bt_resultat = Button(fenetre, text="résultat", fg="red", command=calcul)

    # placement avec grid()
    titre_label.grid(row=0,column=0, columnspan=5)

    textA_label.grid(row=1, column=0)
    textA.grid(row=1,column=1)
    parentheseA.grid(row=1,column=2)

    textB_label.grid(row=1, column=3)
    textB.grid(row=1,column=4)
    parentheseB.grid(row=1,column=5)

    textdet_label.grid(row=1,column=6)
    textdet.grid(row=1, column=7)

    bt_resultat.grid(row=3, rowspan=2, column=4)

    fenetre.mainloop()


if __name__ == '__main__':
    main()