import random

number = random.randrange(0, 10000)
tries = 20
guess = -1
all_tries = list()
val = list()

while tries > 0:
    print('\033c')
    print r'''
 .d8888b.                                          888    888                   888b    888                        888
d88P  Y88b                                         888    888                   8888b   888                        888
888    888                                         888    888                   88888b  888                        888
888        888  888  .d88b.  .d8888b  .d8888b      888888 88888b.   .d88b.      888Y88b 888 888  888 88888b.d88b.  88888b.   .d88b.  888d888 .d8888b
888  88888 888  888 d8P  Y8b 88K      88K          888    888 "88b d8P  Y8b     888 Y88b888 888  888 888 "888 "88b 888 "88b d8P  Y8b 888P"   88K
888    888 888  888 88888888 "Y8888b. "Y8888b.     888    888  888 88888888     888  Y88888 888  888 888  888  888 888  888 88888888 888     "Y8888b.
Y88b  d88P Y88b 888 Y8b.          X88      X88     Y88b.  888  888 Y8b.         888   Y8888 Y88b 888 888  888  888 888 d88P Y8b.     888          X88
 "Y8888P88  "Y88888  "Y8888   88888P'  88888P'      "Y888 888  888  "Y8888      888    Y888  "Y88888 888  888  888 88888P"   "Y8888  888      88888P'
'''
    print '''\nGuess The Number Between 0 and 10000, you have 20 guesses'''
    print "\n Number of tries left: %s\n\n" % tries
    if guess == -1:
        pass
    elif guess == number:
        print '''
Y88b   d88P                       888       888                       888 888 888
 Y88b d88P                        888   o   888                       888 888 888
  Y88o88P                         888  d8b  888                       888 888 888
   Y888P     .d88b.  888  888     888 d888b 888  .d88b.  88888b.      888 888 888
    888     d88""88b 888  888     888d88888b888 d88""88b 888 "88b     888 888 888
    888     888  888 888  888     88888P Y88888 888  888 888  888     Y8P Y8P Y8P
    888     Y88..88P Y88b 888     8888P   Y8888 Y88..88P 888  888      "   "   "
    888      "Y88P"   "Y88888     888P     Y888  "Y88P"  888  888     888 888 888

%s is the correct number
''' % number

        break
    elif guess > number:
        print "Your guess is HIGHER!"
        val.append('HIGH')
    else:
        print "your guess is LOWER!"
        val.append('LOW')
    print "\n\n"
    print "Your Tries: \n"
    for i in xrange(len(all_tries)):
        print "\t%s\t\t%s" % (all_tries[i], val[i])
    print "\n"
    guess = raw_input("Guess the number: ")
    while not guess.isdigit():
        print "\nInvalid Input! Try again! :|\n"
        guess = raw_input("Guess the number: ")
    guess = int(guess)
    all_tries.append(guess)
    tries -= 1
else:
    print "You lost the game :("
