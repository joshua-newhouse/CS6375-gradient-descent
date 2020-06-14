import math


class Hypothesis:
    def function(self, weights, dataPoint):
        if weights.getDimension() != dataPoint.dimension():
            return math.nan
        # fi

        sum = 0
        for i in range(weights.getDimension()):
            sum += weights.get(i) * dataPoint.get(i)
        # rof

        return sum
    # function

    def __init__(self):
        pass
