# Import modules to use
import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

# Design a header for the application
header = figlet_format("DAD JOKE 3000!")
header = colored(header, color="magenta")
print(header)


# Define a function to get a dad joke from the website.
def find_a_joke():
    """Finds a joke from a website based on user input."""
    joke_topic = input("Let me tell you a joke! Give me a topic: ")

    url = "https://icanhazdadjoke.com/search"

    # Get request to url, save in variable. Search for what the user asked for. Get the json version from the api.
    response = requests.get(url, headers={"Accept": "application/json"}, params={"term": joke_topic}).json()

    # Save the total number of jokes returned on the topic searched for using the total_jokes key.
    num_jokes = response["total_jokes"]

    # Save the results key in a variable for easy use.
    results = response["results"]

    if num_jokes > 1:
        print(f"I've got {num_jokes} jokes about {joke_topic}. Here is one: ")
        # Use 'choice' to get a random joke.
        rand_joke = choice(results)["joke"]
        print(rand_joke)
    elif num_jokes == 1:
        print(f"I've got 1 joke about {joke_topic}. Here it is: ")
        # Print the 1st/only joke found.
        print(response["results"][0]["joke"])
    else:
        print(f"I don't have any jokes on {joke_topic}.")


# Call the function
find_a_joke()
