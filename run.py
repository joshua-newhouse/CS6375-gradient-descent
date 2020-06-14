from multiprocessing import Process

from errors import Errors
from hypothesis import Hypothesis
from weights import Weights


ALLOWABLE_MSE_DELTA = 0.1
MAX_ITERATIONS = 1000000
STARTING_ALPHA = 10000
ALPHA_BASE = 2

class Run (Process):
    def __init__(self, threadID, dataSet, minStartWeight, maxStartWeight):
        Process.__init__(self)
        self.threadID = threadID

        self.weights = Weights(dataSet.getDataPoint(0).dimension())
        self.weights.generateRandom(minStartWeight, maxStartWeight)
        weight = """*****\nThread {0} initial weights:\n{1}\n*****"""
        print(weight.format(self.threadID, self.weights.vector))

        self.trainingErrors = Errors(dataSet.trainingDataPoints, dataSet.trainingActualValues)
        self.testingErrors = Errors(dataSet.testingDataPoints, dataSet.testingActualValues)

        self.hypothesis = Hypothesis()

        self.trainingErrors.updateToLower(self.weights, self.hypothesis)

        self.iterations = 0
        self.alpha = STARTING_ALPHA
    # __init__

    def run(self):
        while(self.trainingErrors.greaterThan(ALLOWABLE_MSE_DELTA) and self.iterations < MAX_ITERATIONS and self.alpha > 0):
            self.iterations += 1

            self.weights.update(self.alpha, self.trainingErrors)

            if (not self.trainingErrors.updateToLower(self.weights, self.hypothesis)):
                self.alpha /= ALPHA_BASE
                self.weights.revert()
            # if

            if (self.iterations % 10 == 0):
                self.alpha *= 1.1
            # if
        # while

        self.print()
    # run

    def print(self):
        output = """
        ==========================================================================================================================================
        RUN RESULTS for thread {0}:
        WEIGHT VECTOR:
        {1}
        ----------------------------------------------------------------------------------
        Lowest training data MSE:
        {2}
        ----------------------------------------------------------------------------------
        ALPHA and ITERATIONS:
        {3}
        {4}
        ----------------------------------------------------------------------------------
        Test data MSE:
        {5}
        ==========================================================================================================================================
        """

        self.testingErrors.updateToLower(self.weights, self.hypothesis)
        print(output.format(self.threadID,
                            self.weights.vector,
                            self.trainingErrors.mse,
                            self.alpha,
                            self.iterations,
                            self.testingErrors.mse))
    # print
# Run
