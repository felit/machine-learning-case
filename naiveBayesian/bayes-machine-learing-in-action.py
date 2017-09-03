# -*- coding:utf8 -*-
def loadDataSet():
    postingLists = [
        ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
        ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]
    return postingLists, classVec


def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def setOfWords2Vec(vocatList, inputSet):
    returnVec = [0] * len(vocatList)
    for word in inputSet:
        if word in vocatList:
            returnVec[vocatList.index(word)] = 1
        else:
            print "the word: %s is not in my Vocabulary!" % word
    return returnVec


if __name__ == '__main__':
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    print myVocabList
    print setOfWords2Vec(myVocabList, listOPosts[0])
    print setOfWords2Vec(myVocabList, listOPosts[3])
