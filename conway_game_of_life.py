import random
import time
import copy

WIDTH = 60
HEIGHT = 20

# list of lists for cells

next_cells = []

for x in range(WIDTH):
    column = [] # creates new columns
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') # adds living cell
        else:
            column.append('') # adds dead cell
    next_cells.append(column) # list of column lists

while True: # main program loop
    print('\n\n\n\n\n') # separate steps with newlines
    current_cells = copy.deepcopy(next_cells)

    # print current_cells on screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='') # print the actual '#' or '' markers
        print()
    
    # calculate the next steps's cells based on the current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # grab neighboring coordinations
            # % WIDTH endsures left coordinate is always bettwen 0 and WIDTH -1
            left_coordinate = (x - 1) % WIDTH
            right_coordinate = (x + 1) % WIDTH
            above_coordinate = (y - 1) % HEIGHT
            below_coordinate = (y + 1) % HEIGHT

            # counts living neighbors:
            num_neighbors = 0
            
            if current_cells[left_coordinate][above_coordinate] == '#':
                num_neighbors += 1 # tracks top left neighbor as alive
            if current_cells[x][above_coordinate] == '#':
                num_neighbors += 1 # top neighbor is alive
            if current_cells[right_coordinate][above_coordinate] == '#':
                num_neighbors += 1 # tracks top right neighbor as alive
            if current_cells[left_coordinate][y] == '#':
                num_neighbors += 1 # left neighbor is alive
            if current_cells[right_coordinate][y] == '#':
                num_neighbors += 1 # tracks right neighbor as alive
            if current_cells[left_coordinate][below_coordinate] == '#':
                num_neighbors += 1 # bottom left neighbor is alive
            if current_cells[x][below_coordinate] == '#':
                num_neighbors += 1 # bottom neighbor is alive
            if current_cells[right_coordinate][below_coordinate] == '#':
                num_neighbors += 1 # bottom right neighbor is alive