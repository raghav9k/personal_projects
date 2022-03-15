import json


class Recipes:
    JSON_file = "model/data.json"


    @classmethod
    def load(cls):
        with open(cls.JSON_file,"r") as recipes:
            return json.load(recipes).get("recipes",[])
    
    @classmethod
    def write(cls, recipes: list):
        with open(cls.JSON_file,"w") as recipeFile:
            json.dump({"recipes":recipes}, recipeFile, indent=4)


    @classmethod
    def get_by_name(cls, recipes: list, name: str):
        return next(filter(lambda rec: rec.get("name")==name, recipes), None)

            
    @classmethod
    def update_recipe(cls,recipe: dict,data:dict):
        for k,v in data.items():
            recipe[k] = v