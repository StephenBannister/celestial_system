""" References used (move to main.py when complete):
    - Sheffield Hallam University, 2024. Micro-Lecture - Error Handling. [online] SHUspace. Available at: https://shuspace.shu.ac.uk/ultra/courses/_351506_1/outline/edit/document/_13967799_1?courseId=_351506_1&view=content.
    - Stack Overflow, 2024. Explain the setUp() and tearDown() Python methods used in test cases. [online] Available at: https://stackoverflow.com/questions/6854658/explain-the-setup-and-teardown-python-methods-used-in-test-cases
    - Python Discussion Forum, 2024. Deleting an object. [online] Available at: https://discuss.python.org/t/deleting-an-object/17299/2
"""

""" Update Notes for git commit:
    - modified assert tests to self.assertEqual to improve failure reporting
    - realised I can group tests into functions, updated to reflect this optimisation
    - changed some assert tests to CountEqual to more robustly check lists, regardless of order of elements
    - added a couple of edge case tests for empty orbiting object properties
    - Included tests to check correct relationships between objects
"""

import unittest
from celestial import CelestialBody, Star, Planet, Moon


class CelestialSystemTest(unittest.TestCase):
    def setUp(self) -> None:
        self.star = Star("Sun")
        self.earth = Planet(name="Earth", primary=self.star, mass=0.4, distance=400, rotational=10)
        self.jupiter = Planet(name="Jupiter", primary=self.star, mass=0.2, distance=200, rotational=5)
        self.the_moon = Moon(name="The Moon", primary=self.earth)
        self.io = Moon(name="Io", primary=self.jupiter)

    def tearDown(self) -> None:
        """ Releases resources that were being used by the test framework
        """
        self.star = None
        self.earth = None
        self.jupiter = None
        self.the_moon = None
        self.io = None
        

# ---------------- Test CelestialBody ------------------

    def test_celestial_name(self):
        celestial_body = CelestialBody(name="TestBody")
        self.assertEqual(celestial_body.get_name(), "TestBody", "CelestialBody is not returning the correct name.")

# ---------------- Test Star ------------------

    def test_star_name(self):
        self.assertEqual (self.star.get_name(), "Sun", "Star is not returning the correct name.")

    def test_star_add_orbiting_objects(self): 
        self.star.add_orbiting_objects([self.earth, self.jupiter])
        self.assertEqual (self.star.get_num_orbiting_objects(), 2, "Star is not returning the correct add_orbiting_objects result.")
        self.assertCountEqual (self.star.get_orbiting_objects(), [self.earth, self.jupiter], "Star is not returning the correct orbiting objects.")
        self.assertEqual (self.star.get_num_orbiting_objects(), 2, "Star is not returning the correct number of orbiting objects.")
        self.assertCountEqual (self.star.get_orbiting_object_names(), "Earth, Jupiter", "Star is not returning the correct orbiting object names.")                


# ---------------- Test Planet ------------------

    def test_planet_properties(self):
        self.assertEqual (self.earth.get_name(), "Earth", "Planet is not returning the correct name.")
        self.assertEqual (self.earth.get_mass(), 0.4, "Planet is not returning the correct mass.")
        self.assertEqual (self.earth.get_distance(), 400, "Planet is not returning the correct distance.")
        self.assertEqual (self.earth.get_rotational(), 10, "Planet is not returning the correct rotational speed.")
        self.assertEqual (self.earth.get_primary(), "Sun", "Planet is not returning the correct primary name.")

    def test_planet_add_orbiting_objects(self):
        self.earth.add_orbiting_objects([self.the_moon])
        self.assertEqual (self.earth.get_num_orbiting_objects(), 1, "Planet is not processing the correct add_orbiting_objects result.")
        self.assertCountEqual (self.earth.get_orbiting_objects(), [self.the_moon], "Planet is not returning the correct orbiting objects.")
        self.assertEqual (self.earth.get_num_orbiting_objects(), 1, "Planet is not returning the correct number of orbiting objects.")
        self.assertEqual (self.earth.get_orbiting_object_names(), "The Moon", "Planet is not returning the correct orbiting object names.")
    
# ---------------- Test Moon ------------------

    def test_moon_properties(self):
        self.assertEqual (self.io.get_name(), "Io", "Moon is not returning the correct name.")
        self.assertEqual (self.the_moon.get_name(), "The Moon", "Moon is not returning the correct name.")
        self.assertEqual (self.io.get_primary(), "Jupiter", "Moon is not returning the correct primary name.")
        self.assertEqual(self.the_moon.get_primary(), "Earth", "Moon is not returning the correct primary name.")
        
        
# ---------------- Test Object Relationships ------------------

    def test_object_relationships(self):
        self.star.add_orbiting_objects([self.earth])
        self.earth.add_orbiting_objects([self.the_moon])
        self.assertIn(self.earth, self.star.get_orbiting_objects(), "The relationship between Planet and Star is not correct")
        self.assertIn(self.the_moon, self.earth.get_orbiting_objects(), "The relationship between the Moon and Planet is not correct")
        
# ---------------- Test Edge Cases ------------------

    def test_empty_orbiting_objects(self):
        celestial_body = CelestialBody("All_alone")
        self.assertEqual(celestial_body.get_orbiting_objects(), [], "An empty orbiting objects property causes an error")
        self.assertEqual(celestial_body.get_orbiting_object_names(), "None", "An empty orbiting objects names property causes an error")
        

if __name__ == "__main__":
    unittest.main()
