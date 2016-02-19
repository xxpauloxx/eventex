#!/bin/bash

# Verificando se existe o pyenv.
if ! [ -x "$(command -v pyenv)" ]; then
	curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
	source ~/.bashrc
	pyenv update
fi

# Instalando Python
pyenv install 3.5.1
pyenv local 3.5.1

# Criando Ambiente virtual.
python -m venv .wttd
source .wttd/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

./manage.py test
./manage.py runserver
