# --- Day 1: Historian Hysteria ---

def main():
    left = []
    right = []

    with open('input-1-2.txt', 'r') as f:
        for line in f.readlines():
            numbers = line.split('   ')
            left = insert(left, int(numbers[0].rstrip()))
            right = insert(right, int(numbers[1].rstrip()))
    
    similarity_score = 0
    index_right = 0
    for i in range(len(left)):
        # Find how many instances of the current number are in left
        left_mult = 0
        while i + left_mult < len(left) and left[i] == left[i + left_mult]:
            left_mult += 1

        # Find how many instances of the current number are in right
        right_score = 0
        while right[index_right] <= left[i]:
            if right[index_right] == left[i]:
                right_score += right[index_right]
            index_right += 1
        
        similarity_score += left_mult * right_score
    
    print("Similarity score: " + str(similarity_score))

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
