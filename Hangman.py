from Hangman_graphic import *

word = 'mississippi'
turns = len(word)
wrong = 0
count = 6 #6 chances in hangman

print('Num of character: ' + '_ '*turns)
answer = list('_') * turns #store correct answer in sequence

while count > 0:
    user_input = raw_input('guess a character--> ')

    if user_input not in word:
        count -= 1 #only decrement count when answer is wrong
        print ('wrong! u have ' + str(count) + ' more guesses')
        wrong += 1 #just to print out the hangman
        hangman_graphic(wrong)
        flag = 'LOOSE'
    else:
        for j in range(len(word)):
            if user_input == word[j]:
                answer[j] = user_input #to place the character in sequence
        print ' '.join(answer) #to let player know their current answer
        flag = 'WON'
        if answer == list(word): #if all correct, then win
            break

if flag == 'WON':
    print 'YOU WON'
else:
    print 'YOU LOOSE'













