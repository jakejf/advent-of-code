# --- Day 5: Print Queue ---

import collections

def main():
    rules = collections.defaultdict(list)
    updates = []
    safe_updates = []
    
    parse_input(rules, updates)

    # Find safe updates
    for update in updates:
        if is_safe_update(rules, update):
            safe_updates.append(update)

    # Calculate sum of middles
    middles = 0
    for update in safe_updates:
        middles += int(update[len(update) // 2])

    print("Sum of middles: " + str(middles))

def parse_input(rules, updates):
    rulesDone = False
    with open('input-5.txt', 'r') as f:
        for line in f.readlines():
            # Check if we've finished parsing the rules
            if len(line.rstrip()) == 0:
                rulesDone = True
                continue

            if not rulesDone:
                # Add rules
                rule = line.rstrip().split('|')
                rules[rule[0]].append(rule[1])
            else:
                # Add updates
                updates.append(line.rstrip().split(','))

def is_safe_update(rules, update):
    visited = []
    for i in range(len(update)):
        for j in visited:
            if j in rules[update[i]]:
                return False
        visited.append(update[i])
    return True

main()
