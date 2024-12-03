
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

def read_input():
    total = 0
    for line in fileinput.input():
        series = list(map(int,line.strip(' ').split()))
        if is_series(series) and is_series_safe(series):
            total += 1
    print(total)

if __name__ == '__main__':
    read_input()
