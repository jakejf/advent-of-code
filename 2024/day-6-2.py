# --- Day 6: Guard Gallivant ---

def main():
    grid = []
    start_pos = []
    line_number = 0
    with open('input-test.txt', 'r') as f:
        for line in f.readlines():
            row = parse_row(line.strip(), start_pos, line_number)
            grid.append(row)
            line_number += 1

    obstacles = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if start_pos == [x, y] or not grid[y][x]: continue
            if start_pos[0] == x and start_pos[1] < y: continue
            new_grid = grid.copy()
            new_grid[y][x] = False
            print("x = " + str(x) + " | y = " + str(y) + " | " + str(grid[y][x]))
            if is_patrol_looping(start_pos, new_grid): obstacles.append((x, y))
    
    print("Obstacles looped: " + str(len(obstacles)))

def is_patrol_looping(start, grid):
    visited = []
    position = (start[0], start[1])
    direction = (0, -1)
    while not is_goal(position, grid):
        visited.append(position)
        while not is_next_free(position, direction, grid):
            direction = turn_right(direction)
        position = next_position(position, direction)
        if is_loop(visited): return True

    return False

def is_loop(visited): # change this! if we visit the same square facing the same direction, we've looped!
    if len(visited) <= 8: return False
    return visited[len(visited) - 4:len(visited) - 1] == visited[len(visited) - 8:len(visited) - 5]

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
