# CLI arg read input

# word processor function

# place to hold count, possibly a dict

"""
read raw input
split by regex (not char nor degit)
loop through each of them
put them in a dict, case insensitive so lower case
sort values and pick top 10
output
"""

import re

if __name__ == '__main__':
    text = input()
    processed = re.split("[\W]", text)
    counter = {}
    for word in processed:
        if word not in counter:
            counter[word] = 0
        else:
            counter[word] += 1
    
    result = sorted(counter.values())
    for x in range(10):
        print(result[x])