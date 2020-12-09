
#Version 0
Mot = ['O','S','E','K','O','U','R']
LettreRecherchee = input("Entrer une lettre à chercher (en majuscule)")
for i in range (0, len(Mot)):
    if (Mot[i]) == LettreRecherchee:
        print("Il y a cette lettre à la position :")
        print(i + 1)
