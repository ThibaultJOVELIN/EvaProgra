from colorama import init
init()
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text', end=" ")
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
print(Fore.RED + 'Normalement, je suis rouge')
input()
