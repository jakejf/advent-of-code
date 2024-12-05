# --- Day 2: Red-Nosed Reports ---

def main():
    reports = []

    with open('input-2.txt', 'r') as f:
        for line in f.readlines():
            reports.append(line.rstrip().split(' '))

    safe = 0
    for report in reports:
        if is_safe(report):
            safe += 1

    print("Safe reports: " + str(safe))

def is_safe(report):
    report = [int(n) for n in report]

    # If the first and last are equal, it can't be safe
    if report[0] == report[len(report) - 1]:
        return False
    
    # Increasing values
    if report[0] < report[len(report) - 1]:
        for i in range(len(report) - 1):
            diff = abs(report[i] - report[i + 1])
            if report[i] > report[i + 1] or diff == 0 or diff > 3:
                return False
    
    # Decreasing values
    if report[0] > report[len(report) - 1]:
        for i in range(len(report) - 1):
            diff = abs(report[i] - report[i + 1])
            if report[i] < report[i + 1] or diff == 0 or diff > 3:
                return False

    return True

main()
