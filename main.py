import random
import time
import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

class CircleOfFifths:
    def __init__(self):
        # Define the Circle of Fifths keys
        self.keys = ["C", "G", "D", "A", "E", "B", "F#/Gb", "C#/Db", "Ab", "Eb", "Bb", "F"]
        
        # Define the major and minor chords for each key
        self.major_chords = {
            "C": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],
            "G": ["G", "Am", "Bm", "C", "D", "Em", "F#dim"],
            "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],
            "A": ["A", "Bm", "C#m", "D", "E", "F#m", "G#dim"],
            "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"],
            "B": ["B", "C#m", "D#m", "E", "F#", "G#m", "A#dim"],
            "F#/Gb": ["F#", "G#m", "A#m", "B", "C#", "D#m", "E#dim"],
            "C#/Db": ["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "Cdim"],
            "Ab": ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "Gdim"],
            "Eb": ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "Ddim"],
            "Bb": ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "Adim"],
            "F": ["F", "Gm", "Am", "Bb", "C", "Dm", "Edim"]
        }
        
        # Define the chord degrees
        self.chord_degrees = ["I", "ii", "iii", "IV", "V", "vi", "vii°"]
        
        # Adjacent keys in the Circle of Fifths (for exercises)
        self.adjacent_keys = {
            "C": ["F", "G"],
            "G": ["C", "D"],
            "D": ["G", "A"],
            "A": ["D", "E"],
            "E": ["A", "B"],
            "B": ["E", "F#/Gb"],
            "F#/Gb": ["B", "C#/Db"],
            "C#/Db": ["F#/Gb", "Ab"],
            "Ab": ["C#/Db", "Eb"],
            "Eb": ["Ab", "Bb"],
            "Bb": ["Eb", "F"],
            "F": ["Bb", "C"]
        }
        
        # Initialize user profile with default settings
        self.user_data = {
            "username": "user",
            "exercises_completed": 0,
            "correct_answers": 0,
            "skill_level": 1,  # 1-10 scale
            "key_proficiency": {key: 1 for key in self.keys},
            "exercise_history": [],
            "last_session": None
        }
        
        # Try to load existing user data
        self.load_user_data()
    
    def save_user_data(self):
        """Save user data to JSON file"""
        with open("circle_of_fifths_user_data.json", "w") as f:
            json.dump(self.user_data, f, indent=4, default=str)
        print("Progress saved.")
    
    def load_user_data(self):
        """Load user data from JSON file if it exists"""
        try:
            if os.path.exists("circle_of_fifths_user_data.json"):
                with open("circle_of_fifths_user_data.json", "r") as f:
                    self.user_data = json.load(f)
                print(f"Welcome back, {self.user_data['username']}!")
        except Exception as e:
            print(f"Could not load previous data: {e}")
            print("Starting with a new profile.")
    
    def update_skill_level(self):
        """Update overall skill level based on key proficiencies"""
        self.user_data["skill_level"] = sum(self.user_data["key_proficiency"].values()) / len(self.keys)
    
    def display_main_menu(self):
        """Display the main menu and handle user selection"""
        while True:
            print("\n==== CIRCLE OF FIFTHS - INTERACTIVE LEARNING ====")
            print("1. Learn about the Circle of Fifths")
            print("2. Practice Key Identification")
            print("3. Chord Progression Exercise")
            print("4. Relative Major/Minor Relationships")
            print("5. Key Signature Quiz")
            print("6. View Your Progress")
            print("7. Change Username")
            print("8. Exit")
            
            choice = input("\nSelect an option (1-8): ")
            
            if choice == "1":
                self.show_tutorial()
            elif choice == "2":
                self.key_identification_exercise()
            elif choice == "3":
                self.chord_progression_exercise()
            elif choice == "4":
                self.relative_key_exercise()
            elif choice == "5":
                self.key_signature_quiz()
            elif choice == "6":
                self.show_progress()
            elif choice == "7":
                self.change_username()
            elif choice == "8":
                self.update_skill_level()
                self.user_data["last_session"] = datetime.now()
                self.save_user_data()
                print("Thanks for learning with Circle of Fifths! Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    
    def show_tutorial(self):
        """Display tutorial information about the Circle of Fifths"""
        print("\n==== CIRCLE OF FIFTHS TUTORIAL ====")
        print("\nWhat is the Circle of Fifths?")
        print("The Circle of Fifths is a fundamental concept in music theory that shows the relationship")
        print("between the 12 tones of the chromatic scale, their corresponding key signatures, and the")
        print("associated major and minor keys.")
        
        print("\nThe Circle is arranged as follows:")
        print("  - Starting with C at the top (no sharps/flats)")
        print("  - Moving clockwise, each key adds one sharp (C → G → D → A → E → B → F# → C#)")
        print("  - Moving counterclockwise from C, each key adds one flat (C → F → Bb → Eb → Ab → Db → Gb)")
        
        print("\nKey Applications of the Circle of Fifths:")
        print("1. Finding key signatures: The position on the circle tells you the number of sharps/flats")
        print("2. Identifying closely related keys: Adjacent keys on the circle are closely related")
        print("3. Chord progressions: Common progressions often follow the circle (e.g., ii-V-I)")
        print("4. Modulation: The circle helps musicians understand and navigate key changes")
        
        print("\nChord Structure in Each Key:")
        print("For any major key, the pattern of chords follows:")
        print("I (major) - ii (minor) - iii (minor) - IV (major) - V (major) - vi (minor) - vii° (diminished)")
        
        print("\nExamples in C major:")
        print("C (I) - Dm (ii) - Em (iii) - F (IV) - G (V) - Am (vi) - Bdim (vii°)")
        
        input("\nPress Enter to return to the main menu...")
    
    def key_identification_exercise(self):
        """Run an exercise to identify keys on the Circle of Fifths"""
        print("\n==== KEY IDENTIFICATION EXERCISE ====")
        print("Identify the correct key based on the clue.")
        
        correct = 0
        total = 5  # Number of questions per exercise
        
        # Adjust difficulty based on skill level
        difficulty = min(int(self.user_data["skill_level"]), 3)
        
        for i in range(total):
            # Select question type based on difficulty
            question_type = random.randint(1, difficulty + 1)
            
            if question_type == 1:
                # Basic: Find key with X sharps/flats
                sharp_flat = random.choice(["sharp", "flat"])
                if sharp_flat == "sharp":
                    count = random.randint(0, 7)
                    answer = ["C", "G", "D", "A", "E", "B", "F#/Gb", "C#/Db"][count]
                    print(f"\nQuestion {i+1}: Which major key has {count} sharps?")
                else:
                    count = random.randint(0, 7)
                    answer = ["C", "F", "Bb", "Eb", "Ab", "C#/Db", "F#/Gb", "B"][count]
                    print(f"\nQuestion {i+1}: Which major key has {count} flats?")
            
            elif question_type == 2:
                # Medium: Find position on circle
                position = random.choice(["clockwise", "counterclockwise"])
                steps = random.randint(1, 5)
                start_key = random.choice(self.keys)
                
                if position == "clockwise":
                    start_idx = self.keys.index(start_key)
                    end_idx = (start_idx + steps) % 12
                    answer = self.keys[end_idx]
                    print(f"\nQuestion {i+1}: Starting from {start_key}, what key is {steps} steps clockwise on the Circle of Fifths?")
                else:
                    start_idx = self.keys.index(start_key)
                    end_idx = (start_idx - steps) % 12
                    answer = self.keys[end_idx]
                    print(f"\nQuestion {i+1}: Starting from {start_key}, what key is {steps} steps counterclockwise on the Circle of Fifths?")
            
            elif question_type == 3:
                # Advanced: Relative minor/major or specific chord in key
                subtype = random.choice(["relative", "chord"])
                
                if subtype == "relative":
                    # Find relative minor/major
                    is_to_minor = random.choice([True, False])
                    if is_to_minor:
                        major_key = random.choice(self.keys)
                        major_idx = self.keys.index(major_key)
                        minor_idx = (major_idx + 9) % 12
                        answer = self.keys[minor_idx].lower() + "m"
                        print(f"\nQuestion {i+1}: What is the relative minor of {major_key} major?")
                    else:
                        minor_idx = random.randint(0, 11)
                        minor_key = self.keys[minor_idx].lower() + "m"
                        major_idx = (minor_idx + 3) % 12
                        answer = self.keys[major_idx]
                        print(f"\nQuestion {i+1}: What is the relative major of {minor_key}?")
                else:
                    # Find specific chord in key
                    key = random.choice(self.keys)
                    degree_idx = random.randint(0, 6)
                    chord_degree = self.chord_degrees[degree_idx]
                    answer = self.major_chords[key][degree_idx]
                    print(f"\nQuestion {i+1}: In the key of {key} major, what is the {chord_degree} chord?")
            
            # Get user answer
            user_answer = input("Your answer: ").strip()
            
            # Check answer
            if user_answer.upper() == answer.upper() or user_answer.lower() == answer.lower():
                print("Correct!")
                correct += 1
                # Increase proficiency for this key
                related_key = answer.split('/')[0].replace('m', '')
                if related_key in self.user_data["key_proficiency"]:
                    self.user_data["key_proficiency"][related_key] = min(
                        10, self.user_data["key_proficiency"][related_key] + 0.2
                    )
            else:
                print(f"Incorrect. The correct answer is {answer}.")
        
        # Record results
        score = (correct / total) * 100
        print(f"\nYou scored {score:.1f}% ({correct}/{total})")
        
        self.user_data["exercises_completed"] += 1
        self.user_data["correct_answers"] += correct
        
        # Record exercise history
        self.user_data["exercise_history"].append({
            "date": datetime.now(),
            "type": "Key Identification",
            "score": score,
            "difficulty": difficulty
        })
        
        self.update_skill_level()
        self.save_user_data()
        
        input("\nPress Enter to return to the main menu...")
    
    def chord_progression_exercise(self):
        """Exercise to identify chords in a progression"""
        print("\n==== CHORD PROGRESSION EXERCISE ====")
        print("Identify the chords in the given progression.")
        
        # Choose keys based on user proficiency
        weighted_keys = []
        for key, prof in self.user_data["key_proficiency"].items():
            # Keys with lower proficiency appear more frequently
            weight = max(1, (11 - prof))
            weighted_keys.extend([key] * int(weight))
        
        selected_key = random.choice(weighted_keys)
        
        print(f"\nKey: {selected_key} major")
        
        # Generate a progression
        progression_length = random.randint(3, 5)
        progression = []
        
        # Common progression patterns based on difficulty
        easy_patterns = [
            [0, 3, 4], # I-IV-V
            [0, 4, 3], # I-V-IV
            [0, 5, 3, 4], # I-vi-IV-V
        ]
        
        medium_patterns = [
            [0, 5, 3, 4, 0], # I-vi-IV-V-I
            [0, 1, 4, 0],    # I-ii-V-I
            [5, 1, 4, 0],    # vi-ii-V-I
        ]
        
        hard_patterns = [
            [0, 1, 4, 5, 3, 4, 0], # I-ii-V-vi-IV-V-I
            [0, 5, 1, 4, 0],      # I-vi-ii-V-I
            [0, 2, 5, 3, 4, 0],   # I-iii-vi-IV-V-I
        ]
        
        # Select pattern based on skill level
        if self.user_data["skill_level"] < 3:
            pattern = random.choice(easy_patterns)
        elif self.user_data["skill_level"] < 7:
            pattern = random.choice(medium_patterns)
        else:
            pattern = random.choice(hard_patterns)
        
        # Generate the progression
        for degree_idx in pattern:
            degree = self.chord_degrees[degree_idx]
            chord = self.major_chords[selected_key][degree_idx]
            progression.append((degree, chord))
        
        # Display the progression with some blanks
        num_blanks = min(len(progression) - 1, max(1, int(progression_length / 2)))
        blank_positions = random.sample(range(len(progression)), num_blanks)
        
        questions = []
        for i, (degree, chord) in enumerate(progression):
            if i in blank_positions:
                print(f"Position {i+1}: {degree} - ?")
                questions.append((i, degree, chord))
            else:
                print(f"Position {i+1}: {degree} - {chord}")
        
        # Ask the questions
        correct = 0
        for i, (pos, degree, chord) in enumerate(questions):
            user_answer = input(f"\nWhat is the {degree} chord in {selected_key} major? ").strip()
            
            if user_answer.upper() == chord.upper() or user_answer.lower() == chord.lower():
                print("Correct!")
                correct += 1
                # Increase proficiency
                self.user_data["key_proficiency"][selected_key] = min(
                    10, self.user_data["key_proficiency"][selected_key] + 0.3
                )
            else:
                print(f"Incorrect. The {degree} chord in {selected_key} major is {chord}.")
        
        # Record results
        score = (correct / len(questions)) * 100
        print(f"\nYou scored {score:.1f}% ({correct}/{len(questions)})")
        
        self.user_data["exercises_completed"] += 1
        self.user_data["correct_answers"] += correct
        
        # Record exercise history
        self.user_data["exercise_history"].append({
            "date": datetime.now(),
            "type": "Chord Progression",
            "score": score,
            "key": selected_key
        })
        
        self.update_skill_level()
        self.save_user_data()
        
        input("\nPress Enter to return to the main menu...")
    
    def relative_key_exercise(self):
        """Exercise on relative major/minor keys"""
        print("\n==== RELATIVE MAJOR/MINOR RELATIONSHIPS ====")
        print("Practice identifying relative major and minor keys.")
        
        total_questions = 5
        correct = 0
        
        for i in range(total_questions):
            # Decide if we're asking for relative major or minor
            is_to_minor = random.choice([True, False])
            
            if is_to_minor:
                # Ask for the relative minor
                major_key = random.choice(self.keys)
                major_idx = self.keys.index(major_key)
                minor_idx = (major_idx + 9) % 12
                answer = self.keys[minor_idx].lower() + "m"
                
                print(f"\nQuestion {i+1}: What is the relative minor of {major_key} major?")
            else:
                # Ask for the relative major
                minor_idx = random.randint(0, 11)
                minor_key = self.keys[minor_idx].lower() + "m"
                major_idx = (minor_idx + 3) % 12
                answer = self.keys[major_idx]
                
                print(f"\nQuestion {i+1}: What is the relative major of {minor_key}?")
            
            user_answer = input("Your answer: ").strip()
            
            if user_answer.upper() == answer.upper() or user_answer.lower() == answer.lower():
                print("Correct!")
                correct += 1
                
                # Increase proficiency for both keys
                related_key = answer.split('/')[0].replace('m', '')
                question_key = major_key if is_to_minor else self.keys[major_idx]
                
                if related_key in self.user_data["key_proficiency"]:
                    self.user_data["key_proficiency"][related_key] = min(
                        10, self.user_data["key_proficiency"][related_key] + 0.2
                    )
                
                if question_key in self.user_data["key_proficiency"]:
                    self.user_data["key_proficiency"][question_key] = min(
                        10, self.user_data["key_proficiency"][question_key] + 0.2
                    )
            else:
                print(f"Incorrect. The correct answer is {answer}.")
        
        # Record results
        score = (correct / total_questions) * 100
        print(f"\nYou scored {score:.1f}% ({correct}/{total_questions})")
        
        self.user_data["exercises_completed"] += 1
        self.user_data["correct_answers"] += correct
        
        # Record exercise history
        self.user_data["exercise_history"].append({
            "date": datetime.now(),
            "type": "Relative Keys",
            "score": score
        })
        
        self.update_skill_level()
        self.save_user_data()
        
        input("\nPress Enter to return to the main menu...")
    
    def key_signature_quiz(self):
        """Quiz on key signatures (number of sharps/flats)"""
        print("\n==== KEY SIGNATURE QUIZ ====")
        print("Identify the number of sharps or flats in each key signature.")
        
        total_questions = 5
        correct = 0
        
        for i in range(total_questions):
            # Randomly select a key
            key = random.choice(self.keys)
            
            # Determine if key has sharps or flats
            if key in ["C", "G", "D", "A", "E", "B", "F#/Gb", "C#/Db"]:
                # Sharps
                key_idx = ["C", "G", "D", "A", "E", "B", "F#/Gb", "C#/Db"].index(key)
                if key_idx == 0:
                    answer = "0"
                else:
                    answer = str(key_idx)
                question = f"How many sharps are in the key signature of {key} major?"
            else:
                # Flats
                key_idx = ["C", "F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"].index(key)
                if key_idx == 0:
                    answer = "0"
                else:
                    answer = str(key_idx)
                question = f"How many flats are in the key signature of {key} major?"
            
            print(f"\nQuestion {i+1}: {question}")
            user_answer = input("Your answer: ").strip()
            
            if user_answer == answer:
                print("Correct!")
                correct += 1
                
                # Increase proficiency
                self.user_data["key_proficiency"][key] = min(
                    10, self.user_data["key_proficiency"][key] + 0.2
                )
            else:
                print(f"Incorrect. The correct answer is {answer}.")
        
        # Record results
        score = (correct / total_questions) * 100
        print(f"\nYou scored {score:.1f}% ({correct}/{total_questions})")
        
        self.user_data["exercises_completed"] += 1
        self.user_data["correct_answers"] += correct
        
        # Record exercise history
        self.user_data["exercise_history"].append({
            "date": datetime.now(),
            "type": "Key Signatures",
            "score": score
        })
        
        self.update_skill_level()
        self.save_user_data()
        
        input("\nPress Enter to return to the main menu...")
    
    def show_progress(self):
        """Display user progress statistics and charts"""
        print("\n==== YOUR PROGRESS ====")
        
        # Calculate overall statistics
        total_exercises = self.user_data["exercises_completed"]
        total_correct = self.user_data["correct_answers"]
        
        if total_exercises > 0:
            overall_accuracy = (total_correct / (total_exercises * 5)) * 100
        else:
            overall_accuracy = 0
        
        print(f"Username: {self.user_data['username']}")
        print(f"Skill Level: {self.user_data['skill_level']:.1f}/10")
        print(f"Exercises Completed: {total_exercises}")
        print(f"Overall Accuracy: {overall_accuracy:.1f}%")
        
        if total_exercises > 0:
            # Show proficiency by key
            print("\nProficiency by Key:")
            for key, prof in sorted(self.user_data["key_proficiency"].items(), 
                                  key=lambda x: x[1], reverse=True):
                print(f"  {key}: {'█' * int(prof)}{' ' * (10-int(prof))} {prof:.1f}/10")
            
            # Show recent exercise history
            if self.user_data["exercise_history"]:
                print("\nRecent Exercise History:")
                recent = self.user_data["exercise_history"][-5:]
                for i, exercise in enumerate(reversed(recent)):
                    date_str = exercise["date"] if isinstance(exercise["date"], str) else exercise["date"].strftime("%Y-%m-%d %H:%M")
                    print(f"  {date_str} - {exercise['type']} - Score: {exercise['score']:.1f}%")
            
            # Generate and display progress graph if there's enough data
            if len(self.user_data["exercise_history"]) >= 3:
                self.generate_progress_graph()
                print("\nA progress graph has been saved as 'progress_chart.png'")
        
        input("\nPress Enter to return to the main menu...")
    
    def generate_progress_graph(self):
        """Generate a visual representation of user progress"""
        try:
            # Extract data for plotting
            history = self.user_data["exercise_history"]
            
            # Group by exercise type
            exercise_types = defaultdict(list)
            for ex in history:
                date = ex["date"] if isinstance(ex["date"], str) else ex["date"]
                if isinstance(date, str):
                    try:
                        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
                    except ValueError:
                        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
                exercise_types[ex["type"]].append((date, ex["score"]))
            
            # Create the plot
            plt.figure(figsize=(10, 6))
            
            for ex_type, scores in exercise_types.items():
                # Sort by date
                scores.sort(key=lambda x: x[0])
                
                # Extract dates and scores
                dates = [s[0] for s in scores]
                values = [s[1] for s in scores]
                
                # Plot the line
                plt.plot(dates, values, marker='o', label=ex_type)
            
            plt.title("Your Progress Over Time")
            plt.xlabel("Date")
            plt.ylabel("Score (%)")
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.legend()
            plt.ylim(0, 105)
            
            # Format the date axis
            plt.gcf().autofmt_xdate()
            
            # Save the figure
            plt.savefig("progress_chart.png")
            plt.close()
            
        except Exception as e:
            print(f"Could not generate progress graph: {e}")
    
    def change_username(self):
        """Allow the user to change their username"""
        print("\n==== CHANGE USERNAME ====")
        current = self.user_data["username"]
        print(f"Current username: {current}")
        
        new_name = input("Enter new username (or press Enter to cancel): ").strip()
        
        if new_name and new_name != current:
            self.user_data["username"] = new_name
            print(f"Username changed to {new_name}")
            self.save_user_data()
        else:
            print("Username unchanged.")

def main():
    print("Welcome to Circle of Fifths - Interactive Learning Tool!")
    print("This program will help you master the Circle of Fifths and memorize chords.")
    
    app = CircleOfFifths()
    app.display_main_menu()

if __name__ == "__main__":
    main()
