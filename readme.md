# Kommunity-Konsumption

It is common to dismiss food waste as someone else's problem, the phrase *"I don't waste any food"*. Though at some point you have throw away a fruit or vegetable rotting in the back of the fridge.

## What is the goal of Kommunity-Konsumption?

- Offer a platform to **track food purchased**, and use a first in first out system to minimize waste.
- Offer a platform for users to share unused/unwanted foods. **We believe the community should consume its own resources and that sharing is better than wasting.**
- Our goal is to offer a virtual fridge where people can pay low prices to acquire extra ingredients to combine with ingredients in their existing inventory and create a new recipe. 

We hope that through this platform we can decrease food waste on a **Consumer Level**.

## Required Packages

* [python3](https://www.python.org/)
* pip3
* flask
* passlib
* jsonschema
* requests
* sqlite3

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
