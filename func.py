import requests
import json

def parseJson(data):
    """ Parsing a JSON string to dictionary
    Returns a dictionary
    """
    return (json.loads(data))

def findRecipe(ingridList):
    """ An API call to find recipes with a given set of ingridients
    Returns a dictionary
    """
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

    return parseJson(response.text)

def getRecipeDesc(id):
    """ An API call to get the chosen recipe's description
    Returns a dictionary
    """
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/" + str(id) + "/information"

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "cd8ff82fb4mshe8e538f653b408ap180430jsn5032ccaa46c4"
        }

    response = requests.request("GET", url, headers=headers)

    return parseJson(response.text)