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


# PART 2 :
regex_match = r'do\(\)|don\'t\(\)|mul\(\d+\,\d+\)'
should_do = True
total_with_condition = 0
with open('input_day3.txt') as file:
    for line in file:
        matches = re.findall(regex_match, line)
        for match in matches:
            if 'mul' in match and should_do:
                total_with_condition += eval(match)
            if 'do' in match:
                should_do = True
            if 'don\'t' in match:
                should_do = False

print(total_with_condition)
