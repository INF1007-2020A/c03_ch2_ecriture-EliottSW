#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    for lettre in mot:
        # TODO completer la fonction ici
        lettre = chr(ord(lettre) - 32)
        resultat += lettre
    return resultat


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre' ,
        'ça'
        
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)

    print(majuscule('eliott'))
