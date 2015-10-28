import sys
from eval.challenge_data import ChallengeData
from eval.ndcg import NDCGComputer

solution_path = "data/task1-BRP/mini1-solution.csv"
submission_paths = ["data/task1-BRP/mini1-submission-perfect.csv",
                    "data/task1-BRP/mini1-submission-good.csv",
                    "data/task1-BRP/mini1-submission-bad.csv"]

solution_data = ChallengeData()
submission_data = ChallengeData()

# number of top routes to take into account, we'll compute ndcg at k
k = 4

def read_real_data(solution_file_path):
  solution_data.read_from_file(solution_file_path)

def read_submission_data(submission_file_path):
  submission_data.read_from_file(submission_file_path)

def run(submission_file_path):
  read_submission_data(submission_file_path)
  average_NDCG = 0
  days = solution_data.get_days()
  for day in days:
    submission = submission_data.get(day)
    solution = solution_data.get(day)
    computer = NDCGComputer(submission, solution, k)
    score_for_day = computer.run()
    print("   score for day " + day + " is: " + str(score_for_day))
    average_NDCG += score_for_day
  average_NDCG /= float(len(days))
  return average_NDCG


print("Starting...")
read_real_data(solution_path)


for submission_path in submission_paths:
  print("\n---------------\n")
  print("Using data from " + submission_path)
  result = run(submission_path)
  print("Daily average result for " + submission_path + " is : " + str(result))

print("\nBye!")


