import random
from typing import Optional, Tuple, Union

import customtkinter as ctk


class Game(ctk.CTk):
    def __init__(
        self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs
    ):
        super().__init__(fg_color, **kwargs)

        self.title("Rock Paper Scissors")
        self.geometry("800x600")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.ai_frame = AIFrame(self)
        self.player_frame = PlayerFrame(self)

        self.ai_frame.grid(row=0, column=0)
        self.player_frame.grid(row=1, column=0, sticky="n")


class PlayerFrame(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk, **kwargs):
        super().__init__(parent, **kwargs)

        self.instruction_label = ctk.CTkLabel(
            self, text="Select your choice:", font=("Fira Code", 20)
        )
        self.instruction_label.grid(row=0, column=0, columnspan=6, pady=30)

        self.create_btns()

    def create_btns(self):
        # @ rock btn
        self.rock_btn = ctk.CTkButton(
            self,
            text="Rock",
            font=("Fira Code", 14),
            command=lambda: self.select_btn(self.rock_btn),
        )
        self.rock_btn.grid(row=1, column=1, pady=30, padx=5)

        # @ paper btn
        self.paper_btn = ctk.CTkButton(
            self,
            text="Paper",
            font=("Fira Code", 14),
            command=lambda: self.select_btn(self.paper_btn),
        )
        self.paper_btn.grid(row=1, column=2, pady=30, padx=5)

        # @ scissors btn
        self.scissors_btn = ctk.CTkButton(
            self,
            text="Scissors",
            font=("Fira Code", 14),
            command=lambda: self.select_btn(self.scissors_btn),
        )
        self.scissors_btn.grid(row=1, column=3, pady=30, padx=5)

        # @ submit btn
        self.submit_btn = ctk.CTkButton(
            self,
            text="Submit",
            font=("Fira Code", 14),
            command=self.submit_choice,
        )

        self.user_selection_btns = [
            self.rock_btn,
            self.paper_btn,
            self.scissors_btn,
            self.submit_btn,
        ]

    def select_btn(self, btn: ctk.CTkButton):
        match btn.cget("text"):
            case "Scissors":
                self.user_choice = "scissors"
            case "Paper":
                self.user_choice = "paper"
            case "Rock":
                self.user_choice = "rock"
        self.submit_choice()

    def submit_choice(self):
        # hide btns
        self.instruction_label.grid_forget()
        for i in self.user_selection_btns:
            i.grid_forget()

        # show user choice
        self.user_choice_label = ctk.CTkLabel(
            self,
            text=f"You chose {self.user_choice}",
            font=("Fira Code", 20),
        )
        self.user_choice_label.grid(row=0, column=0, columnspan=6, pady=30)

        # random ai choice
        ai_coices = ["rock", "paper", "scissors"]
        self.ai_choice = random.choice(ai_coices)

        # show ai choice
        # self.ai_choice_label = ctk.CTkLabel(
        #     self,
        #     text=f"AI chose {self.ai_choice}",
        #     font=("Fira Code", 20),
        # )
        # self.ai_choice_label.grid(row=1, column=0, columnspan=6, pady=30)


class AIFrame(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk, **kwargs):
        super().__init__(parent, **kwargs)
        self.waiting_for_user = True

        self.waiting_label = ctk.CTkLabel(self, text="Waiting for user...")
        self.waiting_label.grid(row=0, column=0)


def main():
    game = Game()
    game.mainloop()


if __name__ == "__main__":
    main()
