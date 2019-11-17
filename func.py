import requests
import json

def parseJson(data):
    """ Parsing a JSON string to dictionary
    Returns a dictionary
    """
    return (json.loads(data))

def getRecipes(ingridList):
    """ An API call to find recipes with a given set of ingridients
    Returns a dictionary
    """
    ingridients = ",".join(ingridList)

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

    # number = max nr of recipes response
    # ranking = (1) prioritize using more already owned products, (2) prioritize less missing ingridients
    # ignorePantry = whether to ignore pantry ingredients such as water, salt, flour etc.
    querystring = {"number":"3","ranking":"1","ignorePantry":"true","ingredients": ingridients}

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "7d34f06ddbmshb7ffd6947fe2f04p1ba4a8jsn9ed18d4c415a"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return parseJson(response.text)

def getRandRecipes():
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByNutrients"

    querystring = {"number":"3","maxCalories":"250"}

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "7d34f06ddbmshb7ffd6947fe2f04p1ba4a8jsn9ed18d4c415a"
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
        'x-rapidapi-key': "7d34f06ddbmshb7ffd6947fe2f04p1ba4a8jsn9ed18d4c415a"
        }

    response = requests.request("GET", url, headers=headers)

    return parseJson(response.text)