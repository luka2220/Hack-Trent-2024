import math
import sys


class ScoringAlgorithm:

    def __init__(self, trained_phenomes, untrained_phenomes):

        self.trained_phenomes = trained_phenomes
        self.untrained_phenomes = untrained_phenomes
        self.scores = []

    def scoring_algorithm(self):

        for word_phenome in range(len(self.trained_phenomes)):
            score = 0
            for phenome in range(len(self.trained_phenomes[word_phenome])):
                for phenome2 in range(len(self.untrained_phenomes[word_phenome])):
                    if len(self.untrained_phenomes[word_phenome][phenome2]) == len(self.trained_phenomes[word_phenome][phenome]):
                        for phenome3 in range(len(self.untrained_phenomes[word_phenome][phenome2])):
                            if self.untrained_phenomes[word_phenome][phenome2][phenome3] != self.trained_phenomes[word_phenome][phenome][phenome3]:
                                score += 0.1
                    else:
                        score += 0.5
            if len(self.trained_phenomes[word_phenome]) != len(self.untrained_phenomes[word_phenome]):
                score += 0.2
            self.scores.append(score)
        return self.scores
            
      