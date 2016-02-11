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
import sys

if __name__ == '__main__':
    texts = sys.stdin.readlines()
    counter = {}
    for text in texts:
        processed = re.split("[\W]", text)
        for word in processed:
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1

    result = sorted(counter.values(), reverse=True)
    for x in range(10):
        print(result[x])