#!/bin/bash

virtualenv --python=python3 .wttd
source .wttd/bin/activate
pip install -r requirements.txt

./manage.py test
./manage.py runserver
