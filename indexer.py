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
import operator
import argparse

def text_processor(text):
    texts = text.readlines()
    counter = {}
    for text in texts:
        processed = re.findall("\w+", text)
        for word in processed:
            word = word.lower()
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1

    result = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)
    for x in range(min(10, len(result))):
        print(result[x])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", action="store_true" ,help="if checked, user will be inputting filename")
    parser.add_argument("filename", action="store", nargs="*", help="all the filenames")
    namespace = parser.parse_args()
    if namespace.f:
        for text_file in namespace.filename:
            text_processor(open(text_file))