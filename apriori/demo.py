# -*- coding:utf8 -*-
def loadDataSet():
    return [
        [1, 3, 4],
        [2, 3, 5],
        [1, 2, 3, 5],
        [2, 5],
        # [2, 3, 6]
    ]


def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset, C1)


def scanD(D, Ck, minSupport):
    """
    :param D: 候选集合的列表
    :param Ck: 数据集
    :param minSupport: 最小支持度
    :return:
    """
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not ssCnt.has_key(can):
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.insert(0, key)
        supportData[key] = support
    return retList, supportData


def aprioriGen(Lk, k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(Lk[i])[:k - 2]
            L2 = list(Lk[j])[:k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList


def apriori(dataSet, minSupport=0.5):
    C1 = createC1(dataSet)
    D = map(set, dataSet)
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k - 2]) > 2):
        Ck = aprioriGen(L[k - 2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData


# ------------------------------ 挖掘关联规则 ------------------------------------------
def generateRules(L, supportData, minConf=0.7):
    bigRuleList = []
    for i in range(1, len(L)):
        for freqSet in L[i]:
            if freqSet != frozenset([2, 3, 5]):
                continue
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                # 三个及以上元素的集合
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                # 两个元素的集合
                # print freqSet, H1, supportData, bigRuleList, minConf
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList


def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    ''' 对候选规则集进行评估 '''
    prunedH = []
    for conseq in H:
        if len(freqSet) == 0 or len(freqSet - conseq) == 0 \
                or not supportData.has_key(freqSet) \
                or not supportData.has_key(freqSet - conseq):
            continue
        conf = supportData[freqSet] / supportData[freqSet - conseq]
        if conf >= minConf:
            print freqSet - conseq, '-->', conseq, 'conf:', conf
            brl.append((freqSet - conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH


def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    print "rulesFromConseq:", freqSet, H, brl, minConf
    ''' 生成候选规则集 '''
    m = len(H[0])
    if (len(freqSet) > (m + 1)):
        Hmpl = aprioriGen(H, m + 1)
        # print "Hmpl:", H, m + 1, Hmpl
        Hmpl = calcConf(freqSet, Hmpl, supportData, brl, minConf)
        if (len(Hmpl) > 1):
            rulesFromConseq(freqSet, Hmpl, supportData, brl, minConf)


if __name__ == '__main__':
    dataSet = loadDataSet()
    L, suppData = apriori(dataSet)
    print "L:",L
    print suppData
    print generateRules(L, suppData, minConf=0.7)

    print aprioriGen([frozenset([2, 3]), frozenset([2, 4]), frozenset([3,5]),frozenset([3,4])],3)
    print aprioriGen([frozenset([2]), frozenset([3]), frozenset([5])], 2)