# --- Day 4: Ceres Search ---

grid = []
found = 0
current_str = ''

def main():
    # Instantiate grid
    with open('input-4-1.txt', 'r') as f:
        for line in f.readlines():
            grid.append(list(line.rstrip()))

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'X':
                find_xmas(x, y, -1, -1) # down left
                find_xmas(x, y, -1, 0) # left
                find_xmas(x, y, -1, 1) # up left
                find_xmas(x, y, 0, -1) # down
                find_xmas(x, y, 0, 1) # up
                find_xmas(x, y, 1, -1) # down right
                find_xmas(x, y, 1, 0) # right
                find_xmas(x, y, 1, 1) # up right
   
    print("XMAS found: " + str(found))

def find_xmas(x_pos, y_pos, x_dir, y_dir):
    global found
    global current_str
    
    if not is_valid_position(x_pos, y_pos):
        current_str = ''
        return
    
    current_str += grid[y_pos][x_pos]

    if current_str == 'XMAS':
        current_str = ''
        found += 1
        return
    
    if len(current_str) >= 4:
        current_str = ''
        return
    
    find_xmas(x_pos + x_dir, y_pos + y_dir, x_dir, y_dir)
    
def is_valid_position(x_pos, y_pos):
    if x_pos < 0 or x_pos >= len(grid[0]):
        return False
    
    if y_pos < 0 or y_pos >= len(grid):
        return False
    
    return True

main()
