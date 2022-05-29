import pyinputplus as pyip
from time import *
import threading as th

def new_game():

    guesses = []
    question_num = 1
    score = 0
    def sctn():
        pass
    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        question_num +=1
        S = th.Timer(5.0, sctn)
        S.start()
        guess = pyip.inputMenu(['A', 'B', 'C'])
        guess = guess.upper()
        guesses.append(guess)
        if questions.get(key) == guess and S.is_alive():
            score +=1
        else:
            score -=1
        S.cancel()
    if score < 0:
        result = 0
    else:
        result = score
    print(f"Score : {result}")


# -------------------------
def play_again():

    response = pyip.inputYesNo("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A",
 "n 1768, Captain James Cook set out to explore which ocean?: ": "A",
 "What is actually electricity?: ": "C",
 "Which of the following disorders is the fear of being alone?": "A",
 "Which of the following is a song by the German heavy metal band Scorpions": "B",
 "What is the speed of sound?": "B",
 "Which is the easiest way to tell the age of many trees?": "B",

}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates"],
          ["A. 1989", "B. 1991", "C. 2000"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python"],
          ["A. True","B. False", "C. sometimes"],
          ["A. Pacific Ocean", "B. Atlantic Ocean", "C. Indian Ocean"],
          ["A. A flow of water", "B. A flow of air", "C. A flow of electrons"],
          ["A. Agoraphobia", "B. Aerophobia", "C. Acrophobia"],
          ["A. Stairway to Heaven", "B. Wind of Change", "C. Don’t Stop Me Now"],
          ["A. 120 km/h", "B. 1,200 km/h", "C. 400 km/h"],
          ["A. To measure the width of the tree", "B. To count the rings on the trunk", "C. To count the number of leaves"]
          ]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")

# -------------------------
