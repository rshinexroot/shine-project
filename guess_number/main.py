# This is a game for guessing a number by user which will equal to computer's random number
# If a user will guess correct, it will get also full score,
# Otherwise decrease the score with hint on next chance
# Let's start to make program for it

import random
import first_hint
import last_hint
print('\n Hello User, This is a fun game with computer. Play this game and enhance your logic skills also make high score.')
print(' Computer has a random number. Could you know what is that number ?')
score=0
while True:
    rand_number = random.randrange(1, 100)
    # print(rand_number)
    while True:
        print()
        guess_number = int(input(' Guess that random number and enter here: '))
        if rand_number == guess_number:
            print(f' Excellent, You guess {guess_number} correct number.')
            score = score + 5
            print(f' Your score increase by 4 and now, your score is {score}.')
            like_game=input(' Do you like this game? ---> Enter y/n : ')
            if like_game=='y' or like_game=='n':
                break
        else:
            if score >= 4:
                score = score - 4
                print(f' Your score decrease by 4. Now, you have {score} score.', end=" ")
                first_hint.hint_by_number(rand_number)
            elif score > 4 and score >=0:
                score = score - 4
                print(f' Your score decrease by 4. Now, you have {score} score.', end=" ")
                last_hint.div_by_number(rand_number)
            else:
                print(f' Guess number is not matched. That random number is {rand_number}.')
                print(f' No more chance because your score {score} is less than 0.')
                like_game = input('Do you like this game? ---> Enter y/n : ')
                if like_game == 'y' or like_game == 'n':
                    break
    play_want = input(' Do you want to play again?  --->  Enter y/n : ')
    if play_want == 'n':
        break
