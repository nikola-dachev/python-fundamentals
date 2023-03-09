import random

player_wins = 0
computer_wins = 0
ties = 0

while True:

    rock = 'Rock'
    paper = 'Paper'
    scissors = 'Scissors'
    player_move = input('Choose [r]ock, [p]aper,[s]cissors: ')

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit('Invalid input. Try again...')

    options = [rock, paper, scissors]

    computer_move = random.choice(options)

    if computer_move == 'r':
        computer_move = rock
    elif computer_move == 'p':
        computer_move = paper
    elif computer_move == 's':
        computer_move == scissors

    print(f'\nYou choose {player_move} Computer chooses {computer_move}\n')

    if computer_move == player_move:
        ties += 1
        print(f'Both players chose {player_move}.It is a tie')

    elif computer_move == scissors:
        if player_move == rock:
            player_wins += 1
            print(f'Rock smashes scissors.You win')
        else:
            computer_wins += 1
            print(f'Scissors cut papper. You loose')

    elif computer_move == rock:
        if player_move == scissors:
            computer_wins += 1
            print(f'Rock smashes scissors.You loose')
        else:
            player_wins += 1
            print(f'Paper covers rock. You win')

    elif computer_move == paper:
        if player_move == rock:
            computer_wins += 1
            print(f'Paper covers rock. You loose')
        else:
            player_wins += 1
            print(f'Scissors cut paper.You win')

    another_game = input(f'\nAnother game? y/n:\n')
    if another_game != 'y':
        break

print(f'Computer won: {computer_wins} times')
print(f'You won: {player_wins} times')
print(f'Ties: {ties} times')
