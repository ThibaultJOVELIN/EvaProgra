import random

from colorama import init
init()
from colorama import Fore, Back, Style

#Version 0

ListeDeMots = ListeDeMots = ['oskour','batons','helpme','ballon','castor','lardon','beurre','prison','python','besoin'] #Mots de 6 lettres.
random.shuffle(ListeDeMots)
LettreRecherchee = input("Entrer une lettre (en minuscule) : ")
for i in range (0,len(ListeDeMots[1])):         #Je prends le premier mot de la liste qui a été mélangée.
    if ((ListeDeMots[1])[i]) == LettreRecherchee:
        print("Cette lettre existe en position :")
        print(i + 1)

#Version 1

MotPropose = input("Proposer un mot de 6 lettres : ")
for i in range (0,6):
    if ((ListeDeMots[1])[i]) == MotPropose[i]:
        print (Fore.RED + (ListeDeMots[1])[i])  #Les lettres à la bonne place apparaisent en rouge, les autres n'apparaissent pas.
        
    elif ((ListeDeMots[1])[i]) != MotPropose[i]:
        print (Fore.YELLOW + (ListeDeMots[1])[i]) #Maintenant, les lettres qui ne correspondent pas sont en jaune.
    
    elif MotPropose[i] == ((ListeDeMots[1])[i + 1]) or ((ListeDeMots[1])[i + 2]) or ((ListeDeMots[1])[i + 3]) or ((ListeDeMots[1])[i + 4]) or ((ListeDeMots[1])[i + 5]):
        print (Fore.BLUE + (ListeDeMots[1])[i]) #Les lettres qui ne correspondent pas apparaissent en bleu (mais là ça marche pas)
    
    
input()