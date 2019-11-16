# Kommunity-Konsumption

## Required Packages

* [python3](https://www.python.org/)
* pip3
* flask
* sqlalchemy
* passlib
* jsonschema

## Set up build environment

First get the virtualenv package in order to set up a development environment:

```bash
$ pip3 install virtualenv
```

Set up and activate a virtual development environment:

```bash
$ virtualenv -p python3 venv
$ cd venv
$ source bin/activate
```

Install the required packages:

```bash
$ pip3 install -r requirements.txt
```

## Running the application

To run the application locally enter the following in your terminal:

```bash
$ python3 app.py
```
The app should be runnning on your local host on port 5000.
