import random

number = random.randrange(0,10000)
tries = 20
guess = -1
all_tries = list()
low_tries = list()
high_tries = list()

while tries > 0:
    print('\033c')
    print '''
 ___                                 _    _                _   _                    _                  
(  _`\                              ( )_ ( )              ( ) ( )                  ( )                 
| ( (_) _   _    __    ___   ___    | ,_)| |__     __     | `\| | _   _   ___ ___  | |_      __   _ __ 
| |___ ( ) ( ) /'__`\/',__)/',__)   | |  |  _ `\ /'__`\   | , ` |( ) ( )/' _ ` _ `\| '_`\  /'__`\( '__)
| (_, )| (_) |(  ___/\__, \\\\__, \   | |_ | | | |(  ___/   | |`\ || (_) || ( ) ( ) || |_) )(  ___/| |   
(____/'`\___/'`\____)(____/(____/   `\__)(_) (_)`\____)   (_) (_)`\___/'(_) (_) (_)(_,__/'`\____)(_)   
                                                                                                       
                                                                                                    
'''
    print '''\nGuess The Number Between 0 and 10000, you have 20 guesses'''
    print "\n Number of tries left: %s\n\n" % tries
    if guess == -1:
        pass
    elif guess == number:
        print '''
 _     _                   _       _                _  _  _ 
( )   ( )                 ( )  _  ( )              ( )( )( )
`\`\_/'/'   _    _   _    | | ( ) | |   _     ___  | || || |
  `\ /'   /'_`\ ( ) ( )   | | | | | | /'_`\ /' _ `\| || || |
   | |   ( (_) )| (_) |   | (_/ \_) |( (_) )| ( ) || || || |
   (_)   `\___/'`\___/'   `\___x___/'`\___/'(_) (_)(_)(_)(_)
                                                   (_)(_)(_)
                                                            
%s is the correct number
''' % number

        break
    elif guess > number:
        print "Your guess is higher"
        high_tries.append(guess)
    else:
        print "Your guess is lower"
        low_tries.append(guess)
    print "\n\n\n"
    print "You tires:\n"
    print "All tries: %s" % ','.join(map(str, all_tries))
    print "Low tries: %s" % ','.join(map(str, low_tries))
    print "High tries: %s" % ','.join(map(str, high_tries))
    print "\n\n\n"
    guess = raw_input("Guess the number: ")
    while not guess.isdigit():
        print "\nInvalid Input! Try again! :|\n"
        guess = raw_input("Guess the number: ")
    guess = int(guess)
    all_tries.append(guess)
    tries -= 1
else:
    print "You lost the game :("
