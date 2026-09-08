import random
def vocabulary_matrix():
    vocabulary_matrix = (("input", "-Predefined function to ask data to the user"),("int", "-Used for whole numbers"),("float","-Used for decimal numbers"),("string", "-Used for text"),("print","-Predefined function to show to show something on the screen"),("//","-Aritmeticoperator for integer division"),("%","-Aritmetic operator for the remainder of a division"),("*","-Aritmetic operator for a multiplication"))
    return vocabulary_matrix
"""
This functioncreates the dictionary or the vocabulary matrix of the game
Create a list with the terms and the definitions
return the list
"""
def random_question(vocabulary_matrix):
    correct_term, correct_definition = random.choice(vocabulary_matrix)
    return correct_term, correct_definition
"""
This functionn chooses a random definition from the vocabulary matrix
The random.choice is used to select a random definition from the list
Correct_term,correct_definition= is used to separate the term and the definition
Return the correct term and also the correct definition
"""
def check_the_answer(player_answer,correct_term):
    if player_answer==correct_term:
        return True
    else:
        return False
"""
This function checks if the answer that the player gives is correct or incorrect
Compares the player_answer with the correct_term
If the player_answer and the correct_term are equal return True
Else return False
"""
def main ():
    matrix=vocabulary_matrix()
    score=0
    correct_term, correct_definition=random_question(matrix)
    print("What is the correct term for this definition?")
    print(correct_definition)
    player_answer = input("Answer:")
    if check_the_answer(player_answer,correct_term):
        print("CORRECT!!!")
        score=score+1
    else:
        print("INCORRECT, the right answer was",correct_term)
    print("Score:", score)
main()
"""
This is the main function of the game
get the matrix
set the players score to 0
get a random question from the vocabulary matrix 
check the players answer
print if the answer is correct or incorrect
change the score
print the final score
"""

    