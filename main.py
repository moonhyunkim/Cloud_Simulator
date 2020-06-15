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



number_of_Host =100
number_of_VM=1006
Queue_VM = [] 
Run_VM = [] 
Complete_VM = []
Detect_Policy = ['static_threshold','MAD','LR']
VM_Selection_Policy = ['Random', 'High_Usage']

#Order = [k for k in range(1,number_of_VM+1)]
Order = module.Order
schedule = module.schedule

print("---- Start initializing ...")
##time.sleep(2)
print("---- [1] Create Host ...")
Host_list = module.create_Host(number_of_Host)
##time.sleep(1)
print("---- [2] Create VM ...")
VM_list = module.create_VM(number_of_VM)
##time.sleep(1)

#초기화된 호스트 리스트 전달 받음
Activated_Host_list, Run_VM = module.initialize(Host_list, VM_list, Run_VM, Order, Detect_Policy[0], VM_Selection_Policy[0]) 

print("---- Initailize - [done]\n")
print("---- Start System ...")
##time.sleep(2)
module.Number_of_migration = 0
i = 0 
while Run_VM or schedule : 
    module.executing_1Cycle(Activated_Host_list, VM_list, Run_VM, Queue_VM, schedule, Order, Detect_Policy[0], VM_Selection_Policy[0], i)
    i += 1
