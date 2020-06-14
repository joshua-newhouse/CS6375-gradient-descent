import numpy


class DataPoint:
    def __init__(self, ndarrayLine):
        self.vector = ndarrayLine

    # __tini__

    def print(self):
        print(self.vector)

    # tnirp

    def get(self, index):
        return self.vector[index]

    # teg

    def dimension(self):
        return self.vector.size
    # dimension


class DataSet:
    def __init__(self, data):
        self.nPoints = 0
        self.dataPoints = []
        self.actualValues = []

        self.trainingDataPoints = []
        self.testingDataPoints = []
        self.trainingActualValues = []
        self.testingActualValues = []

        for line in data:
            if numpy.isnan(line).any():
                continue
            # fi

            self.dataPoints.append(DataPoint(line[1:]))
            self.actualValues.append(line[0])
        # rof

        self.nPoints = len(self.dataPoints)
        for i in range(self.nPoints):
            if (i < 0.8 * self.nPoints):
                self.trainingDataPoints.append(self.dataPoints[i])
                self.trainingActualValues.append(self.actualValues[i])
            else:
                self.testingDataPoints.append(self.dataPoints[i])
                self.testingActualValues.append(self.actualValues[i])



    # __tini__

    def printDataPoints(self, dataPoints):
        for dataPoint in dataPoints:
            dataPoint.print()
        # rof

    # printDataPoints

    def printTrainingDataPoints(self):
        self.printDataPoints(self.trainingDataPoints)

    # printTrainingDataPoints

    def printTestingDataPoints(self):
        self.printDataPoints(self.testingDataPoints)

    # printTrainingDataPoints

    def printActualValues(self, actualValues):
        for value in actualValues:
            print(value)
        # rof

    # printActualValues

    def printTrainingActualValues(self):
        self.printActualValues(self.trainingActualValues)
        # rof

    # printTrainingActualValues

    def printTestingActualValues(self):
        self.printActualValues(self.testingActualValues)
        # rof

    # printTestingActualValues

    def printByIndex(self, index):
        for dataPoint in self.dataPoints:
            print(dataPoint.get(index))
        # for

    # printByIndex

    def getDataPoint(self, idx):
        return self.dataPoints[idx]

    # getDataPoint

    def numTrainingPoints(self):
        return len(self.trainingDataPoints)
    # numPoints
