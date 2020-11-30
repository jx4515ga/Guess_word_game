# Boris Paul Pizha 
# Sinple Game 
import random

# List of words that will choosen randomly 
list_words = ["store","sleep","do","bed","room","glass","highway","car","juice","rabit",
            "cart","bottle","window","seat","soup","rice","potatos","chair","bus","letter",
            "phone","sheep","wall","air","unfortunately","smile","happy","life","sky","sea"]
# Gettting only one word from the list 
word = random.choice(list_words) 

current = ["_" for i in range(len(word))]
# Number of letter guessed correctly 
correct = False 
# user has 10 attempts to try to guess the word 
attempts = 5
print("\n Guess the word game. You have 5 attempts to guess the letters in " , " ".join(current),"\n")
while (True): 
        letter = input("Please enter a letter: ")[0].lower() # taking input from user and taking the first letter and convert it to lower case letter
        # if letter was already guesses by user message will display letting user know that letter was already guessed
        if ( (letter in current) and letter != "_"): 
                print("You've already guessed " + letter)
        # if letter in word display a message, letter is in the word 
        elif letter in word:  
                print(f"'{letter}' is in the word")
                for i in range(len(word)): 
                        if letter == word[i]:
                            # incrementing the correct guesses by user 
                                correct = correct + 1 
                                current[i] = letter  
                if (correct == len(word)): 
                        # Winning game after guessing all the letter in the random word
                        print(f"You are the winner. The word is '{word}'")
                        break 
        else:   
                # number os attemps decrese every time user doesnt guess a word 
                attempts = attempts - 1 
                print(f"There is no '{letter}' in the word")
                if (attempts == 0): 
                        # user run out of ottempts and lose the game
                        print(f"You lost the game. The word was '{word}'")
                        break 
        print(f"{' '.join(current)}\tNumber of attempts left: {attempts}\n")
