#!/bin/bash

pipenv run python e_l_p/manage.py makemigrations

pipenv run python e_l_p/manage.py migrate

pipenv run python e_l_p/manage.py collectstatic --noinput

pipenv run python e_l_p/manage.py runserver 0.0.0.0:8000
