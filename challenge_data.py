import sys

class ChallengeData:

  def __init__(self):
    self.daily_lists = {}

  def read_from_file(self, file_name):
    f = open(file_name, "r")
    for line in f:
      records = line.split(",")
      day = records[0]
      entity = records[1]
      value = float(records[2])
      if day not in self.daily_lists:
        self.daily_lists[day] = {}
      self.daily_lists[day][entity] = value

  def get(self,day):
    return self.daily_lists[day]

  def get_days(self):
    return self.daily_lists
