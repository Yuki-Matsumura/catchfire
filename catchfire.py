import glob

corepath = "/sys/devices/platform/coretemp.0/hwmon/hwmon2/"

core = glob.glob(corepath + "temp*_input")
num = len(core)

for i in range(num):
  i = i + 1
  for line in open(corepath + "temp" + str(i) + "_input", "r"):
    print("core +" + line[:2] + "." + line[2:5] + "  degree Celsius")
