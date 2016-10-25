<<<<<<< HEAD
Django Hackathon Starter
------------------------

A boilerplate application for Django web applications.

If you've attented hackathons, you already know how much time can be wasted figuring out what language to pick, which web framework to choose. Django Hackathon Starter aims to provide these features out of the box, allowing the team to save hours of time getting these pieces together.

Even if you are not using this for a hackathon, Django Hackathon Starter is sure to save any developer hours or even days of development time and can serve as a learning guide for web developers.

Table of Contents
-----------------

- [Features](#features)
- [Pre-requisites](#pre-requisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

Features
--------
* User Registration
* Sphinx Documentation
* Django Nosetests
* Integration with Django Rest Framework
* Basic Authentication with username and password

<hr>


Pre-requisites
--------------

This project relies on `bower` for front-end dependencies, which in turn requires [npm](https://www.npmjs.com/). `npm` is now bundled with `NodeJS`, which you can download and install [here](https://nodejs.org/download/).

For Python-specific libraries, this project relies on [pip](https://pypi.python.org/pypi/pip). The easiest way to install `pip` can be [found here](https://pip.pypa.io/en/latest/installing.html).

Getting Started
---------------
To get up and running, simply do the following:

    $ git clone https://github.com/DrkSephy/django-hackathon-starter.git
    $ cd django-hackathon-starter

    # Install the requirements
    $ pip install -r requirements.txt

    # Install bower
    $ npm install -g bower
    $ bower install

    # Perform database migrations
    $ python manage.py makemigrations
    $ python manage.py migrate


**NOTE**: We highly recommend creating a [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/). Python Virtual Environments allow developers to work in isolated sandboxes and to create separation between python packages installed via [pip](https://pypi.python.org/pypi/pip).
=======
# django-starter
A template for django projects built with user auth. and minimal model data. Originally for a capital one hackathon application
>>>>>>> a0dcb8bf0973cef590e507b92c429240ce42385c
