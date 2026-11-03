import random

"""
This function creates the vocabulary matrix
It returns a nested list (matrix) with term, definition and hint
"""
def vocabulary_matrix():
    vocabulary_matrix = [
        ["input", "Predefined function to ask data to the user", "starts with in"],
        ["int", "Used for whole numbers", "like 1, 2, 3"],
        ["float", "Used for decimal numbers", "like 3.5"],
        ["str", "Used for text", "uses quotes"],
        ["loop", "Cyclic behavior that repeats code", "for or while"],
        ["if", "Conditional for decisions", "checks True or False"],
        ["print", "Function to show text on screen", "you use it a lot"],
        ["list", "Used to store many variables", "uses brackets []"]
    ]
    return vocabulary_matrix

"""
This function chooses a random question from the matrix
Returns term, definition and hint
"""
def random_question(vocabulary_matrix):
    correct_term, correct_definition, hint = random.choice(vocabulary_matrix)
    return correct_term, correct_definition, hint

"""
This function checks if the answer is correct
Uses string functions to compare without caring about capital letters
"""
def check_the_answer(player_answer, correct_term):
    player_answer = player_answer.strip().lower()
    correct_term = correct_term.strip().lower()
    if player_answer == correct_term:
        return True
    else:
        return False

"""
Main function of the game
Now with configurable rounds and better lists
"""
def main():
    matrix = vocabulary_matrix()
    total_input = input("How many rounds do you want to play? (1-8): ")
    if not total_input.isdigit():
        print("Not a number, we will use 3 rounds")
        total = 3
    else:
        total = int(total_input)
        if total > len(matrix):
            total = len(matrix)
        if total < 1:
            total = 3
    score = 0
    correct_list = []
    wrong_list = []
    for i in range(total):
        correct_term, correct_definition, hint = random_question(matrix)
        print("\nWhat is the correct term for this definition?")
        print(correct_definition)
        player_answer = input("Answer: ")
        if player_answer.strip() == "":
            print("You didn't give an answer, that counts as incorrect")
            print(f"The answer was {correct_term}")
            print(f"Hint: {hint}")
            wrong_list.append(correct_term)
        else:
            if check_the_answer(player_answer, correct_term):
                print("CORRECT!!!")
                score = score + 1
                correct_list.append(correct_term)
            else:
                print(f"INCORRECT, you said {player_answer}")
                print(f"The right answer was {correct_term}")
                print(f"Hint for next time: {hint}")
                wrong_list.append(correct_term)
        print(f"Score: {score}")
    average = score / total
    percent = average * 100
    lost = total - score
    print("\n--- Final Results ---")
    print(f"Final Score: {score} out of {total}")
    print(f"You got {percent} % correct")
    print(f"You lost {lost}")
    print("Correct answers: " + ", ".join(correct_list))
    print("Wrong answers: " + ", ".join(wrong_list))
    if percent >= 70:
        print("GOOD JOB!!!")
    else:
        print("Keep studying")
main()
