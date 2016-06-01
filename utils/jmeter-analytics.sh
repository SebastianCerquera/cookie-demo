#! /bin/bash

BASE=$(pwd | xargs dirname)
UTILS=/opt/utils/demo

cat results.jtl | perl -ne 'print $_ if($_ !~ "jp\@gc - Dummy Sampler")' > single.csv

cat single.csv | awk 'BEGIN{print "6"} NR != 1{print $0}' | python $UTILS/transaction.py > transactions.csv 2> errors.log

mkdir $BASE/notebook/
cp -f transactions.csv $BASE/notebook/
cp -f single.csv $BASE/notebook/

