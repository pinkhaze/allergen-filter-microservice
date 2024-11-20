# **Allergen Filtering Microservice**

[![License](https://img.shields.io/badge/License-MIT-orange.svg)](https://choosealicense.com/licenses/mit/)

## **Description**

The Allergen Filtering Microservice filters recipes based on an allergen or allergens specified by the user. The microservice communicates with the main program via text files. Recipes and allergen tags are read from `recipes.txt`, allergen requests are sent via `allergen_request.txt`, and the filtered recipes are written to `filtered_recipes.txt`.

The application has the following features:
- **Input Recipes:** Processes recipes stored in `recipes.txt` with associated allergens.
- **Allergen Requests:** Reads allergen exclusions from `allergen_request.txt`.
- **Filtered Output:** Outputs a list of safe recipes to `filtered_recipes.txt`.
- **File-Based Communication:** Enables interaction between the main program and the microservice.

---

## **Table of Contents**
- [Installation](#installation)
- [Usage](#usage)
- [Request Data from Microservice](#request-data)
- [Receive Data from Microservice](#received-data)
- [UML Sequence Diagram](#uml-sequence-diagram)

---

## **Installation**

1. Download the allergen-filtering-microservice.zip file from  the [repository](git@github.com:pinkhaze/allergen-filter-microservice.git).
2. Extract the ZIP file to a directory on your local machine.
3. Move the microservice.py file to your root directory where your main program is located.
4. If Python is not already installed on your system, download it from [Python.org](https://www.python.org).

---

## **Usage**

### Setting Up Recipes
Place the recipes.txt file in your root directory. Ensure it follows the following format: 

```bash
    Spaghetti; Dairy, Gluten
    Caesar Salad; Dairy
    Peanut Butter Cookies; Dairy, Gluten, Nuts
``` 

> **Key Points**
> * Recipe name: 
>   * Comes before the semicolon (;)
> * Allergen(s): 
>   * A list of comma-separated allergens after the semicolon.
>   * The list is not case-sensitive (e.g. Nuts, nuts, NUTS)
> * Uniformity:
>   * Make sure the allergens listed in `recipes.txt` match those used in ` allergen_request.txt`.
>
> The `allergen_request.txt` and `filtered_recipes.txt` files do not need to be created beforehand. 

### Running the Microservice

__Start the Microservice:__ Run the microservie to monitor `allergen_request.txt` for new allergen requests.

```sh
    python microservice.py
```

__Send a Request:__ Run the test-program to send an allergen request by writing an allergen or allergens to `allergen_request.txt`.

```bash
    python test-program.py
```

Example allergen request
```bash
    nuts, dairy
``` 

__Processing:__ The microservice reads `allergen_request.txt`, processes the recipes and allergen tags in `recipes.txt` and filters out any recipes that contain those allergens.

Example input file for recipes and their allergen tags:
```bash
    Fried Rice; Soy, Nuts
    Caesar Salad: Dairy
    Spaghetti and Meatballs: Gluten
```

After filtering, the microservice writes the filtered recipes to `filtered_recipes.txt`. 

Example output file for filtered recipes:
```bash
    Spaghetti and Meatballs
```

---

## Example Call for Requesting Data from Microservice
```bash
    with open("allergen_request.txt", "w") as file:
        file.write("gluten, dairy")
``` 
---
## Example Call for Receiving Data from Microservice 

```bash
    if os.path.exists("filtered_recipes.txt"):
    with open("filtered_recipes.txt", "r") as file:
        response = file.read()
        print("Filtered Recipes:")
        print(response)
``` 
---

## **UML Sequence Diagram**

![Screenshot from 2024-11-19 21-44-49](https://github.com/user-attachments/assets/ed2babbf-7ff2-4286-a3c6-60660f2fdcfc)

---