# POWER 4

Created by POIX Alexandre and HUMBERT Thomas.
With the library keyboard made by Boppreh 
link to the repo :
https://github.com/boppreh/keyboard

## Objective of this project

Create a power 4 in python completly portable.

## Goals

- line up 4 pawns in a row, column or diagonal

## How to play

Each round, the player need to choose where he wants to put his token (the number of the column).
Every player, even IA, have a special token that can reverse the column where he is put.
To use it, you need to add at the end of your input, the character 'r' or 'R'.
Exemple: '5' -> special token not used
         '5r' or '5R' -> special token is used

## Rules

- 2 players required
- each player plays in turn
- a player choose a column and a pawn is placed at the bottom of the column
- the game ends when a player line up 4 pawns or when the grid is full
- if the grid is full and no player line up 4 pawns, the game is a draw
- each player has a special pawn which can be used to reverse the column
- the special pawn can be used only once per game

## Main Menu

- In the main menu, you can choose between :
    1. SinglePlayer, you will play against the IA
    2. Multiplayer, let's play with a friend
    3. No gaming, you just love to watch IA choose some random numbers
    4. Change the names of the players
    5. Leave the program


