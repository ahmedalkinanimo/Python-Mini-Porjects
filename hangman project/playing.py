from movieList import movie_titles
import random
import re
from hangManPrint import * 
from art import *

def specialCharacter(char):
    special_characters = [',', '.', '?', '!', ':', ';', '-', "'", '"', '(', ')', '[', ']', '{', '}', '&', '@', '#', '$', '%', '*', '+', '=']
    if char in special_characters:
        return True
    else:
        return False
    
def print_title(mo:str):
    for x in range(len(mo)):
        if(mo[x]=="_"):
            print("_",end="")
        else:
            print(mo[x],end="")
    print()


def replace_alpha_with_underscore(string):
    # Use regular expressions to replace alpha characters with "_"
    replaced_string = re.sub(r'[a-zA-Z]', '_', string)
    
    # Create a list of characters from the replaced string
    char_list = list(replaced_string)
    
    return char_list

if __name__ == "__main__":
    #chosenTitle = movie_titles[random.randint(0,len(movie_titles)-1)].lower()
    movie_titles=list(set(movie_titles))
    #print(chosenTitle)
    answer="yes"
    print(text2art("Hangman"))
    print(text2art("Movie Version"))
    while answer=="yes" or answer=="Yes" or answer=="YES":
        chosenTitle = random.choice(movie_titles).lower()
        guesList=replace_alpha_with_underscore(chosenTitle)
        counter=0
        incorrect_choices=[]
        while True:
            print_title(guesList)
            print_hangman_parts(counter)
            if counter!=0:
                print("avoid re entering the following characters: ", incorrect_choices)
            charEnter=input("enter a single character: ").lower().strip()
            if len(charEnter)==1 and charEnter.isalpha():
            
                if charEnter in chosenTitle:
                    indices = [m.start() for m in re.finditer(charEnter, chosenTitle)]
                    for index in indices:
                        guesList[index]=chosenTitle[index]
                    if ''.join(guesList) == chosenTitle:                
                        print("WINNER, the movie is : ", chosenTitle)
                        print('     .-""""""-.')
                        print("   .'          '.")
                        print("  /   O      O   \\")
                        print(" :           `    :")
                        print(" |                |")
                        print(" :    '      '    :")
                        print("  \    \----/    /")
                        print("   '.          .'")
                        print("     '-......-'")
                        break

                else:
                    if charEnter in incorrect_choices:
                        print("You already entered ",charEnter)
                    else:
                        counter+=1
                        incorrect_choices.append(charEnter)
                        print("Wronge, ",6-counter, "left")
                        if counter==6:
                            print("LOOSER, the movie is : ", chosenTitle)
                            print_hangman_parts(counter)
                            break

            else:
                print("Invalid input, please provide an acceptable entry")
        answer=input("Would you like to play again? [yes or no]: ")
    print("the end")
    
