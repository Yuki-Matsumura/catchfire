import glob

corepath = "/sys/devices/platform/coretemp.0/hwmon/hwmon2/"

core = glob.glob(corepath + "temp*_input")
num = len(core)

now = []
for i in range(num):
  i = i + 1
  for coretemp in open(corepath + "temp" + str(i) + "_input", "r"):
    now.append(int(coretemp))
    for crit in open(corepath + "temp" + str(i) + "_crit", "r"):
      print("Core" + str(i) + ":  " + coretemp[:2] + "." + coretemp[2:5] + "  Crit: +" + crit[:2] + "." + crit[2:5])
print now

#test
