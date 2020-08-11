def static_threshold (Host_list) :
    Upper_Threshold = 80.0
    lower_Threshold = 20.0
    for i in Host_list : 
        if i.Total_CPU_Usage > Upper_Threshold :
            i.Status = 'Overloaded'
        elif i.Total_CPU_Usage < lower_Threshold and i.Total_CPU_Usage > 0  :
            i.Status = 'Underloaded'
        elif i.Total_CPU_Usage == 0.0 :
            i.Status = 'Shutdown'
        else : 
            i.Status = 'Normal' 