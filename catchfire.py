import glob
import time
import os

global corepath
corepath = "/sys/devices/platform/coretemp.0/hwmon/hwmon2/"
core = glob.glob(corepath + "temp*_input")
global num
num = len(core)
global high
high = []

##### Get CPU info #####
def cpuinfo():
  cpupath = "/proc/cpuinfo"
  with open(cpupath) as f:
    for i, line in enumerate(f):
      if 'model name' in line:
        break
  cpuname = line.split(":")
  global cpuname
  cpuname = str(cpuname[1])[1:].rstrip('\n')
##### Get CPU info #####

##### Get now Temp #####
def nowtemp():
  global now
  now = []
  i = 0
  for i in range(num):
    i = i + 1
    for coretemp in open(corepath + "temp" + str(i) + "_input", "r"):
      now.append(int(coretemp))
##### Get now Temp #####

##### Get Maximum Temp #####
def maximumtemp():
  global maximum
  maximum = []
  i = 0
  for i in range(num):
    i = i + 1
    for crit in open(corepath + "temp" + str(i) + "_crit", "r"):
      maximum.append(int(crit))
##### Get Maximum Temp #####

##### Get high Temp #####
def hightemp():
  if not high:
    for i in range(num):
      high.append(0)
    difftemp = high
  nowtemp()
  global difftemp
  difftemp = [max(nowdifftemp) for nowdifftemp in zip(now, difftemp)]
##### Get high Temp #####

##### Display #####
def disp():
  print("+==============================================================+" + '\n' +
        "| CPU: " + cpuname + "                 |" + '\n' +
        "+==============================================================+" )
  i = 0
  for i in range(num):
    no = i + 1
    print("| Core" + str(no) + " " + str(now[i])[0:2] + "." + str(now[i])[2:3])

##### Display #####

##### Main #####
def action():
  try:
    maximumtemp()
    cpuinfo()
    while True:
      pass
      os.system('clear')
      hightemp()
##### display logic #####
      disp()
      print("now:  ")
      print now
      print("high: ")
      print difftemp
      print("max:  ")
      print maximum
##### display logic #####
      time.sleep(2)
  except KeyboardInterrupt:
    os.system('clear')
    print("End script.")
##### Main #####


action()


class color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    END = '\033[0m'
#print("Core" + str(i) + ":  " + coretemp[:2] + "." + coretemp[2:5] + "  Crit: +" + crit[:2] + "." + crit[2:5])
