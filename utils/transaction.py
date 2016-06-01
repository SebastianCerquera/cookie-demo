#! /usr/bin/python


import sys
import itertools as it

entries = sys.stdin.read().split('\n')
entries.pop()
rpt = int(entries.pop(0))

entries = map(lambda x:  x.split(','), entries)


def group(entries):
    groups = {}
    # FIXME evitar copias innecesarias
    data = sorted(entries, key=lambda x:x[5])
    for k, g in it.groupby(data, key=lambda x:x[5]):
        groups[k] = list(g)
    return groups


def transactions(thread, entries):
    upper = len(entries)
    upper = upper - (upper % rpt)
    if upper == 0:
        print >> sys.stderr,'El thread {:s} solo lanzo una peticion'.format(thread)
        return []

    # FIXME evitar copias innecesarias
    entries = sorted(entries, key=lambda x:x[0])
    
    results = []
    for i in xrange(0, upper, rpt):
        elapsed = reduce(lambda a, b: b + a, map(lambda e: int(e[1]), entries[i:i+rpt-1]))
        int(entries[i+rpt-1][0]) + int(entries[i+rpt-1][1]) - int(entries[i][0])
        if int(entries[i][0]) + int(entries[i][1]) > int(entries[i+rpt-1][0]):
            print >> sys.stderr,'{:s} + {:s} > {:s}'.format(entries[i][0], entries[i][1], entries[i+rpt-1][0])
        # FIXME El calculo de los bytes funciona bien si y solo si las transacciones esta conformadas por 2 peticiones.
        _bytes = int(entries[i+rpt-1][9]) + int(entries[i][9])
        state = "true"
        for j in range(0, rpt):
            if entries[i+j][7] == "false":
                state = "false"
                break
        results.append([entries[i][0],elapsed,"otp",200,"OK",entries[i][5],"text",state,_bytes,entries[i][10],entries[i][11],elapsed])
    for i in xrange(upper, len(entries)):
        print >> sys.stderr,'{:s},{:s},{:s} no tiene una repuesta'.format(entries[i][0], entries[i][2], entries[i][5])
    return results
        
        
def build(groups):
    for g in groups.keys():
        groups[g] = transactions(g, groups[g])
    return groups


def printer(groups):
    print "timeStamp,elapsed,label,responseCode,responseMessage,threadName,dataType,success,bytes,grpThreads,allThreads,Latency"
    for g in groups.keys():
        for e in groups[g]:
            print "{:d},{:d},{:s},{:d},{:s},{:s},{:s},{:s},{:d},{:d},{:d},{:d}".format(int(e[0]), int(e[1]), e[2], int(e[3]), e[4], e[5], e[6], e[7], int(e[8]), int(e[9]), int(e[10]), int(e[11]))
            
    
printer(build(group(entries)))
lambda a: etl.select(groupThreads(results, a), 'threadName')
    


