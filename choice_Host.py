"""
Cloud Simulator

 • Author : Moonhyun kim
 • Date : May 22 , 2020
 • Last modified date : Aug 2, 2020

 • Department of Computer Science at Chungbuk National University
"""

from random import randrange
from random import shuffle
import time
import module

def random_choice(VM, Host_list, Run_VM) :
    flag = 0
    if Host_list :
        for i in Host_list : #Shutdown일때 flag검증
            if i.Status != 'Shutdown' :
                flag = 1 
                break
        if flag == 0 :
            shuffle(Host_list)
            temp = Host_list[0]
            print('\t '+temp.Host_name+" is now activated")
            module.Number_of_Host_restart += 1
            return temp
        else :
            shuffle(Host_list)
            for i in Host_list :
                if i.Total_CPU_Usage + module.find_VM_CPU_usage(VM,Run_VM) < 80 and i.Status != 'Shutdown':
                    return i
                elif i == Host_list[-1] :
                    if len(Host_list) == 60 : #할당부분
                        shutdownHost = [] 
                        for i in Host_list :
                            if i.Status == "Shutdown" :
                                shutdownHost.append(i)
                        shuffle(shutdownHost)
                        temp = shutdownHost[0]
                        print('\t '+temp.Host_name+" is now activated")
                        module.Number_of_Host_restart += 1
                        return temp
                    return 0
    else : 
        return 0 

#추후에 Allocation시 모두 shutdown되어 있을 경우 코드 수정필요있음
def low_cpu_usage(VM, Host_list, Run_VM) :
    flag = 0
    if Host_list :
        for i in Host_list : #Shutdown일때 flag검증
            if i.Status != 'Shutdown' :
                flag = 1 
                break
        if flag == 0 : #모두 shutdown 되있다면
            shuffle(Host_list)
            temp = Host_list[0]
            print('\t '+temp.Host_name+" is now activated")
            module.Number_of_Host_restart += 1
            return temp
        else:
            temp_Host = sorted(Host_list, key=lambda  x: x.Total_CPU_Usage)
            for i in temp_Host :
                if i.Total_CPU_Usage + module.find_VM_CPU_usage(VM, Run_VM) < 80 and i.Status != 'Shutdown': 
                    return i 
                elif i == temp_Host[-1] :
                    if len(Host_list) == 60 : #할당부분
                        shutdownHost = [] 
                        for i in Host_list :
                            if i.Status == "Shutdown" :
                                shutdownHost.append(i)
                        shuffle(shutdownHost)
                        temp = shutdownHost[0]
                        print('\t '+temp.Host_name+" is now activated")
                        module.Number_of_Host_restart += 1
                        return temp
                    return 0 
    else :
        return 0

def low_cpu_low_disk(VM, Host_list, Run_VM) :
    flag = 0
    if Host_list :
        for i in Host_list : #Shutdown일때 flag검증
            if i.Status != 'Shutdown' :
                flag = 1 
                break
        if flag == 0 :
            shuffle(Host_list)
            temp = Host_list[0]
            print('\t '+temp.Host_name+" is now activated")
            module.Number_of_Host_restart += 1
            return temp
        else : 
            temp_Host = sorted(Host_list, key=lambda x: (x.Total_CPU_Usage, x.Total_Disk_Usage))
            for i in temp_Host :
                if i.Total_CPU_Usage + module.find_VM_CPU_usage(VM, Run_VM) < 80 and i.Status != 'Shutdown': 
                    return i 
                elif i == temp_Host[-1] :
                    if len(Host_list) == 60 : #할당부분
                        shutdownHost = [] 
                        for i in Host_list :
                            if i.Status == "Shutdown" :
                                shutdownHost.append(i)
                        shuffle(shutdownHost)
                        temp = shutdownHost[0]
                        print('\t '+temp.Host_name+" is now activated")
                        module.Number_of_Host_restart += 1
                        return temp
                    return 0 
    else :
        return 0
        

def MMEHS(VM, Host_list, Run_VM) :
    min_time = 60
    flag = 0
    if Host_list :
        for i in Host_list :
            if i.Status != 'Shutdown':
                flag = 1
                break

        if flag == 0 : 
            shuffle(Host_list)
            temp = Host_list[0]
            temp.FLAG = 1 
            temp.TIME = 0
            print('\t' + temp.Host_name+" is now activated")
            module.Number_of_Host_restart += 1
            return temp

        else : #실제 알고리즘 부분
            #FLAG가 1이 아닌 호스트(직전에 작업할당 받지 않은 호스트)를 추려낸다.
            temp_list = []
            for i in Host_list :
                if i.FLAG != 1 and i.Status != 'Shutdown':
                    temp_list.append(i)
            #다 직전에 작업을 받은 호스트 밖에 없다 
            if not temp_list : 
                #마이그레이션과 할당부분 나누기
                for i in Host_list : #FLAG가 다 1이고, 다 꺼져있는 호스트만 있을때
                    if i.FLAG == 1 and (i.Number_of_Job <= 2) : 
                        temp_list.append(i)
                if temp_list : #없으면 하나 재시작
                    temp_list = sorted(temp_list, key = lambda x: x.TIME , reverse=True)
                    for i in temp_list :
                        if i.Total_CPU_Usage + module.find_VM_CPU_usage(VM, Run_VM) < 80 : 
                            temp = i 
                            temp.TIME = module.find_VM_info(VM, Run_VM).VM_curTime 
                            if temp.TIME > module.find_VM_info(VM, Run_VM).VM_curTime :
                                temp.TIME = module.find_VM_info(VM, Run_VM).VM_curTime 
                            if temp.TIME > min_time : 
                                temp.FLAG = 0
                            else : 
                                temp.FLAG = 1
                            return temp
                    if len(Host_list) != 60 : 
                        return 0 
                    else:
                        shutdownHost = [] 
                        for i in Host_list :
                            if i.Status == "Shutdown" :
                                shutdownHost.append(i)
                        shuffle(shutdownHost)
                        temp = shutdownHost[0]
                        temp.FLAG = 1
                        temp.TIME = 0 #지금 작업을 할당받을 것이기 때문에
                        print('\t'+temp.Host_name+' is now activated')
                        module.Number_of_Host_restart += 1 #리스타트 +1 (할당부분이기 때문에)
                        return temp
                else:
                    if len(Host_list) != 60 : 
                        return 0 
                    else:
                        shutdownHost = [] 
                        for i in Host_list :
                            if i.Status == "Shutdown" :
                                shutdownHost.append(i)
                        shuffle(shutdownHost)
                        temp = shutdownHost[0]
                        temp.FLAG = 1
                        temp.TIME = 0 #지금 작업을 할당받을 것이기 때문에
                        print('\t'+temp.Host_name+' is now activated')
                        module.Number_of_Host_restart += 1 #리스타트 +1 (할당부분이기 때문에)
                        return temp

            #이전에 작업을 받지 않은 호스트집합을 찾은 경우
            else :
                temp_time = []
                for i in temp_list :
                    temp_time.append(i.TIME)
                
                if max(temp_time) < min_time :
                    AVG = max(temp_time) #다 들어온지 얼마 안됬으면 가장오래된걸로
                else :
                    AVG = sum(temp_time)/len(temp_time)

                #time 평균과 가까운 값 추출 
                Available_Group = []
                for i in temp_list :
                    if i.TIME == takeClosest(temp_time, AVG) :
                        Available_Group.append(i)

                Available_Group = sorted(Available_Group, key=lambda x: x.Total_CPU_Usage)
                for i in Available_Group :
                    if i.Total_CPU_Usage + module.find_VM_CPU_usage(VM, Run_VM) < 80 and i.Status != 'Shutdown' :
                        i.FLAG = 1
                        i.TIME = 0 
                        return i 
                    #마땅한 호스트가 없다면 꺼져있던 호스트에 할당
                    elif i == Available_Group[-1] :
                        temp_list = []
                        if len(Host_list) == 60 : #할당부분
                            for i in Host_list : #FLAG가 다 1이고, 다 꺼져있는 호스트만 있을때
                                if i.FLAG == 1 and (i.Number_of_Job <= 2) : 
                                    temp_list.append(i)
                            if temp_list : 
                                temp_list = sorted(temp_list, key = lambda x: x.TIME , reverse=True)
                                for i in temp_list :
                                    if i.Total_CPU_Usage + module.find_VM_CPU_usage(VM, Run_VM) < 80 : 
                                        temp = i 
                                        temp.TIME = module.find_VM_info(VM, Run_VM).VM_curTime 
                                        if temp.TIME > module.find_VM_info(VM, Run_VM).VM_curTime :
                                            temp.TIME = module.find_VM_info(VM, Run_VM).VM_curTime 
                                        if temp.TIME > min_time : 
                                            temp.FLAG = 0
                                        else : 
                                            temp.FLAG = 1
                                        return temp
                                shutdownHost = [] 
                                for i in Host_list :
                                    if i.Status == "Shutdown" :
                                        shutdownHost.append(i)
                                shuffle(shutdownHost)
                                temp = shutdownHost[0]
                                temp.FLAG = 1
                                temp.TIME = 0
                                print('\t '+temp.Host_name+" is now activated")
                                module.Number_of_Host_restart += 1
                                return temp
                            else :
                                shutdownHost = [] 
                                for i in Host_list :
                                    if i.Status == "Shutdown" :
                                        shutdownHost.append(i)
                                shuffle(shutdownHost)
                                temp = shutdownHost[0]
                                temp.FLAG = 1
                                temp.TIME = 0
                                print('\t '+temp.Host_name+" is now activated")
                                module.Number_of_Host_restart += 1
                                return temp
                        else :
                            return 0 
    else : 
        return 0


def takeClosest(myList, myNumber):
     closest = myList[0]
     for i in myList:
       if abs(i - myNumber) < closest:
         closest = i
     return closest

