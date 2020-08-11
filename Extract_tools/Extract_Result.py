Active_time = []
MaxHost = []
Migration =[]
Restart = []
CPUSLAV = []
DISKSLAV = []
Energy = [] 
for i in range(1, 51) :

    #f = open('Result/ThrMmtRs'+str(i)+'.txt')
    f = open('Result_6/ThrMuMMEHS_min55_'+str(i)+'.txt')
    b = f.readlines()
    Active_time.append(float(b[1].split(' ')[6].replace('sec\n','')))
    MaxHost.append(int(b[2].split(' ')[5]))
    Migration.append(int(b[5].split(' ')[5]))
    Restart.append(int(b[6].split(' ')[6]))
    CPUSLAV.append(float(b[7].split(' ')[8].replace('%','')))
    DISKSLAV.append(float(b[8].split(' ')[8].replace('%','')))
    Energy.append(float(b[9].split(' ')[6].replace('kWh', '')))
print('평균 active 시간', round(sum(Active_time)/len(Active_time),2))
print('평균 최대 호스트', round(sum(MaxHost)/len(MaxHost),2))
print('평균 마이그레이션', round(sum(Migration)/len(Migration),2))
print('평균 호스트재시작', round(sum(Restart)/len(Restart),2))
print('평균 CPU SLAV' , round(sum(CPUSLAV)/len(CPUSLAV),5))
print('평균 DISK SLAV', round(sum(DISKSLAV)/len(DISKSLAV),5))
print('평균 에너지 소비량', round(sum(Energy)/len(Energy),5))
print('-----------')
print('Best/Worst active 시간', max(Active_time), min(Active_time))
print('Best/Worst 최대 호스트', max(MaxHost), min(MaxHost))
print('Best/Worst 마이그레이션', max(Migration), min(Migration))
print('Best/Worst 호스트재시작', max(Restart), min(Restart))
print('Best/Worst CPU SLAV' , max(CPUSLAV)-round(sum(CPUSLAV)/len(CPUSLAV),5), round(sum(CPUSLAV)/len(CPUSLAV),5)-min(CPUSLAV))
print('Best/Worst DISK SLAV', max(DISKSLAV)-round(sum(DISKSLAV)/len(DISKSLAV),5), round(sum(DISKSLAV)/len(DISKSLAV),5)-min(DISKSLAV))