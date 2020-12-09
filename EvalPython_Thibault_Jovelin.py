import random

from colorama import init
init()
from colorama import Fore, Back, Style

#Version 0

ListeDeMots = ['osekour','programmation','secourisme','naufrage','difficile','compliqué','aidezmoi','silvousplait','python','cestdur']
random.shuffle(ListeDeMots)
LettreRecherchee = input("Entrer une lettre (en minuscule) : ")
for i in range (0,len(ListeDeMots[1])):         #Je prends le premier mot de la liste qui a été mélangée
    if ((ListeDeMots[1])[i]) == LettreRecherchee:
        print("Cette lettre existe en position :")
        print(i + 1)

#Version 1

MotPropose = [input("Proposer un mot : ")]
for i in range (0,len(ListeDeMots[1])):
    if ((ListeDeMots[1])[i]) == MotPropose[i]:
        print (Fore.RED + (ListeDeMots[1])[i]) 
