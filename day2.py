
import fileinput

def is_series_safe(series):
    if len(series)== 1:
        return True
    for i in range(1,len(series)):
        if abs(series[i] - series[i-1]) not in [1,2,3]:
            return False
    return True

def is_series(series):
    if series == sorted(series):
        return True
    elif series == sorted(series,reverse=True):
        return True
    return False

def is_series_with_1bad(series):
    # try to remove one element and check if the series is safe
    for i in range(len(series)):
        new_series = series[:i]+series[i+1:]
        if is_series(new_series) and is_series_safe(new_series):
            return True
    return False

def read_input():
    total = 0
    total_with_1_bad = 0
    for line in fileinput.input():
        series = list(map(int,line.strip(' ').split()))
        if is_series(series) and is_series_safe(series):
            total += 1
        elif is_series_with_1bad(series):
            total_with_1_bad += 1

    print(f"PART1: total safe report:{total}")
    print(f"PART2: safe reports with atmost 1 bad levl : {total+total_with_1_bad}")

if __name__ == '__main__':
    read_input()
