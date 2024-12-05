# --- Day 2: Red-Nosed Reports ---

def main():
    reports = []

    with open('input-2.txt', 'r') as f:
        for line in f.readlines():
            reports.append(line.rstrip().split(' '))

    safe = 0
    for report in reports:
        if is_safe(report, 0):
            safe += 1

    print("Safe reports: " + str(safe))

def is_safe(report, attempts):
    if attempts > 1:
        return False

    report = [int(n) for n in report]

    # If the first and last are equal, it can't be safe
    if report[0] == report[len(report) - 1]:
        return len(report) == 2 and attempts == 0
    
    # Increasing values
    if report[0] < report[len(report) - 1]:
        for i in range(len(report) - 1):
            diff = abs(report[i] - report[i + 1])
            if report[i] > report[i + 1] or diff == 0 or diff > 3:
                left = report.copy()
                left.pop(i)
                report.pop(i + 1)
                return is_safe(report, attempts + 1) or is_safe(left, attempts + 1)
    
    # Decreasing values
    if report[0] > report[len(report) - 1]:
        for i in range(len(report) - 1):
            diff = abs(report[i] - report[i + 1])
            if report[i] < report[i + 1] or diff == 0 or diff > 3:
                left = report.copy()
                left.pop(i)
                report.pop(i + 1)
                return is_safe(report, attempts + 1) or is_safe(left, attempts + 1)

    return True

main()
