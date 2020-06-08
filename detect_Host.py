def static_threshold (Host_list) :
    Overloaded_Host, Underloaded_Host, Normal_Host = [], [], [] 
    Upper_Threshold = 80.0
    lower_Threshold = 30.0
    for i in Host_list : 
        if i.Total_CPU_Usage > Upper_Threshold :
            Overloaded_Host.append(i)
        elif i.Total_CPU_Usage < lower_Threshold :
            Underloaded_Host.append(i)
        else : 
            Normal_Host.append(i)
    return Overloaded_Host, Underloaded_Host, Normal_Host