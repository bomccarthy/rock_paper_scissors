import random
import os

def rock(player_choice, comp_count, player_count, ties):
    if player_choice == 'r':
        ties += 1
        print(f'\nRock! Paper! Scissors! SHOOT!!!\n\nMy choice is Rock! You chose Rock!')
        choice = input(f'\nWe tied.\n\nYour Wins: {player_count}  My Wins: {comp_count}  Ties: {ties}\n\nDo you want to play again? "y" or "n"  ')
        os.system('cls')
        if choice == 'y':
            rockPaperScissors(comp_count, player_count, ties)
        elif choice == 'n':
            quit(comp_count, player_count, ties)
        else:
            print('Since you can\'t do simple thing like pick "y" or "n", you\'re outta here!!!\n')
            quit(comp_count, player_count, ties)
    elif player_choice == 'p':
        player_count += 1
        print(f'\nRock! Paper! Scissors! SHOOT!!!\n\nMy choice is Rock! You chose Paper!')
        choice = input(f'\nPaper covers Rock...you win!!!\n\nYour Wins: {player_count}  My Wins: {comp_count}  Ties: {ties}\n\nDo you want to play again? "y" or "n"  ')
        os.system('cls')
        if choice == 'y':
            rockPaperScissors(comp_count, player_count, ties)
        elif choice == 'n':
            quit(comp_count, player_count, ties)
        else:
            print('Since you can\'t do simple thing like pick "y" or "n", you\'re outta here!!!\n')
            quit(comp_count, player_count, ties)
    else:
        comp_count += 1
        print(f'\nRock! Paper! Scissors! SHOOT!!!\n\nMy choice is Rock! You chose Scissors!')
        choice = input(f'\nRock destroys Scissors...I win!!!\n\nYour Wins: {player_count}  My Wins: {comp_count}  Ties: {ties}\n\nDo you want to play again? "y" or "n"  ')
        os.system('cls')
        if choice == 'y':
            rockPaperScissors(comp_count, player_count, ties)
        elif choice == 'n':
            quit(comp_count, player_count, ties)
        else:
            print('Since you can\'t do simple thing like pick "y" or "n", you\'re outta here!!!\n')
            quit(comp_count, player_count, ties)

def paper(player_choice, comp_count, player_count, ties):
    if player_choice == 'p':
        ties += 1
        print(f'\nRock! Paper! Scissors! SHOOT!!!\n\nMy choice is Paper! You chose Paper!')
        choice = input(f'\nWe tied.\n\nYour Wins: {player_count}  My Wins: {comp_count}  Ties: {ties}\n\nDo you want to play again? "y" or "n"  ')
        os.system('cls')
        if choice == 'y':
            rockPaperScissors(comp_count, player_count, ties)
        elif choice == 'n':
            quit(comp_count, player_count, ties)
        else:
            print('Since you can\'t do simple thing like pick "y" or "n", you\'re outta here!!!\n')
            quit(comp_count, player_count, ties)
    elif player_choice == 's':
        player_count += 1
        print(f'\nRock! Paper! Scissors! SHOOT!!!\n\nMy choice is Paper! You chose Scissors!')
        choice = input(f'\nScissors cuts Paper...you win!!!\n\nYour Wins: {player_count}  My Wins: {comp_count}  Ties: {ties}\n\nDo you want to play again? "y" or "n"  ')
        os.system('cls')
        if choice == 'y':
            rockPaperScissors(comp_count, player_count, ties)
        elif choice == 'n':
            quit(comp_count, player_count, ties)
        else:
            print('Since you can\'t do simple thing like pick "y" or "n", you\'re outta here!!!\n')
            quit(comp_count, player_count, ties)
    else:
        comp_count += 1
        print(f'\nRock! Paper! Scissors! SHOOT!!!\n\nMy choice is Paper! You chose Rock!')
        choice = input(f'\nPaper covers Rock...I win!!!\n\nYour Wins: {player_count}  My Wins: {comp_count}  Ties: {ties}\n\nDo you want to play again? "y" or "n"  ')
        os.system('cls')
        if choice == 'y':
            rockPaperScissors(comp_count, player_count, ties)
        elif choice == 'n':
            quit(comp_count, player_count, ties)
        else:
            print('Since you can\'t do simple thing like pick "y" or "n", you\'re outta here!!!\n')
            quit(comp_count, player_count, ties)

def scissors(player_choice, comp_count, player_count, ties):
    if player_choice == 's':
        ties += 1
        print(f'\nRock! Paper! Scissors! SHOOT!!!\n\nMy choice is Scissors! You chose Scissors!')
        choice = input(f'\nWe tied.\n\nYour Wins: {player_count}  My Wins: {comp_count}  Ties: {ties}\n\nDo you want to play again? "y" or "n"  ')
        os.system('cls')
        if choice == 'y':
            rockPaperScissors(comp_count, player_count, ties)
        elif choice == 'n':
            quit(comp_count, player_count, ties)
        else:
            print('Since you can\'t do simple thing like pick "y" or "n", you\'re outta here!!!\n')
            quit(comp_count, player_count, ties)
    elif player_choice == 'r':
        player_count += 1
        print(f'\nRock! Paper! Scissors! SHOOT!!!\n\nMy choice is Scissors! You chose Rock!')
        choice = input(f'\nRock destroys scissors...you win!!!\n\nYour Wins: {player_count}  My Wins: {comp_count}  Ties: {ties}\n\nDo you want to play again? "y" or "n"  ')
        os.system('cls')
        if choice == 'y':
            rockPaperScissors(comp_count, player_count, ties)
        elif choice == 'n':
            quit(comp_count, player_count, ties)
        else:
            print('Since you can\'t do simple thing like pick "y" or "n", you\'re outta here!!!\n')
            quit(comp_count, player_count, ties)
    else:
        comp_count += 1
        print(f'\nRock! Paper! Scissors! SHOOT!!!\n\nMy choice is Scissors! You chose Paper!')
        choice = input(f'\nScissors cuts Paper...I win!!!\n\nYour Wins: {player_count}  My Wins: {comp_count}  Ties: {ties}\n\nDo you want to play again? "y" or "n"  ')
        os.system('cls')
        if choice == 'y':
            rockPaperScissors(comp_count, player_count, ties)
        elif choice == 'n':
            quit(comp_count, player_count, ties)
        else:
            print('Since you can\'t do simple thing like pick "y" or "n", you\'re outta here!!!\n')
            quit(comp_count, player_count, ties)
    pass

def quit(comp_count, player_count, ties):
    print(f'The final tally is...\n\nYour Wins: {player_count}  My Wins: {comp_count}  Ties: {ties}\n')
    print('Good Game!!!')

def choices(comp_count, player_count, ties):
    os.system('cls')
    player_choice = input('Then make your choice. Type "r" for rock, "p" for paper, or "s" for scissors.  ')
    comp_choice = random.choice(['r','p','s'])
    if comp_choice == 'r':
        rock(player_choice, comp_count, player_count, ties)
    elif comp_choice == 'p':
        paper(player_choice, comp_count, player_count, ties)
    elif comp_choice == 's':
        scissors(player_choice, comp_count, player_count, ties)
    else:
        print('What?!? Come on, it\'s "r", "p", or "s"! It\'s not that hard!!!')
        choices(comp_count, player_count, ties)

# --------------------------------- Main Body --------------------------------- #

def rockPaperScissors(comp_count, player_count, ties):
    if comp_count==0 and player_count==0 and ties==0:
        play = input(f'Do you want to play Rock, Paper, Scissors? "y" or "n"  ')
        if play == 'y':
            choices(comp_count, player_count, ties)
        elif play == 'n':
            os.system('cls')
            print('Don\'t waste my time...')
        else:
            os.system('cls')
            print('Do you even know what you are doing. Type something that makes sense.')
            rockPaperScissors(comp_count, player_count, ties)
    else:
        choices(comp_count, player_count, ties)

rockPaperScissors(0,0,0)