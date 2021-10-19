from sys import argv
from colorama import Fore, init
import os

def main():
    
    init()
    
    print(Fore.CYAN, end="")
    print("Flake8")
    print(Fore.RESET, end="")
    os.system('flake8 ' + argv[1])

    print(Fore.CYAN, end="")
    print("pylint")
    print(Fore.RESET, end="")
    os.system('pylint ' + argv[1])

    print(Fore.CYAN, end="")
    print("pydocstyle")
    print(Fore.RESET, end="")
    os.system('pydocstyle --convention=numpy ' + argv[1])

    print(Fore.CYAN, end="")
    print("mypy")
    print(Fore.RESET, end="")
    os.system('mypy --ignore-missing-imports ' + argv[1])

if __name__ == '__main__':
    exit(main())



 
