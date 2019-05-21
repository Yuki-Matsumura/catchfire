import glob

corepath = "/sys/devices/platform/coretemp.0/hwmon/hwmon2/"

core = glob.glob(corepath + "temp*_input")
num = len(core)

for i in range(num):
  i = i + 1
  for input in open(corepath + "temp" + str(i) + "_input", "r"):
    for crit in open(corepath + "temp" + str(i) + "_crit", "r"):
      print("Core" + str(i) + ":  " + input[:2] + "." + input[2:5] + "  Crit: +" + crit[:2] + "." + crit[2:5])
