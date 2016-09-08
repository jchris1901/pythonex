import random

#f = open("words.txt","r")
WORDS=['new',
'bad',
'easy',
'difficult',
'sad',
'tough',
'screwed',
'fucked']#f.readlines()

def random_word():
    word = random.choice(WORDS)
    return word
##chooses a random word from the list

def jumble(word):
    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position +1):]
    return jumble
##jumbles the word

def play(word,jumble):
    print jumble
##prints jumbled version

##getting the player's guess

    guess = raw_input("\nGuess: ")
    guess = guess.lower()
    while (guess != word):  
            print "Wrong"
            guess = raw_input("Guess: ")
            guess = guess.lower()
    print "Right"

##putting the functions together
def main():
    the_word = random_word()
    the_jumble = jumble(the_word)
    play(the_word, the_jumble)

main()
#f.close()