"""Utiliza varios linters para analizar código."""
import sys
import os
from colorama import Fore
from colorama import init


def colorear_titulo(titulo: str) -> None:
    """Colorea e imprime el título."""
    print(Fore.CYAN, end="")
    print(titulo)
    print(Fore.RESET, end="")


def main():
    """Método principal."""
    init()

    colorear_titulo("flake8")
    os.system('flake8 ' + sys.argv[-1])

    colorear_titulo("mypy")
    os.system('mypy --ignore-missing-imports ' + sys.argv[-1])

    if sys.argv[1] == "--no-docs":

        colorear_titulo("pylint")
        os.system('pylint --disable=missing-docstring ' + sys.argv[-1])

    else:

        colorear_titulo("pylint")
        os.system('pylint ' + sys.argv[-1])

        colorear_titulo("pydocstyle")
        os.system('pydocstyle --convention=numpy ' + sys.argv[-1])


if __name__ == '__main__':
    main()
    sys.exit()
