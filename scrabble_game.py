import random
import time
import string
import threading
from nltk.corpus import words
import nltk
nltk.download('words')



# Scrabble score map
LETTER_VALUES = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

# Function to calculate score
def calculate_score(word):
    if not word.isalpha():
        raise ValueError("Invalid input! Please enter alphabets only.")
    score = 0
    for letter in word.upper():
        score += LETTER_VALUES.get(letter, 0)
    return score

# Validate if the word length matches
def validate_word_length(word, length_required):
    return len(word) == length_required

# Validate if word is in dictionary
def is_valid_word(word):
    word_list = words.words()  # Load dictionary from nltk
    return word.lower() in word_list

# Timer-based input prompt
def get_user_word_with_timer(length_required):
    start_time = time.time()
    user_word = None
    print(f"Enter a word with {length_required} letters (you have 15 seconds):")
    
    # Timeout logic using a thread
    timer = threading.Timer(15, lambda: print("Time's up!"))
    timer.start()
    
    user_word = input()  # Capture user input
    
    timer.cancel()  # Stop the timer if input is received in time
    elapsed_time = time.time() - start_time
    
    return user_word, elapsed_time

# # Main game loop

def play_game():
    total_score = 0
    round_count = 0
    max_rounds = 10  # Limit to 10 rounds
    
    while round_count < max_rounds:
        length_required = random.randint(3, 7)  # Generate a random word length requirement
        user_word, elapsed_time = get_user_word_with_timer(length_required)
        
        # Check if input contains only alphabets
        if not user_word.isalpha():
            print("Invalid input! Please enter alphabets only.")
            continue
        
        # Validate word length
        if not validate_word_length(user_word, length_required):
            print(f"Invalid word length! You need a word of {length_required} letters.")
            continue
        
        # Validate if the word is from the dictionary
        if not is_valid_word(user_word):
            print(f"'{user_word}' is not a valid word.")
            continue
        
        # Calculate score based on how quickly the word was entered
        score = calculate_score(user_word)
        time_bonus = max(0, 5 - int(elapsed_time))  # Bonus for faster input
        total_score += score + time_bonus
        
        print(f"Your score for this round: {score} (Bonus: {time_bonus})")
        round_count += 1
    
    # Game over after 10 rounds, print total score
    print(f"Game Over! Your total score after {max_rounds} rounds: {total_score}")


if __name__ == "__main__":
    play_game()




