# Pryvacy

#### What is this?

Essentially, Pryvacy is a simple app that allows users to:
- create an account with a username and a password
- message other users
- view a feed of messages from the entire user base
- display a public PGP key as their profile
- encrypt and decrypt text using PGP keys

This is an application designed to generate class discussion and reflection on the topics of internet privacy and encryption.  I lead this activity in a seminar with about 20 teenagers.  As preparation for this unit, we watch a [video](https://youtu.be/vXr-2hwTk58) which provokes thought around technology, freedom of information, and law.  Students subsequently work with pencil-and-paper [substitution ciphers](https://en.wikipedia.org/wiki/Substitution_cipher) to help define the concepts of [encryption](https://en.wikipedia.org/wiki/Cryptography), [keys](https://en.wikipedia.org/wiki/Key_(cryptography)), and [secure channels](https://en.wikipedia.org/wiki/Secure_channel).  Through substitution ciphers, students recognize the challenges posed by symmetric algorithms.  This app, Pryvacy, introduces students to asymmetric encryption and its advantages.  It also poses an opportunity for a social experiment in the classroom.

*TODO: add substitution cipher to encryption options so that students enrolled in elective computer science can try to decode messages.*

#### Using in the classroom
This repository is ready-to-deploy on [Heroku](https://www.heroku.com/) with the [mongolab add-on](https://elements.heroku.com/addons/mongolab)

#### Requirements
- [mongoDB](http://www.mongodb.org/)
- [Python 3](https://www.python.org/)
- [pip3](https://pip.pypa.io/en/latest/installing.html)
- [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) (recommended)

#### Set up Python environment (install dependencies via pip)
```
$ cd Pryvacy
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

#### Run locally
Activate the virtual environment, if needed, and start the mongo database.
```
$ source venv/bin/activate
$ sudo mongod
$ python3 server.py
 * Running on http://0.0.0.0:5000/
```



