import tkinter as tk
from tkinter import ttk, messagebox


class PlanetCard:
    """
    A class to create and display a card containing planetary details.

    Attributes:
        display_frame (tk.Widget): The parent frame where the card will be displayed.
        planet (Planet): The planet object containing details to display.

    Methods:
        create_labels(): Creates and adds labels for planetary details to the card.
    """

    def __init__(self, display_frame, planet) -> None:
        """
        Initializes the PlanetCard with a display frame and planet object.

        Args:
            display_frame (tk.Widget): The parent frame where the card will be displayed.
            planet (Planet): The planet object containing details to display.
        """
        self.display_frame = display_frame
        self.planet = planet
        self.card = ttk.Frame(self.display_frame, padding=10, relief="ridge")
        self.labels = [
            f"Name: {self.planet.get_name()}",
            f"Orbits: {self.planet.get_primary()}",
            f"Mass: {self.planet.get_mass()} x 10^24 kg",
            f"Distance from Sun: {self.planet.get_distance()} million km",
            f"Rotational speed: {self.planet.get_rotational()} m/s",
            f"Fact 1: {self.planet.get_planet_fact1()}",
            f"Fact 2: {self.planet.get_planet_fact2()}",
            f"Number of moons: {self.planet.get_num_orbiting_objects()}",
            f"Moon names: {self.planet.get_orbiting_object_names()}",
        ]

    def create_labels(self) -> None:
        """
        Creates and adds labels displaying planetary details to the card.
        """
        self.card.pack(padx=10, pady=10, fill="x")

        for text in self.labels:
            if text[:10] == "Moon names" and self.planet.get_num_orbiting_objects() == 0:
                continue  # Skip showing "Moon Names" if there are no moons
            ttk.Label(self.card, text=text, wraplength=650, justify="left").pack(anchor="w", pady=2)


class ScrollableFrame:
    """
    A class to create a scrollable frame for displaying long content.

    Attributes:
        root (tk.Widget): The parent widget for the scrollable frame.
        frame (ttk.Frame): The container frame for the canvas and scrollbar.
        canvas (tk.Canvas): The canvas to hold the scrollable content.
        scrollbar (ttk.Scrollbar): The vertical scrollbar for the canvas.
        scrollable_frame (ttk.Frame): The frame inside the canvas for content.

    Methods:
        create_sf(): Sets up the scrollable frame with a canvas and scrollbar.
    """

    def __init__(self, root) -> None:
        """
        Initializes the ScrollableFrame.

        Args:
            root (tk.Widget): The parent widget for the scrollable frame.
        """
        self.root = root
        self.frame = ttk.Frame(self.root)
        self.canvas = tk.Canvas(self.frame)
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

    def create_sf(self) -> None:
        """
        Sets up the scrollable frame with a canvas and a vertical scrollbar.
        """
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame.pack(fill="both", expand=True)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")


class ClearFrame:
    """
    A class to clear all widgets from a given frame.

    Attributes:
        frame (tk.Widget): The frame to clear.

    Methods:
        clear_frame(): Removes all widgets from the frame.
    """

    def __init__(self, frame) -> None:
        """
        Initializes the ClearFrame with a specific frame.

        Args:
            frame (tk.Widget): The frame to clear.
        """
        self.frame = frame

    def clear_frame(self) -> None:
        """
        Clears all widgets from the frame.
        """
        for widget in self.frame.winfo_children():
            widget.destroy()


class ShowSystemAll:
    """
    A class to display all the objects in a solar system in a scrollable frame.

    Attributes:
        solar_system (Star): The solar system object containing planets and moons.
        root (tk.Tk): The root window for the display.

    Methods:
        show_complete_system(): Displays all planetary and moon details.
    """

    def __init__(self, s) -> None:
        """
        Initializes the ShowSystemAll class.

        Args:
            s (Star): The solar system object containing planets and moons.
        """
        self.solar_system = s
        self.root = tk.Tk()

    def show_complete_system(self) -> None:
        """
        Displays all planetary and moon details in a scrollable frame.
        """
        self.root.title("The Complete Solar System")
        self.root.geometry("700x800")

        sf = ScrollableFrame(self.root)
        sf.create_sf()

        for planet in self.solar_system.get_orbiting_objects():
            planet_card = PlanetCard(sf.scrollable_frame, planet)
            planet_card.create_labels()

        ttk.Button(self.root, text="Close", command=lambda: self.root.destroy()).pack(pady=5, anchor="nw")


class ShowInfo:
    """
    A class to display specific information about a planet based on user input.

    Attributes:
        solar_system (Star): The solar system object containing planets and moons.
        message (str): The user-selected operation to perform.
        root (tk.Tk): The root window for the display.
        display_frame (ttk.Frame): The frame to display planetary details.
        cf (ClearFrame): A ClearFrame instance for clearing the display frame.

    Methods:
        get_input_and_display(): Gets user input and displays the relevant information.
        set_display_area(): Sets up the input and display interface.
        run(): Runs the application.
    """

    def __init__(self, solar_system, message, p_value) -> None:
        """
        Initializes the ShowInfo class.

        Args:
            solar_system (Star): The solar system object containing planets and moons.
            message (str): The user-selected operation to perform.
        """
        self.solar_system = solar_system
        self.message = message
        self.planet_choice = p_value
        self.root = tk.Tk()
        self.display_frame = ttk.Frame(self.root)
        self.cf = ClearFrame(self.display_frame)

    def get_input_and_display(self) -> None:
        """
        Gets the user input for a planet name and displays the relevant information.
        """
        self.cf.clear_frame()
        
        # We check to see if a planet was entered in the menu input and gather input if not
        if not self.planet_choice:
            user_input = self.entry.get().strip()
            if not user_input:
                ttk.Label(self.display_frame, text="Please enter a valid planet name.", font=("Arial", 12)).pack(pady=50)
                return
            self.planet_choice = user_input.capitalize()
        
        # Use the 'message' variable from the menu to drive the appropriate display
        for planet in self.solar_system.get_orbiting_objects():
            if planet.get_name() == self.planet_choice:
                if self.message == "1":
                    planet_card = PlanetCard(self.display_frame, planet)
                    planet_card.create_labels()
                elif self.message == "2":
                    ttk.Label(self.display_frame, text=f"The mass of planet {planet.get_name()} is: {planet.get_mass()} x 10^24 kg.",
                              font=("Arial", 12)).pack(pady=50)
                elif self.message == "3":
                    ttk.Label(self.display_frame, text=f"Yes! Planet {planet.get_name()} exists.",
                              font=("Arial", 12)).pack(pady=50)
                elif self.message == "4":
                    if planet.get_orbiting_object_names() != "None":
                        ttk.Label(self.display_frame, text=f"The number of moons orbiting planet {planet.get_name()} is: {planet.get_num_orbiting_objects()}.\n\nThey are {planet.get_orbiting_object_names()}",
                                  font=("Arial", 12)).pack(pady=50)
                    else:
                        ttk.Label(self.display_frame, text=f"{planet.get_name()} has no moons.",
                                  font=("Arial", 12)).pack(pady=50)
        
                self.planet_choice = None # reset the entry for the next input
                self.entry.delete(0, tk.END) # Clear the entry input box
                return
        ttk.Label(self.display_frame, text="Planet can't be found, please try again.",
                          font=("Arial", 12)).pack(pady=50)
        self.planet_choice = None # reset the entry for the next input
        self.entry.delete(0, tk.END) # Clear the entry input box

    def set_display_area(self) -> None:
        """
        Sets up the input interface for the user to enter a planet name.
        """
        self.root.title("Find information about a planet")
        self.root.geometry("700x450")

        ttk.Label(self.root, text="Enter the name of a planet:",
                   font=("Arial", 12)).pack(pady=10)
        
        self.entry = ttk.Entry(self.root, width=30)
        self.entry.pack(pady=5)
        
        # Determine if we have a planet input already and if so, display its information
        if self.planet_choice:
            # Automatically display the planet information
            self.get_input_and_display()
        #else:
            # Wait for user input and bind Submit button to get_input_and_display
        ttk.Button(self.root, text="Submit", command=self.get_input_and_display).pack(pady=10)
        
        self.display_frame.pack(fill="both", expand=True)

        ttk.Button(self.root, text="Close", command=lambda: self.root.destroy()).pack(
            pady=5, anchor="nw")

    def run(self) -> None:
        """
        Runs the application by initializing the display area and starting the Tkinter main loop.
        """
        self.set_display_area()
        self.root.mainloop()
