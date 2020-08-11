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



number_of_Host = 60
number_of_VM = 1133
Queue_VM = [] 
Run_VM = [] 
Complete_VM = []
Detect_Policy = ['static_threshold','MAD','LR']
VM_Selection_Policy = ['random_choice', 'high_usage','low_usage']
Host_Selection_Policy = ['random_choice', 'low_cpu_usage', 'low_cpu_low_disk', 'MMEHS', 'ha']
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
Activated_Host_list, Run_VM = module.initialize(Host_list, VM_list, Run_VM, Order, Detect_Policy, VM_Selection_Policy) 

print("---- Initailize - [done]\n")
print("---- Start System ...")
##time.sleep(2)
module.Number_of_migration = 0
i = 0 
while Run_VM or schedule : 
    # flag =0
    # for j in Host_list :
    #     if j.Status != 'Shutdown' :
    #         flag = 1 
    #         break
    # if flag == 0 :
    #     module.print_current_status()
    #     break 
    # else : 
    module.executing_1Cycle(Activated_Host_list, VM_list, Run_VM, Queue_VM, schedule, Order, Detect_Policy, VM_Selection_Policy, Host_Selection_Policy, i)
    i += 1