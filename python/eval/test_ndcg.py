from ndcg import NDCGComputer
import math
import operator


class TestNDCGComputer:

  def test1(self):
    submission = {1:1, 2:2, 3:3, 4:4}
    solution = {1:1, 2:2, 3:3, 4:4}
    K = 10
    computer = NDCGComputer(submission, solution, K)
    ndcg = computer.run()
    assert ndcg == 1

  def test_differentweights(self):
    submission = {1:3, 2:1, 3:6, 4:2, 5:7}
    solution = {1:9, 2:4, 3:12, 4:8, 5:13}
    K = 5
    computer = NDCGComputer(submission, solution, K)
    ndcg = computer.run()
    assert ndcg == 1

  def test_unordered(self):
    #test ordering: if the algorithm didn't order the maps, it would cut wrong part and get different DCGs
    submission = { 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7 }
    solution = { 1:2, 2:1, 3:3, 4:4, 5:5, 6:6, 7:7 }
    K = 5
    computer = NDCGComputer(submission, solution, K)
    ndcg = computer.run()
    assert ndcg == 1

  def test_empty_intersection(self):
    submission = { 6:1, 7:2, 8:3, 9:4, 10:5 }
    solution = { 1:1, 2:2, 3:3, 4:4, 5:5 }
    K = 5
    computer = NDCGComputer(submission, solution, K)
    ndcg = computer.run()
    assert ndcg == 0

  def test_dcg(self):
    submission = { 1:5, 2:4, 3:3, 4:2, 5:1 }
    solution = { 1:3, 2:0, 3:4, 5:0 }
    K = 5
    computer = NDCGComputer(submission, solution, K)
    submission_list = sorted(submission.iteritems(), key=operator.itemgetter(1), reverse=True)
    dcg = computer.compute_DCG(submission_list)
    assert dcg == 5

  def test_repeatable(self):
    submission = { 1:1, 2:1, 3:1, 4:1 }
    solution = { 1:1, 2:2, 3:3, 4:4 }
    K = 10
    computer = NDCGComputer(submission,solution,K)
    ndcg_first = computer.run()
    computer = NDCGComputer(submission,solution,K)
    ndcg = computer.run()
    assert ndcg_first == ndcg

  def test_repeadted_weights(self):
    submission = { 1:1, 2:1, 3:4, 4:4, 5:5 }
    solution = { 1:1, 2:2, 3:3, 4:4, 5:5 }
    K = 4
    computer = NDCGComputer(submission,solution,K)
    solution_list = sorted(solution.iteritems(), key=operator.itemgetter(1), reverse=True)
    idcg = computer.compute_DCG(solution_list)
    ndcg = computer.run()
    ndcg_expected = 5.0/math.log(2,2) + 3.5/math.log(3,2) + 3.5/math.log(4,2) + 1.5/math.log(5,2)
    assert ndcg_expected/idcg == ndcg
