import threading

from errors import Errors
from hypothesis import Hypothesis
from weights import Weights


ALLOWABLE_MSE_DELTA = 500
MAX_ITERATIONS = 2000000
STARTING_ALPHA = 10000
ALPHA_BASE = 10

class Run (threading.Thread):
    def __init__(self, threadID, dataSet, minStartWeight, maxStartWeight):
        threading.Thread.__init__(self)
        self.threadID = threadID

        self.weights = Weights(dataSet.getDataPoint(0).dimension())
        self.weights.generateRandom(minStartWeight, maxStartWeight)
        self.trainingErrors = Errors(dataSet.trainingDataPoints, dataSet.trainingActualValues)
        self.testingErrors = Errors(dataSet.testingDataPoints, dataSet.testingActualValues)

        self.hypothesis = Hypothesis()

        self.trainingErrors.updateToLower(self.weights, self.hypothesis)
    # __init__

    def run(self):
        self.iterations = 0
        self.alpha = STARTING_ALPHA
        while(self.trainingErrors.greaterThan(ALLOWABLE_MSE_DELTA) and self.iterations < MAX_ITERATIONS and self.alpha > 0):
            self.iterations += 1

            self.weights.update(self.alpha, self.trainingErrors)

            if (not self.trainingErrors.updateToLower(self.weights, self.hypothesis)):
                self.alpha /= ALPHA_BASE
                self.weights.revert()
            # if

            if (self.iterations % 1000 == 0):
                self.alpha *= 1.1
            # if
        # while
    # run

    def print(self):
        print("==========================================================================================================================================")
        print("RUN RESULTS for thread {}:".format(self.threadID))
        print("WEIGHT VECTOR:")
        self.weights.print()
        print("______________")
        print("Lowest MSE:")
        self.trainingErrors.printMSE()
        print("___________")
        print("ALPHA and ITERATIONS:")
        print(self.alpha)
        print(self.iterations)
        print("_____________________")

        self.testingErrors.updateToLower(self.weights, self.hypothesis)
        print("Test data MSE:")
        self.testingErrors.printMSE()
        print("==========================================================================================================================================")
    # print
# Run
