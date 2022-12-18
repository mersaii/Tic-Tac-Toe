# Tic-Tac-Toe

**Tic-tac-toe** is a game where two players take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Tic-tac-toe-game-1.svg/958px-Tic-tac-toe-game-1.svg.png"/> 
</div>

In this project, you'll build a complete Tic Tac Toe game.

# Requirements

- Two players should be able to play the game. One chooses X or O.
- The game recognizes three game ends: winning, losing, and drawing.
- Players choose a username before playing. 
  - Two players can pick the same username.
  - Username is a 3 to 12 characters long string.
  - It can't start with a number and can't contain special characters except the dash '-'.
  - Samples of valid usernames are: kibo, victor-d12, spiderman
- Game history (counts of wins and losses per player) must be stored in a file, 
    and there is an option to display them before we start any game.

![image](https://user-images.githubusercontent.com/27410841/203982478-6264a103-177a-4595-bc77-a441528037f3.png)

## Example

You can find [here](https://replit.com/@MohammedSaudi/tick-tac-toe#main.py) a weak and buggy implementation of a simple tic-tac-toe game. It might give you an idea of a simple implementation. You are expected to write cleaner more organized code, and your game should be complete.
![image](https://user-images.githubusercontent.com/27410841/203983540-a096484c-da50-4fb8-a2cb-c323132a3172.png)

## Evaluation

Here's what we'll be looking for when evaluating your project:

- Does the program run without errors?
- Is your code readable and easy to follow?
- Does your code properly use the programming constructs we learned: variables, conditionals, loops, Lists, functions, dictionaries, etc? 

## Rubric

Points | Criteria | Description
 --------- | ------- | ---------
 30 | Program runs without errors | No errors found when running the program and entering different and unexpected user in put
 10 | Menu of options | Program displays a menu of options for the user to choose, and performs the appropriate action whe n they enter the option.
 20 | Game Play | Can successfully play the game of tic-tac-toe
 10 | Player names | Players can choose their names, following the rules
 25 | Game history | Play history is stored to a file and can be displayed
 15 | Code organization | Code is styled well, organized effectively, uses good variable names, comments are clear and app ropriate
