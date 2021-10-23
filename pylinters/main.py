"""Utiliza varios linters para analizar codigo."""
import sys
import os
from colorama import Fore
from colorama import init


def main():
    """Metodo principal."""
    init()

    print(Fore.CYAN, end="")
    print("flake8")
    print(Fore.RESET, end="")
    os.system('flake8 ' + sys.argv[-1])

    print(Fore.CYAN, end="")
    print("mypy")
    print(Fore.RESET, end="")
    os.system('mypy --ignore-missing-imports ' + sys.argv[-1])

    if sys.argv[1] == "--no-docs":

        print(Fore.CYAN, end="")
        print("pylint")
        print(Fore.RESET, end="")
        os.system('pylint --disable=missing-docstring ' + sys.argv[-1])

    else:

        print(Fore.CYAN, end="")
        print("pylint")
        print(Fore.RESET, end="")
        os.system('pylint ' + sys.argv[-1])

        print(Fore.CYAN, end="")
        print("pydocstyle")
        print(Fore.RESET, end="")
        os.system('pydocstyle --convention=numpy ' + sys.argv[-1])


if __name__ == '__main__':
    main()
    sys.exit()
