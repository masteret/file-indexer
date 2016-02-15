# Simple Distributed File Indexer
# Author: Ka Hei Chan
# email: kaheichan@utexas.edu

import os
import re
import sys
import operator
import argparse
from multiprocessing import Process

# input: python file pointer
# output: none
# print: top 10 words in file/if file has less than 10 words, print all words
def text_processor(text):
    try:
        # read in text from text file
        texts = text.readlines()
        counter = {}
        for text in texts:
            # split each line of text
            processed = re.findall("\w+", text)
            for word in processed:
                word = word.lower()
                if word not in counter:
                    counter[word] = 1
                else:
                    counter[word] += 1

        # sort result
        result = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)
        for x in range(min(10, len(result))):
            print(result[x])
    except UnicodeDecodeError:
        print("only support text file")

# main method
# input: filenames from cmd line (optional) or text from stdin
# output: None
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # capture all the file names
    parser.add_argument("filename", action="store", nargs="*", help="all the filenames")
    namespace = parser.parse_args()
    # if filename is presented, pass file pointer as arg
    if len(namespace.filename) > 0:
        for text_file in namespace.filename:
            if os.path.exists(text_file):
                p = Process(target=text_processor, args=(open(text_file), ))
                p.start()
                p.join()
            else:
                print("Hey dude,", text_file, "doesn't even exist!")
    else:
        # if no filename is present, pass stdin
        text_processor(sys.stdin)