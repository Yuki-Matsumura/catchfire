import glob
import time
import os

global corepath
corepath = "/sys/devices/platform/coretemp.0/hwmon/hwmon2/"
core = glob.glob(corepath + "temp*_input")
global num
num = len(core)


##### Get CPU info #####
def cpuinfo():
  cpupath = "/proc/cpuinfo"
  with open(cpupath) as f:
    for i, line in enumerate(f):
      if 'model name' in line:
        break
  cpuname = line.split(":")
  global cpuname
  cpuname = str(cpuname[1])[1:]
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


##### Get high Temp #####
def hightemp():
  global high
  high = []
  i = 0
  for i in range(num):
    i = i + 1
    for crit in open(corepath + "temp" + str(i) + "_crit", "r"):
      high.append(int(crit))
##### Get high Temp #####


def action():
  hightemp()
  while True:
    os.system('clear')
    nowtemp()
    print now
    print high
    time.sleep(2)

action()

#print("Core" + str(i) + ":  " + coretemp[:2] + "." + coretemp[2:5] + "  Crit: +" + crit[:2] + "." + crit[2:5])
