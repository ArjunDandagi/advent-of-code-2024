import sys
import re

regex_match = r'mul\(\d+\,\d+\)' # regex pattern to match the number after 'mul'

def mul(a,b):
    return a*b

total = 0

with open('input_day3.txt') as file:
    for line in file:
        matches = re.findall(regex_match, line) # find all matches
        for match in matches:
            total += eval(match) # evaluate the match and add to total

print(total)
