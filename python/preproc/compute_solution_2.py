import sys
import operator

# the structure of the test file is the same as the structure of the train.csv

test_file_name = sys.argv[1]
solution_file_name = sys.argv[2]
station_max_vals = {}
station_vals = {}

f = open(test_file_name, "r")
f.readline()  # header line

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
  station_vals[key_s] -= 1
  station_vals[key_t] += 1
  if station_vals[key_s] < station_max_vals[key_s]:
    station_max_vals[key_s] = station_vals[key_s]

f_out = open(solution_file_name, "w")

sorted_max_vals = sorted(station_max_vals.items(), key=operator.itemgetter(0))
for item in sorted_max_vals:
  f_out.write(item[0] + "," + str(-item[1]) + "\n")

