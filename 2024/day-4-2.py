# --- Day 4: Ceres Search ---

grid = []
found = 0

def main():
    # Instantiate grid
    with open('input-4-2.txt', 'r') as f:
        for line in f.readlines():
            grid.append(list(line.rstrip()))

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'A':
                find_xmas(x, y)
    
    print("X-MAS found: " + str(found))

def find_xmas(x_pos, y_pos):
    global found
    
    # Check if diagonals exist
    if not (is_valid_position(x_pos - 1, y_pos - 1) and is_valid_position(x_pos + 1, y_pos + 1)):
        return
    if not (is_valid_position(x_pos - 1, y_pos + 1) and is_valid_position(x_pos + 1, y_pos - 1)):
        return

    forward_diagonal = ''
    forward_diagonal += grid[y_pos - 1][x_pos - 1]
    forward_diagonal += grid[y_pos + 1][x_pos + 1]

    # Check if / contains MAS
    if not (forward_diagonal == 'MS' or forward_diagonal == 'SM'):
        return

    backward_diagonal = ''
    backward_diagonal += grid[y_pos + 1][x_pos - 1]
    backward_diagonal += grid[y_pos - 1][x_pos + 1]

    # Check if \ contains MAS
    if not (backward_diagonal == 'MS' or backward_diagonal == 'SM'):
        return

    found += 1
    
def is_valid_position(x_pos, y_pos):
    if x_pos < 0 or x_pos >= len(grid[0]):
        return False
    
    if y_pos < 0 or y_pos >= len(grid):
        return False
    
    return True

main()
