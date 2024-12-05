# --- Day 5: Print Queue ---

import collections

def main():
    rules = collections.defaultdict(list)
    updates = []
    safe_updates = []
    
    parse_input(rules, updates)

    # Calculate sum of middles
    middles = 0
    for update in updates:
        if is_safe_update(rules, update):
            continue
        safe_update = make_safe(rules, update)
        middles += int(safe_update[len(safe_update) // 2])

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

def make_safe(rules, update):
    visited = []
    for i in range(len(update)):
        for j in visited:
            if j in rules[update[i]]:
                update[i], update[update.index(j)] = update[update.index(j)], update[i]
        visited.append(update[i])
    
    if not is_safe_update(rules, update):
        make_safe(rules, update)

    return update

main()
