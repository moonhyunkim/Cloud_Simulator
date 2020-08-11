from random import randrange
import time 
import numpy as np 


def random_choice (Host, Run_VM) :
    selected_VM = Host.VMs.pop(randrange(0, len(Host.VMs)))  #호스트의 VM 중 랜덤으로 pop // input 호스트, output VM이름(str)
    return selected_VM

def high_usage (Host, Run_VM) :
    import module
    
    temp = [] 
    for i in Host.VMs :
        temp.append(module.find_VM_info(i, Run_VM))
    

    cor_list = []
    for i in temp :
        temp_usage = []
        cmp1 = [] 
        cmp2 = []
        for j in range (0, len(i.VM_usage)) :
            temp_usage.append(float(i.VM_usage[j].split(' ')[1]))
            
        if len(Host.Usage) >= len(temp_usage) :
            cmp1 = Host.Usage[len(Host.Usage)-len(temp_usage) : ]
            cmp2 = temp_usage 
        else : 
            cmp1 = Host.Usage
            cmp2 = temp_usage[len(temp_usage) - len(Host.Usage): ]
        if len(cmp1) == 1 : 
            pass
        else : 
            #print(cmp1)
            #print(cmp2)
            #time.sleep(0.01)
            cor = np.corrcoef(cmp1, cmp2)[0][1]
            cor_list.append((i,cor))
    

    if len(cor_list) == 0 :
        temp_list = sorted(temp, key=lambda x: float(x.VM_usage[int(x.VM_curTime)].split(' ')[1]), reverse=True)
        # for i in temp_list :
        #     print(i.VM_name)
        #     print(i.VM_usage[int(i.VM_curTime)].split(' ')[1]) #제대로 뽑혔는지 확인
        for i in range(0, len(Host.VMs)) :
            if Host.VMs[i] == temp_list[0].VM_name : 
                selected_VM = Host.VMs.pop(i)
                break
        return  selected_VM   

    else : 
        temp_list = sorted (cor_list, key=lambda x : x[1], reverse=True)
        for i in range(0, len(Host.VMs)) :
            if Host.VMs[i] == temp_list[0][0].VM_name : 
                selected_VM = Host.VMs.pop(i)
                break
        return  selected_VM   



def Most_Correlation (Host, Run_VM) :
    import module
    
    temp = [] 
    for i in Host.VMs :
        temp.append(module.find_VM_info(i, Run_VM))
    temp_list = sorted(temp, key=lambda x: float(x.VM_usage[int(x.VM_curTime)].split(' ')[1]), reverse=True)
    # for i in temp_list :
    #     print(i.VM_name)
    #     print(i.VM_usage[int(i.VM_curTime)].split(' ')[1]) #제대로 뽑혔는지 확인
    for i in range(0, len(Host.VMs)) :
        if Host.VMs[i] == temp_list[0].VM_name : 
            selected_VM = Host.VMs.pop(i)
            break
    return  selected_VM   



def low_usage (Host, Run_VM) :
    import module
    
    temp = [] 
    for i in Host.VMs :
        temp.append(module.find_VM_info(i, Run_VM))
    temp_list = sorted(temp, key=lambda x: float(x.VM_usage[int(x.VM_curTime)].split(' ')[5]))
    # for i in temp_list :
    #     print(i.VM_name)
    #     print(i.VM_usage[int(i.VM_curTime)].split(' ')[5]) #제대로 뽑혔는지 확인
    # time.sleep(1)
    for i in range(0, len(Host.VMs)) :
        if Host.VMs[i] == temp_list[0].VM_name : 
            selected_VM = Host.VMs.pop(i)
            break
        
    return  selected_VM   

    