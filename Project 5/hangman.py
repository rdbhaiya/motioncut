import random
import os
import json
from tkinter import *
from tkinter import messagebox

def play_hangman_game(category, difficulty):
    score = 0
    run = True

    def start_game():
        nonlocal score, run
        root = Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = 905
        window_height = 740
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2 - 50
        root.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')
        root.title('HANG MAN')
        root.config(bg='#E7FFFF')

        count = 0
        win_count = 0

        with open(r'C:\Users\RUPAM DAS\Desktop\MotionCut\Project 5\words.json') as json_file:
            words_data = json.load(json_file)

        
        selected_word_data = random.choice(words_data[category][difficulty])
        selected_word = selected_word_data["word"].upper()
        hint = selected_word_data["hint"]

        dash_labels = []
        x = 70
        for i in range(len(selected_word)):
            x += 60
            dash = Label(root, text="_", bg="#E7FFFF", font=("arial", 40))
            dash.place(x=x, y=450)
            dash_labels.append(dash)

        letter_images = {}
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        base_path = r'C:\Users\RUPAM DAS\Desktop\MotionCut\Project 5\Images'

        buttons = {}
        x, y = 45, 558
        for let in letters:
            try:
                letter_images[let] = PhotoImage(file=os.path.join(base_path, f'{let}.png'))
                buttons[let] = Button(root, bd=0, command=lambda l=let: check(l, buttons[l]), bg="#E7FFFF", activebackground="#E7FFFF", font=10, image=letter_images[let])
                buttons[let].place(x=x, y=y)
                x += 63
                if x > 800:
                    x = 45
                    y += 57
            except Exception as e:
                print(f"Error loading {let}.png: {e}")

        
        hint_image = PhotoImage(file=os.path.join(base_path, 'hint.png'))
        hint_button = Button(root, bd=0, command=lambda: check('hint', hint_button), bg="#E7FFFF", activebackground="#E7FFFF", font=10, image=hint_image)
        hint_button.place(x=x, y=y)

       
        hangman_images = {}
        for i in range(1, 8):
            try:
                hangman_images[i] = PhotoImage(file=os.path.join(base_path, f'h{i}.png'))
            except Exception as e:
                print(f"Error loading h{i}.png: {e}")

        
        hangman_labels = {}
        for i in range(1, 8):
            if i in hangman_images:
                hangman_labels[i] = Label(root, bg="#E7FFFF", image=hangman_images[i])

       
        if 1 in hangman_labels:
            hangman_labels[1].place(x=280, y=101)
        else:
            print("Error: First hangman image not loaded correctly.")

        
        def close():
            nonlocal run
            answer = messagebox.askyesno('ALERT', 'YOU WANT TO EXIT THE GAME?')
            if answer:
                run = False
                root.destroy()

        e1 = PhotoImage(file=os.path.join(base_path, 'exit.png'))
        ex = Button(root, bd=0, command=close, bg="#E7FFFF", activebackground="#E7FFFF", font=10, image=e1)
        ex.place(x=750, y=10)
        
        s2 = f'SCORE: {score}'
        s1 = Label(root, text=s2, bg="#E7FFFF", font=("arial", 25))
        s1.place(x=10, y=10)

     
        def check(letter, button):
            nonlocal count, win_count, score
            if letter == 'hint':
                if score > 0:
                    score -= 1
                    messagebox.showinfo("Hint", f"The hint is: {hint}")
                    s1.config(text=f'SCORE: {score}')
                else:
                    messagebox.showinfo("Hint", "You don't have enough score to use hint!")
            elif letter in selected_word:
                for i in range(len(selected_word)):
                    if selected_word[i] == letter:
                        win_count += 1
                        dash_labels[i].config(text=letter)
                if win_count == len(selected_word):
                    score += 1
                    answer = messagebox.askyesno('GAME OVER', 'YOU WON!\nWANT TO PLAY AGAIN?')
                    if answer:
                        root.destroy()
                    else:
                        run = False
                        root.destroy()
            else:
                count += 1
                if count in hangman_labels:
                    hangman_labels[count].destroy()
                if count + 1 in hangman_labels:
                    hangman_labels[count + 1].place(x=280, y=101)
                if count == 6:
                    answer = messagebox.askyesno('GAME OVER', f'YOU LOST!\nTHE WORD WAS: {selected_word}\nWANT TO PLAY AGAIN?')
                    if answer:
                        run = True
                        score = 0
                        root.destroy()
                    else:
                        run = False
                        root.destroy()
            button.destroy() 
        root.mainloop()
    while run:
        start_game()

