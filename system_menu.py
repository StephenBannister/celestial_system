import tkinter as tk
from tkinter import ttk, messagebox
from system_ui import ShowSystemAll, ShowInfo


class SystemMenu:
    """
    A class to manage the Solar System GUI menu and user interactions.

    Attributes:
        solar_system (Star): The solar system object containing planets and moons.
        root (tk.Tk): The root window for the GUI.
        entry (ttk.Entry): The input field for user commands.

    Methods:
        determine_menu_choice(user_input): Determines the menu choice based on user input.
        handle_choice(choice): Handles the action for a selected menu choice.
        process_input(): Processes the user's input and executes the corresponding menu action.
        create_widgets(): Creates and arranges the GUI widgets.
        run(): Starts the Tkinter main loop.
    """

    def __init__(self, solar_system) -> None:
        """
        Initializes the SystemMenu class with a solar system object.

        Args:
            solar_system (Star): The solar system object containing planets and moons.
        """
        self.solar_system = solar_system
        self.root = tk.Tk()
        self.root.title("Solar System Menu")
        self.root.geometry("650x400")
        self.create_widgets()

    def determine_menu_choice(self, user_input: str) -> str | None:
        """
        Determines the menu choice based on user input.

        Args:
            user_input (str): The user's input string.

        Returns:
            str | None: The corresponding menu choice as a string, or None if no match is found.
        """
        user_input = user_input.lower()
        choices = {
            1: ["tell me about", "details about", "planet details", "planet info", "display planet", "show planet"],
            2: ["mass", "weight", "heavy", "weigh"],
            3: ["check planet", "in the list", "exists", "exist", "list of planets", "in list", "a planet"],
            4: ["moons", "how many", "how many moons", "planet's moons", "number of moons", "show number"],
            5: ["show all", "all information", "all info", "everything", "complete system", "solar system"],
            6: ["exit", "quit", "leave", "close", "bye"],
        }
        
        # Get the planet names and see if the user typed the name of one in their input
        planet_names = [name.strip() for name in self.solar_system.get_orbiting_object_names().split(",")]
        for planet in planet_names:
            if planet.lower() in user_input:
                planet_choice = planet
                break
        else:
            planet_choice = None

        # Determine if a single word is entered by the user that is the name of a planet
        if len(user_input.split()) < 2 and planet_choice is not None:
            choice = 1  # Default to the menu choice showing the information related to that planet only
            return choice, planet_choice

        for choice, keywords in choices.items():
            if any(keyword in user_input for keyword in keywords):
                return choice, planet_choice
        return None, None

    def handle_choice(self, planet_choice, choice: int) -> None:
        """
        Handles the action for a selected menu choice.

        Args:
            choice (int): The menu choice number.
        """
        if choice == 1:
            planet_info = ShowInfo(self.solar_system, "1", planet_choice)
            planet_info.run()
        elif choice == 2:
            planet_mass = ShowInfo(self.solar_system, "2", planet_choice)
            planet_mass.run()
        elif choice == 3:
            planet_exists = ShowInfo(self.solar_system, "3", planet_choice)
            planet_exists.run()
        elif choice == 4:
            planet_moons = ShowInfo(self.solar_system, "4", planet_choice)
            planet_moons.run()
        elif choice == 5:
            show_all = ShowSystemAll(self.solar_system)
            show_all.show_complete_system()
        elif choice == 6:
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Invalid input. Please try again.")

    def process_input(self) -> None:
        """
        Processes user input from the entry field and triggers the corresponding menu action.
        """

        user_input = self.entry.get()
        # Checks for empty or whitespace-only input and shows an error if so
        if not user_input.strip():
            messagebox.showerror(
                "Error", "Input cannot be blank. Please enter a valid command.")
            return  # Stop further processing and returns control to the menu

        choice, planet_choice = self.determine_menu_choice(user_input)
        if choice:
            self.entry.delete(0, tk.END)
            self.handle_choice(planet_choice, choice)
        else:
            messagebox.showerror(
                "Error", "Could not understand what you asked for. Please try again.")
            self.entry.delete(0, tk.END)

    def create_widgets(self) -> None:
        """
        Creates and arranges the widgets for the GUI.
        """
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="WELCOME TO THE CELESTIAL SYSTEM",
                  font=("Arial", 14, "bold")).pack(pady=10)
        ttk.Label(frame, text="Here you can discover many things about our solar system",
                  font=("Arial", 12)).pack(pady=10)
        ttk.Label(frame, text="Please type what you'd like to see:",
                  font=("Arial", 12)).pack(pady=5)
        self.entry = ttk.Entry(frame, width=50)
        self.entry.pack(pady=5)
        
        # Automatically focus the cursor in the entry field
        self.entry.focus()
    
        # Bind the Enter key to submit the input
        self.root.bind("<Return>", lambda event: self.process_input())
        
        ttk.Button(frame, text="Submit",
                   command=self.process_input).pack(pady=10)
        ttk.Label(frame, text="You can say things like:",
                  font=("Arial", 12)).pack(pady=5)
        ttk.Label(frame, text="'tell me about Earth' or 'show planet jupiter'",
                  font=("Arial", 10)).pack(pady=2)
        ttk.Label(frame, text="'What is the mass of Venus' or 'is Pluto in the list'",
                  font=("Arial", 10)).pack(pady=2)
        ttk.Label(frame, text="'How many moons does Saturn have' or 'Neptune's Moons'",
                  font=("Arial", 10)).pack(pady=2)
        ttk.Label(frame, text="'show all' or 'tell me everything'", font=("Arial", 10)).pack(pady=2)
        ttk.Label(frame, text="'exit' or 'bye' - if you don't want to learn anymore 🥺", font=("Arial", 10)).pack(pady=2)

    def run(self) -> None:
        """
        Starts the Tkinter main loop.
        """
        self.root.mainloop()
