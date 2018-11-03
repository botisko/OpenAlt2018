#Rock, paper, scissors simple game

import random


def input_human_play(input=input):
    play = input('Rock, Paper or Scissors? ')
    while not is_valid_play(play):
        play = input('Rock, Paper or Scissors? ')
    return play


def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']


def generate_computer_play():
    return random.choice(['rock','paper','scissors'])


def evaluate_game(human, computer):
    if human == computer:
       return 'tie'
    elif (human == 'rock' and computer == 'paper') or (human == 'paper' and computer == 'scissors') or (human == 'scissors' and computer == 'rock'):
       return 'computer'
    elif (human == 'rock' and computer == 'scissors') or (human == 'paper' and computer == 'rock') or (human == 'scissors' and computer == 'paper'):
       return 'human'
    else:
       return 'unknown'


def main(input=input):
    human = input_human_play(input)
    computer = generate_computer_play()

    print(computer)
    game = evaluate_game(human, computer)
    if game == 'tie':
        print('it is a tie')
    else:
        print(f'{game} won')


if __name__ == '__main__':
    main()
