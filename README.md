# Django-Todolist

[![License][license-image]][license-url] [![Build Status][travis-image]][travis-url]

Django-Todolist is a todolist web application with the most basic features of most web apps, i.e. accounts/login, API and (somewhat) interactive UI.

---
CSS | [Skeleton](http://getskeleton.com/)
JS  | [jQuery](https://jquery.com/)

I've also build a quite similar app in Flask: https://github.com/0xfoo/flask-todolist


## Explore
Try it out by installing the requirements. (Works with Python 2 and 3.)

    pip install -r requirements.txt

Migrate:

    python manage.py migrate

And then start the server (default: http://localhost:8000)

    python manage.py runserver


Now you can browse the [API](http://localhost:8000/api/)
or start on the [landing page](http://localhost:8000/)


[license-url]: https://github.com/0xfoo/django-todolist/blob/master/LICENSE
[license-image]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat

[travis-url]: https://travis-ci.org/0xfoo/django-todolist
[travis-image]: https://travis-ci.org/0xfoo/django-todolist.svg?branch=master
