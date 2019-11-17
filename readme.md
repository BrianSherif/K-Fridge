K-Fridge
-------------
Everyone has experienced this: you go to a supermarket, make a purchase based on impulse, without even knowing if and how will you use the bought produce. Two weeks later the same product ends in your trash bin, as it expired before you could get inspired on how to use it. K-Fridge is trying to fill this gap with the simple motto: Why waste when you can share? 

#### What is the goal of K-Fridge?

- Offer a platform to **track food purchased**, and use a first in first out system that tracks expiry dates to minimize waste.
- Offer a platform that gives recipe suggestions based on foods that are in the inventory of the user.
- Offer a platform for users to share unused/unwanted foods. **We believe the community should consume its own resources and that sharing is better than wasting.**
 - Offer a community fridge where people can either deposit soon to be expired produce or pay reduced prices to acquire extra ingredients to combine with ingredients in their existing inventory and create a new recipe. 
 - Offer the K-group an opportunity to lead a circular economy for the betterment of food sustainability. 

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
