#!/usr/bin/env python3
import subprocess
import time
import sys
import os

CMD_TEMPLATE = '/usr/bin/env python3 {0}'
DEFAULT_SLEEP = 2


def exec_program(prog):
    cmd = CMD_TEMPLATE.format(os.path.realpath(prog))
    out = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    out = out.communicate()[0]
    return out.decode().strip()


def main():
    lenarg = len(sys.argv)
    if lenarg != 2:
        print("Please specify a program.")
        sys.exit(1)

    pname = sys.argv[1]
    if not os.path.isfile(pname):
        print("\"{0}\" is not a file!".format(pname))
        sys.exit(1)
    
    while True:
        print(exec_program(pname))
        time.sleep(DEFAULT_SLEEP)
        os.system('clear')

if __name__ == '__main__':
    main()
