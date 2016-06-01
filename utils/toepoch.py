#! /usr/bin/python

import numpy as np
import pylab as pl
import sys
import time
from datetime import datetime

entries = sys.stdin.read().split('\n')
entries.pop()

print entries.pop(0)
entries = map(lambda x: x.split(','), entries)

for entry in entries:
    results = []
    date = datetime.strptime('{:s} {:s}'.format(entry[0], entry[1]), '%d/%m/%y %H:%M:%S')
    results.append("{:f},".format(time.mktime(date.timetuple())))
    for i in range(2, len(entry) - 1):
        results.append("{:s},".format(entry[i]))
    results.append("{:s}".format(entry[len(entry) - 1]))
    print "".join(results)





