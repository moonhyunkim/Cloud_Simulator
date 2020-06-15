from random import randrange
from random import shuffle
import module

def random_choice(VM, Host_list, Run_VM) :
    shuffle(Host_list)
    for i in Host_list :
        if i.Total_CPU_Usage + module.find_VM_CPU_usage(VM,Run_VM) < 80 :
            return i
        elif i == Host_list[-1] :
            return 0 
        
        