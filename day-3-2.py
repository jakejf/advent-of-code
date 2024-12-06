# --- Day 3: Mull It Over ---

import re

def main():
    text = []

    with open('input-3.txt', 'r') as f:
        text = f.read()

    filtered = filter_do(text)
    mults = find_mults(str(filtered))

    total = 0
    for i in mults:
        total += int(i[0]) * int(i[1])

    print("Sum of mults is: " + str(total)) 

def filter_do(text):
    text_split = re.split('do', text)

    filtered = []
    for i in text_split:
        if i != '' and i != None and not i.startswith("n't()"):
            filtered.append(i)

    return filtered

def find_mults(text):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    hits = re.findall(pattern, text)
    return hits

main()
