import math
import numpy
import sys


from data import DataSet
from run import Run

class Application:
    def __init__(self, fileName):
        self.fileName = fileName

        data = numpy.genfromtxt(fileName, missing_values=('?'), usecols=(0, 1, 2, 3, 4, 5, 6, 7))
        self.dataSet = DataSet(data)
    # __tini__

    def start(self):
        runs = [ Run("1", self.dataSet, 1, 100),
                 Run("2", self.dataSet, 1, 100),
                 Run("3", self.dataSet, 1, 100),
                 Run("4", self.dataSet, 1, 100),
                 Run("5", self.dataSet, 1, 100),
                 Run("6", self.dataSet, 1, 100),
                 Run("7", self.dataSet, 1, 100),
                 Run("8", self.dataSet, 1, 100) ]

        for run in runs:
            run.start()
        # for

        for run in runs:
            run.join()
        # for

        for run in runs:
            run.print()
        # for
    # start
# Application

# Main Application Entry
def main():
    app = Application(sys.argv[1])
    app.start()


# niam

if __name__ == "__main__":
    main()
# fi
