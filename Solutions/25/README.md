### Miss Pacman
If you are not familiar with this game, use this [link](https://www.google.com/search?q=pac-man).

##### Rules :
  - In this game, you have a player and some enemies that can kill the player.
  - Player starts in a particular place and starts moving when user presses a key. From now
the player moves toward the last direction chosen by player until user changes the
direction or player reaches a wall. The player stops moving if reaches a wall.
  - Game map has some blocks and all other places of the map are filled with food.
  - Player can earn score by eating foods and the score must be displayed during the game.
  - Game is over when there is no more food in map or the player is killed by an enemy.
  - Enemies move randomly. (direction in every move is randomly chosen). Two enemies can be at the same place at a time, but enemies cannot move through the walls.
  - The game must have a menu that lets player start a new game and see the high scores.
  - You have to read map (place of each wall) from a file with a given name. (Have to ask for name each time)


##### Map file format
The first line of file has two numbers separated by space and indicates the size of game window (console). (The default size of console is 80 * 24) The second line of file is a number (n) that indicates the number of walls and the next n lines of file are the positions of the walls. (The position lines have two space separated numbers that the first number is x and the second is y).The next line is a number that indicates the number of enemies.
The map file format is “.txt”.


Features like:

  - Saving and loading the game
  - Game pause
  - And other extra features…

are optional and have bonus grade.
