#min_time변화에 따른 수치 변화 파악

import numpy as np
import matplotlib.pyplot  as plt
import matplotlib.ticker as ticker
a = [
    #00, 01, 02, 10, 11, 12
    [71829.83,74251.2,74402.73,92260.77,74215.6,75653.17,75740.73, 94663.3], #Active 타임
    [30.0, 30.5, 30.57,46.63, 31.3, 31.4, 31.13, 46.4], #최대 호스트
    [2613.0, 1020.3, 1004.43, 1428.87, 1981.2, 867.03, 849.5, 1073.2], #마이그레이션
    [72.43, 62.33, 62.37, 517.4, 73.1, 64.53, 62.57, 441.27], #호스트 재시작
    [2.90307, 1.02256, 1.00508, 0.73378, 2.46183, 0.96059, 0.94578, 0.53249], #CPU SLAV
    [0.6037, 0.63983, 0.6001, 0.29701,  0.55114, 0.57829, 0.5533, 0.31687]  #Disk SLAV
]

label = [5,10,15,20,25,30,35,40,45,50,55]
index = np.arange(len(label))
b = [90741.64, 89421.72, 88809.2, 88299.32, 88430.36, 88932.56, 89416.82, 89846.08, 90837.22, 91643.82, 92296.96]
fig = plt.figure(figsize=(5,6))
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

plt.bar(range(len(b)), b)
plt.ylabel('Total Activated Host Time')
plt.xlabel('Allocation Denied Time')
plt.xticks(index, label)
plt.tight_layout()

plt.ylim(85000, 95000)


plt.show()

b = [0.67678, 0.63541, 0.58861, 0.53772, 0.49818, 0.4608, 0.43603, 0.40113, 0.37671, 0.35089, 0.33357]
fig = plt.figure(figsize=(5,6))
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

plt.bar(range(len(b)), b,  color='firebrick')
plt.ylabel('CPU SLAV(%)')
plt.xlabel('Allocation Denied Time')
plt.xticks(index, label)
plt.ylim(0, 0.8)
plt.tight_layout()

plt.show()