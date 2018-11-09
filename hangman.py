import random
mode = input("Do you want to play against a friend or a computer? ")
if mode == ("friend"):
    print("you have friends??")
    
    lives = int(input("how many miserable lives(guesses) do you want your friend to have? "))
    
    alpha = "qwertyuiopasdfghjklzxcvbnm1234567890"
    alphalist = list(alpha)
    word = input("Enter a word for your friend to guess: ")
    word = word.lower()
    wordArray = list(word)
    display = ['-' for x in wordArray]
    wrongArray = []
    win = True





    print("""









































    """)
    while True:
        print("".join(display))
        guess = input("Enter a guess: ")
                    
                    
        if guess in alphalist:
            
            if guess != (""):
                    
                if guess in wordArray:
                    if guess not in display:
                            print("You found a letter!")
                            print("You have " + str(lives) + " lives left")
                            for i in range(len(wordArray)):
                                    if guess is wordArray[i]:
                                            display[i] = guess
                    else:
                        print("You already guessed that!")
                else:
                    if guess not in wrongArray:
                            print("Incorrect guess, try again!")
                            wrongArray.append(guess)
                            lives = lives - 1
                            print("You have " + str(lives) + " lives left")
                    else:
                        print("You already guessed that wrongly. people never learn from their mistakes :(")
                if lives <= 0:
                        print("Game over - you ran out of lives. The word was '" + (word) + "'")
                        win = False
                        break
                if '-' not in display:
                        break
            else:
                print("please enter a character")
        else:
            print("pleaase enter a valid character")
                    

    if win is True:
            print("Good job! you guessed '" + str("".join(display)) + " 'correctly")
    

elif mode == ("computer"):
    print("as expected of a loner such as yourself")
    alpha = "qwertyuiopasdfghjklzxcvbnm"
    alphalist = list(alpha)
    dif = input("Easy(1), Medium(2), or Hard(3)? ")
    
    with open('easylist.txt', 'r') as f:
        a = f.read()
        dicE = [a[i:i+3] for i in range(0, len(a), 3)]
    
    with open('medlist.txt', 'r') as f:
        a = f.read()
        dicM = [a[i:i+5] for i in range(0, len(a), 5)]
        
    with open('hardlist.txt', 'r') as f:
        a = f.read()
        dicH = [a[i:i+7] for i in range(0, len(a), 7)]
    
    if dif == ("1"):
        word = random.choice(dicE)
        wordArray = list(word)
        display = ['-' for x in wordArray]
        lives = 10
        wrongArray = []
        win = True
        print("Easy Mode! Three letters: ---")
        while True:
            print("".join(display))
            guess = input("Enter a guess: ")
                    
                    
            if guess in alphalist:
                if guess != (""):
                    
                    if guess in wordArray:
                        if guess not in display:
                                print("You found a letter!")
                                print("You have " + str(lives) + " lives left")
                                for i in range(len(wordArray)):
                                        if guess is wordArray[i]:
                                                display[i] = guess
                        else:
                            print("You already guessed that!")
                    else:
                        if guess not in wrongArray:
                                print("Incorrect guess, try again!")
                                wrongArray.append(guess)
                                lives = lives - 1
                                print("You have " + str(lives) + " lives left")
                        else:
                            print("You already guessed that wrongly. people never learn from their mistakes :(")
                    if lives <= 0:
                            print("Game over - you ran out of lives. The word was '" + (word) + "'")
                            win = False
                            break
                    if '-' not in display:
                            break
                else:
                    print("please enter a character")
            else:
                print("pleaase enter a valid character")
                    

        if win is True:
                print("Good job! you guessed '" + str("".join(display)) + " 'correctly")

                
    elif dif == ("2"):
            word = random.choice(dicM)
            wordArray = list(word)
            display = ['-' for x in wordArray]
            lives = 10
            wrongArray = []
            win = True
            print("Medium Mode! Five letters: -----")
            while True:
                print("".join(display))
                guess = input("Enter a guess: ")
                        
                        
                if guess in alphalist:
                    if guess != (""):
                        
                        if guess in wordArray:
                            if guess not in display:
                                    print("You found a letter!")
                                    print("You have " + str(lives) + " lives left")
                                    for i in range(len(wordArray)):
                                            if guess is wordArray[i]:
                                                    display[i] = guess
                            else:
                                print("You already guessed that!")
                        else:
                            if guess not in wrongArray:
                                    print("Incorrect guess, try again!")
                                    wrongArray.append(guess)
                                    lives = lives - 1
                                    print("You have " + str(lives) + " lives left")
                            else:
                                print("You already guessed that wrongly. people never learn from their mistakes :(")
                        if lives <= 0:
                                print("Game over - you ran out of lives. The word was '" + (word) + "'")
                                win = False
                                break
                        if '-' not in display:
                                break
                    else:
                        print("please enter a character")
                else:
                    print("pleaase enter a valid character")
                        

            if win is True:
                    print("Good job! you guessed '" + str("".join(display)) + " 'correctly")

            
        
    elif dif == ("3"):
            word = random.choice(dicH)
            wordArray = list(word)
            display = ['-' for x in wordArray]
            lives = 10
            wrongArray = []
            win = True
            print("Hard Mode! Seven letters: -------")
            while True:
                print("".join(display))
                guess = input("Enter a guess: ")
                        
                        
                if guess in alphalist:
                    if guess != (""):
                        
                        if guess in wordArray:
                            if guess not in display:
                                    print("You found a letter!")
                                    print("You have " + str(lives) + " lives left")
                                    for i in range(len(wordArray)):
                                            if guess is wordArray[i]:
                                                    display[i] = guess
                            else:
                                print("You already guessed that!")
                        else:
                            if guess not in wrongArray:
                                    print("Incorrect guess, try again!")
                                    wrongArray.append(guess)
                                    lives = lives - 1
                                    print("You have " + str(lives) + " lives left")
                            else:
                                print("You already guessed that wrongly. people never learn from their mistakes :(")
                        if lives <= 0:
                                print("Game over - you ran out of lives. The word was '" + (word) + "'")
                                win = False
                                break
                        if '-' not in display:
                                break
                    else:
                        print("please enter a character")
                else:
                    print("pleaase enter a valid character")
                        

            if win is True:
                    print("Good job! you guessed '" + str("".join(display)) + " 'correctly")
                    
        

