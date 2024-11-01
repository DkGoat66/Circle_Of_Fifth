import random

# Circle of Fifths: Keys with their corresponding major chords
circle_of_fifths = {
    "C": ["C", "E", "G"],
    "G": ["G", "B", "D"],
    "D": ["D", "F#", "A"],
    # Add the rest of the keys
}

#Function to randomly select a key from the Circle of Fifths
def get_random_key():
    return random.choice(list(circle_of_fifths.keys()))

# Function to promopt the user with a question asking for the major chords
def ask_question(key):
    # Ask the user to input the major chord for the given key
    answer = input(f"What are the major chords for the key of {key}? Use comma-separated values (e.g., C,E,G): ")
    chords = [chord.strip() for chord in answer.split(",")]
    return chords

# Function to check if the user's input matches the correct chords for the given key
def check_answer(key, user_chords):
    correct_chords = circle_of_fifths[key]
    # Compare the user's chords to the correct chords, ignoring order by converting both to sets
    return set(user_chords) == set(correct_chords)

# Main function to run the quiz game
def main():
    while True:
        key = get_random_key()
        user_chords = ask_question(key)
        if check_answer(key, user_chords):
            print("Correct!")
        else:
            print(f"Incorrect. The correct chords for the key of {key} are {','.join(circle_of_fifths[key])}.")

        if input("Try another key? (yes/no): ").lower() != "yes":
            break

# Entry point of the program 
if __name__ == "__main__":
    main()
