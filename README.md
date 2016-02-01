# Pryvacy

#### What is this?
This is a application designed to generate class discussion and reflection on the topics of internet privacy and encryption.

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



