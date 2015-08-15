__author__ = 'Wichito'
import math


def solveProblem502():
    return getSecondValue()


def getFirstValue():
    return solveCastles(10**12,100)

def getSecondValue():
    return  solveCastles(1000,1000)


def getThirdValue():
    return  solveCastles(100,10**12)


def solveTestValues():
    #print(solveCastles(4,2)/10)
    print(solveCastles(4,5))
    print(solveCastles(10,13)/37959702514)
    print(solveCastles(13,10)/3729050610636)
    print((solveCastles(100,100)%1000000007)/841913936)

def solveCastles(width,height):
    totalHeight=height-1
    #invalidCastles=getOddCastlesWithTuple(width,totalHeight-1)
    print('Finished invalid castles')
    overcountedCastles=getOddCastlesWithTuple(width,totalHeight)
    #return overcountedCastles-invalidCastles

def getOddCastlesWithTuple(width,realHeight):
    arrays= {'even': getFirstArrayOfEvenCastlesPerHeight(realHeight),
             'odd': getFirstArrayOfOddCastlesPerHeight(realHeight)}
    for currentColumn in range(1,width):
        arrays=getNextArraysOfCastlesPerHeightTwoAtATime(realHeight,arrays)
        #print(currentColumn)
    return sum(arrays['odd'])

def getOddCastles(width,realHeight):
    previousEvenCastlesByHeight=getFirstArrayOfEvenCastlesPerHeight(realHeight)
    previousOddCastlesByHeight=getFirstArrayOfOddCastlesPerHeight(realHeight)
    for currentColumn in range(1,width):
        temp=getNextArrayOfEvenCastlesPerHeight(realHeight,previousEvenCastlesByHeight,previousOddCastlesByHeight)
        previousOddCastlesByHeight=getNextArrayOfOddCastlesPerHeight(realHeight,previousEvenCastlesByHeight,previousOddCastlesByHeight)
        previousEvenCastlesByHeight=temp
    return sum(previousOddCastlesByHeight)


def getFirstArrayOfEvenCastlesPerHeight(totalHeight):
    evenCastlesByHeight=[]
    for index in range(totalHeight+1):
        if index%2==0:
            evenCastlesByHeight.append(1)
        else:
            evenCastlesByHeight.append(0)

    return evenCastlesByHeight


def getFirstArrayOfOddCastlesPerHeight(totalHeight):
    oddCastlesByHeight=[]
    for index in range(totalHeight+1):
        if index%2==0:
            oddCastlesByHeight.append(0)
        else:
            oddCastlesByHeight.append(1)

    return oddCastlesByHeight


def getNextArrayOfEvenCastlesPerHeight(totalHeight, previousArrayOfEvenCastles, previousArrayOfOddCastles):
    evenCastlesByHeight=[]
    evenStart=0
    for index in range(totalHeight+1):
        if index%2==0:
            evenStart=0
        else:
            evenStart=1
        # the (eventStart-1)^2 is to turn eventStart from 0 to 1 and from 1 to 0
        partialEvenSumAlternating=[previousArrayOfEvenCastles[x] for x in range(evenStart,index-2+1,2)]
        partialOddSumAlternating=[previousArrayOfOddCastles[x] for x in range((evenStart-1)**2,index-1+1,2)]
        evenCastlesByHeight.append(sum(partialEvenSumAlternating)+\
                                       sum(previousArrayOfEvenCastles[index:])+\
                                       sum(partialOddSumAlternating))
    return evenCastlesByHeight


def getNextArrayOfOddCastlesPerHeight(totalHeight, previousArrayOfEvenCastles, previousArrayOfOddCastles):
    oddCastlesByHeight=[]
    oddStart=0
    for index in range(totalHeight+1):
        if index%2==0:
            oddStart=1
        else:
            oddStart=0
        # the (eventStart-1)^2 is to turn eventStart from 0 to 1 and from 1 to 0
        partialEvenSumAlternating=[previousArrayOfEvenCastles[x] for x in range(oddStart,index-1+1,2)]
        partialOddSumAlternating=[previousArrayOfOddCastles[x] for x in range((oddStart-1)**2,index-2+1,2)]
        oddCastlesByHeight.append(sum(partialEvenSumAlternating)+\
                                       sum(previousArrayOfOddCastles[index:])+\
                                       sum(partialOddSumAlternating))
    return oddCastlesByHeight


def getNextArraysOfCastlesPerHeight(totalHeight,arrays):
    evenCastlesByHeight=[]
    oddCastlesByHeight=[]
    evenStart=0
    for index in range(totalHeight+1):
        if index%2==0:
            evenStart=0
        else:
            evenStart=1

        # the (eventStart-1)^2 is to turn eventStart from 0 to 1 and from 1 to 0
        partialEvenSumAlternating=[arrays['even'][x] for x in range(evenStart,index-2+1,2)]
        partialOddSumAlternating=[arrays['odd'][x] for x in range((evenStart-1)**2,index-1+1,2)]
        evenCastlesByHeight.append(sum(partialEvenSumAlternating)+\
                                       sum(arrays['even'][index:])+\
                                       sum(partialOddSumAlternating))

        # the (eventStart-1)^2 is to turn eventStart from 0 to 1 and from 1 to 0
        partialEvenSumAlternating=[arrays['even'][x] for x in range((evenStart-1)**2,index-1+1,2)]
        partialOddSumAlternating=[arrays['odd'][x] for x in range(evenStart,index-2+1,2)]
        oddCastlesByHeight.append(sum(partialEvenSumAlternating)+\
                                       sum(arrays['odd'][index:])+\
                                       sum(partialOddSumAlternating))

    arrays['even']=evenCastlesByHeight
    arrays['odd']=oddCastlesByHeight

    return arrays

def getNextArraysOfCastlesPerHeightTwoAtATime(totalHeight,arrays):
    evenCastlesByHeight=[]
    oddCastlesByHeight=[]
    partialSumAlternatingOne=[]
    partialSumAlternatingTwo=[]
    evenStart=0
    for index in range(0,totalHeight+1,2):
        for x in range(evenStart,index+1,2):
            if(x>=1):
                partialSumAlternatingOne.append(arrays['even'][x]+ arrays['odd'][x-1])
                partialSumAlternatingTwo.append(arrays['odd'][x] + arrays['even'][x-1])
            else:
                partialSumAlternatingOne.append(arrays['even'][x])
                partialSumAlternatingTwo.append(arrays['odd'][x])

        evenSum=sum(arrays['even'][index+1:])
        oddSum=sum(arrays['odd'][index:])

        evenCastlesByHeight.append(sum(partialSumAlternatingOne)+evenSum)
        evenCastlesByHeight.append(sum(partialSumAlternatingTwo) + evenSum-arrays['even'][index+1])

        oddCastlesByHeight.append(sum(partialSumAlternatingTwo) + oddSum)
        oddCastlesByHeight.append(sum(partialSumAlternatingOne) + oddSum-arrays['odd'][index])

    arrays['even']=evenCastlesByHeight
    arrays['odd']=oddCastlesByHeight

    return arrays

