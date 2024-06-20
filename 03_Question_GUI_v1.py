from tkinter import *
from functools import partial  # to prevent unwanted windows
import csv
import random


class Play:

    def __init__(self, how_many):

        self.play_box = Toplevel()

        # If users press cross at top, closes help and
        # 'releases' help button
        self.play_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_play))

        # Variables used to work out statistics, when game ends etc
        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        # Initially set rounds played and rounds won to 0
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        self.rounds_won = IntVar()
        self.rounds_won.set(0)

    # Initialise variables (such as the feedback variable)
    self.var_feedback = StringVar()
    self.var_feedback.set("")

    self.var_has_error = StringVar()
    self.var_has_error.set("no")

    # common format for all buttons
    # Arial size 14 bold, with white text
    button_font = ("Arial", "14", "bold")
    button_fg = "#FFFFFF"

    # Set up GUI frame
    self.fear_frame = Frame(padx=10, pady=10)
    self.fear_frame.grid()

    self.fear_heading = Label(self.fear_frame,
                              text="Fears Quiz",
                              font=("Arial", "16", "bold")
                              )
    self.fear_heading.grid(row=0)

    instructions = "Please read the question and " \
                   "then try to guess the name of the fear."

    self.fear_instructions = Label(self.fear_frame,
                                   text=instructions,
                                   wrap=250, width=40,
                                   justify="left")
    self.fear_instructions.grid(row=1)

    self.fear_entry = Entry(self.fear_frame,
                            font=("Arial", "14")
                            )
    self.fear_entry.grid(row=2, padx=10, pady=10)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Fears Quiz")
    ChooseRounds()
    root.mainloop()
