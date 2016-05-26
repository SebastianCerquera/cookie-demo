#! /bin/bash

mkdir /tmp/performance/baseline && cd /tmp/performance/baseline
/tmp/performance/apache-jmeter-3.0/bin/jmeter.sh -n -t /tmp/performance/plans/baseline.jmx -l /tmp/performance/baseline/results.jtl -j /tmp/performance/baseline/results.log

mkdir /tmp/performance/peak && cd /tmp/performance/peak
/tmp/performance/apache-jmeter-3.0/bin/jmeter.sh -n -t /tmp/performance/plans/peak.jmx -l /tmp/performance/peak/results.jtl -j /tmp/performance/peak/results.log
