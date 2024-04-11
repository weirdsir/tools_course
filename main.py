import tkinter as tk

class AlphabetApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Alphabet Colors")
        self.geometry("400x200")

        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#5D6D7E', '#34495E', '#2E4053', '#212F3C',
                       '#566573', '#1F618D', '#2874A6', '#2980B9', '#5499C7', '#7FB3D5', '#AED6F1', '#EBF5FB',
                       '#1ABC9C', '#17A589', '#148F77', '#117A65', '#0E6655', '#0B5345', '#0A3E23', '#117A65',
                       '#1E8449', '#239B56']

        self.create_alphabet_labels()

    def create_alphabet_labels(self):
        for i, letter in enumerate(self.alphabet):
            tk.Label(self, text=letter, font=("Comic Sans MS", 18), fg=self.colors[i]).grid(row=0, column=i, padx=5)

if __name__ == "__main__":
    app = AlphabetApp()
    app.mainloop()
