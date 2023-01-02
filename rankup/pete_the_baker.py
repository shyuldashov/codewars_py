def cakes(recipe, available):
    """Calculates the maximum possible number of cakes from the available ingredients

    Args:
        recipe (dict): Dict[str, int]
        available (dict): Dict[str, int]

    Returns:
        int: number of cakes
    """

    recipe_keys = set(recipe.keys())
    available_keys = set(available.keys())

    # if the recipe is not a subset of the ingredients
    if not recipe_keys.issubset(available_keys):
        return 0

    # intersection of sets
    keys = recipe_keys & available_keys

    return min([available[key] // recipe[key] for key in keys])


if __name__ == '__main__':

    # Original Kata: https://www.codewars.com/kata/525c65e51bf619685c000059

    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

    print(cakes(recipe, available))  # 2

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    print(cakes(recipe, available))  # 0
