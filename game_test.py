


#
# FYI: this is to satisfy the OPTIONAL testing challenge objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/challenges.md
#

from game import determine_winner


def test_determination_of_the_winner():

    assert determine_winner("rock", "rock") == "It's a tie!"
    assert determine_winner("rock", "paper") == "You lose!"
    assert determine_winner("rock", "scissors") == "You win!"

    assert determine_winner("paper", "rock") == "You win!"
    assert determine_winner("paper", "paper") == "It's a tie!"
    assert determine_winner("paper", "scissors") == "You lose!"

    assert determine_winner("scissors", "rock") == "You lose!"
    assert determine_winner("scissors", "paper") == "You win!"
    assert determine_winner("scissors", "scissors") == "It's a tie!"
