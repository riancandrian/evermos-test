import curses
from random import randint
# setup windows
curses.initscr()
win = curses.newwin(10, 27, 0, 0) # y, x
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

# obstacle
obstacle = [(2,10), (2,11), (2,12), (2,13), (2,14), (2,15), (2,16), (2,17), 
            (3,10), (3,17), 
            (4,10), (4,12), (4,13), (4,14), (4,17),
            (5,10), (5,14), (5,16), (5,17), 
            (6,10), (6,12), (6,17), 
            (7,10), (7,11), (7,12), (7,13), (7,14), (7,15), (7,16), (7,17)]

person = (6, 11)

treasure = (5, 15)

# game logic 
score = 0

ESC = 27
key = win.getch()

while key != ESC:
    win.addstr(0,2, 'Score ' + str(score) + ' ')
    event = win.getch()

    y = person[0]
    x = person[1]

    # move person
    if event == curses.KEY_DOWN:
        y += 1
    if event == curses.KEY_UP:
        y -= 1
    if event == curses.KEY_LEFT:
        x -= 1
    if event == curses.KEY_RIGHT:
        x += 1

    # if person hit border
    if person in obstacle[1:]: break 

    win.addch(person[0], person[1], ' ')
    person = (y, x)

    # if person found treasure
    if person == treasure:
        score +=1
        treasure = ()
        while treasure == ():
            treasure = (randint(3, 6), randint(11, 16))
            if treasure in obstacle:
                treasure = ()
        win.addch(treasure[0], treasure[1], ' ')

    for c in obstacle:
        win.addch(c[0], c[1], '#')
    
    win.addch(person[0], person[1], 'X')

curses.endwin()
print("Final Score = "+ str(score) +" ")