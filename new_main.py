"""
Cloud Simulator - Module

 • Author : Moonhyun kim
 • Date : May  , 2020
 • Last modified date : May 28, 2020

 • Department of Computer Science at Chungbuk National University
"""

from random import randrange
from random import shuffle
import vm_Selection
import detect_Host
import time

class new_Host :
    Host_name = ''
    Host_number = 0
    Host_CPUs = 72
    Host_RAM = 400
    Number_of_Job = 0
    VMs = []
    Total_CPU_Usage = 0.0
    Total_Disk_Usage = 0.0
    Status = ''
    
    def __init__ (self, Hname, Hnumber, Hcpu, Hram, Jnum, VM, TCU, TDU, STAT) :
        self.Host_name=Hname
        self.Host_number=Hnumber
        self.Host_CPUs = Hcpu
        self.Host_RAM = Hram
        self.Number_of_Job = Jnum
        self.VMs = VM
        self.Total_CPU_Usage = TCU
        self.Total_Disk_Usage = TDU
        self.Status = STAT 
    
         
#원하는 개수만큼 호스트 생성
def create_Host(number) :
    Host_list = []
    for i in range(1, number+1): 
        new_host1 = new_Host('Host#'+str(i), i, 72, 400, 0 , [], 0.0, 0.0 , 'Stop')
        #new_host = {'Host_name': 'Host#'+str(i), 'Host_CPUs':72, 'Host_RAM':400, 'Number_of_Job' : 0 , 'VMs':[] , 'Total_CPU_Usage' : 0.0, 'Total_Disk_Usage': 0.0, 'Status':'Stop'}
        Host_list.append(new_host1)
    return Host_list


#원하는 개수만큼 가상머신 생성
def create_VM (number) :
    folder_path = 'usage_data2'
    VM_list = []
    for i in range(1, number+1) :
        f = open(folder_path+'/data'+str(i)+'.txt')
        usage_data = f.readlines()
        new_VM = {'index': i, 'VM_name':'VM#'+str(i), 'Usage': usage_data, 'Current_Time' : 0 , "Execution_Time" : len(usage_data)}   
        VM_list.append(new_VM)
    return VM_list



#시물레이션을 위한 초기화 (Host에 VM할당 // Overload, Underload 탐지)
def initialize (Host_list, VM_list, Run_VM, Order, Detect_Policy, VM_Selection_Policy) :
    for i in range(1,31) :
        random_value = Order.pop(0)
        Run_VM.append(VM_list.pop(VM_list.index(list(item for item in VM_list if item['index']==random_value)[0])))
        Host_list[i-1].append(Run_VM[i-1]["VM_name"])                         #호스트 리스트가 0부터 시작하기 때문에 -1
        print(Run_VM[i-1]["VM_name"]+"\t is allocated to "+Host_list[i-1]["Host_name"])
        for j in Host_list[i-1]["VMs"] :
            Host_list[i-1]["Total_CPU_Usage"] += find_VM_CPU_usage(j, Run_VM)
            Host_list[i-1]["Total_Disk_Usage"] += find_VM_Disk_usage(j, Run_VM)
            Host_list[i-1]["Number_of_Job"] += 1
            Host_list[i-1]["Status"] = 'Activated' 
##        time.sleep(0.3)
    for k in Host_list:
##        time.sleep(0.3)
        print(k)

    #부하 탐지 함수 호출
    print('---- Check the Host\'s status ...')
    Overloaded_Host, Underloaded_Host, Normal_Host= check_Host_Status(Host_list, Detect_Policy)
    time.sleep(1)
    for i in range(0,2) :
        if i == 0 : 
            status = 'Overloaded Host'
            temp = Overloaded_Host
        else : 
            status = 'Underloaded Host'
            temp = Underloaded_Host
        if len(temp)== 0 and i == 0  : print(status+' : None')
        else :
            print(status+' : '+str(len(temp))+' Hosts // ', end='')
            for j in range(0, len(temp)) : 
                if j != len(temp)-1 : 
                    print(temp[j]['Host_name'], end=' ')
                else :
                    print(temp[j]['Host_name'], end='\n')
    
    #초기 마이그레이션진행
    print('---- Start migration\n\n\n')
    #migrate_VMs(Overloaded_Host, Normal_Host, Underloaded_Host)

    

    

#VM의 CPU 사용량 찾기
def find_VM_CPU_usage (VM_name, Run_VM) :
    VM_CPU_usage=0.0
    VM_number = int(VM_name.replace("VM#",''))
    for i in Run_VM : 
        if i['VM_name'] == VM_name :
            VM_CPU_usage = float(i['Usage'][i['Current_Time']].split(' ')[1])
            break
    return VM_CPU_usage


#VM의 Disk 사용량 찾기
def find_VM_Disk_usage (VM_name, Run_VM) :
    VM_Disk_usage=0.0
    VM_number = int(VM_name.replace("VM#",''))
    for i in Run_VM : 
        if i['VM_name'] == VM_name :
            VM_Disk_usage = float(i['Usage'][i['Current_Time']].split(' ')[3])
            break
    return VM_Disk_usage


#Overload, Underload 탐지
def check_Host_Status (Host_list, Detect_Policy) :
    Overloaded_Host = []
    Underloaded_Host = []
    Normal_Host=[] 
    #1.Static_threshold Policy
    if Detect_Policy=='static_threshold' : 
        Upper_Threshold = 80.0
        lower_Threshold = 30.0
        for i in Host_list : 
            if i['Total_CPU_Usage'] > Upper_Threshold :
                Overloaded_Host.append(i)
            elif i['Total_CPU_Usage'] < lower_Threshold :
                Underloaded_Host.append(i)
            else : 
                Normal_Host.append(i)
        return Overloaded_Host, Underloaded_Host, Normal_Host
    #2.Mad
    #3.LR
    else : 
        print('Select Detect_Policy')
        return 0
        
        
#VM 마이그레이션 진행
def migrate_VMs(Overload_host, Normal_Host, Underload_host, VM_Selection_Policy) :
    if not Overload_host : 
        print('Overload Host is not detected')
        return 

    #overloaded --> Normal Host
    #   VM selection (Random, High Utilization,,)
    #   Host selection (Host Selection)
    #   if normal host is full, then migration to Extra_Host(underloaded Host)
    #   Update Run_VM, Queue_VM, Host_list(change status)
    # 


#실행될 VM list 대기열 이동 
#def pop_VMs (Vm_list, Queue_VM, schedule) :
    # first, pop vm_number from order_list following Schdule
    # extract number --> check order_list
    # find VM+number in VM list 


#호스트 변경사항 저장   
#def update_Host() 

#VM 정보 찾기
#def find_VM_info()