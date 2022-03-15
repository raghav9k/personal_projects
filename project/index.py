import json
from flask import Flask, request
from .model.recipes import Recipes
import requests


app = Flask(__name__)

@app.get("/recipes")
def get_recipes():
    response = []
    for i in Recipes.load():
        response.append(i.get("name"))
    return {"recipeNames":response}


@app.get("/recipes/details/<name>")
def get_recipe_by_name(name):
    response = {}
    recipes = list(Recipes.load())
    recipe = Recipes.get_by_name(recipes,name)
    print(recipe)
    if recipe:
        response = {
            "details": {
                "ingredients":recipe.get("ingredients"),
            "numsteps": len(recipe.get("instructions")),
            }
        }
    return response
 

@app.post("/recipes")
def add_recipe():
    new_recipe = request.get_json()
    recipes = Recipes.load()

    if Recipes.get_by_name(recipes, new_recipe.get("name")):
        return {"error":"Recipe already exists"}, 400
    else:
        recipes.append(new_recipe)
        Recipes.write(recipes)
        return '',201

@app.put("/recipes")
def update_recipe():
    data = request.get_json()
    recipes = Recipes.load()

    existing_recipe = Recipes.get_by_name(recipes, data.get("name"))
    print(existing_recipe)
    if not existing_recipe:
        return {"error":"Recipe does not exists"},404
    else:
        Recipes.update_recipe(existing_recipe,data)
        Recipes.write(recipes)
        return "",204





if __name__ == "__main__":
    app.run(debug = True)