#!/usr/bin/python3
import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    string = sys.argv[2]
    founds = re.findall(rf"{re.escape(keyword)}", string)
    if founds:
        print(len(founds))
    else:
        print("none")
