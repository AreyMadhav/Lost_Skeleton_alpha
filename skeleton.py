import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Data for each scene
scene_data = [
    # Add the Epilogue scene
    {"text": "Epilogue: Legacy of Compassion\nSee how Lucas' story becomes a part of the town's lore, inspiring generations.\nDiscover the long-term effects of your actions on the town's landscape, culture, and relationships.",
    "choices": ["Continue helping others", "Search for your purpose", "Reflect on your journey"],
    "valid_choices": ["Continue helping others", "Search for your purpose", "Reflect on your journey"]},
    
    # Add the Epilogue scenes based on the script
    {"text": "INT. LUCAS' BEDROOM - NIGHT\nLucas lies in bed, staring at the ceiling, his expression reflecting his discontent. The room is dimly lit."},
    {"text": "EXT. QUIET TOWN - DAY\nEstablishing shot of the peaceful town nestled between hills and lakes."},
    {"text": "INT. LUCAS' HOUSE - KITCHEN - MORNING\nLucas sits at the breakfast table, his family chatting happily. His friends — AIDEN, EMMA, OLIVER, MAYA, and BEN — join him."},
    {"text": "LUCAS\n(sighs)\nI just feel like there should be more to life, you know?\nAIDEN\n(smiling)\nMaybe you just need a change of scenery, buddy."},
    {"text": "EXT. SCHOOL - AFTERNOON\nThe group of friends walks together.\nOLIVER\nMaybe we should plan something exciting this weekend, shake things up a bit."},
    {"text": "INT. LUCAS' BEDROOM - NIGHT\nLucas, frustrated, looks out the window."},
    {"text": "INT. LUCAS' DREAM - MISTY FOREST - NIGHT\nLucas wanders through the dreamlike forest until he finds the peculiar old tree."},
    {"text": "INT. LUCAS' BEDROOM - MORNING\nLucas wakes up, startled.\nLUCAS\n(whispering)\nWhat was that?"},
    {"text": "EXT. TOWN - DAY\nLucas, now a skeleton, moves through the town unnoticed."},
    {"text": "VARIOUS LOCATIONS - DAY\nLucas helps the lost kitten, encourages the struggling artist, and comforts the child."},
    {"text": "EXT. TOWN SQUARE - DAY\nPeople start talking about the mysterious skeletal figure.\nMAYA\n(whispering)\nHave you heard about the skeleton that helps people?"},
    {"text": "INT. LUCAS' HOUSE - LIVING ROOM - EVENING\nLucas' family discusses the mysterious helper.\nEMMA\nMaybe it's a sign, like a guardian angel."},
    {"text": "EXT. TOWN - DAY\nLucas continues performing acts of kindness."},
    {"text": "INT. LUCAS' BEDROOM - NIGHT\nLucas looks at his skeletal hands, contemplative.\nLUCAS\nMaybe this is my chance to make a real difference."},
    {"text": "EXT. TOWN - DAY (MONTAGE)\nLucas' acts of kindness multiply, bringing hope and joy to the town."},
    {"text": "INT. LUCAS' BEDROOM - NIGHT\nLucas, now partially human, reflects on his journey.\nLUCAS\nI'm beginning to understand. It's about connecting with others."},
    {"text": "EXT. TOWN SQUARE - DAY\nThe townsfolk gather, sharing stories of encounters with the mysterious helper.\nAIDEN\n(to Lucas)\nYou've become a legend, my friend."},
    {"text": "INT. LUCAS' BEDROOM - NIGHT\nLucas, almost fully human, smiles as he drifts into a peaceful sleep."},
    {"text": "EXT. TOWN - DAY\nLucas wakes up, fully human, embracing his second chance at life.\nLUCAS\n(to himself)\nLife's magic lies in the simplest acts of compassion."},
    {"text": "EXT. TOWN - DAY (EPILOGUE)\nThe town flourishes, inspired by Lucas' tale. The friends gather, appreciating the newfound magic in their lives."},
    {"text": "FADE OUT."},

    # Add the remaining scenes
    {"text": "Prologue: The Awakening\nBegin the game by experiencing Lucas' monotonous routine and his yearning for something more.\nWitness his mysterious transformation into a skeleton after touching the old tree in his dream.",
     "choices": ["Explore the town", "Touch the tree again", "Quit"],
     "valid_choices": ["Explore the town", "Touch the tree again", "Quit"]},

    {"text": "Chapter 1: Embrace of Liberation\nNavigate the town as a skeleton, unseen by most.\nSolve puzzles and overcome obstacles that require using Lucas' unique skeletal abilities.\nInteract with characters and listen to their conversations to learn about their challenges.",
     "choices": ["Continue exploring", "Explore new areas", "Search for your purpose"],
     "valid_choices": ["Continue exploring", "Explore new areas", "Search for your purpose"]},

    {"text": "Chapter 2: Kindness Unveiled\nEngage in acts of kindness, helping the lost kitten, encouraging the struggling artist, and comforting the child afraid of the dark.\nExperience the town's transformation as stories of your benevolence spread.",
     "choices": ["Perform more acts of kindness", "Continue helping others", "Experience more stories"],
     "valid_choices": ["Perform more acts of kindness", "Continue helping others", "Experience more stories"]},

    {"text": "Chapter 3: Pursuit of Humanity\nAs you perform more acts of kindness, Lucas' form gradually shifts back to that of a living boy.\nEncounter more complex puzzles and challenges that combine both skeletal and human abilities.",
     "choices": ["Continue spreading kindness", "Explore new areas", "Quit"],
     "valid_choices": ["Continue spreading kindness", "Explore new areas", "Quit"]},

    {"text": "Chapter 4: Finding Purpose\nDive deeper into the lives of townsfolk, addressing their unique problems with empathy and creativity.\nWitness the blossoming connections and friendships you've fostered.",
     "choices": ["Continue helping others", "Search for your purpose", "Reflect on your journey"],
     "valid_choices": ["Continue helping others", "Search for your purpose", "Reflect on your journey"]},

    {"text": "Chapter 5: Echoes of Inspiration\nFully restored to human form, Lucas continues to positively impact the town's residents.\nExperience heartwarming moments of gratitude and transformation as your efforts change lives.",
     "choices": ["Continue spreading kindness", "Final reflections", "Quit"],
     "valid_choices": ["Continue spreading kindness", "Final reflections", "Quit"]},
]

class TextAdventureGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Lost Skeleton")
        self.master.configure(bg="black")

        self.chapter = 0
        self.skeleton_form = True

        # Set initial font size
        self.font_size = 12

        self.scene_text = tk.StringVar()
        self.choice_buttons = []

        self.create_widgets()

    def create_widgets(self):
        # Create a label for scene text
        self.scene_label = tk.Label(
            self.master,
            textvariable=self.scene_text,
            wraplength=600,
            justify=tk.LEFT,
            fg="white",
            bg="black",
            font=("Super Legend Boy", self.font_size)
        )
        self.scene_label.pack(padx=10, pady=10)

        # Create buttons for choices
        for i in range(3):
            button = tk.Button(
                self.master,
                text="",  # Empty initially, will be updated dynamically
                command=lambda i=i: self.process_choice(i),
                fg="white",
                bg="black",
                bd=0
            )
            button.pack(pady=5)
            self.choice_buttons.append(button)

        # Create a progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            self.master,
            variable=self.progress_var,
            maximum=len(scene_data),
            length=400,
            mode='determinate',
            style="TProgressbar"
        )
        self.progress_bar.pack(padx=10, pady=5)

        # Create "Restart" and "Quit" buttons
        restart_button = tk.Button(
            self.master,
            text="Restart",
            command=self.restart_game,
            fg="white",
            bg="black",
            bd=0
        )
        restart_button.pack(pady=5)

        quit_button = tk.Button(
            self.master,
            text="Quit",
            command=self.quit_game,
            fg="white",
            bg="black",
            bd=0
        )
        quit_button.pack(pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TProgressbar", thickness=30, troughcolor="black", background="white")

        self.display_scene()

    def display_scene(self):
        if int(self.chapter) < len(scene_data):
            current_scene = scene_data[int(self.chapter)]
            self.scene_text.set(current_scene["text"])
            self.progress_var.set(int(self.chapter) + 1)

            # Update choice buttons
            choices = current_scene["choices"]
            for i, button in enumerate(self.choice_buttons):
                if i < len(choices):
                    button["text"] = choices[i]
                else:
                    button["text"] = ""  # Hide unused buttons


    def process_choice(self, choice_index):
        if int(self.chapter) < len(scene_data):
            choices = scene_data[int(self.chapter)]["choices"]

            if 0 <= choice_index < len(choices):
                user_choice = choices[choice_index]

                if user_choice in scene_data[int(self.chapter)]["valid_choices"]:
                    self.update_game_state(user_choice)
                    self.display_scene()
                else:
                    messagebox.showinfo("Invalid Choice", "Please select a valid option.")
            else:
                messagebox.showinfo("Invalid Choice", "Please select a valid option.")
        else:
            messagebox.showinfo("Game Over", "The game has ended. Thanks for playing.")

    def update_game_state(self, user_choice):
        if int(self.chapter) < len(scene_data):
            current_scene = scene_data[int(self.chapter)]

            # Handle special events
            if "event" in current_scene and current_scene["event"] == "end_game":
                self.chapter = len(scene_data)  # Set chapter to the end to trigger game over
            else:
                # Update chapter based on user's choice
                next_chapter = user_choice
                if isinstance(next_chapter, str):
                    # Handle string values for next_chapter
                    if next_chapter in current_scene["valid_choices"]:
                        self.chapter = current_scene["choices"].index(next_chapter)
                else:
                    self.chapter = int(next_chapter)

    def restart_game(self):
        self.chapter = 0
        self.display_scene()

    def quit_game(self):
        messagebox.showinfo("Thanks for playing", "Goodbye.")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = TextAdventureGame(root)
    root.mainloop()
