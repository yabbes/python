#! /usr/bin/env python3
# simple command line timer for linux

import sys
import time
import os


def main():
    print("Starting stopwatch...")
    i = 1
    while(True):
        i += 1
        time.sleep(1)
        os.system("clear")
        m, s = divmod(i, 60)
        # '\033[1;42mHighlighted Green like Grass\033[1;m'
        print("\033[1;42m%02d:%02d \033[1;m\nPress 'q' to stop" % (m, s))
    print("{} ::: FINISHED".format(time.ctime()))

if __name__ == '__main__':
    main()
