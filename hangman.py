import random
import sys

words = [];
#Get a list of viable words from SOWPODS dictionary
with open('dic.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        words.append(line);
        line = open_file.readline()

#Main Game Loop
while True:
    word = words[random.randint(0, len(words))]
    guess_list = [];
    guessed = set();
    playing = True;
    left = 6;
    
    # Fill the word being guessed with blanks
    for i in range(len(word) - 1):
        guess_list.append('_')

    # Start playing
    while playing:
        # Print out the current guesses and word progress
        print(''.join(guess_list))
        print('\n')
        print('Guessed letters: ' + ", ".join(guessed));

        # Get a letter from the player
        guess = input('Guess a letter!\n')    
        guess = guess.upper()

        # Replace blanks with guessed letter in word, otherwise mark wrong
        if guess in word and len(guess) == 1 and guess not in guessed:
            count = 0
            print('Nice!')
            if left == 1:
                print(str(left) + ' guess left!')
            else:
                print(str(left) + ' guesses left!')
            for i in word:
                if i == guess:
                    guess_list[count] = guess                    
                count += 1
        elif len(guess) == 1 and guess not in guessed:        
            left -= 1
            if left == 1:
                print('Wrong! ' + str(left) + ' guess left!')
            else:
                print('Wrong! ' + str(left) + ' guesses left!')
        elif len(guess) == 1:
            print('You already guessed that...')
        
        # Add letter to set of guessed letters
        guessed.add(guess)

        # Check for win
        if '_' not in guess_list:
            playing = False
            print('You Win!')
            print('The word was ' + word + '!')
        # Check for loss
        if left <= 0:
            playing = False
            print('You Lose!')
            print('The word was ' + word + '!')

    #Ask for another round
    again = input("Play again? y/n \n")
    if again != "y":
        sys.exit() 
