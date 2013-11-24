from time import *
from random import *
import pygame

#def plot(coord, rgb):
        #"Plots a coloured point at coord"
        #screen.set_at((int(coord[0]),int(coord[1])), (int(rgb[0]),int(rgb[1]), int(rgb[2])))
        #screen.set_at(coord, rgb)
        #pygame.display.flip()   #refresh the screen - makes this SLOW!

#Initialise pygame
pygame.init()



#Initialise the screen
xmax = 360 #Width of screen in pixels
ymax = 360 #Height of screen in pixels
screen = pygame.display.set_mode((xmax, ymax), 0, 24) #New 24-bit screen

def evolve_cell(alive, neighbours):
    if alive:
        return neighbours in [2, 3]
    return neighbours == 3

def count_neighbours(grid, position):
    x,y = position
    neighbour_cells = [(x-1, y-1), (x-1, y), (x-1, y+1),
                       (x, y-1),             (x  , y+1),
                       (x+1, y-1), (x+1, y), (x+1, y+1)]
    count = 0
    for x,y in neighbour_cells:
        if x >= 0 and y >= 0:
            try:
                count += grid[x][y]
            except:
                pass
    return count

def make_empty_grid(x, y):
    grid = []
    for r in range(x):
        row = []
        for c in range(y):
            row.append(0)
        grid.append(row)
    return grid

def make_random_grid(x, y):
        grid = []
        for r in range(x):
            row = []
            for c in range(y):
                row.append(randint(0,1))
            grid.append(row)
        return grid

def evolve(grid):
    x = len(grid)
    y = len(grid[0])
    new_grid = make_empty_grid(x, y)
    for r in range(x):
        for c in range(y):
            cell = grid[r][c]
            neighbours = count_neighbours(grid, (r, c))
            new_grid[r][c] = 1 if evolve_cell(cell, neighbours) else 0
    return new_grid

BLACK = (0, 0, 0)

def draw_block(x, y, alive_color):
    block_size = 9
    x *= block_size
    y *= block_size
    center_point = ((x + (block_size / 2)), (y + (block_size / 2)))
    pygame.draw.circle(screen, alive_color, center_point, block_size / 2,0)
        

def main():
    h = 0
    cell_number = 0
    cells_that_have_been_alive = []
    cells_that_have_been_dead = []
    dead_color = BLACK
    genaration = 0
    alive_color = pygame.Color(0,0,0)
    alive_color.hsva = [h, 100, 100]
    xlen = xmax / 9
    ylen = ymax / 9
    world = make_random_grid(xlen, ylen)
    while True:
        for x in range(xlen):
            for y in range(ylen):
                alive = world[x][y]
                if alive:
                    cell_color = alive_color
                else:
                    cell_color = dead_color

                draw_block(x, y, cell_color)                       
        pygame.display.flip() 
        h = (h + 2) % 360
        alive_color.hsva = (h, 100, 100)
        sleep(0.5)
        world = evolve(world)
        cell_number = 0

if __name__ == '__main__':
    main()
