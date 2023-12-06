import random
import tkinter as tk
from tkinter import messagebox

def choose_word():
    words = ["python", "programming", "language", "learning", "challenge", "improvement"]
    return random.choice(words)

def scramble_word(word):
    scrambled_word = list(word)
    random.shuffle(scrambled_word)
    return ''.join(scrambled_word)

def next_word(entry, attempts_label, show_word_button, next_word_button, word_label):
    entry.delete(0, tk.END)
    attempts_label.config(text="3")
    show_word_button.config(state=tk.DISABLED)
    next_word_button.config(state=tk.DISABLED)

    global original_word
    original_word = choose_word()
    scrambled_word = scramble_word(original_word)
    word_label.config(text=scrambled_word)

def check_guess(entry, original_word, attempts_label, show_word_button, next_word_button):
    guess = entry.get().lower()

    if guess == original_word:
        messagebox.showinfo("Correct!", "You unscrambled the word.")
        show_word_button.config(state=tk.NORMAL)
        next_word_button.config(state=tk.NORMAL)
    else:
        attempts_left = int(attempts_label.cget("text"))
        attempts_left -= 1
        attempts_label.config(text=str(attempts_left))
        if attempts_left == 0:
            show_word_button.config(state=tk.NORMAL)
            next_word_button.config(state=tk.NORMAL)
        if attempts_left > 0:
            messagebox.showwarning("Incorrect", f"Incorrect. You have {attempts_left} {'attempts' if attempts_left > 1 else 'attempt'} left.")

def show_correct_word(original_word):
    messagebox.showinfo("Correct Word", f"The correct word was: {original_word}")

def main():
    global original_word
    original_word = choose_word()
    scrambled_word = scramble_word(original_word)

    global window
    window = tk.Tk()
    window.title("Word Scramble Game")
    window.geometry("400x300")

    # Configure fonts
    title_font = ("Helvetica", 14, "bold")
    word_font = ("Helvetica", 16)
    label_font = ("Helvetica", 12)
    button_font = ("Helvetica", 12)

    # Configure colors
    bg_color = "#f0f0f0"
    label_color = "#333333"
    button_bg_color = "#4caf50"  # Green
    button_fg_color = "white"

    window.configure(bg=bg_color)

    tk.Label(window, text="Unscramble the following word:", font=title_font, bg=bg_color, fg=label_color).pack(pady=10)
    global word_label
    word_label = tk.Label(window, text=scrambled_word, font=word_font, bg=bg_color, fg=label_color)
    word_label.pack()

    entry = tk.Entry(window, font=label_font)
    entry.pack(pady=10)

    attempts_label = tk.Label(window, text="3", font=label_font, bg=bg_color, fg=label_color)
    attempts_label.pack()

    button_frame = tk.Frame(window, bg=bg_color)
    button_frame.pack(pady=10)

    show_word_button = tk.Button(button_frame, text="Show Correct Word", command=lambda: show_correct_word(original_word),
                                 state=tk.DISABLED, font=button_font, bg=button_bg_color, fg=button_fg_color)
    show_word_button.grid(row=0, column=0, padx=5)

    next_word_button = tk.Button(button_frame, text="Next Word", command=lambda: next_word(entry, attempts_label, show_word_button, next_word_button, word_label),
                                 state=tk.DISABLED, font=button_font, bg=button_bg_color, fg=button_fg_color)
    next_word_button.grid(row=0, column=1, padx=5)

    check_button = tk.Button(window, text="Check Guess", command=lambda: check_guess(entry, original_word, attempts_label, show_word_button, next_word_button),
                             font=button_font, bg=button_bg_color, fg=button_fg_color)
    check_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
