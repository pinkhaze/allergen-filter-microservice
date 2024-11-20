import time
import os


def write_allergen_request(allergens):
    """
    Writes allergen request to allergen_request.txt.

    Args:
        allergens (str): Comma-separated allergen tags to exclude from filtered_recipes.txt.
    """
    with open("allergen_request.txt", "w+") as file:
        file.write(allergens)
        print("Your allergen request has been sent to the microservice.")


def process_microservice_output():
    """
    Checks if the microservice has responded and reads the filtered recipes.

    Args: 
        None

    Returns:
        str: Filtered recipes if available, or an error message if not
    """
    if os.path.exists("filtered_recipes.txt"):
        with open("filtered_recipes.txt", "r") as file:
            return file.read()
    else:
        return "Error: Received no response from the microservice."


def main():
    """
    Main program to handle allergen filtering requests by interacting with the microservice.
    """
    while True:
        allergen_tags = "dairy"
        write_allergen_request(allergen_tags)

        print("Waiting for the microservice to process your request...")
        time.sleep(10)

        try:
            response = process_microservice_output()
            print("Here are your filtered recipes:")
            print(response)
        except FileNotFoundError:
            print(
                "Error: The filtered_recipes.txt file was not found. Ensure the microservice is running.")
        break


if __name__ == "__main__":
    main()
