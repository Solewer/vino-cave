# vinocave
L'application de gestion de cave en Django

## Installation des prérequis
### Virtualenv
* [Sous Windows](https://pymote.readthedocs.io/en/latest/install/windows_virtualenv.html)
* [Sous Linux](https://virtualenv.pypa.io/en/stable/installation/)



## Comment on en est-on arrivé là ?
Étapes pour recréer un projet à partir de zéro, pas nécessaires, sauf pour recommencer.

```
$ virtualenv env
$ . env/bin/activate
(env)$ pip install django
(env)$ django-admin startproject vinocave
(env)$ cd vinocave
(env)$ python manage.py startapp core
```
