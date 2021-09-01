#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# IMPORTANT:
# This script must be run with root rights.
#
# sudo -s
# python ssidcollect_linux.py
#
# by Daniel Müllner, muellner@math.stanford.edu
from subprocess import Popen, PIPE, STDOUT
from time import time
from re import search, finditer, MULTILINE
import sys


def collect():
    process = Popen(['iwlist','scan'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    timestamp = time()
    match = finditer('Address: (..:..:..:..:..:..).*\n.*\n.*\n.*Signal level=([-0-9]*) dBm', stdout, MULTILINE)
    for f in match:
        print(timestamp, f.group(1), f.group(2))
        file_out.write( '{0} {1} {2}'.format(timestamp, f.group(1), f.group(2)) + "\n" )


if __name__ == '__main__':

    file_out = open("output","w")

    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        for i in range(n):
            collect()
        exit(0)
    while True:
        collect()
