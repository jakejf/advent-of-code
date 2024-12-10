# --- Day 6: Guard Gallivant ---

def main():
    grid = []
    start_pos = []
    line_number = 0
    with open('input-6.txt', 'r') as f:
        for line in f.readlines():
            row = parse_row(line.strip(), start_pos, line_number)
            grid.append(row)
            line_number += 1

    visited = []
    position = (start_pos[0], start_pos[1])
    direction = (0, -1)
    while not is_goal(position, grid):
        visited.append(position)
        while not is_next_free(position, direction, grid):
            direction = turn_right(direction)
        position = next_position(position, direction)
        
    print("Distinct positions: " + str(len(set(visited))))

def is_next_free(start, direction, grid):
    next_pos = next_position(start, direction)
    return is_goal(next_pos, grid) or grid[next_pos[1]][next_pos[0]]

def turn_right(direction):
    if direction == (0, -1): return (1, 0)
    if direction == (1, 0): return (0, 1)
    if direction == (0, 1): return (-1, 0)
    if direction == (-1, 0): return (0, -1)

def next_position(start, direction):
    return (start[0] + direction[0], start[1] + direction[1])

def is_goal(postition, grid):
    return not 0 <= postition[0] <  len(grid[0]) or not 0 <= postition[1] <  len(grid)

def parse_row(line, start_pos, line_number):
    row = []
    for i in range(len(line)): 
        if line[i] == '^': 
            start_pos += i, line_number
        row.append(line[i] !=  '#')
    return row

main()
