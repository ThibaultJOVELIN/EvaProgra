
import random

#Version 0

ListeDeMots = ['osekour','programmation','secourisme','naufrage','difficile','compliqué','aidezmoi','silvousplait','python','cestdur']
random.shuffle(ListeDeMots)
(ListeDeMots[1]) = PremierMot 
Mot = [PremierMots]
LettreRecherchee = input("Entrer une lettre : ")
for i in range (0,len(Mot)):
    if Mot[i] == LettreRecherchee:
        print("Cette lettre existe en position :")
        print(i + 1)


print(ListeDeMots[1])
print (Mot)
