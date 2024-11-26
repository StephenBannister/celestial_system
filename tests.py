""" References used (move to main.py when complete):
    - Sheffield Hallam University, 2024. Micro-Lecture - Error Handling. [online] SHUspace. Available at: https://shuspace.shu.ac.uk/ultra/courses/_351506_1/outline/edit/document/_13967799_1?courseId=_351506_1&view=content.
"""

import unittest
from celestial import CelestialBody, Star, Planet, Moon


class CelestialSystemTest(unittest.TestCase):
    def setUp(self) -> None:
        self.celestial_primary = CelestialBody("primary")
        self.celestial_body = CelestialBody("celestial")
        self.star = Star("Sun")
        self.earth = Planet(name="Earth", primary=self.star, mass=0.4, distance=400, rotational=10)
        self.jupiter = Planet(name="Jupiter", primary=self.star, mass=0.2, distance=200, rotational=5)
        self.the_moon = Moon(name="The Moon", primary=self.earth)
        self.io = Moon(name="Io", primary=self.jupiter)

    def tearDown(self) -> None:
        """ Releases resources that were being used by the test framework
        """
        pass

# ---------------- Test CelestialBody ------------------

    def test_celestial_name(self) -> str:
        assert self.celestial_body.get_name(
        ) == "celestial", "CelestialBody is not returning the correct name."

# ---------------- Test Star ------------------

    def test_star_name(self) -> str:
        assert self.star.get_name() == "Sun", "Star is not returning the correct name."

    def test_star_add_orbiting_objects(self) -> None: 
        self.star.add_orbiting_objects([self.earth, self.jupiter])
        assert self.star.get_num_orbiting_objects() == 2, "Star is not returning the correct add_orbiting_objects result."

    def test_star_get_orbiting_objects(self) -> list:
        self.star.add_orbiting_objects([self.earth, self.jupiter])
        assert self.star.get_orbiting_objects() == [self.earth, self.jupiter], "Star is not returning the correct orbiting objects."
        
    def test_star_get_num_orbiting_objects(self) -> int:
        self.star.add_orbiting_objects([self.earth, self.jupiter])
        assert self.star.get_num_orbiting_objects() == 2, "Star is not returning the correct number of orbiting objects."

    def test_star_get_orbiting_object_names(self) -> str:
        self.star.add_orbiting_objects([self.earth, self.jupiter])
        assert self.star.get_orbiting_object_names() == "Earth, Jupiter", "Star is not returning the correct orbiting object names."

# ---------------- Test Planet ------------------

    def test_planet_name(self) -> str:
        assert self.earth.get_name() == "Earth", "Planet is not returning the correct name."

    def test_planet_mass(self) -> float:
        assert self.earth.get_mass() == 0.4, "Planet is not returning the correct mass."

    def test_planet_distance(self) -> float:
        assert self.earth.get_distance() == 400, "Planet is not returning the correct distance."

    def test_planet_rotational(self) -> float:
        assert self.earth.get_rotational() == 10, "Planet is not returning the correct rotational speed."

    def test_planet_primary(self) -> str:
        assert self.earth.get_primary() == "Sun", "Planet is not returning the correct primary name."

    def test_planet_add_orbiting_objects(self) -> int:
        self.earth.add_orbiting_objects([self.the_moon])
        assert self.earth.get_num_orbiting_objects() == 1, "Planet is not processing the correct add_orbiting_objects result."

    def test_planet_get_orbiting_objects(self) -> list:
        self.earth.add_orbiting_objects([self.the_moon])
        assert self.earth.get_orbiting_objects() == [self.the_moon], "Planet is not returning the correct orbiting objects."

    def test_planet_get_num_orbiting_objects(self) -> int:
        self.earth.add_orbiting_objects([self.the_moon])
        assert self.earth.get_num_orbiting_objects() == 1, "Planet is not returning the correct number of orbiting objects."

    def test_planet_get_orbiting_object_names(self) -> str:
        self.earth.add_orbiting_objects([self.the_moon])
        assert self.earth.get_orbiting_object_names() == "The Moon", "Planet is not returning the correct orbiting object names."

# ---------------- Test Moon ------------------

    def test_moon_name(self) -> str:
        assert self.io.get_name() == "Io", "Moon is not returning the correct name."

    def test_moon_primary(self) -> str:
        print("Testing Moon:Primary")
        assert self.io.get_primary() == "Jupiter", "Moon is not returning the correct primary name."

if __name__ == "__main__":
    unittest.main()
