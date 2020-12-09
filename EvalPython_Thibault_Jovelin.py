
import random

#Version 0

ListeDeMots = ['osekour','programmation','secourisme','naufrage','difficile','compliqué','aidezmoi','silvousplait','python','cestdur'] #Liste de mots de plus de 6 lettres
random.shuffle(ListeDeMots)
print(ListeDeMots[1])
LettreRecherchee = input("Entrer une lettre : ")
for i in range (0,len(ListeDeMots[1])):
    if ((ListeDeMots[1])[i]) == LettreRecherchee:
        print("Cette lettre existe en position :")
        print(i + 1)
