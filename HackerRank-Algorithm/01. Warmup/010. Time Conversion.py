s = input()
hh = int(s[0:2])
mm = int(s[3:5])
ss = int(s[6:8])
am_pm = s[8:]
if(am_pm == 'PM' and hh !=12):
    hh = hh + 12
elif(am_pm == 'AM' and hh==12):
    hh = 0
    
print('{:02}:{:02}:{:02}'.format(hh,mm,ss))
