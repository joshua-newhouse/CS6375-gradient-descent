import math


class Errors:
    def __init__(self, dataPoints, actualValues):
        self.dataPoints = dataPoints
        self.actualValues = actualValues
        self.vector = [math.inf] * len(dataPoints)
        self.mse = math.inf
        self.prevMSE = 0
    # __init__

    def numPoints(self):
        return len(self.vector)
    # numPoints

    def get(self, idx):
        return self.vector[idx]
    # get

    def MSE(self):
        sum = 0

        for i in range(self.numPoints()):
            sum += self.get(i) ** 2
        # for

        return sum / (2 * self.numPoints())
    # MSE

    def MSEGradient(self, i):
        sum = 0

        for j in range(self.numPoints()):
            sum += self.get(j) * self.dataPoints[j].get(i)
        # for

        return sum / self.numPoints()
    # MSEGradient

    def updateToLower(self, weights, hypothesis):
        newErrors = []
        prevErrors = self.vector

        for j in range(self.numPoints()):
            error = hypothesis.function(weights, self.dataPoints[j]) - self.actualValues[j]
            newErrors.append(error)
        # for

        self.vector = newErrors
        tmpMSE = self.MSE()
        if (tmpMSE > self.mse):
            self.vector = prevErrors
            return False
        # if

        self.prevMSE = self.mse
        self.mse = tmpMSE
        return True
    # updateToLower

    def greaterThan(self, mseDelta):
        return self.prevMSE - self.mse > mseDelta
    # greaterThan

    def printMSE(self):
        print(self.mse)
    # printMSE
