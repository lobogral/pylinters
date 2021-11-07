# pylinters

Uso de distintos linters para mejorar la calidad del código en python[^fn1].

Este paquete está diseñado para ejecutar distintos linters con características
específicas[^fn2][^fn3], los cuales son:

1. flake8.
2. pylint.
3. pydocstyle (Se utiliza la convención numpy[^fn4]).
4. mypy (Ignora librerías perdidas[^fn5]).

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


[^fn1]: https://realpython.com/python-pep8/

[^fn2]: https://realpython.com/python-code-quality/

[^fn3]: https://medium.com/@gonzaloandres.diaz/escribiendo-codigo-de-alta-calidad-en-python-parte-2-linters-64ffd8d2df91

[^fn4]: https://stackoverflow.com/questions/42123798/is-there-any-way-to-lint-a-python-file-to-check-for-numpy-documentation-style-ad

[^fn5]: https://stackoverflow.com/questions/57785471/why-does-mypy-think-library-imports-are-missing
