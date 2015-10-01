
import sys


# the structure of the test file is the same as the structure of the train.csv

test_file_name = sys.argv[1]
solution_file_name = sys.argv[2]
station_max_vals = {}
station_vals = {}

f.readline()

for line in f:
  line = line.strip("\n")
  records = line.split(",")
  time = records[1].split(" ")[0]
  source = records[3]
  target = records[4]
  key_s = time + "," + source 
  key_t = time + "," + target
  for key in [key_s,key_t]:
    if key not in station_vals:
      station_vals[key] = 0
      station_max_vals[key] = 0
  station_vals[key_s] -=1
  station_vals[key_t] +=1
  if station_vals[key_s]  < station_max_vals[key_s] :
    station_max_vals[key_s] = station_vals[key_s]

ff = open(solution_file_name,"w")

for key in station_max_vals:
  ff.write(key + "," + str(-station_max_vals[key]) + "\n")

