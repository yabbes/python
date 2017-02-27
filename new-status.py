#!/usr/bin/env python3
import os
import time
from datetime import datetime


def loopCheck():
        uptime_string = os.popen('uptime').read()
        formatted_df_string = parse_df_string()
        extra_info = get_extra_info()
        f = open("/home/yabbes/www/status", "w")
        f.write("<h1>yabPI status report</h1>"
                "<p>{}</p>"
                "<p>{}</p>"
                "<p>{}</p>".format(uptime_string,
                                   formatted_df_string,
                                   extra_info))
        f.close()


def parse_df_string():
        df_string_root = list(get_root())
        path, size, used, avail, percent, mount = df_string_root[0].split()
        return "{}({}) of {} in use".format(percent, used, size)


def get_extra_info():
        extra = os.popen("uname -a | awk ' {print $2 \" \" "
                         "$3 \" \" $11 \" \" $12 }'").read()
        return extra


def get_root():
        df_string = os.popen('df -h').read()
        df_string_l = df_string.split('\n')
        return filter(lambda x: x.startswith('/dev/root'), df_string_l)


def main():
        while True:
                time.sleep(30)
                loopCheck()
                print("Server is still alive {}".format(datetime.now()))


if __name__ == '__main__':
        main()
