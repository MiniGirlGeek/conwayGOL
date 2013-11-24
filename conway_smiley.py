from random import *
from time import *

def evolve_cell(alive, neighbours):
	if alive:
		return neighbours in [2, 3]
	return neighbours == 3

def count_neighbours(grid, position):
	x,y = position
	neighbour_cells = 	[(x-1, y-1), (x-1, y), (x-1, y+1),
						 (x, y-1),             (x, y+1),
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

def main():
	world = make_random_grid(16, 16)
	while True:
		for row in world:
			out = ''
			for cell in row:
				out += ' :) ' if cell else '   '
			print out
		sleep(0.2)
		world = evolve(world)

if __name__ == '__main__':
	main()