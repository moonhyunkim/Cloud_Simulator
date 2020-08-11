#! /bin/bash

NUM1=1

until [ $NUM1 -eq 51 ];
do
       echo `python3 main.py |tail -10 > Result_7/ThrMMTMMEVMP_$NUM1.txt`	
       NUM1=$(($NUM1+1))
done
