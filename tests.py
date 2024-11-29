""" References used (move to main.py when complete):
    - Sheffield Hallam University, 2024. Micro-Lecture - Error Handling. [online] SHUspace. Available at: https://shuspace.shu.ac.uk/ultra/courses/_351506_1/outline/edit/document/_13967799_1?courseId=_351506_1&view=content.
    - Stack Overflow, 2024. Explain the setUp() and tearDown() Python methods used in test cases. [online] Available at: https://stackoverflow.com/questions/6854658/explain-the-setup-and-teardown-python-methods-used-in-test-cases
    - Python Discussion Forum, 2024. Deleting an object. [online] Available at: https://discuss.python.org/t/deleting-an-object/17299/2
    - Python Software Foundation, 2024. unittest.mock.Mock — Mock class. [online] Available at: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
"""

''' Git commit notes:



'''

import unittest
from unittest.mock import MagicMock
from celestial import CelestialBody, Star, Planet, Moon
from system_menu import SystemMenu
from main import load_json_data


class CelestialSystemTest(unittest.TestCase):
    def setUp(self) -> None:
        self.star = Star("Sun")
        self.earth = Planet(name="Earth", primary=self.star, mass=5.97, distance=149.6, rotational=1670, f1="I have life.", f2="I have tectonic plates.")
        self.jupiter = Planet(name="Jupiter", primary=self.star, mass=1898, distance=778.5, rotational=12600, f1="I an huge.", f2="I have a giant storm.")
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

    #Test Plan Reference: Core_001
    def test_celestial_name(self):
        celestial_body = CelestialBody(name="TestBody")
        self.assertEqual(celestial_body.get_name(), "TestBody", "CelestialBody is not returning the correct name.")

# ---------------- Test Star ------------------
    #Test Plan Reference: Core_002
    def test_star_name(self):
        self.assertEqual (self.star.get_name(), "Sun", "Star is not returning the correct name.")

    #Test Plan Reference: Core_003
    def test_star_add_orbiting_objects(self): 
        self.star.add_orbiting_objects([self.earth, self.jupiter])
        self.assertCountEqual (self.star.get_orbiting_objects(), [self.earth, self.jupiter], "Star is not returning the correct orbiting objects.")
        self.assertEqual (self.star.get_num_orbiting_objects(), 2, "Star is not returning the correct number of orbiting objects.")
        self.assertCountEqual (self.star.get_orbiting_object_names(), "Earth, Jupiter", "Star is not returning the correct orbiting object names.")                


# ---------------- Test Planet ------------------
    #Test Plan Reference: Core_004
    def test_planet_properties(self):
        expected_output = (
            "My name is Earth, my mass is 5.97e+24 kg, my distance from the Sun is 149.6 million km, "
            "I rotate at 1670 m/s, I orbit Sun and I have 0 orbiting objects: None."
            "2 facts about me are: I have life. I have tectonic plates."
        )
        self.assertEqual (self.earth.get_name(), "Earth", "Planet is not returning the correct name.")
        self.assertEqual (self.earth.get_mass(), 5.97, "Planet is not returning the correct mass.")
        self.assertEqual (self.earth.get_distance(), 149.6, "Planet is not returning the correct distance.")
        self.assertEqual (self.earth.get_rotational(), 1670, "Planet is not returning the correct rotational speed.")
        self.assertEqual (self.earth.get_primary(), "Sun", "Planet is not returning the correct primary name.")
        self.assertEqual (str(self.earth), expected_output, "Planet is not returning the correct string representation")
    
    #Test Plan Reference: Core_005
    def test_planet_add_orbiting_objects(self):
        self.earth.add_orbiting_objects([self.the_moon])
        self.assertEqual (self.earth.get_num_orbiting_objects(), 1, "Planet is not processing the correct add_orbiting_objects result.")
        self.assertCountEqual (self.earth.get_orbiting_objects(), [self.the_moon], "Planet is not returning the correct orbiting objects.")
        self.assertEqual (self.earth.get_num_orbiting_objects(), 1, "Planet is not returning the correct number of orbiting objects.")
        self.assertEqual (self.earth.get_orbiting_object_names(), "The Moon", "Planet is not returning the correct orbiting object names.")
    
# ---------------- Test Moon ------------------
    #Test Plan Reference: Core_006
    def test_moon_properties(self):
        self.assertEqual (self.io.get_name(), "Io", "Moon is not returning the correct name.")
        self.assertEqual (self.the_moon.get_name(), "The Moon", "Moon is not returning the correct name.")
        self.assertEqual (self.io.get_primary(), "Jupiter", "Moon is not returning the correct primary name.")
        self.assertEqual(self.the_moon.get_primary(), "Earth", "Moon is not returning the correct primary name.")
        
        
# ---------------- Test Object Relationships ------------------
    #Test Plan Reference: Core_007
    def test_object_relationships(self):
        self.star.add_orbiting_objects([self.earth])
        self.earth.add_orbiting_objects([self.the_moon])
        self.assertIn(self.earth, self.star.get_orbiting_objects(), "The relationship between Planet and Star is not correct")
        self.assertIn(self.the_moon, self.earth.get_orbiting_objects(), "The relationship between the Moon and Planet is not correct")
        


# ---------------- Test Edge Cases ------------------

    #Test Plan Reference: Core_008
    def test_empty_orbiting_objects(self):
        celestial_body = CelestialBody("All_alone")
        self.assertEqual(celestial_body.get_orbiting_objects(), [], "An empty orbiting objects property causes an error")
        self.assertEqual(celestial_body.get_orbiting_object_names(), "None", "An empty orbiting objects names property causes an error")


       
class FileOperationsTest(unittest.TestCase):
    def setUp(self) -> None:
        pass
    
    def tearDown(self) -> None:
        """ Releases resources that were being used by the test framework
        """
        pass

# ---------------- Test JSON File Operations ------------------
    #Test Plan Reference: File_001
    def test_load_json_valid(self):
        data = load_json_data("planets.json")
        self.assertIsInstance(data, list, "List not created")
        self.assertTrue(any("Earth" in item["name"] for item in data), "JSON file not loaded correctly")

    #Test Plan Reference: File_002
    def test_load_json_invalid(self):
        with self.assertRaises(FileNotFoundError):
            load_json_data("DoesntExist.json")


class MenuSystemTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_solar_system = MagicMock()
        self.mock_solar_system.get_orbiting_object_names.return_value = "Earth, Mars, Venus, Jupiter"
        self.menu = SystemMenu(self.mock_solar_system)
        
        
    def tearDown(self) -> None:
        self.mock_solar_system = None
        self.menu = None
        
    
  # ---------------- Menu Choice NLP and Logic ------------------  
    #Test Plan Reference: Menu_001
    def test_check_menu_choice_valid_sentence_is_all_planet_info(self):
        choice, planet_choice = self.menu.determine_menu_choice("tell me about Mars")
        self.assertEqual (choice, 1)
        self.assertEqual (planet_choice, "Mars")
        
    #Test Plan Reference: Menu_002
    def test_check_menu_choice_valid_word_is_all_planet_info(self):
        choice, planet_choice = self.menu.determine_menu_choice("venus")
        self.assertEqual (choice, 1)
        self.assertEqual (planet_choice, "Venus")
        
    #Test Plan Reference: Menu_003
    def test_check_menu_choice_valid_sentence_is_planet_mass(self):
        choice, planet_choice = self.menu.determine_menu_choice("What is the mass of mars")
        self.assertEqual (choice, 2)
        self.assertEqual (planet_choice, "Mars")
        
    #Test Plan Reference: Menu_004
    def test_check_menu_choice_valid_sentence_is_planet_exists(self):
        choice, planet_choice = self.menu.determine_menu_choice("does earth exist")
        self.assertEqual (choice, 3)
        self.assertEqual (planet_choice, "Earth")
        
    #Test Plan Reference: Menu_005
    def test_check_menu_choice_valid_sentence_how_many_moons(self):
        choice, planet_choice = self.menu.determine_menu_choice("how many moons does earth have")
        self.assertEqual (choice, 4)
        self.assertEqual (planet_choice, "Earth")
        
    #Test Plan Reference: Menu_006
    def test_check_menu_choice_valid_sentence_show_all(self):
        choice, planet_choice = self.menu.determine_menu_choice("tell me everything")
        self.assertEqual (choice, 5)
        self.assertEqual (planet_choice, None)
        
    #Test Plan Reference: Menu_007  
    def test_check_menu_choice_valid_non_matched_input(self):
        choice, planet_choice = self.menu.determine_menu_choice("this is unmatched")
        self.assertIsNone(choice, None)
        self.assertIsNone(planet_choice, None)
    
   

if __name__ == "__main__":
    unittest.main()
