""" References used (move to main.py when complete):
    - Sheffield Hallam University, 2024. Micro-Lecture - Error Handling. [online] SHUspace. Available at: https://shuspace.shu.ac.uk/ultra/courses/_351506_1/outline/edit/document/_13967799_1?courseId=_351506_1&view=content.
"""

import unittest
from celestial import CelestialBody

class CelestialBodyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.orbiting_objects = ["The Moon", "Io", "Ganymede"]
        self.celestial_primary = CelestialBody("primary")
        self.celestial_body = CelestialBody("celestial", primary=self.celestial_primary, mass=0.33, distance=2000, rotational=3.5)

    
    def tearDown(self) -> None:
        """ Releases resources that were being used by the test framework
        """
        pass
    
    def test_name(self) -> str:
        assert self.celestial_body.get_name() == "celestial", "CelestialBody is not returning the correct name."
    
    def test_mass(self) -> float:
        assert self.celestial_body.get_mass() == 0.33, "CelestialBody is not returning the correct mass."
    
    def test_distance(self) -> float:
        assert self.celestial_body.get_distance() == 2000, "CelestialBody is not returning the correct distance."
    
    def test_rotational(self) -> float:
        assert self.celestial_body.get_rotational() == 3.5, "CelestialBody is not returning the correct rotational speed."
    
    def test_primary(self) -> str:
        assert self.celestial_body.get_primary() == "primary", "CelestialBody is not returning the correct primary name."
    
    def add_orbiting_objects(self, objects) -> None:
        assert self.celestial_body.add_orbiting_objects(self, self.orbiting_objects) == None, "CelestialBody is not returning the correct add_orbiting_objects result." 

    def get_orbiting_objects(self) -> list:
        assert self.celestial_body.get_orbiting_objects() == None, "CelestialBody is not returning the correct orbiting objects."

    def get_num_orbiting_objects(self) -> int:
        assert self.celestial_body.get_num_orbiting_objects() == None, "CelestialBody is not returning the correct number of orbiting objects."
    
    def get_orbiting_object_names(self) -> str:
        assert self.celestial_body.get_orbiting_object_names() == None, "CelestialBody is not returning the correct orbiting object names."

if __name__ == "__main__":
    unittest.main()
    
