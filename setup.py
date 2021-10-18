from setuptools import setup, find_packages

setup(
    name="linters",
    version="0.1",
    packages=find_packages(),
    install_requires = [
        'flake8',
        'pylint',
        'pydocstyle',
        'mypy'
    ],
    entry_points= {
        'console_scripts': [
            'pylints = linters.pylints:main',
            'pylintsnodocs = linters.pylintsnodocs:main'
        ]
    }
)
