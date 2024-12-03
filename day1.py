
import fileinput

def read_input():
    left = []
    right = []
    for line in fileinput.input():
        left_num, right_num = line.strip(' ').split()
        left.append(int(left_num))
        right.append(int(right_num))
    left = sorted(left)
    right = sorted(right)
    total = 0
    for i in range(len(left)):
        total += abs(left[i] - right[i])
    print(total)

if __name__ == '__main__':
    read_input()
