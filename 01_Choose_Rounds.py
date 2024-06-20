# users choose 3, 5 or 10 rounds
class ChooseRounds:

    def __init__(self):
        button_fg = "#FFFFFF"
        button_font = ("Arial", "13", "bold")

        # Set up GUI frame
        self.intro_frame = Frame(padx=10, pady=10)
        self.intro_frame.grid()

        # heading and brief instructions
        self.intro_heading_label = Label(self.intro_frame, text="Fears Quiz",
                                         font=("Arial", "16", "bold"))
        self.intro_heading_label.grid(row=0)

        choose_instructions_txt = "In each round you will be given " \
                                  "the name of a random fear, " \
                                  "and six different answers to choose from. " \
                                  "Try to guess the fear correctly! " \
                                  "To begin, choose how many rounds " \
                                  "you'd like to play..."
        self.choose_instructions_label = Label(self.intro_frame,
                                               text=choose_instructions_txt,
                                               wraplength=300,
                                               justify="left")
        self.choose_instructions_label.grid(row=1)

        # Rounds buttons...
        self.how_many_frame = Frame(self.intro_frame)
        self.how_many_frame.grid(row=2)

        # list to set up rounds button. First item in each
        # sublist is the background colour, second item is
        # the number of rounds
        btn_colour_value = [
            ["#CC0000", 3], ["#009900", 5], ["#000099", 10]
        ]

        for item in range(0, 3):
            self.rounds_button = Button(self.how_many_frame,
                                        fg=button_fg,
                                        bg=btn_colour_value[item][0],
                                        text="{} Rounds".format(btn_colour_value[item][1]),
                                        font=button_font, width=10,
                                        command=lambda i=item: self.to_play(btn_colour_value[i][1])
                                        )
            self.rounds_button.grid(row=0, column=item,
                                    padx=5, pady=5)

    def to_play(self, num_rounds):
        Play(num_rounds)

        # Hide root window (ie: hide rounds choice window).
        root.withdraw()