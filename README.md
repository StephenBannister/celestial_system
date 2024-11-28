# celestial_system
A Python program that displays information about planets in our solar system.

For each planet the program holds details about:

    - Its name.
    - Which star it orbits.
    - Its mass.
    - Its distance from the Sun.
    - Its rotational speed.
    - A sensible list of the planet's moons.
    - A couple of facts about the planet.

All data is held using appropriate data types and is stored in JSON files. Wikipedia was used to help with values for the planets and moons.

A user can query the data through a Tkinter GUI driven menu by asking free text questions such as:

    - Tell me everything about Saturn
    - How massive is Neptune?
    - Is Pluto in the list of planets?
    - How many moons does Earth have?
    - I want to see everything

A test plan has been prepared which makes use of unittest. The file tests.py contains the automated unittests for the program. There are references in the tests.py file which indicate where the developer obtained input and information to help the creation of the unittest scenarios.

There are areas for further development which are currently being worked on. These are:

    - Improved error handling
    - Enhanced natural language processing
    - Potential code optimisation and simplification

At the beginning of main.py there is a list of references which were used in the development of this program.
