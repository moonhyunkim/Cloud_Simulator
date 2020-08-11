#! /bin/bash

NUM1=5
NUM2=1
until [ $NUM1 -eq 60 ];
do 
       NUM2=1
       until [ $NUM2 -eq 51 ];
       do
              echo `python3 main.py |tail -10 > Result_6/ThrMuMMEHS_min$(($NUM1))_$NUM2.txt`	
              NUM2=$(($NUM2+1))
       done
       echo `python3 min_time_Test/test_$(($NUM1/5)).py`
       NUM1=$(($NUM1+5))
done


