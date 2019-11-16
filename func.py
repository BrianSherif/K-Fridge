import requests
# from db.__init__ import *

# Django

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

def findRecipe(ingridList):
    ingridients = ",".join(ingridList)

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

    # number = max nr of recipes response
    # ranking = (1) prioritize using more already owned products, (2) prioritize less missing ingridients
    # ignorePantry = whether to ignore pantry ingredients such as water, salt, flour etc.
    querystring = {"number":"5","ranking":"1","ignorePantry":"true","ingredients": ingridients}

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "cd8ff82fb4mshe8e538f653b408ap180430jsn5032ccaa46c4"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

def getRecipeDesc(id):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/" + str(id) + "/information"

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "cd8ff82fb4mshe8e538f653b408ap180430jsn5032ccaa46c4"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)