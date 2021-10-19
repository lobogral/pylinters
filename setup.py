from setuptools import setup, find_packages

setup(
    name="pylinters",
    version="0.1",
    packages=find_packages(),
    install_requires = [
        'flake8',
        'pylint',
        'pydocstyle',
        'mypy',
        'colorama'
    ],
    entry_points= {
        'console_scripts': [
            'pylinters = pylinters.estandar:main',
            'pylintersnodocs = pylinters.nodocs:main'
        ]
    }
)
