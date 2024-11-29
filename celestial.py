class CelestialBody:
    """
    A base class to represent a celestial body such as a planet, moon, or star.

    Attributes:
        name (str): The name of the celestial body.
        primary (CelestialBody, optional): The celestial body this object orbits.
        mass (int): The mass of the celestial body (in arbitrary units).
        distance (int): The distance from its primary (in arbitrary units).
        rotational (int): The rotational speed of the celestial body (in arbitrary units).
        orbiting_objects (list): A list of objects orbiting this celestial body.

    Methods:
        get_name(): Returns the name of the celestial body.
        get_mass(): Returns the mass of the celestial body.
        get_distance(): Returns the distance from its primary.
        get_rotational(): Returns the rotational speed of the celestial body.
        get_primary(): Returns the name of the primary celestial body.
        add_orbiting_objects(objects): Adds objects to the list of orbiting objects.
        get_orbiting_objects(): Returns the list of orbiting objects.
        get_num_orbiting_objects(): Returns the number of orbiting objects.
        get_orbiting_object_names(): Returns a comma-separated string of orbiting object names.
    """

    def __init__(self, name, primary=None, mass=0.0, distance=0.0, rotational=0.0, orbiting_objects=None) -> None:
        """
        Initializes a celestial body with the given attributes.

        Args:
            name (str): The name of the celestial body.
            primary (CelestialBody, optional): The celestial body this object orbits. Defaults to None.
            mass (int): The mass of the celestial body. Defaults to 0.0.
            distance (int): The distance from its primary. Defaults to 0.0.
            rotational (int): The rotational speed. Defaults to 0.0.
            orbiting_objects (list, optional): A list of orbiting objects. Defaults to an empty list.
        """
        self.name = name
        self.primary = primary
        self.mass = mass
        self.distance = distance
        self.rotational = rotational
        self.orbiting_objects = orbiting_objects or []

    def __str__(self) -> str:
        """
        Returns a string representation of the celestial body.

        Returns:
            str: The name of the celestial body.
        """
        return f"{self.name}"
    
    def get_name(self) -> str:
        """
        Returns the name of the celestial body.

        Returns:
            str: The name of the celestial body.
        """
        return self.name

    def get_mass(self) -> float:
        """
        Returns the mass of the celestial body.

        Returns:
            float: The mass of the celestial body.
        """
        return self.mass

    def get_distance(self) -> float:
        """
        Returns the distance from the primary celestial body.

        Returns:
            float: The distance from the primary celestial body.
        """
        return self.distance
    
    def get_rotational(self) -> float:
        """
        Returns the rotational speed of the celestial body.

        Returns:
            float: The rotational speed of the celestial body.
        """
        return self.rotational
    
    def get_primary(self) -> str:
        """
        Returns the name of the primary celestial body this object orbits.

        Returns:
            str: The name of the primary celestial body.
        """
        if self.primary.name:
            return self.primary.name
        else: return "None"
    
    def add_orbiting_objects(self, objects) -> None:
        """
        Adds objects to the list of orbiting objects.

        Args:
            objects (list): A list of objects to add to the orbiting objects.
        """
        self.orbiting_objects.extend(objects)

    def get_orbiting_objects(self) -> list:
        """
        Returns the list of orbiting objects.

        Returns:
            list: The list of orbiting objects.
        """
        return self.orbiting_objects

    def get_num_orbiting_objects(self) -> int:
        """
        Returns the number of orbiting objects.

        Returns:
            int: The number of orbiting objects.
        """
        return len(self.orbiting_objects)
    
    def get_orbiting_object_names(self) -> str:
        """
        Returns a comma-separated string of orbiting object names.

        Returns:
            str: The names of orbiting objects, or 'None' if no objects orbit.
        """
        if len(self.orbiting_objects) > 0:
            return ', '.join(orbiter.get_name() for orbiter in self.orbiting_objects)
        else:
            return 'None'


class Star(CelestialBody):
    """
    A class to represent a star, inheriting from CelestialBody.

    Methods:
        __str__(): Returns a descriptive string about the star and its orbiting objects.
    """

    def __init__(self, name="Unnamed") -> None:
        """
        Initializes a Star with the given name.

        Args:
            name (str): The name of the star. Defaults to "Unnamed".
        """
        super().__init__(name)

    def __str__(self) -> str:
        """
        Returns a descriptive string about the star and its orbiting objects.

        Returns:
            str: The star's name and its orbiting objects.
        """
        return f"My name is {self.name} and my orbiting objects are {self.get_orbiting_object_names()}"


class Planet(CelestialBody):
    """
    A class to represent a planet, inheriting from CelestialBody.

    Attributes:
        fact1 (str): A fun fact about the planet.
        fact2 (str): Another fun fact about the planet.

    Methods:
        get_planet_fact1(): Returns the first fun fact.
        get_planet_fact2(): Returns the second fun fact.
        get_planet_facts(): Returns both fun facts.
    """

    def __init__(self, primary=None, name="Unnamed", mass=0.0, distance=0.0, rotational=0.0, f1="", f2="") -> None:
        """
        Initializes a Planet with specific attributes.

        Args:
            primary (CelestialBody, optional): The celestial body the planet orbits. Defaults to None.
            name (str): The name of the planet. Defaults to "Unnamed".
            mass (int): The mass of the planet. Defaults to 0.0.
            distance (int): The distance from the Sun. Defaults to 0.0.
            rotational (int): The rotational speed of the planet. Defaults to 0.0.
            f1 (str): The first fun fact about the planet. Defaults to an empty string.
            f2 (str): The second fun fact about the planet. Defaults to an empty string.
        """
        super().__init__(name, primary, mass, distance, rotational)
        self.fact1 = f1
        self.fact2 = f2

    def __str__(self) -> str:
        """
        Returns a descriptive string about the planet and its attributes.

        Returns:
            str: The planet's details and fun facts.
        """
        return (
            f"My name is {self.get_name()}, my mass is {self.get_mass()}e+24 kg, "
            f"my distance from the Sun is {self.get_distance()} million km, I rotate at "
            f"{self.get_rotational()} m/s, I orbit {self.get_primary()} and I have "
            f"{self.get_num_orbiting_objects()} orbiting objects: {self.get_orbiting_object_names()}."
            f"2 facts about me are: {self.get_planet_facts()}"
        )

    def get_planet_fact1(self) -> str:
        """
        Returns the first fun fact about the planet.

        Returns:
            str: The first fun fact.
        """
        return self.fact1

    def get_planet_fact2(self) -> str:
        """
        Returns the second fun fact about the planet.

        Returns:
            str: The second fun fact.
        """
        return self.fact2

    def get_planet_facts(self) -> str:
        """
        Returns both fun facts about the planet.

        Returns:
            str: The combined fun facts.
        """
        return (f"{self.fact1} "
                f"{self.fact2}"
        )


class Moon(CelestialBody):
    """
    A class to represent a moon, inheriting from CelestialBody.

    Methods:
        __str__(): Returns a descriptive string about the moon and its primary.
    """

    def __init__(self, name="Unnamed", primary=None) -> None:
        """
        Initializes a Moon with specific attributes.

        Args:
            name (str): The name of the moon. Defaults to "Unnamed".
            primary (CelestialBody, optional): The celestial body the moon orbits. Defaults to None.
        """
        super().__init__(name, primary)

    def __str__(self) -> str:
        """
        Returns a descriptive string about the moon and its primary celestial body.

        Returns:
            str: The moon's name and its primary celestial body.
        """
        return f"My name is {self.name} and I orbit {self.get_primary()}"
