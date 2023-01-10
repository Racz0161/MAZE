import random
import time
import pygame  ###an extension which can demonstrate the animation of the program###




###COLOURS###
YELLOW = (255, 255, 255)
RED = (0, 255, 0,)
GREEN = (0, 0, 255)
YELLOW = (255 ,255 ,0)





###width and height of the maze programme###
HEIGHT = 500
WIDTH = 500




###creates the MAZE programme###
pygame.display.set_caption("MAZE FOR YOU")
pygame.mixer.init()
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))




###variables of the maze###

a = 0       ###x row###
b = 0            ###y row###
w = 20                   ###the width of the cells###







###creates the grid of the programme###
def build_grid(a, b, w):
    for i in range(1,21):
        a = 20
        b = b + 20
        for j in range(1, 21):
            pygame.draw.line(display, YELLOW, [a + w, b], [a + w, b + w]) ###right side of the cell###
            pygame.draw.line(display, YELLOW, [a, b + w], [a, b])  ###left side of the cell###
            pygame.draw.line(display, YELLOW, [a, b], [a + w, b])           ###top side of the cell###
            pygame.draw.line(display, YELLOW, [a + w, b + w], [a, b + w])   ###bottom side of the cell###
            grid.append((a,b))                                            ###adds a cell###
            a = a + 20                                                    ###moves the cell into a new place###





def go_right(a, b):
    pygame.draw.rect(display, GREEN, (a +1, b +1, 39, 19), 0)
    pygame.display.update()

def go_left(a, b):
    pygame.draw.rect(display, GREEN, (a - w +1, b +1, 39, 19), 0)      ###-------------------all this functions indicates the directios the pointer is moving towards###
    pygame.display.update()

def go_up(a, b):
    pygame.draw.rect(display, GREEN, (a + 1, b - w + 1, 19, 39), 0)         


def go_down(a, b):
    pygame.draw.rect(display, GREEN, (a +  1, b + 1, 19, 39), 0)
    pygame.display.update()







def backwards_cell(a, b):
    pygame.draw.rect(display, GREEN, (a +1, b +1, 18, 18), 0)        ###this shows if pointer on a path that has been already visited###

def one_cell( a, b):
    pygame.draw.rect(display, GREEN, (a +1, b +1, 18, 18), 0)          ###single width cell###
    pygame.display.update()

def solution_cell(a,b):
    pygame.draw.rect(display, YELLOW, (a+8, b+8, 5, 5), 0)             ###shows the path found to start to finish###
    pygame.display.update()                                        




grid = []
store = []
solution = {}
inspected = []

def cut_maze(a,b):
    one_cell(a, b)                                              # starting positing of maze
    store.append((a,b))                                           ###method###
    while len(store) > 0:                                          ###loop###
        time.sleep(.07)                                            ###slows down the program a little###
        cell_maze = []

        if (a , b + w) not in inspected and (a , b + w) in grid:      ###------------IF STATEMENTS----------###
            cell_maze.append("down")          

        if (a + w, b) not in inspected and (a + w, b) in grid:       
            cell_maze.append("right")

        if (a, b - w) not in inspected and (a , b - w) in grid:
            cell_maze.append("up")                             

        if (a - w, b) not in inspected and (a - w, b) in grid: 
            cell_maze.append("left")



        if len(cell_maze) > 0:
            chosen = (random.choice(cell_maze))                    ###randomly selects a cell###

            if chosen == "right":
                go_right(a, b)
                solution[(a + w, b)] = a, b
                a = a + w
                inspected.append((a, b))
                store.append((a, b))

            elif chosen == "left":
                go_left(a, b)
                solution[(a - w, b)] = a, b
                a = a - w
                inspected.append((a, b))
                store.append((a, b))

            elif chosen == "down":
                go_down(a, b)
                solution[(a , b + w)] = a, b
                b = b + w
                inspected.append((a, b))
                store.append((a, b))

            elif chosen == "up":
                go_up(a, b)
                solution[(a , b - w)] = a, b
                b = b - w
                inspected.append((a, b))
                store.append((a, b))
        else:
            a, b = store.pop()                                    # if no cells are available pop one from the stack
            one_cell(a, b)                                     # use single_cell function to show backtracking image
            time.sleep(.05)                                       # slow program down a bit
            backwards_cell(a, b)                               # change colour to green to identify backtracking path


def route_back(x,y):
    solution_cell(x, y)               
    while (x, y) != (20,20):                                     
        x, y = solution[x, y]                                    
        solution_cell(x, y)                                      
        time.sleep(.1)



a, b = 20, 20
build_grid(40, 0, 20)             # 1st argument = x value, 2nd argument = y value, 3rd argument = width of cell
cut_maze(a,b)               # calling the creating the maze function###
route_back(400, 400)


#loop#
quit = True
while quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
