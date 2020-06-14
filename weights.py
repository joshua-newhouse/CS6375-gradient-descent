import random

class Weights:
    def __init__(self, dimension):
        self.dimension = dimension

    # __init__

    def generateRandom(self, lower, upper):
        self.vector = []
        for i in range(self.dimension):
            self.vector.append(random.randrange(lower, upper, 1))

        self.previousWeights = self.vector.copy()
    # generateRandom

    def getDimension(self):
        return self.dimension

    # dimension

    def get(self, idx):
        return self.vector[idx]
    # get

    def print(self):
        print(self.vector)
    # print

    def update(self, alpha, error):
        self.previousWeights = self.vector.copy()

        for i in range(self.dimension):
            self.vector[i] = self.vector[i] - alpha * error.MSEGradient(i)
        # for
    # update

    def revert(self):
        self.vector = self.previousWeights
    # revert
