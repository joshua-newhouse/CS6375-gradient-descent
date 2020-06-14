import math
import numpy
import sys

from scikitlinreg import ScikitLinReg


from data import DataSet
from run import Run

class Application:
    def __init__(self, fileName):
        self.fileName = fileName

        data = numpy.genfromtxt(fileName, missing_values=('?'), usecols=(0, 1, 2, 3, 4, 5, 6, 7))
        self.dataSet = DataSet(data)

        self.scikit = ScikitLinReg(data)
    # __init__

    def start(self):
        runs = [ Run("1", self.dataSet, 0, 2),
                 Run("2", self.dataSet, 0, 2),
                 Run("3", self.dataSet, -2, 2),
                 Run("4", self.dataSet, -2, 2),
                 Run("5", self.dataSet, -2, 2),
                 Run("6", self.dataSet, 0, 3),
                 Run("7", self.dataSet, 0, 3),
                 Run("8", self.dataSet, 0, 3) ]

        for run in runs:
            run.start()
        # for

        for run in runs:
            run.join()
        # for

        self.scikit.calculateLinReg()
    # start
# Application

# Main Application Entry
def main():
    app = Application(sys.argv[1])
    app.start()
# main

if __name__ == "__main__":
    main()
# fi
