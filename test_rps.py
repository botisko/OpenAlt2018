import rps
import pytest
import subprocess
import sys


def test_rock_is_valid_play():
    assert rps.is_valid_play('rock') is True


def test_paper_is_valid_play():
    assert rps.is_valid_play('paper') is True


def test_scissors_is_valid_play():
    assert rps.is_valid_play('scissors') is True


def test_lizard_is_invalid_play():
    assert rps.is_valid_play('lizard') is False


def test_spock_is_invalid_play():
    assert rps.is_valid_play('spock') is False


def test_computer_play_is_valid():
    for _ in range(2000):
        play = rps.generate_computer_play()
        assert rps.is_valid_play(play)

def test_computer_plays_randomly():
    plays = [rps.generate_computer_play() for _ in range(2000)]
    rocks = plays.count('rock') 
    papers = plays.count('paper')
    scissors = plays.count('scissors')
    print(rocks, papers, scissors)
    assert rocks > 200
    assert papers > 200
    assert scissors > 200


def test_evaluate_game_computer_paper_win():
    assert rps.evaluate_game('rock', 'paper') == 'computer'


def test_evaluate_game_computer_rock_win():
    assert rps.evaluate_game('scissors', 'rock') == 'computer'


def test_evaluate_game_computer_sciss_win():
    assert rps.evaluate_game('paper', 'scissors') == 'computer'


def test_evaluate_game_human_rock_win():
    assert rps.evaluate_game('paper', 'rock') == 'human'


def test_evaluate_game_human_paper_win():
    assert rps.evaluate_game('paper', 'rock') == 'human'


def test_evaluate_game_human_sciss_win():
    assert rps.evaluate_game('scissors', 'paper') == 'human'


def test_evaluate_game_tie_rock():
    assert rps.evaluate_game('rock', 'rock') == 'tie'


def test_evaluate_game_tie_paper():
    assert rps.evaluate_game('paper', 'paper') == 'tie'


def test_evaluate_game_tie_sciss():
    assert rps.evaluate_game('scissors', 'scissors') == 'tie'


def input_faked_rock(prompt):
    print(prompt)
    return 'rock'


def input_faked_paper(prompt):
    print(prompt)
    return 'paper'


def input_faked_scissors(prompt):
    print(prompt)
    return 'scissors'


def test_full_game(capsys):
    rps.main(input=input_faked_rock)
    captured = capsys.readouterr()
    assert 'Rock, Paper or Scissors?' in captured.out


def test_wrong_play_results_in_repeated_question():
    cp = subprocess.run([sys.executable, 'rps.py'], encoding='utf-8', stdout=subprocess.PIPE, input='dragon\nrock\n', check=True)
    assert cp.stdout.count('Rock, Paper or Scissors?') == 2
