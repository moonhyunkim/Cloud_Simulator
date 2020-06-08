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


#호스트 클래스 
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
    
    def print_Status (self): 
        print('{0} {1} {2} {3} {4} {5}'.format(self.Host_name, self.Host_number, self.VMs, self.Total_CPU_Usage, self.Total_Disk_Usage, self.Status))



#VM 클래스
class new_VM : 
    VM_name = ''
    VM_number = 0 
    VM_usage = []
    VM_curTime = 0
    VM_exeTime = 0

    def __init__ (self, Vname, Vnumber, Vusage, cTime, eTime) : 
        self.VM_name = Vname
        self.VM_number = Vnumber
        self.VM_usage = Vusage
        self.VM_curTime = cTime
        self.VM_exeTime = eTime 



#원하는 개수만큼 호스트 생성
def create_Host(number) :
    Host_list = []
    for i in range(1, number+1): 
        Host = new_Host('Host#'+str(i), i, 72, 400, 0 , [], 0.0, 0.0 , 'Stop')
        Host_list.append(Host)
    return Host_list



#원하는 개수만큼 가상머신 생성
def create_VM (number) :
    folder_path = 'usage_data2'
    VM_list = []
    for i in range(1, number+1) :
        f = open(folder_path+'/data'+str(i)+'.txt')
        usage_data = f.readlines()
        VM = new_VM('VM#'+str(i), i, usage_data, 0, len(usage_data))
        VM_list.append(VM)
    shuffle(VM_list)
    return VM_list



#Host 출력
def print_HostList (Overload_host, Underload_host, Normal_Host) : 
    print("Overload_host : ", end='')
    if not Overload_host : 
        print("None")
    else : 
        for i in Overload_host : 
            if i == Overload_host[-1] :
                print(i.Host_name)
            else :
                print(i.Host_name, end=' ' )
    print("Underloaded Host : ", end ='')
    if not Underload_host : 
        print("None")
    else : 
        for i in Underload_host : 
            if i == Underload_host[-1] : 
                print(i.Host_name)
            else : 
                print(i.Host_name, end=' ')

    
#VM의 CPU 사용량 찾기
def find_VM_CPU_usage (VM_name, Run_VM) :
    VM_CPU_usage=0.0
    #VM_number = int(VM_name.replace("VM#",''))
    for i in Run_VM : 
        if i.VM_name == VM_name : 
            VM_CPU_usage += float(i.VM_usage[i.VM_curTime].split(' ')[1])
            break
    return VM_CPU_usage


#VM의 Disk 사용량 찾기
def find_VM_Disk_usage (VM_name, Run_VM) :
    VM_Disk_usage=0.0
    #VM_number = int(VM_name.replace("VM#",''))
    for i in Run_VM : 
        if i.VM_name == VM_name :
            VM_Disk_usage += float(i.VM_usage[i.VM_curTime].split(' ')[3])
            break
    return VM_Disk_usage


#Overload, Underload 탐지
def check_Host_Status (Host_list, Detect_Policy) :

    #1.Static_threshold Policy
    if Detect_Policy == 'static_threshold' :
        return detect_Host.static_threshold(Host_list)
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



def migration_Overloadhost (Overload_Host, Underload_Host, Normal_Host) :
    


#시물레이션을 위한 초기화 (Host에 VM할당 // Overload, Underload 탐지)
def initialize (Host_list, VM_list, Run_VM, Order, Detect_Policy, VM_Selection_Policy) :
    Activated_Host_list = []
    Shutdown_Host_list = []

    for i in range(1,31) :
        Run_VM.append(VM_list.pop(0))
        #Run_VM.append(VM_list.pop(VM_list.index(list(item for item in VM_list if item['index']==random_value)[0])))
        Host_list[i-1].VMs.append(Run_VM[i-1].VM_name)                         #호스트 리스트가 0부터 시작하기 때문에 -1
        print(Run_VM[i-1].VM_name+"\t is allocated to "+Host_list[i-1].Host_name)
        for j in Host_list[i-1].VMs :
            Host_list[i-1].Total_CPU_Usage += find_VM_CPU_usage(j, Run_VM)
            Host_list[i-1].Total_Disk_Usage += find_VM_Disk_usage(j, Run_VM)
            Host_list[i-1].Number_of_Job += 1
            Host_list[i-1].Status = 'Activated' 
        time.sleep(0.3)
    for k in Host_list:
        time.sleep(0.3)
        k.print_Status()

    #부하 탐지 함수 호출
    print('---- Check the Host\'s status ...')
    Overload_Host, Underload_Host, Normal_Host = check_Host_Status(Host_list, Detect_Policy)
    time.sleep(1)
    print_HostList(Overload_Host, Underload_Host, Normal_Host)

    
    #초기 마이그레이션진행
    print('---- Start migration\n\n\n')
    #migrate_VMs(Overloaded_Host, Normal_Host, Underloaded_Host)