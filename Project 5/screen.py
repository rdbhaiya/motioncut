from tkinter import *
from hangman import play_hangman_game
def play_game():
    category = category_var.get()
    difficulty = difficulty_var.get()
    root.destroy()
    play_hangman_game(category, difficulty)

root = Tk()
root.title('Hangman - Category & Difficulty Selection')

root.configure(bg="#FFFFFF")
style = {"font": ("Arial", 12), "bg": "#FFFFFF", "fg": "#333333"}

frame = Frame(root, bg="#FFFFFF")
frame.pack(expand=True, fill=BOTH)

category_label = Label(frame, text="Select Category:", **style)
category_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

category_var = StringVar()
category_var.set("Animals")  
category_options = ["Animals", "Fruits", "Countries"]
category_menu = OptionMenu(frame, category_var, *category_options)
category_menu.config(width=15, **style)
category_menu.grid(row=0, column=1, pady=10, padx=10, sticky="w")


difficulty_label = Label(frame, text="Select Difficulty:", **style)
difficulty_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")

difficulty_var = StringVar()
difficulty_var.set("Easy")  
difficulty_options = ["Easy", "Medium", "Hard"]
difficulty_menu = OptionMenu(frame, difficulty_var, *difficulty_options)
difficulty_menu.config(width=15, **style)
difficulty_menu.grid(row=1, column=1, pady=10, padx=10, sticky="w")


start_button = Button(frame, text="Start Game", command=play_game, **style)
start_button.grid(row=2, columnspan=2, pady=20, padx=10, sticky="ew")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400
window_height = 200
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2


root.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')

root.mainloop()
