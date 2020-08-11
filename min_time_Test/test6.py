import os
f = open("/Users/moonhyunkim/Desktop/Cloud Simulator/Cloud_Simulator/module.py", 'r') 
line = f.readlines()

for i in range(0,len(line)) :
    if line[i] == '    min_time = 10\n' :
        line[i]="    min_time = 11\n"
temp = line
f.close()
f = open("/Users/moonhyunkim/Desktop/Cloud Simulator/Cloud_Simulator/module.py", 'w')
f.writelines(temp)
f.close()

f = open("/Users/moonhyunkim/Desktop/Cloud Simulator/Cloud_Simulator/choice_Host.py", 'r') 
line = f.readlines()

for i in range(0,len(line)) :
    if line[i] == '    min_time = 10\n' :
        line[i]="    min_time = 11\n"
temp = line
f.close()
f = open("/Users/moonhyunkim/Desktop/Cloud Simulator/Cloud_Simulator/choice_Host.py", 'w')
f.writelines(temp)
f.close()