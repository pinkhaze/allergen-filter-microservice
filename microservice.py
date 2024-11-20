import time


def parse_recipes(filename):
    """
    Parses recipes from a text file into a list of tuples.

    Args: 
        filename (str): Name of the file containing recipes, located in the current directory.

    Returns: 
        list of tuples: 
            - str: Recipe name.
            - list of str: Allergen tags (lowercase).
    """
    recipes = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line or ";" not in line:
                continue
            name, tags = line.split(";")
            name = name.strip()
            tag_list = tags.split(",")
            processed_tags = []
            for tag in tag_list:
                processed_tags.append(tag.strip().lower())
            tag_list = processed_tags
            recipes.append((name, tag_list))
    return recipes


def filter_recipes(recipes, allergens):
    """
    Fitlers out recipes that contain any of the specified allergens.

    Args:
        recipes (list of tuples): Each tuple contains a recipe name and its associated allergen tags.
        allergens (list of str): Allergen tags to filter out.

    Returns:
        list of str: Recipe names that do not contain any of the specified allergens.
    """
    filtered_recipes = []
    for name, tags in recipes:
        contains_allergen = any(allergen in tags for allergen in allergens)
        if not contains_allergen:
            free_from_tags = [f"{allergen}-free" for allergen in allergens]
            free_from_summary = ", ".join(free_from_tags)
            filtered_recipes.append(
                f"Recipe Name: {name}\nTags: {free_from_summary}")
    return filtered_recipes


def process_allergen_request():
    """
    Processes allergen requests by reading from 'allergen_request.txt', filtering recipes 
    from 'recipes.txt' and writing the filtered recipes to 'filtered_recipes.txt'.

    Args:
        None

    Returns: 
        None
    """
    try:
        with open("allergen_request.txt", "r") as file:
            unprocessed_allergens = file.read().split(",")

        allergens = []
        for allergen in unprocessed_allergens:
            processed_allergen = allergen.strip().lower()
            allergens.append(processed_allergen)

        print(f"Processing the request for the following allergens: {
              allergens}")

        recipes = parse_recipes("recipes.txt")
        filtered_recipes = filter_recipes(recipes, allergens)

        with open("filtered_recipes.txt", "w") as file:
            for recipe in filtered_recipes:
                file.write(f"{recipe}\n")
        print("Your filtered recipes were written to filtered_recipes.txt")

    except FileNotFoundError:
        print("Request file not found.")


def main():
    """
    Main program to continuously process allergen filter requests.
    """
    while True:
        process_allergen_request()
        print("Waiting for the next request...")

        time.sleep(10)


if __name__ == "__main__":
    main()
