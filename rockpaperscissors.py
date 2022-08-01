#!/bin/python3

'''
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game)
'''


gameover = ''

def player1_wins():
    print("Player 1 wins!")

def player2_wins():
    print("Player 2 wins!")

while gameover != "quit":

    player1 = str(input("Player 1 type rock, paper, or scissors: "))
    player2 = str(input("Player 2 type rock, paper, or scissors: "))

    if player1 == "rock" and player2 == "paper":
        player1_wins()
    elif player1 == "rock" and player2 == "scissors":
        player2_wins()
    elif player1 == "scissors" and player2 == "rock":
        player2_wins()
    elif player1 == "scissors" and player2 == "paper":
        player1_wins()
    elif player1 == "paper" and player2 == "rock":
        player1_wins()
    elif player1 == "paper" and player2 == "scissors":
        player2_wins()
    elif player1 == player2:
        print("Draw!")
    else:
        print("Unexpected input...")

    gameover = str(input("Type 'quit' to exit or hit enter to play again: "))

