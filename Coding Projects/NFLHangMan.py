import random
print("Please guess an NFL team")
# List of teams to choose from
words = ['patriots', 'colts', 'chargers', 'ravens', 'broncos', 'chiefs', 'cowboys', 'packers', '49ers', 'giants', 'bills', 'cardinals', 'vikings',
'raiders', 'bears', 'seahawks', 'bengals', 'dolphins', 'buccaneers', 'commanders', 'lions', 'saints', 'jets', 'rams', 'panthers', 'texans', 
'browns', 'titans', 'jaguars', 'falcons', 'steelers', 'eagles']

# Select a random word from the list
word = random.choice(words)

# Convert the word to a list of letters
letters = list(word)

# Create a list of underscores to represent the hidden word
hidden = ['_'] * len(letters)

# Track the number of incorrect guesses
mistakes = 0

# Keep playing until the word is guessed or the player makes too many mistakes
while '_' in hidden and mistakes < 6:
    # Print the current state of the game
    print(' '.join(hidden))
    print(f'Guesses left: {6 - mistakes}')
    
    # Prompt the player to guess a letter
    guess = input('Guess a letter: ').lower()
    
    # Check if the guess is correct
    if guess in letters:
        # Update the hidden word with the guessed letter
        for i, letter in enumerate(letters):
            if letter == guess:
                hidden[i] = guess
    else:
        # Increment the number of mistakes
        mistakes += 1
        print(f'Incorrect! You have {6 - mistakes} guesses left.')
        
# Print the final state of the game
print(' '.join(hidden))

# Check if the player won or lost
if '_' not in hidden:
    print('Congratulations! You won!')
else:
    print('Sorry, you lost. The word was', word)