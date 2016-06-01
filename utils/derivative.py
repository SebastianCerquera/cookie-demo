#! /usr/bin/python

import numpy as np
import pylab as pl

import sys

entries = sys.stdin.read().split('\n')
entries.pop()
entries = map(lambda x: map(float, x.split(',')), entries)


for i in xrange(1, len(entries)):
    print "{:f},{:f}".format(entries[i][0], (entries[i][1] - entries[i-1][1]))

    
    
