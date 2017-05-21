from numpy import *
import operator


def createDataSet():
    group = array([[1.0, 0.9], [1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def kNNClassify(newInput, dataSet, labels, k):
    numSamples = dataSet.shape[0]
    print numSamples
    diff = tile(newInput, (numSamples, 1)) - dataSet
    print diff
    squaredDiff = diff ** 2
    print squaredDiff
    squaredDist = sum(squaredDiff, axis=1)
    print squaredDist
    distance = squaredDist ** 0.5
    print distance

    # step 2
    sortedDistIndices = argsort(distance)
    print sortedDistIndices

    classCount = {}
    for i in xrange(k):
        # step 3
        voteLabel = labels[sortedDistIndices[i]]
        # step 4
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

    # step 5
    maxCount = 0
    for label, count in classCount.items():
        if count > maxCount:
            maxCount = count
            maxIndex = label
    return maxIndex


if __name__ == '__main__':
    dataSet, labels = createDataSet()

    testX = array([1.2, 1.0])
    testX = array([0.2, 0.1])
    k = 3
    outputLabel = kNNClassify(testX, dataSet, labels, 3)
    print(outputLabel)
