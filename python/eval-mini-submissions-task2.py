import sys
from eval.decrease_evaluator import DecreaseEvaluator

solution_path = "data/task2-DSDP/mini2-solution.csv"
submission_paths = ["data/task2-DSDP/mini2-submission-perfect.csv",
                    "data/task2-DSDP/mini2-submission-good.csv",
                    "data/task2-DSDP/mini2-submission-bad.csv"]


print("Starting...")

for submission_path in submission_paths:
  print("---------------")
  evaluator = DecreaseEvaluator()
  evaluator.read_data(submission_path, solution_path)
  result = evaluator.run()
  print("Root mean squared error for " + submission_path + " is : " + str(result))

print("---------------")
print("\nBye!")


