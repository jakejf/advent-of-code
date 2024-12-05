# --- Day 1: Historian Hysteria ---

def main():
    left = []
    right = []

    with open('input-1-1.txt', 'r') as f:
        for line in f.readlines():
            numbers = line.split('   ')
            left = insert(left, int(numbers[0].rstrip()))
            right = insert(right, int(numbers[1].rstrip()))
    
    total_distance = 0
    for i in range(len(left)):
        total_distance += abs(left[i] - right[i])
    
    print("Total distance: " + str(total_distance))

def insert(list, node):
    index = len(list)

    for i in range(len(list)):
        if list[i] > node:
            index = i
            break
    
    if index == len(list):
        list = list[:index] + [node]
    else:
        list = list[:index] + [node] + list[index:]
    
    return list

main()
