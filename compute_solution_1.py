import sys

# the structure of the test file is the same as the structure of the train.csv

test_file_name = sys.argv[1]
solution_file_name = sys.argv[2]
f = open(test_file_name)
  
edge_weights = {}

f.readline()

for line in f:
  line = line.strip("\n")
  records = line.split(",")
  time = records[1].split(" ")[0]
  source = records[3]
  target = records[4]
  key = time + "," + source + "-" + target
  if key not in edge_weights:
    edge_weights[key] = 0
  edge_weights[key] += 1

f_out = open(solution_file_name,"w")

for key in edge_weights:
  f_out.write(key + "," + str(edge_weights[key]) + "\n")

