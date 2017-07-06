#! /usr/bin/env python3
# simple command line timer for linux

import sys
import time
import os


def main():
    if len(sys.argv) == 1:
        print("no arguments given")
        return
    if str.isdigit(sys.argv[1]) is False:
        print("please supply number of minutes as a number")
        return
    if (str.isdigit(sys.argv[1])):
        print("{} given as argument, will start timer".format(
            sys.argv[1]))
    minutes_set = int(sys.argv[1])
    seconds = minutes_set * 60
    for i in range(seconds, 0, -1):
        time.sleep(1)
        os.system("clear")
        m, s = divmod(i, 60)
        print("%02d:%02d" % (m, s))
    print("{} ::: FINISHED".format(time.ctime()))

if __name__ == '__main__':
    main()
