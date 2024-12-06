# --- Day 3: Mull It Over ---

import re

def main():
    text = []

    with open('input-3.txt', 'r') as f:
        text = f.read()

    mults = find_mults(text)
    total = 0
    for i in mults:
        total += int(i[0]) * int(i[1])

    print("Sum of mults is: " + str(total)) 
    
def find_mults(text):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    hits = re.findall(pattern, text)
    return hits

main()
