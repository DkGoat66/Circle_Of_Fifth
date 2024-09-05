import random
import tkinter as tk
from tkinter import messagebox

# Circle of Fifths: Keys with their corresponding major chords
circle_of_fifths = {
    "C": ["C", "E", "G"],
    "G": ["G", "B", "D"],
    "D": ["D", "F#", "A"],
    # Add more keys here as needed
}


# Function to get a random key
def get_random_key():
    return random.choice(list(circle_of_fifths.keys()))


# Function to check if the user's answer is correct
def check_answer():
    user_chords = entry_chords.get().split(",")
    user_chords = [chord.strip() for chord in user_chords]

    if set(user_chords) == set(circle_of_fifths[current_key]):
        messagebox.showinfo("Result", "Correct!")
    else:
        correct_chords = ", ".join(circle_of_fifths[current_key])
        messagebox.showinfo("Result", f"Incorrect. The correct chords for {current_key} are {correct_chords}.")

    # Ask if the user wants to continue
    ask_new_key()


# Function to ask the next question
def ask_new_key():
    global current_key
    current_key = get_random_key()
    label_question.config(text=f"What are the major chords for the key of {current_key}?")
    entry_chords.delete(0, tk.END)


# Main window
root = tk.Tk()
root.title("Circle of Fifths Quiz")

# Question label
label_question = tk.Label(root, text="Press 'Next' to start.")
label_question.pack(pady=20)

# Entry field for user input
entry_chords = tk.Entry(root, width=50)
entry_chords.pack(pady=10)

# Submit button to check the answer
btn_submit = tk.Button(root, text="Submit", command=check_answer)
btn_submit.pack(pady=5)

# Next button to move to the next key
btn_next = tk.Button(root, text="Next", command=ask_new_key)
btn_next.pack(pady=5)

# Start with the first question
ask_new_key()

# Run the GUI event loop
root.mainloop()
