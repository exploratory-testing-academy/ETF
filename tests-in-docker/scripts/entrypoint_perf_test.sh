#!/bin/bash -ex

cp test.robot /tmp/

for i in {1..50} ;
do cp ./test.robot /tmp/${i}-test.robot ; done

pabot --processes 25 --console verbose --outputdir reports /tmp/*-test.robot
