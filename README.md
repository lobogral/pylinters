# pylinters

Uso de distintos linters para mejorar la calidad del código en python.

Este paquete está diseñado para ejecutar distintos linters con características
específicas, los cuales son:

1. flake8
2. pylint
3. pydocstyle (Se utiliza la convención numpy)
4. mypy (Ignora librerías perdidas)

## Instalación

Para instalar la versión más reciente de ``pylinters`` usando pip:

1. Descargar el archivo .tar.gz mediante el siguiente [link](https://github.com/lobogral/pylinters/releases/latest/download/pylinters.tar.gz).

2. Ejecutar el comando:

        $ pip install pylinters.tar.gz

Si se desea instalar para desarrollo, ejecutar lo siguiente:

    $ git clone https://github.com/lobogral/pylinters.git
    $ cd pylinters
    $ pip install -e .

## Ejecución

Existen 2 formas de ejecutar el código:

1. Estándar, útil para revisar código de paquetes, utiliza flake8, pylint, pydocstyle, mypy.

        $ pylinters codigo.py
    
2. No documentación, útil para revisar códigos simples, utiliza flake8, pylint, mypy.

        $ pylinters --no-docs codigo.py
