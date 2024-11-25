"""
This is the main script used to model a basic solar system with stars, planets, and moons. It includes
functions for creating celestial objects from JSON files, and a main menu to interact
with the solar system model.

Key references used in the coding of this application:
    - Gray, D (2023), Python Tutorial for Beginners (with mini-projects), free CodeCamp. https://youtu.be/qwAFL1597eM?si=1DQAWVE6F4FlF4zc
    - Spronk, P. (2023), The Coder's Apprentice. https://www.spronck.net/pythonbook/
    - Downey, A. (2012), Think Python: How to Think Like a Computer Scientist: Learning with Python 3, Greentea Press. http://www.thinkpython.com
    - Real Python, 2024. Composition in Python. [online video] Available at: https://realpython.com/videos/composition/
    - Real Python, 2024. Inheritance in Python. [online video] Available at: https://realpython.com/videos/inheritance-python/
    - GeeksforGeeks, 2024. Python super(). [online] Available at: https://www.geeksforgeeks.org/python-super/
    - Python Software Foundation, 2024. unittest — Unit testing framework. [online] Available at: https://docs.python.org/3/library/unittest.html
    - Python Software Foundation, 2024. unittest.mock — mock object library. [online] Available at: https://docs.python.org/3/library/unittest.mock.html
    - Stack Overflow, 2024. Reading JSON from a file. [online] Available at: https://stackoverflow.com/questions/20199126/reading-json-from-a-file
    - W3Schools, 2024. Python JSON. [online] Available at: https://www.w3schools.com/python/python_json.asp
    - GeeksforGeeks, 2024. Read JSON file using Python. [online] Available at: https://www.geeksforgeeks.org/read-json-file-using-python/
    - Python Software Foundation, 2024. PEP 257 — Docstring Conventions. [online] Available at: https://peps.python.org/pep-0257/
    - Python Software Foundation, 2024. PEP 3107 — Function Annotations. [online] Available at: https://peps.python.org/pep-3107/
    - Stack Overflow, 2024. Where can I find proper examples of the PEP 257 docstring conventions?. [online] Available at: https://stackoverflow.com/questions/10017776/where-can-i-find-proper-examples-of-the-pep-257-docstring-conventions
    - Stack Overflow, 2024. What is the best way to structure a Tkinter application?. [online] Available at: https://stackoverflow.com/questions/17466561/what-is-the-best-way-to-structure-a-tkinter-application
    - Python Software Foundation, 2024. Using ttk. [online] Available at: https://docs.python.org/3/library/tkinter.ttk.html#using-ttk
    - Stack Overflow, 2024. How to pass arguments to a button command in Tkinter?. [online] Available at: https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
    - Reddit, 2024. In Tkinter, is it OK to add root.mainloop() at the end of a class?. [online] Available at: https://www.reddit.com/r/learnpython/comments/urh4st/in_tkinter_is_it_ok_to_add_rootmainloop_at_the/
    - Stack Overflow, 2024. How to clear the Entry widget after a button is pressed in Tkinter?. [online] Available at: https://stackoverflow.com/questions/2260235/how-to-clear-the-entry-widget-after-a-button-is-pressed-in-tkinter
    - W3Schools, 2024. Python Exceptions. [online] Available at: https://www.w3schools.com/python/python_ref_exceptions.asp
    - GeeksforGeeks, 2024. JSON parsing errors in Python. [online] Available at: https://www.geeksforgeeks.org/json-parsing-errors-in-python/
    - Python Software Foundation, 2024. logging — Logging facility for Python. [online] Available at: https://docs.python.org/3/library/logging.html
    
"""

import sys, json, logging
from typing import Any
from celestial import Star, Planet, Moon
from system_menu import SystemMenu

# ------------------- Helper Functions ----------------


def load_json_data(filename: str) -> Any:
    """
    Load data from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        Any: The parsed JSON data.
    """

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError as e:
        logging.error(f"The file '{filename}' was not found.")
        raise e
    except json.JSONDecodeError as e:
        logging.error(f"The file '{filename}' does not contain valid JSON.")
        raise e
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise e    


# ------------------- Solar System Creation ----------------


def create_planets(s: Star) -> None:
    """
    Create planet objects from JSON data and add them to the solar system.

    Args:
        s (Star): The star object representing the solar system.
    """
    try:
        filename = "planets.json"
        planet_data = load_json_data(filename)
        planets = [Planet(s, name=item["name"], mass=item["mass"], distance=item["distance"],
                        rotational=item['rotational'], f1=item["fact1"], f2=item["fact2"],) for item in planet_data]
        s.add_orbiting_objects(planets)
    except (KeyError, TypeError) as e:
        logging.error(f"Error in {filename} data structure: {e}")
        raise ValueError(f"Invalid planet in data structure in {filename}")
    except Exception as e:
        logging.error(f"Failed to create planets {e}")
        raise
                 

def create_moons(s: Star) -> None:
    """
    Create moon objects from JSON data and associate them with their respective planets.

    Args:
        s (Star): The star object representing the solar system.
    """
    try:
        filename = "moons.json"
        moon_data = load_json_data(filename)
        for planet in s.get_orbiting_objects():
                moon_names = moon_data.get(planet.get_name(), [])
                planet.add_orbiting_objects([Moon(name, planet)
                                        for name in moon_names])
    except (KeyError, TypeError) as e:
        logging.error(f"Error in {filename} data structure: {e}")
        raise ValueError(f"Invalid moon in data structure in {filename}")
    except Exception as e:
        logging.error(f"Failed to create moons {e}")
        raise

def create_system(star_name: str) -> Star:
    """
    Instantiate the star, planets, and moons for the solar system.

    Args:
        star_name (str): The name of the star in the solar system.

    Returns:
        Star: The star object representing the solar system.
    """

    s = Star(name=star_name)
    create_planets(s)
    create_moons(s)
    return s

# ------------------- Main ----------------


def main() -> None:
    """
    Initialize the solar system and run the application menu.
    """
    
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        star_name = "Sol"
        s = create_system(star_name)
        logging.info("Solar system created successfully")
    except Exception as e:
        logging.critical(f"Critical error {e}")
        sys.exit(1)
        
    app = SystemMenu(s)
    app.run()

        

if __name__ == "__main__":
    main()
