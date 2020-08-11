import numpy as np
import matplotlib.pyplot  as plt
import matplotlib.ticker as ticker
from matplotlib import colors as mcolors

Label = ['ThrMmt', 'ThrRs', 'ThrMu']
a = [
    #00, 01, 02, 10, 11, 12
    [71829.83,74251.2,74402.73,92260.77,74215.6,75653.17,75740.73, 94663.3], #Active 타임
    [30.0, 30.5, 30.57,46.63, 31.3, 31.4, 31.13, 46.4], #최대 호스트
    [2613.0, 1020.3, 1004.43, 1428.87, 1981.2, 867.03, 849.5, 1073.2], #마이그레이션
    [72.43, 62.33, 62.37, 517.4, 73.1, 64.53, 62.57, 441.27], #호스트 재시작
    [2.90307, 1.02256, 1.00508, 0.73378, 2.46183, 0.96059, 0.94578, 0.53249], #CPU SLAV
    [0.6037, 0.63983, 0.6001, 0.29701,  0.55114, 0.57829, 0.5533, 0.31687]  #Disk SLAV
]

b = [
    [2.93684 - 0.26893, 2.70082 - 0.25595, 2.37735-0.24134],
    [1.15236 - 0.11563, 1.14121- 0.14667,1.02311-0.14979],
    [1.15734 - 0.16811, 1.14512- 0.14231,1.03256-0.20794],
    [0.60905 - 0.063310, 0.62191- 0.07665, 0.57003-0.056270]
]
c = [
    [0.29502-0.0615, 0.29595-0.07817, 0.26953-0.06012],
    [0.29771-0.08612, 0.2993-0.04311, 0.2683-0.07271],
    [0.23725-0.06683, 0.24135-0.04731, 0.21815-0.06221],
    [0.08221-0.0259000, 0.08963-0.02383, 0.08486-0.03553]
]
d= [#마이그레이션횟수
    [3418, 997, 2650],  #RS일때 mmt Rs mu 
    [1465, 1028, 1260],
    [1442, 1035, 1227],
    [1040, 901, 1007]
]

e = [#호스트 재시작 횟수
    [101, 96,  104],
    [94, 98, 101],
    [99, 91, 98 ],
    [203, 198, 207 ]
]

f = [#호스트 활성화 시간
    [71152.0, 72657.0, 71547.0],
    [74071.0, 75232.0, 74443.0],
    [73908.0, 74390.0, 74009.0],
    [84539.0, 84797.0, 83580.0]
]

g = [#최대 호스트 개수
    [28, 29, 29],
    [29, 30, 29 ],
    [29, 30, 29],
    [33, 34, 34]
]

h = [#에너지 소비량
    [3102.847, 3138.615, 3131.366 ],
    [3184.185, 3205.369, 3204.227],
    [3187.886, 3195.686, 3173.918],
    [3729.874, 3719.299, 3700.921]
]



fig = plt.figure(figsize=(9,12))
X = np.arange(len(Label), step=1)
#plt.bar(X+0.00, a[0], color='r', width=0.25)
#plt.bar(X+0.02, a[1], color='r', width=0.25)
#plt.bar(X+0.065, a[2], color='r', width=0.25)
#plt.bar(X+0.065, a[3], color='r', width=0.25)
ax1 = fig.add_subplot(3,2,1)
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')



plt.bar(X-0.19625, b[0], color='lightskyblue' , width=0.12)
plt.bar(X-0.065, b[1], color='dodgerblue', width=0.12)
plt.bar(X+0.065, b[2], color='royalblue', width=0.12)
plt.bar(X+0.19625, b[3], color='b', width=0.12)
plt.ylabel('CPU SLA Violation(%)')
plt.xlabel('Algorithm')
plt.title('(a) CPU SLA Violation Chart')

plt.legend( ['Random Selection', 'Low CPU usage', 'Low CPU-DISK usage', 'MMEVMP'], loc='upper right',fontsize=5,title='VMP', title_fontsize=5)
plt.ylim(0, 3.5)

temp = [0.26638 + 0.26893, 0.24846 + 0.25595, 0.22538 + 0.24134]
plt.bar(X-0.19625, temp, bottom=b[0], width=0.12, color = 'lightskyblue', alpha=0.5)
temp =  [2.93684, 2.70082 , 2.37735],
plt.scatter(X-0.19625,temp, color='b',zorder=2, s=7, marker='s', )
#yerr1 = np.array([[0.26893, 0.25595, 0.24134  ],[0.26638, 0.24846 ,0.22538]])


temp = [0.11563 + 0.14189, 0.14667 + 0.14843, 0.14979 + 0.11899]
plt.bar(X-0.065, temp, bottom=b[1], width=0.12, color = 'dodgerblue', alpha=0.5)
temp = [1.15236, 1.14121,1.02311],
plt.scatter(X-0.065, temp, color='b',zorder=2, s=7,marker='s')
#plt.errorbar(X-0.065, b[1], yerr=[[0.11563,0.14667,0.14979 ],[0.14189,0.14843, 0.11899]]  , capsize=3, ls='none', ecolor='r', zorder=4)


temp = [0.16811 + 0.09971, 0.14231 + 0.11366, 0.20794 + 0.11269]
plt.bar(X+0.065, temp, bottom=b[2], width=0.12, color = 'royalblue',alpha=0.5)
temp = [1.15734, 1.14512,1.03256]
plt.scatter(X+0.065, temp, color='b',zorder=2, s=7,marker='s')
#plt.scatter(X+0.065,b[2], color='b',zorder=2, s=7)
#plt.errorbar(X+0.065, b[2], yerr=[[0.16811, 0.14231, 0.20794],[0.09971 ,0.11366, 0.11269]] , capsize=3, ls='none', ecolor='r', zorder=4)

temp = [0.063310 + 0.046699, 0.07665 + 0.06006, 0.056270 + 0.051559]
plt.bar(X+0.19625, temp, bottom=b[3], width=0.12, color = 'b', alpha=0.6)
temp = [0.60905, 0.62191, 0.57003]
plt.scatter(X+0.19625, temp, color='b',zorder=2, s=7,marker='s')
#plt.scatter(X+0.19625,b[3], color='b',zorder=2, s=7)
#plt.errorbar(X+0.19625, b[3], yerr=[[0.063310,0.07665,0.056270], [0.046699, 0.06006,0.051559]] , capsize=3, ls='none', ecolor='r', zorder=4)
ax1.set_xticks([-0.5,0,1,2,2.5])
ax1.set_xticklabels(['',"ThrMmt","ThrRs",'ThrMu',''])



ax2 = fig.add_subplot(3,2,2)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

plt.bar(X-0.19625, c[0], color='lightskyblue' , width=0.12)
plt.bar(X-0.065, c[1], color='dodgerblue', width=0.12)
plt.bar(X+0.065, c[2], color='royalblue', width=0.12)
plt.bar(X+0.19625, c[3], color='b', width=0.12)
plt.ylabel('Disk SLA Violation(%)')
plt.xlabel('Algorithm')
plt.title('(b) Disk SLA Violation Chart')

plt.legend( ['Random Selection', 'Low CPU usage', 'Low CPU-DISK usage', 'MMEVMP'], loc='upper right',fontsize=5, title='VMP', title_fontsize=5)
plt.yticks([0, 0.1, 0.2, 0.3,0.4])
plt.ylim([0, 0.4])

temp = [0.0615 + 0.06486, 0.07817 + 0.05136, 0.06012 + 0.04937]
plt.bar(X-0.19625, temp, bottom=c[0], width=0.12, color = 'lightskyblue', alpha=0.5)
temp = [0.29502, 0.29595, 0.26953]
plt.scatter(X-0.19625, temp, color='b',zorder=2, s=7,marker='s')
#plt.scatter(X-0.19625,c[0], color='b',zorder=2, s=7)
#plt.errorbar(X-0.19625, c[0], yerr=[[0.0615,0.07817,0.06012],[0.06486,0.05136,0.04937]] , capsize=3, ls='none', ecolor='b', zorder=4)

temp = [0.08612 + 0.04637, 0.04311 + 0.06059, 0.07271 + 0.03864]
plt.bar(X-0.065, temp, bottom=c[1], width=0.12, color = 'dodgerblue', alpha=0.5)
temp = [0.29771, 0.2993, 0.2683]
plt.scatter(X-0.065, temp, color='b',zorder=2, s=7,marker='s')
#plt.scatter(X-0.065,c[1], color='b',zorder=2, s=7)
#plt.errorbar(X-0.065, c[1], yerr=[[0.08612,0.04311,0.07271],[0.04637, 0.06059 , 0.03864]] , capsize=3, ls='none', ecolor='b', zorder=4)

temp = [0.06683 + 0.05335, 0.04731 + 0.06456, 0.06221 + 0.05255]
plt.bar(X+0.065, temp, bottom=c[2], width=0.12, color = 'royalblue', alpha=0.5)
temp = [0.23725, 0.24135, 0.21815]
plt.scatter(X+0.065, temp, color='b',zorder=2, s=7,marker='s')
#plt.scatter(X+0.065,c[2], color='b',zorder=2, s=7)
#plt.errorbar(X+0.065, c[2], yerr=[[0.06683,0.04731,0.06221],[0.05335,0.06456, 0.05255]] , capsize=3, ls='none', ecolor='b', zorder=4)


temp = [0.0259000 + 0.0217899999, 0.02383 + 0.02707, 0.03553 + 0.02561]
plt.bar(X+0.19625, temp, bottom=c[3], width=0.12, color = 'b', alpha=0.5)
temp =   [0.08221, 0.08963, 0.08486]
plt.scatter(X+0.19625, temp, color='b',zorder=2, s=7,marker='s')
#plt.scatter(X+0.19625,c[3], color='b',zorder=2, s=7)
#plt.errorbar(X+0.19625, c[3], yerr=[[0.0259000,0.02383,0.03553],[0.0217899999 , 0.02707 , 0.02561]] , capsize=3, ls='none', ecolor='b', zorder=4)
ax2.set_xticks([-0.5,0,1,2,2.5])
ax2.set_xticklabels(['',"ThrMmt","ThrRs",'ThrMu',''])






ax3 = fig.add_subplot(3,2,3)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(1000))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(500))
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

plt.bar(X-0.19625, d[0], color='lightsalmon' , width=0.12)
plt.bar(X-0.065, d[1], color='salmon', width=0.12)
plt.bar(X+0.065, d[2], color='orangered', width=0.12)
plt.bar(X+0.19625, d[3], color='red', width=0.12)
plt.ylabel('Number of Migrations')
plt.xlabel('Algorithm')
plt.title('(a) Number of Migrations Chart')
ax3.set_xticks([-0.5,0,1,2,2.5])
ax3.set_xticklabels(['',"ThrMmt","ThrRs",'ThrMu',''])
plt.legend( ['Random Selection', 'Low CPU usage', 'Low CPU-DISK usage', 'MMEVMP'], loc='upper right',fontsize=5, title='VMP', title_fontsize=5)
#최대최소 범위
temp = [689, 1593, 421]
plt.bar(X-0.19625, temp, bottom=d[0], width=0.12, color = 'lightsalmon', alpha=0.5)
temp =   [3798.32, 2276.86, 2828.68]
plt.scatter(X-0.19625, temp, color='r',zorder=2, s=7,marker='s')

#최대최소 범위
temp = [413, 207, 242] #차이 
plt.bar(X-0.065, temp, bottom=d[1], width=0.12, color = 'salmon', alpha=0.5)
temp =   [1620.84, 1120.06, 1377.2] #평균
plt.scatter(X-0.065, temp, color='r',zorder=2, s=7,marker='s')

#최대최소 범위
temp = [370, 246, 301] #차이 
plt.bar(X+0.065, temp, bottom=d[2], width=0.12, color = 'orangered', alpha=0.5)
temp =   [1638.9, 1129.38, 1374.18] #평균
plt.scatter(X+0.065, temp, color='r',zorder=2, s=7,marker='s')

#최대최소 범위
temp = [224, 148, 195] #차이 
plt.bar(X+0.19625, temp, bottom=d[3], width=0.12, color = 'red', alpha=0.5)
temp =   [1146.18, 965.68, 1097.24] #평균
plt.scatter(X+0.19625, temp, color='r',zorder=2, s=7,marker='s')

plt.ylim(0, 4500)
plt.tight_layout()


ax4 = fig.add_subplot(3,2,4)
ax4.yaxis.set_major_locator(ticker.MultipleLocator(100))
ax4.yaxis.set_minor_locator(ticker.MultipleLocator(50))
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

plt.bar(X-0.19625, e[0], color='lightsalmon' , width=0.12)
plt.bar(X-0.065, e[1], color='salmon', width=0.12)
plt.bar(X+0.065, e[2], color='orangered', width=0.12)
plt.bar(X+0.19625, e[3], color='red', width=0.12)
plt.ylabel('Number of Host restart')
plt.xlabel('Algorithm')
plt.title('(b) Number of Host restart Chart')
ax4.set_xticks([-0.5,0,1,2,2.5])
ax4.set_xticklabels(['',"ThrMmt","ThrRs",'ThrMu',''])
plt.legend( ['Random Selection', 'Low CPU usage', 'Low CPU-DISK usage', 'MMEVMP'], loc='upper right',fontsize=5, title='VMP', title_fontsize=5)
plt.ylim(0, 400)

#MMT RS MU
#최대최소 범위 //Thr - RS
temp = [43, 28, 31] #차이 
plt.bar(X-0.19625, temp, bottom=e[0], width=0.12, color = 'lightsalmon', alpha=0.5)
temp =   [121.02, 110.4, 120.84] # 평균
plt.scatter(X-0.19625, temp, color='r',zorder=2, s=7,marker='s')

#최대최소 범위 //Thr - LC
temp = [37, 23, 34] #차이 
plt.bar(X-0.065, temp, bottom=e[1], width=0.12, color = 'salmon', alpha=0.5)
temp =   [110.8, 107.0, 114.04] #평균
plt.scatter(X-0.065, temp, color='r',zorder=2, s=7,marker='s')

#최대최소 범위 // Thr - LCD
temp = [35, 28, 33] #차이 
plt.bar(X+0.065, temp, bottom=e[2], width=0.12, color = 'orangered', alpha=0.5)
temp =   [113.66, 105.66, 113.34] #평균
plt.scatter(X+0.065, temp, color='r',zorder=2, s=7,marker='s')

#최대최소 범위 // Thr -MMEVMP
temp = [53, 48, 43] #차이 
plt.bar(X+0.19625, temp, bottom=e[3], width=0.12, color = 'red', alpha=0.5)
temp =   [228.26, 220.22, 224.84] #평균
plt.scatter(X+0.19625, temp, color='r',zorder=2, s=7,marker='s')


ax5 = fig.add_subplot(3,2,5)
ax5.yaxis.set_major_locator(ticker.MultipleLocator(20000))
ax5.yaxis.set_minor_locator(ticker.MultipleLocator(10000))
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

plt.bar(X-0.19625, f[0], color='lightsalmon' , width=0.12)
plt.bar(X-0.065, f[1], color='salmon', width=0.12)
plt.bar(X+0.065, f[2], color='orangered', width=0.12)
plt.bar(X+0.19625, f[3], color='red', width=0.12)
plt.ylabel('Host Activated Time(sec)')
plt.xlabel('Algorithm')
plt.title('(c) Host Activated Time Chart')
ax5.set_xticks([-0.5,0,1,2,2.5])
ax5.set_xticklabels(['',"ThrMmt","ThrRs",'ThrMu',''])
plt.legend( ['Random Selection', 'Low CPU usage', 'Low CPU-DISK usage', 'MMEVMP'], loc='upper right',fontsize=5, title='VMP', title_fontsize=5)
plt.ylim(0, 120000)

#MMT RS MU
#최대최소 범위 //Thr - RS
temp = [2113.0, 3920.0, 1923.0] #차이 
plt.bar(X-0.19625, temp, bottom=f[0], width=0.12, color = 'lightsalmon', alpha=0.5)
temp =   [72107.0, 73626.08, 72509.14] # 평균
plt.scatter(X-0.19625, temp, color='r',zorder=2, s=7,marker='s')

#최대최소 범위 //Thr - LC
temp = [2044.0, 1963.0, 1923.0] #차이 
plt.bar(X-0.065, temp, bottom=f[1], width=0.12, color = 'salmon', alpha=0.5)
temp =   [75063.18, 75965.12, 75313.7] #평균
plt.scatter(X-0.065, temp, color='r',zorder=2, s=7,marker='s')

#최대최소 범위 // Thr - LCD
temp = [2109.0, 2522.0, 2416.0] #차이 
plt.bar(X+0.065, temp, bottom=f[2], width=0.12, color = 'orangered', alpha=0.5)
temp =   [75092.3, 75927.94, 75158.6] #평균
plt.scatter(X+0.065, temp, color='r',zorder=2, s=7,marker='s')

#최대최소 범위 // Thr -MMEVMP
temp = [1767.0, 2749.0, 2719.0] #차이 
plt.bar(X+0.19625, temp, bottom=f[3], width=0.12, color = 'red', alpha=0.5)
temp =   [85388.5, 85927.2, 84814.66] #평균
plt.scatter(X+0.19625, temp, color='r',zorder=2, s=7,marker='s')


ax6 = fig.add_subplot(3,2,6)
ax6.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax6.yaxis.set_minor_locator(ticker.MultipleLocator(5))
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

plt.bar(X-0.19625, g[0], color='lightsalmon' , width=0.12)
plt.bar(X-0.065, g[1], color='salmon', width=0.12)
plt.bar(X+0.065, g[2], color='orangered', width=0.12)
plt.bar(X+0.19625, g[3], color='red', width=0.12)
plt.ylabel('Maximum number of Hosts')
plt.xlabel('Algorithm')
plt.title('(d) Maximum number of Hosts Chart')
ax6.set_xticks([-0.5,0,1,2,2.5])
ax6.set_xticklabels(['',"ThrMmt","ThrRs",'ThrMu',''])
plt.legend( ['Random Selection', 'Low CPU usage', 'Low CPU-DISK usage', 'MMEVMP'], loc='upper right',fontsize=5, title='VMP', title_fontsize=5)
plt.ylim(0, 80)
plt.tight_layout()


#MMT RS MU
#최대최소 범위 //Thr - RS
temp = [3, 3, 2] #차이 
plt.bar(X-0.19625, temp, bottom=g[0], width=0.12, color = 'lightsalmon', alpha=0.5)
temp =   [29.56, 30.24, 29.72] # 평균
plt.scatter(X-0.19625, temp, color='r',zorder=2, s=7,marker='s')

#최대최소 범위 //Thr - LC
temp = [2, 2, 2] #차이 
plt.bar(X-0.065, temp, bottom=g[1], width=0.12, color = 'salmon', alpha=0.5)
temp =   [30.3, 30.78, 30.3] #평균
plt.scatter(X-0.065, temp, color='r',zorder=2, s=7,marker='s')

#최대최소 범위 // Thr - LCD
temp = [3, 2, 2] #차이 
plt.bar(X+0.065, temp, bottom=g[2], width=0.12, color = 'orangered', alpha=0.5)
temp =   [30.42, 30.74, 30.32] #평균
plt.scatter(X+0.065, temp, color='r',zorder=2, s=7,marker='s')

#최대최소 범위 // Thr -MMEVMP
temp = [7, 5, 4] #차이 
plt.bar(X+0.19625, temp, bottom=g[3], width=0.12, color = 'red', alpha=0.5)
temp =   [35.62, 35.94, 35.44] #평균
plt.scatter(X+0.19625, temp, color='r',zorder=2, s=7,marker='s')
plt.show()


fig = plt.figure(figsize=(5,5))
X = np.arange(len(Label), step=1)
ax7 = fig.add_subplot(1,1,1)
ax7.yaxis.set_major_locator(ticker.MultipleLocator(1000))
ax7.yaxis.set_minor_locator(ticker.MultipleLocator(250))
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

plt.bar(X-0.19625, h[0], color='lightsalmon', width=0.12)
plt.bar(X-0.065, h[1], color='salmon', width=0.12)
plt.bar(X+0.065, h[2], color='orangered', width=0.12)
plt.bar(X+0.19625, h[3], color='red', width=0.12)
plt.ylabel('Energy Consumption (kWH)')
plt.xlabel('Algorithm')
plt.title('Energy Consumption  Chart')
ax7.set_xticks([-0.5,0,1,2,2.5])
ax7.set_xticklabels(['',"ThrMmt","ThrRs",'ThrMu',''])
plt.legend( ['Random Selection', 'Low CPU usage', 'Low CPU-DISK usage', 'MMEVMP'], loc='upper right',fontsize=5, title='VMP', title_fontsize=5)


#MMT RS MU
#최대최소 범위 //Thr - RS
temp = [99.897, 118.73, 85.50] #차이 
plt.bar(X-0.19625, temp, bottom=h[0], width=0.12, color = 'lightsalmon', alpha=0.5)
temp =   [3155.73796, 3179.98242, 3167.75448] # 평균
plt.scatter(X-0.19625, temp, color='r',zorder=2, s=7,marker='s')

#최대최소 범위 //Thr - LC
temp = [85.99, 77.420, 86.273] #차이 
plt.bar(X-0.065, temp, bottom=h[1], width=0.12, color = 'salmon', alpha=0.5)
temp =   [3225.14376, 3244.86928, 3239.76124] #평균
plt.scatter(X-0.065, temp, color='r',zorder=2, s=7,marker='s')

#최대최소 범위 // Thr - LCD
temp = [76.0660, 93.270, 97.159] #차이 
plt.bar(X+0.065, temp, bottom=h[2], width=0.12, color = 'orangered', alpha=0.5)
temp =   [3232.12632, 3240.87184, 3233.48992] #평균
plt.scatter(X+0.065, temp, color='r',zorder=2, s=7,marker='s')

#최대최소 범위 // Thr -MMEVMP
temp = [131.072, 123.0560,  137.7940] #차이 
plt.bar(X+0.19625, temp, bottom=h[3], width=0.12, color = 'red', alpha=0.5)
temp =   [3793.40428, 3792.90918, 3768.43472] #평균
plt.scatter(X+0.19625, temp, color='r',zorder=2, s=7,marker='s')

plt.ylim(0, 4750)
plt.tight_layout()
plt.show()


fig = plt.figure(figsize=(5,5))
X = np.arange(len(Label), step=1)
ax7 = fig.add_subplot(1,1,1)
ax7.yaxis.set_major_locator(ticker.MultipleLocator(20))
ax7.yaxis.set_minor_locator(ticker.MultipleLocator(10))
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

l = b+c
m = [] 
for i in range(0, len(h)) :
    for j in range(0, len(h[i])) :
        h[i][j] = (h[i][j] * l[i][j])/100
print(h)

plt.bar(X-0.19625, h[0], color='lightsalmon', width=0.12)
plt.bar(X-0.065, h[1], color='salmon', width=0.12)
plt.bar(X+0.065, h[2], color='orangered', width=0.12)
plt.bar(X+0.19625, h[3], color='red', width=0.12)
plt.ylabel('ESV (Total SLA violation X Energy Consumption')
plt.xlabel('Algorithm')
plt.title('ESV Graph')
ax7.set_xticks([-0.5,0,1,2,2.5])
ax7.set_xticklabels(['',"ThrMmt","ThrRs",'ThrMu',''])
plt.legend( ['Random Selection', 'Low CPU usage', 'Low CPU-DISK usage', 'MMEVMP'], loc='upper right',fontsize=5, title='VMP', title_fontsize=5)
plt.scatter(X-0.19625, h[0], color='red',zorder=2, s=7,marker='o')
plt.scatter(X-0.065, h[1], color='red',zorder=2, s=7,marker='o')
plt.scatter(X+0.065, h[2], color='red',zorder=2, s=7,marker='o')
plt.scatter(X+0.19625, h[3], color='red',zorder=2, s=7,marker='o')
plt.ylim(0,100)
plt.tight_layout()
plt.show()