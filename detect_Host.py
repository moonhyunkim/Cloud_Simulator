"""
Cloud Simulator

 • Author : Moonhyun kim
 • Date : May 15 , 2020
 • Last modified date : Jul 5, 2020

 • Department of Computer Science at Chungbuk National University
"""


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
