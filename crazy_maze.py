
hard_maze = [
"+++++ ++++++++++++++",
"+ s            +   +",
"+ ++++++++++++ +++ +",
"+ +          +     +",
"+ + ++++++ + +++++ +",
"+++ +    + + +     +",
"  + + ++ +++ + +++ +",
"+ + + +      +   + +",
"+ + + ++++++ + + +++",
"+   +      + + +   +",
"+ + +++ ++ + +++++ +",
"+ +   + +  +       +",
"+++++ + ++ +++++++++",
"+   + +  +          ",
"+ + + ++++++ +++++++",
"+ +++ +      +     +",
"+     + ++++++++++ +",
"+   + +            +",
"+++++ ++++++ +++++++",
"+                  +",
"++++++++++++++e+++++",
"+ s            +   +",
"+ ++++++++++++ +++ +",
"+ +          +     +",
"+ + ++++++++ +++++ +",
"+++ +      + +     +",
"+ + + ++ +++ + +++ +",
"+ + + +      +   + +",
"+ + + ++++++ + + +++",
"+   +      + + +   +",
"+ + +++ ++ + +++++ +",
"+ +   + +  +       +",
"+++++ + ++++++++++++",
"+   + +             ",
"+ + + ++++++ +++++++",
"+ +++ + +    +     +",
"+     + ++ +++ +++ +",
"+   + +          + +",
"+++++ ++++++ +++++++",
"+                  +",
"++++++++++++++e+++++",
]

obstacle_list = []


def create_random_obstacles():
    """
    This function generates random obstacles
    in the range of 1-10
    between -99, 99 and -199,199
    """

    obstacles = []

    for y in range(len(hard_maze)):
        for x in range(len(hard_maze[y])):
            symbol = hard_maze[y][x]
            window_x = -100 + (x * 10)
            window_y = 200 - (y * 10)
            if symbol == '+':
                # my_maze.setposition(-100,-200)
                obstacles.append((window_x,window_y))
    
    return obstacles


def is_position_blocked(x, y):
    """
    This function returns True if position (x,y) falls inside an obstacle.
    """
    for x1,y1 in obstacles_list:
        if x1 <= x <= x1+10 and y1 <= y <= y1+10:
            return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    This function returns True if there is an obstacle
    in the line between the coordinates (x1, y1) and (x2, y2).
    """
    for (x,y) in obstacles_list:
        if x1 == x2 and x <= x1 <= x+10 and (y1 <= y <= y2 or y2 <= y <= y1):
            return True
        if y1 == y2 and y <= y1 <= y+10 and (x1 <= x <= x2 or x2 <= x <= x1):
            return True
    return False


def get_obstacles():
    
    obstacles = create_random_obstacles()
    
    return obstacles