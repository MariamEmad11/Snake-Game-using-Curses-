# Snake-Game-using-Curses- 

https://replit.com/@MariamEmad11/Snakegame#main.py 

This is a simple snake game implemented in Python using the curses library. The game creates a window and allows the player to move the snake around to eat food and grow longer. The game loop continues until the player loses or quits.

![Snake-Game-in-py](https://user-images.githubusercontent.com/88942103/231101708-d74a6072-0412-477d-a8be-076ace3b9d71.jpg)  

Here is how the game works:

1-The game initiates the curses library to create the screen and hides the mouse.

2-The maximum screen size (height and width) is retrieved using the getmaxyx function and assigned to screen_hight and screen_width.

3-A new window is created using the newwin function and keypad is enabled to allow input from the keyboard.

4-The initial position of the snake is defined using snake_x and snake_y.

5-The initial position of the snake body is defined as an array containing three coordinates: the head, body, and tail.

6-A food object is created in the center of the screen.

7-The game loop begins, and the player can move the snake using the arrow keys.

8-If the snake hits the wall or itself, the game ends, and the program quits.

9-The snake's head position is updated based on the player's input, and the new position is added to the front of the snake array.

10-If the snake eats the food, a new food object is generated at a random position on the screen, and the snake grows longer.

11-If the snake doesn't eat the food, the tail is removed, and the snake's position is updated on the screen.


Overall, this is a fun and straightforward game that demonstrates how to use the curses library to create a game in Python.




https://user-images.githubusercontent.com/88942103/231110568-32a4fa9a-ae95-4703-adde-a6a7f4ed15b7.mp4


