import random

#the answer
answer = "gamer"

#Display feedback for each guess
def give_feedback(guess, answer):
    feedback = ""
    for i in range(5):
        if guess[i] == answer[i]:
            feedback += f"[{guess[i].upper()}]" #Correct letter and position
        elif guess[i] in answer:
            feedback += f"({guess[i]})" #Correct letter, wrong position
        else:
            feedback += guess[i] #Incorrect letter
    return feedback

#Main game loop
attempts = 6
print("Welcome to my word game! Try to guess the 5 letter word in the least amount of tries possible!")
print("Correct letters in correct positions will be shown in [brackets].")
print("Letters that are in the word, but are in the wrong position will be shown in (parentheses).")
print("All other letters are not in the word.")

for attempt in range(1, attempts + 1):
    guess = input(f"Attempt {attempt}/{attempts}: ").lower()

    #Validate the guess
    if len(guess) != 5:
        print("Please enter a 5 letter word.")
        continue

    #Give feedback on the guess
    feedback = give_feedback(guess, answer)
    print("Feedback:", feedback)

    #Check if guess is correct
    if guess == answer:
        print("You guessed the word!")
        break
else:
    print("Sorry, you've run out of guesses. The word was:", answer)
