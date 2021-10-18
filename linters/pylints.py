from sys import argv
import os

def main():
    print("Flake8")
    os.system('flake8 ' + argv[1])
    print("pylint")
    os.system('pylint ' + argv[1])
    print("pydocstyle")
    os.system('pydocstyle --convention=numpy ' + argv[1])
    print("mypy")
    os.system('mypy --ignore-missing-imports ' + argv[1])

if __name__ == '__main__':
    exit(main())



 
