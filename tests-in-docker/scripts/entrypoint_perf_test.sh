#!/bin/bash -ex

cp test.robot /tmp/

for i in {1..50} ;
do cp suites/perf_test.robot /tmp/${i}-perf_test.robot ; done

pabot --processes 25 --console verbose --outputdir reports /tmp/*perf_test.robot