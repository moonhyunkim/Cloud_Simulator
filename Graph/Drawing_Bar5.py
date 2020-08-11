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

fig = plt.figure(figsize=(7,5))


ax1 = fig.add_subplot(1,2,2)
ax1.yaxis.set_major_locator(ticker.MultipleLocator(10000))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(1250))
label = [5,10,15,20,25,30,35,40,45,50,55]
index = np.arange(len(label))
#b = [83698.2, 83570.68, 83473.1, 84018.38, 84669.6, 85525.68, 86466.94,87586.06,88642.04,89605.5,90703.26]
a = [4020.415, 3863.72844, 3791.0652, 3766.09396, 3766.38788,3802.95408,3853.4237,3919.5901,3951.72476,4004.24066,4083.2374]
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

plt.bar(range(len(a)), a,  color=['red','orangered','salmon','lightsalmon','lightsalmon','salmon','tomato','tomato','orangered','red','red'])
plt.ylabel('Energy Consumption(kWh)')
plt.xlabel('Allocation Denied Time')
plt.yticks()
plt.xticks(index, label)
#ax1.set_yticks([0, 80000, 82500,  85000,  87500, 90000, 92500, 95000])
ax1.set_yticks([ 3700, 3750, 3800, 3850, 3900, 3950,4000, 4050, 4100, 4150, 4200])
plt.tight_layout()

plt.ylim(3600, 4200)


ax2 = fig.add_subplot(1,2,1)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.025))
b = [0.14842, 0.10626, 0.09634, 0.09148, 0.0894, 0.08332, 0.0805,0.07928,0.07911,0.0787,0.07855]


plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

plt.bar(range(len(b)), b,  color=['b','royalblue','royalblue','cornflowerblue','cornflowerblue','dodgerblue','dodgerblue','deepskyblue','deepskyblue','lightskyblue','lightskyblue'])
plt.ylabel('Disk SLA violation(%)')
plt.xlabel('Allocation Denied Time')
plt.xticks(index, label)
plt.ylim(0, 0.2)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

fig.suptitle('(g) Performance indicator changes according to ADT')

plt.show()

fig = plt.figure(figsize=(4,5))

label = [5,10,15,20,25,30,35,40,45,50,55]
index = np.arange(len(label))
#b = [83698.2, 83570.68, 83473.1, 84018.38, 84669.6, 85525.68, 86466.94,87586.06,88642.04,89605.5,90703.26]
c = [] 
for i in range(0, len(a)) :
    c.append(a[i]*b[i]/100)
print(c)
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')
plt.title('ESV changes according to ADT')
plt.plot(label, c, marker='s', color='firebrick')
plt.ylabel('ESV (Disk SLA violation X Energy consumption)')
plt.xlabel('Allocation Denied Time')
plt.yticks()
plt.xticks(label)
plt.text(11, 3.15, 'Optimal', color='b')
#ax1.set_yticks([0, 80000, 82500,  85000,  87500, 90000, 92500, 95000])
ax1.set_yticks([ 3700, 3750, 3800, 3850, 3900, 3950,4000, 4050, 4100, 4150, 4200])
plt.tight_layout()

plt.ylim(2.7, 6.5)
plt.show()
b = [4020.415, 3863.72844, 3791.0652, 3766.09396, 3766.38788,3782.95408,3803.4237,3829.5901,3851.72476,3904.24066,3953.2374]