import numpy as np
import matplotlib.pyplot  as plt
import matplotlib.ticker as ticker
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

b = [                           # SLAV
    [2.79551, 2.41395,2.04184],             #MMT Rs MU
    [1.10993, 1.04758,0.93962],             #Rs
    [1.08388, 1.07159,0.95455],             #lowcpu
    [0.65708, 0.63205,0.52088]              #lowcpu, Disk  
                                            #MMEHS
                                    
]


c = [                            # Disk SLAV
    [0.18822, 0.18713, 0.17283],
    [0.1912, 0.17549,0.16158],
    [0.18421, 0.18196, 0.16102],
    [0.09008, 0.08357, 0.08085]   
]

d= [                             # Migration
    [3596.54, 2308.32, 1770.0],
    [1543.1, 1144.82, 944.66],
    [1510.06, 1168.24, 952.58],
    [1302.4, 1102.78, 945.8]
]

e = [                            # Host Restart
    [101.36, 119.2,  112.94],
    [91.42, 113.46, 106.26],
    [89.98, 114.04, 105.78 ],
    [325.3, 298.52, 288.44]
]
                                # Total Active Time
f = [
    [72450.58, 73529.42, 75697.86],
    [75472.16, 75808.82, 77572.12],
    [75667.1, 75775.3, 77412.38],
    [89506.66, 86755.14,86633.72]
]

g = [                           # Max Host
    [29.52, 30.16, 31.26],
    [30.16, 30.7, 31.7 ],
    [30.12, 30.68, 31.56],
    [39.56, 37.88, 37.76]
]

fig = plt.figure(figsize=(10,12))
X = np.arange(len(Label), step=1)
#plt.bar(X+0.00, a[0], color='r', width=0.25)
#plt.bar(X+0.02, a[1], color='r', width=0.25)
#plt.bar(X+0.05, a[2], color='r', width=0.25)
#plt.bar(X+0.06, a[3], color='r', width=0.25)
ax1 = fig.add_subplot(3,2,1)
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')



plt.bar(X-0.15, b[0], color='firebrick', width=0.10)
plt.bar(X-0.05, b[1], color='indianred', width=0.10)
plt.bar(X+0.05, b[2], color='lightcoral', width=0.10)
plt.bar(X+0.15, b[3], color='dodgerblue', width=0.10)

plt.ylabel('CPU SLA Violation(%)')
plt.xlabel('Algorithm')
plt.title('Result Chart')

plt.legend( ['Random Selection', 'Low CPU usage', 'Low CPU DISK usage', 'MMEHS'], loc='upper right',fontsize=5,title='Host Selection', title_fontsize=5)
plt.ylim(0, 4)
plt.scatter(X-0.15,b[0], color='b',zorder=2, s=7)
yerr1 = np.array([[0.26893, 0.25595, 0.24134  ],[0.26638, 0.24846 ,0.22538]])
plt.errorbar(X-0.15, b[0], yerr=yerr1 , capsize=3, ls='none', ecolor='b', zorder=4)
plt.scatter(X-0.05,b[1], color='b',zorder=2, s=7)
plt.errorbar(X-0.05, b[1], yerr=[[0.11563,0.14667,0.14979 ],[0.14189,0.14843, 0.11899]]  , capsize=3, ls='none', ecolor='b', zorder=4)
plt.scatter(X+0.05,b[2], color='b',zorder=2, s=7)
plt.errorbar(X+0.05, b[2], yerr=[[0.16811, 0.14231, 0.20794],[0.09971 ,0.11366, 0.11269]] , capsize=3, ls='none', ecolor='b', zorder=4)
plt.scatter(X+0.15,b[3], color='b',zorder=2, s=7)
plt.errorbar(X+0.15, b[3], yerr=[[0.04759,0.083949,0.08871], [0.05166,0.06559,0.053129]] , capsize=3, ls='none', ecolor='b', zorder=4)
ax1.set_xticks([-0.5,0,1,2,2.5])
ax1.set_xticklabels(['',"ThrMmt","ThrRs",'ThrMu',''])



ax2 = fig.add_subplot(3,2,2)
ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

plt.bar(X-0.15, c[0], color='firebrick', width=0.10)
plt.bar(X-0.05, c[1], color='indianred', width=0.10)
plt.bar(X+0.05, c[2], color='lightcoral', width=0.10)
plt.bar(X+0.15, c[3], color='dodgerblue', width=0.10)
plt.ylabel('Disk SLA Violation(%)')
plt.xlabel('Algorithm')
plt.title('Result Chart')

plt.legend( ['Random Selection', 'Low CPU usage', 'Low CPU DISK usage', 'MMEHS'], loc='upper right',fontsize=5, title='Host Selection', title_fontsize=5)
plt.yticks([0, 0.1, 0.2, 0.3])
plt.ylim([0, 0.3])

plt.scatter(X-0.15,c[0], color='b',zorder=2, s=7)
plt.errorbar(X-0.15, c[0], yerr=[[0.0615,0.07817,0.06012],[0.06486,0.05136,0.04937]] , capsize=3, ls='none', ecolor='b', zorder=4)
plt.scatter(X-0.05,c[1], color='b',zorder=2, s=7)
plt.errorbar(X-0.05, c[1], yerr=[[0.08612,0.04311,0.07271],[0.04637, 0.06059 , 0.03864]] , capsize=3, ls='none', ecolor='b', zorder=4)
plt.scatter(X+0.05,c[2], color='b',zorder=2, s=7)
plt.errorbar(X+0.05, c[2], yerr=[[0.06683,0.04731,0.06221],[0.05335,0.06456, 0.05255]] , capsize=3, ls='none', ecolor='b', zorder=4)
plt.scatter(X+0.15,c[3], color='b',zorder=2, s=7)
plt.errorbar(X+0.15, c[3], yerr=[[0.042579,0.030879,0.042749],[0.025680 , 0.02920 , 0.022610]] , capsize=3, ls='none', ecolor='b', zorder=4)
ax2.set_xticks([-0.5,0,1,2,2.5])
ax2.set_xticklabels(['',"ThrMmt","ThrRs",'ThrMu',''])






ax3 = fig.add_subplot(3,2,3)
ax3.yaxis.set_major_locator(ticker.MultipleLocator(1000))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(500))
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

plt.bar(X-0.15, d[0], color='firebrick', width=0.10)
plt.bar(X-0.05, d[1], color='indianred', width=0.10)
plt.bar(X+0.05, d[2], color='lightcoral', width=0.10)
plt.bar(X+0.15, d[3], color='dodgerblue', width=0.10)
plt.ylabel('Number of Migrations')
plt.xlabel('Algorithm')
plt.title('Result Chart')
ax3.set_xticks([-0.5,0,1,2,2.5])
ax3.set_xticklabels(['',"ThrMmt","ThrRs",'ThrMu',''])
plt.legend( ['Random Selection', 'Low CPU usage', 'Low CPU DISK usage', 'MMEHS'], loc='upper right',fontsize=5, title='Host Selection', title_fontsize=5)
plt.ylim(0, 4000)
plt.tight_layout()


ax4 = fig.add_subplot(3,2,4)
ax4.yaxis.set_major_locator(ticker.MultipleLocator(200))
ax4.yaxis.set_minor_locator(ticker.MultipleLocator(100))
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

plt.bar(X-0.15, e[0], color='firebrick', width=0.10)
plt.bar(X-0.05, e[1], color='indianred', width=0.10)
plt.bar(X+0.05, e[2], color='lightcoral', width=0.10)
plt.bar(X+0.15, e[3], color='dodgerblue', width=0.10)
plt.ylabel('Number of Host restart')
plt.xlabel('Algorithm')
plt.title('Result Chart')
ax4.set_xticks([-0.5,0,1,2,2.5])
ax4.set_xticklabels(['',"ThrMmt","ThrRs",'ThrMu',''])
plt.legend( ['Random Selection', 'Low CPU usage', 'Low CPU DISK usage', 'MMEHS'], loc='upper right',fontsize=5, title='Host Selection', title_fontsize=5)
plt.ylim(0, 800)

ax5 = fig.add_subplot(3,2,5)
ax5.yaxis.set_major_locator(ticker.MultipleLocator(50000))
ax5.yaxis.set_minor_locator(ticker.MultipleLocator(10000))
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

plt.bar(X-0.15, f[0], color='firebrick', width=0.10)
plt.bar(X-0.05, f[1], color='indianred', width=0.10)
plt.bar(X+0.05, f[2], color='lightcoral', width=0.10)
plt.bar(X+0.15, f[3], color='dodgerblue', width=0.10)
plt.ylabel('Host Activated Time(sec)')
plt.xlabel('Algorithm')
plt.title('Result Chart')
ax5.set_xticks([-0.5,0,1,2,2.5])
ax5.set_xticklabels(['',"ThrMmt","ThrRs",'ThrMu',''])
plt.legend( ['Random Selection', 'Low CPU usage', 'Low CPU DISK usage', 'MMEHS'], loc='upper right',fontsize=5, title='Host Selection', title_fontsize=5)
plt.ylim(0, 120000)

ax6 = fig.add_subplot(3,2,6)
ax6.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax6.yaxis.set_minor_locator(ticker.MultipleLocator(5))
plt.grid(which='major', linewidth = '0.8', axis = 'y')
plt.grid(which='minor', linewidth = '0.3', axis = 'y')

plt.bar(X-0.15, g[0], color='firebrick', width=0.10)
plt.bar(X-0.05, g[1], color='indianred', width=0.10)
plt.bar(X+0.05, g[2], color='lightcoral', width=0.10)
plt.bar(X+0.15, g[3], color='dodgerblue', width=0.10)
plt.ylabel('Maximum number of Hosts')
plt.xlabel('Algorithm')
plt.title('Result Chart')
ax6.set_xticks([-0.5,0,1,2,2.5])
ax6.set_xticklabels(['',"ThrMmt","ThrRs",'ThrMu',''])
plt.legend( ['Random Selection', 'Low CPU usage', 'Low CPU DISK usage', 'MMEHS'], loc='upper right',fontsize=5, title='Host Selection', title_fontsize=5)
plt.ylim(0, 60)
plt.tight_layout()
plt.show()