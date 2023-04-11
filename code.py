# import modules
import random as rd
import curses as cr

# initiate the curses library to creat our screen
screen = cr.initscr()
# hide the mouse
cr.curs_set(0)
# getmax screen (hight and width) , #unpacking
screen_hight, screen_width = screen.getmaxyx()
# creat a new window
window = cr.newwin(screen_hight, screen_width, 0, 0)
# allaw window to receve inpute from the keyboard
window.keypad(1)
# set the delay for updating the screen
window.timeout(100)
# set the x and y coordinates of the initial position of the sankes's head
snake_x, snake_y = screen_width // 4, screen_hight // 2
# define the initial position of the snake body
snake = [[snake_y, snake_x], #head
         [snake_y, snake_x - 1], #body
         [snake_y, snake_x - 2] # last point (tail)
        ] 
# creat the food of the middle of the window
food = [screen_hight // 2, screen_width // 2]
# add the food shape by using Curses.ACS characters
window.addch(food[0], food[1], cr.ACS_STERLING)
# set initial motion direction of the snake to the right
key = cr.KEY_RIGHT
# create game loop that continue until the player loses or quits
while True:
    # get the next key that will be pressed by the user
    next_key = window.getch()
# if the user dose not inpute anything, key remains the same, else key will be equal to the next pressed key
    key = key if next_key == -1 else next_key
# check if the snake messes up with the walls or itself ?
    if snake[0][0] in [0, screen_hight] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
# if answer is yes, close the window and exit tge program
      cr.endwin()
      quit()
#set the new position of the snake head based on the direction
    new_head = [snake[0][0] , snake[0][1]]

    if key == cr.KEY_LEFT:
      new_head[1] -=1 
    if key == cr.KEY_RIGHT:
      new_head[1] +=1
    if key == cr.KEY_UP:
      new_head[0] -=1
    if key == cr.KEY_DOWN:
      new_head[0] +=1
#insert the new head to the to the first position of the snake
    snake.insert( 0 , new_head)
#check if the snake ate the food and remove the food if the snake ate it
    if snake[0] == food:
      food = None
#while food is removed, generate a new food in a randoom place
      while food is None:
        new_food = [ rd.randint(1, screen_hight -1),
              rd.randint(1, screen_width -1)
             ]
#set the new food on food and generate the food if only it wasnt on the snake's body
        food = new_food if new_food not in snake else None
      window.addch(food[0], food[1], cr.ACS_STERLING)
#otherwise remove the last segment of the snake's body (tail)
    else:
      tail = snake.pop()
      window.addch(tail[0], tail[1] , ' ')
#update the posision of the snake on the screen
    window.addch(snake[0][0], snake[0][1], cr.ACS_CKBOARD)