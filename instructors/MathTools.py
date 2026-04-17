'''
@file MathTools.py
@brief A collection of math tools for use in the project.
@author: SLCCE Inc. (Madison Thompson @madisonthompson27)
@copyright: SLCCE Inc. 2026
'''

'''
@class MathTools
@brief A collection of math tool functions that use lists to manipulate data. 
       This class is for instructors to verify the functions.
@author: SLCCE Inc. (Madison Thompson @madisonthompson27)
@copyright: SLCCE Inc. 2026
'''
class MathTools:
    # initialization
    def __init__(self):
        self.sum = 0
        self.difference = 0
        self.product = 0
        self.quotient = 0
        self.factorList = []
    
    # addition of two or more inputted values
    def addition(self, a, b):
        self.sum = a + b
        return self.sum
    
    # subtraction
    def subtraction(self, a, b):
        self.difference = a - b
        return self.difference
    
    # multiplication
    def multiplication(self, a, b):
        self.product = a * b
        return self.product
    
    # division
    def division(self, a, b):
        self.quotient = a / b
        return self.quotient
    
    # add all values in a list, using a for loop
    def forLoopMath(self, numList, operation):
        if not numList:
            return 0

        if operation == "addition":
            for i in range(len(numList)):
                self.sum += numList[i]
            return self.sum

        elif operation == "subtraction":
            self.difference = numList[0]
            for i in range(1, len(numList)):
                self.difference -= numList[i]
            return self.difference

        elif operation == "multiplication":
            self.product = numList[0]
            for i in range(1, len(numList)):
                self.product *= numList[i]
            return self.product

        elif operation == "division":
            self.quotient = numList[0]
            for i in range(1, len(numList)):
                self.quotient /= numList[i]
            return self.quotient
    
    # add all values in a list, using pop
    def popListMath( self, numList, operation ):
        if not numList:
            return 0

        if operation == "multiplication":
            self.product = numList.pop()
            while numList:
                self.product *= numList.pop()
            return self.product

        elif operation == "division":
            self.quotient = numList.pop()
            while numList:
                self.quotient /= numList.pop()
            return self.quotient

        elif operation == "addition":
            while numList:
                self.sum += numList.pop()
            return self.sum

        elif operation == "subtraction":
            self.difference = numList.pop()
            while numList:
                self.difference -= numList.pop()
            return self.difference
    
    # find and print all even OR odd numbers in a list
    # and add them to a new list
    def indexListParity( self, numList, parity ):
        parityList = []
        for num in numList:
            if num % 2 == 0 and parity == "even":
                parityList.append(num)
                print(num)
            elif num % 2 != 0 and parity == "odd":
                parityList.append(num)
                print(num)
        
        self.numList = parityList
        return self.numList
        
    # sort a list of numbers in ascending or descending order
    # direction will either be "ascending" or "descending"
    def sortListDirection( self, numList, direction ):
        if direction == "ascending":
            for i in range(len(numList)):
                for j in range(i + 1, len(numList)):
                    if numList[i] > numList[j]:
                        numList[i], numList[j] = numList[j], numList[i]
                        
        elif direction == "descending":
            for i in range(len(numList)):
                for j in range(i + 1, len(numList)):
                    if numList[i] < numList[j]:
                        numList[i], numList[j] = numList[j], numList[i]
        
        self.numList = numList
        return self.numList
    
    # prune the input list to only contain all even or odd numbers
    def sublistParity( self, numList, parity ):
        for num in numList[:]:
            if num % 2 == 0 and parity == "odd":
                numList.remove(num)
            elif num % 2 != 0 and parity == "even":
                numList.remove(num)
        
        self.numList = numList
        return self.numList

    # return the indexes of all numbers larger or smaller than a given threshold
    # CHALLENGE: add a dictonary to the class to store the indexes of the numbers larger or smaller than the threshold
    def indexListThreshold( self, numList, threshold, comparison ):
        indexList = []
        indexDict = {}
        if comparison == "larger":
            for i in range(len(numList)):
                if numList[i] > threshold:
                    indexList.append(i)
                    indexDict[i] = numList[i]
        elif comparison == "smaller":
            for i in range(len(numList)):
                if numList[i] < threshold:
                    indexList.append(i)
                    indexDict[i] = numList[i]
        
        self.numList = indexList
        return self.numList, indexDict
    
    # find all factors of a number and return them in a list (CHALLENGE)
    def sublistFactors( self, result ):
        factorList = []
        for i in range(1, result + 1):
            if result % i == 0:
                factorList.append(i)
        
        self.numList = factorList
        return self.numList