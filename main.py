"""
Cloud Simulator

 • Author : Moonhyun kim
 • Date : May 15 , 2020
 • Last modified date : May 28, 2020

 • Department of Computer Science at Chungbuk National University
"""

import module
import time
from random import randrange
from random import shuffle                                

number_of_Host = 30
number_of_VM=1006
Queue_VM = [] 
Run_VM = [] 
Complete_VM = []
Detect_Policy = ['static_threshold','MAD','LR']
VM_Selection_Policy = ['Random', 'High_Usage']

Order = [k for k in range(1,number_of_VM+1)]
shuffle(Order)
print(Order)
schedule = [8, 3, 10, 5, 6, 1, 1, 2, 9, 9, 9, 6, 0, 9, 2, 10, 8, 3, 0, 5, 7, 0, 8, 4, 2, 3, 8, 5, 2, 2, 3, 6, 7, 1,
            4, 1, 7, 5, 7, 5, 1, 9, 10, 1, 5, 6, 0, 3, 0, 10, 4, 1, 10, 7, 4, 1, 1, 5, 8, 2, 10, 5, 9, 0, 2, 0, 0, 6,
            1, 10, 0, 4, 10, 5, 8, 7, 5, 1, 7, 10, 0, 2, 9, 9, 9, 3, 5, 4, 1, 5, 10, 1, 6, 0, 3, 2, 2, 8, 6, 5, 1, 8, 
            5, 1, 2, 1, 4, 1, 4, 5, 4, 2, 3, 0, 4, 4, 9, 9, 0, 2, 4, 6, 6, 0, 1, 8, 6, 0, 6, 1, 3, 7, 4, 9, 7, 7, 3, 6, 
            5, 6, 4, 2, 7, 9, 5, 6, 1, 10, 7, 9, 0, 7, 6, 5, 2, 10, 5, 7, 9, 0, 8, 2, 7, 5, 6, 2, 6, 1, 9, 6, 6, 3, 6, 
            6, 3, 2, 1, 3, 10, 3, 9, 3, 3, 9, 6, 8, 7, 2, 0, 9, 4, 4, 2, 6, 9, 2, 6, 10, 9, 6, 5, 4, 10, 9, 1]


print("---- Start initializing ...")
time.sleep(2)
print("---- Create Host ...")
Host_list = module.create_Host(number_of_Host)
time.sleep(1)
print("---- Create VM ...")
VM_list = module.create_VM(number_of_VM)
time.sleep(1)

module.initialize(Host_list, VM_list, Run_VM, Order, Detect_Policy[0], VM_Selection_Policy[0]) 

print("---- Initailize - [done]\n")
print("---- Start System ...")
time.sleep(2)
