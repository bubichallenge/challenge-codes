import sys
import math
from challenge_data import ChallengeData

class DecreaseEvaluator:

  def __init__(self):
    self.submission_data = ChallengeData()
    self.solution_data = ChallengeData()

  def read_data(self, submission_file, solution_file):
    self.submission_data.read_from_file(submission_file)
    self.solution_data.read_from_file(solution_file)

  def run(self):
    MSE = 0
    N = 0
    days = self.solution_data.get_days()
    for day in days:
      solution = self.solution_data.get(day)
      submission = self.submission_data.get(day)
      for station in solution:
        pred = 0
        if station in submission:
          pred = submission[station]
        MSE += math.pow(pred-solution[station], 2)
        N += 1
    return math.pow(MSE / float(N), 0.5)
