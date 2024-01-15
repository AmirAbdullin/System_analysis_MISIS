from io import StringIO
import csv
import math

class InformationEntropyCalculator:
    def __init__(self, csvString):
        self.n = 0
        self.R = []

        self.read_data(csvString)

    def read_data(self, csvString):
        f = StringIO(csvString)
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            self.R.append([int(ri) for ri in row])
            self.n += 1

    def calculate_entropy(self):
        H = 0.0

        for node in self.R:
            probabilities = []

            for ri in node:
                probabilities.append(ri * 1.0 / (self.n - 1))

            node_H = 0.0

            for p in probabilities:
                if p != 0:
                    node_H += p * math.log(p, 2)

            H -= node_H

        return H


def task(csvString):
    calculator = InformationEntropyCalculator(csvString)
    return calculator.calculate_entropy()

print(task("1,0,4,0,0\n2,1,2,0,0\n2,1,0,1,1\n0,1,0,1,1\n0,1,0,2,1\n0,1,0,2,1"))
