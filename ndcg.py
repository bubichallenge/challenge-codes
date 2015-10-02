import math
import random
import operator

class NDCGComputer:

  def __init__(self, submission_, solution_, K_):
    self.submission = submission_
    self.solution = solution_
    self.K = K_
    self.submission_list = self.sorter(self.submission)
    self.solution_list = self.sorter(self.solution)

  def compute_relevances(self, toplist):
    relevances = {}
    rank = 0
    while rank < len(toplist):
      link, score = toplist[rank]
      rank += 1
      same_score_links = [link]
      while(rank < len(toplist) and toplist[rank][1] == score):
        same_score_links.append(toplist[rank][0])
        rank += 1
      avg_relevance = 0
      for link in same_score_links:
        if link in self.solution:
          avg_relevance += self.solution[link]
      avg_relevance /= float(len(same_score_links))
      for link in same_score_links:
        relevances[link] = avg_relevance
    return relevances

  def compute_DCG(self, toplist):
    relevances = self.compute_relevances(toplist)
    DCG = 0
    rank = 0
    for link, score in toplist:
      rank += 1
      if(rank > self.K):
        break
      weight = 1 / math.log(rank + 1, 2)
      relevance = relevances[link]
      DCG += weight * relevance
    return DCG

  def run(self):
    DCG = self.compute_DCG(self.submission_list)
    iDCG = self.compute_DCG(self.solution_list)
    return DCG / float(iDCG)

  def sorter(self, data):
    return sorted(data.iteritems(), key=operator.itemgetter(1), reverse=True)

