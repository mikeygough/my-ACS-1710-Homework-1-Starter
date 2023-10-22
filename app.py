from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/")
def homepage():
    """Shows a greeting to the user."""
    return "Are you there, world? It's me, Ducky!"


@app.route("/animal/<users_animal>")
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f"Wow, {users_animal} is my favorite animal, too!"


@app.route("/dessert/<users_dessert>")
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f"How did you know I liked {users_dessert}?"


@app.route("/madlibs/<adjective>/<noun>")
def madlibs(adjective, noun):
    """Display a madlib to the user that changes based on their inputted adjective and noun."""
    return f"The {adjective} cow jumped over the {noun}!"


@app.route("/multiply/<number1>/<number2>")
def multiply(number1, number2):
    """Display the product of number1 and number2."""
    # check valid types
    try:
        number1 = float(number1)
        number2 = float(number2)
    except:
        return "Invalid inputs. Please try again by entering 2 numbers!"
    return f"{number1} times {number2} is {number1 * number2}"


@app.route("/sayntimes/<word>/<n>")
def sayntimes(word, n):
    """Display word repeated n number of times."""
    # check valid type
    try:
        n = int(n)
    except:
        return "Invalid input. Please try again by entering a word and a number!"
    return f"{(word + ' ') * n}"


@app.route("/dicegame")
def dicegame():
    """Display a random number between 1 and 6 (inclusive). Display a winning message if 6, else display a losing message"""
    if randint(1, 6) == 6:
        return "You rolled a 6. You won!"
    else:
        return "You rolled a 2. You lost!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
