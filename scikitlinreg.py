import numpy
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


class ScikitLinReg:
    def __init__(self, data):
        self.xVectors = []
        self.yValues = []

        for line in data:
            if numpy.isnan(line).any():
                continue
            # if

#             self.xVectors.append(numpy.append(line[1:], [1]))
            self.xVectors.append(line[1:])
            self.yValues.append(line[0])
        # for

        self.xVectors = numpy.array(self.xVectors)
        self.yValues = numpy.array(self.yValues)
    # __init__

    def print(self):
        print(self.xVectors)
        print(self.yValues)
    # print

    def calculateLinReg(self):
        trainingXVectors = []
        trainingYValues = []

        testingXVectors = []
        testingYValues = []

        for i in range(len(self.xVectors)):
            if (i < .8 * len(self.xVectors)):
                trainingXVectors.append(self.xVectors[i])
                trainingYValues.append(self.yValues[i])
            else:
                testingXVectors.append(self.xVectors[i])
                testingYValues.append(self.yValues[i])
            # if
        # for
        model = LinearRegression().fit(trainingXVectors, trainingYValues)

        pred_y = []
        for x in testingXVectors:
            pred_y.append(model.predict([x]))
        # for

        mse = mean_squared_error(testingYValues, pred_y)

        output = """
        *************************************************
             Linear Regression Lib Results (0 Bias Term)

        weight vector: {0}
        MSE: {1}
        *************************************************
        """
        print(output.format(model.coef_, mse))
    # calculateLinReg
# ScikitLinReg
