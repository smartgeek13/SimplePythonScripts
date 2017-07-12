number = 13
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('****!!!Congratulations, you guessed it!!!****')
        # this causes the while loop to stop
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('Well Done.')
    # Add some more code or comments...

#print('Done')
