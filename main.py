"""
This script is used to model a basic solar system with stars, planets, and moons. It includes
functions for creating celestial objects from JSON files, and a main menu to interact
with the solar system model.

Key references used in the coding of this application:
    - https://realpython.com/videos/composition/
    - https://realpython.com/videos/inheritance-python/
    - https://www.geeksforgeeks.org/python-super/
    - https://docs.python.org/3/library/unittest.html
    - https://docs.python.org/3/library/unittest.mock.html
    - https://stackoverflow.com/questions/20199126/reading-json-from-a-file
    - https://peps.python.org/pep-0257/
    - https://peps.python.org/pep-3107/
    - https://stackoverflow.com/questions/10017776/where-can-i-find-proper-examples-of-the-pep-257-docstring-conventions
    - https://stackoverflow.com/questions/17466561/what-is-the-best-way-to-structure-a-tkinter-application
    - https://docs.python.org/3/library/tkinter.ttk.html#using-ttk
    - https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
    - https://www.reddit.com/r/learnpython/comments/urh4st/in_tkinter_is_it_ok_to_add_rootmainloop_at_the/
    - https://stackoverflow.com/questions/2260235/how-to-clear-the-entry-widget-after-a-button-is-pressed-in-tkinter
"""

from typing import Any
import json
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
    with open(filename, "r") as file:
        return json.load(file)


# ------------------- Solar System Creation ----------------


def create_planets(s: Star) -> None:
    """
    Create planet objects from JSON data and add them to the solar system.

    Args:
        s (Star): The star object representing the solar system.
    """
    planet_data = load_json_data("planets.json")
    planets = [Planet(s, name=item["name"], mass=item["mass"], distance=item["distance"],
                      rotational=item['rotational'], f1=item["fact1"], f2=item["fact2"],) for item in planet_data]
    s.add_orbiting_objects(planets)


def create_moons(s: Star) -> None:
    """
    Create moon objects from JSON data and associate them with their respective planets.

    Args:
        s (Star): The star object representing the solar system.
    """
    moon_data = load_json_data("moons.json")
    for planet in s.get_orbiting_objects():
        moon_names = moon_data.get(planet.get_name(), [])
        planet.add_orbiting_objects([Moon(name, planet)
                                    for name in moon_names])


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
    star_name = "Sol"
    s = create_system(star_name)

    app = SystemMenu(s)
    app.run()


if __name__ == "__main__":
    main()
