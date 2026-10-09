import random

"""
This function creates the dictionary or the vocabulary matrix of the game
Create a list with the terms and the definitions
return the list
"""
def vocabulary_matrix():
    vocabulary_matrix = (("input", "-Predefined function to ask data to the user"),("int", "-Used for whole numbers"),("float","-Used for decimal numbers"),("str","-Used for text"),("loop","-Cyclic behavior that repeats code"),("if","-Conditional for decisions"))
    return vocabulary_matrix

"""
This functionn chooses a random definition from the vocabulary matrix
The random.choice is used to select a random definition from the list
Correct_term,correct_definition= is used to separate the term and the definition
Return the correct term and also the correct definition
"""
def random_question(vocabulary_matrix):
    correct_term, correct_definition = random.choice(vocabulary_matrix)
    return correct_term, correct_definition

"""
This function checks if the answer that the player gives is correct or incorrect
Compares the player_answer with the correct_term
If the player_answer and the correct_term are equal return True
Else return False
"""
def check_the_answer(player_answer,correct_term):
    if player_answer==correct_term:
        return True
    else:
        return False

"""
This is the main function of the game
get the matrix
set the players score to 0
set the total questions to 3 by using a loop
get a random question from the vocabulary matrix
check if thee players answer is empty whith a conditional
 check the players answer
print if the answer is correct or incorrect
change the score
print the current score in each round
calculate the average
calculate the questios that were wrong 
print the final score and percentage
"""
def main():
    matrix=vocabulary_matrix()
    score=0
    total=3
    for i in range(total):
        correct_term, correct_definition=random_question(matrix)
        print("What is the correct term for this definition?")
        print(correct_definition)
        player_answer = input("Answer:")
        if player_answer == "":
            print("You didn´t give an answer, that counts as incorrect")
        else:    
            if check_the_answer(player_answer,correct_term):
                print("CORRECT!!!")
                score=score+1
            else:
                print("INCORRECT, the right answer was",correct_term)   
        print("Score:", score)
        print("")
    average = score / total
    percent = average * 100
    lost = total - score 
    print("Final Score:", score, "out of", total)
    print("You got", percent, "% correct")
    print("You lost", lost)
    if percent >= 70:
        print("GOOD JOB!!!")
    else:
        print("Keep studying")

main()