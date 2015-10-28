import sys
import operator

# the structure of the test file is the same as the structure of the train.csv

test_file_name = sys.argv[1]
solution_file_name = sys.argv[2]
f = open(test_file_name, "r")

edge_weights = {}

l = f.readline() # header

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

f_out = open(solution_file_name, "w")

sorted_edge_weights = sorted(edge_weights.items(), key=operator.itemgetter(0))
for item in sorted_edge_weights:
  f_out.write(item[0] + "," + str(item[1]) + "\n")
