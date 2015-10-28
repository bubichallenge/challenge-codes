import sys
from challenge_data import ChallengeData
from ndcg import NDCGComputer

class RankingEvaluator:

  def __init__(self):
    self.submission_data = ChallengeData()
    self.solution_data = ChallengeData()

  def read_data(self, submission_file, solution_file):
    self.submission_data.read_from_file(submission_file)
    self.solution_data.read_from_file(solution_file)

  def run(self):
    average_NDCG = 0
    days = self.solution_data.get_days()
    for day in days:
      submission = self.submission_data.get(day)
      solution = self.solution_data.get(day)
      computer = NDCGComputer(submission, solution, 100)
      average_NDCG += computer.run()
    average_NDCG /= float(len(days))
    return average_NDCG
