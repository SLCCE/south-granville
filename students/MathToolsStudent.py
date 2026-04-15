'''
@file MathToolsStudent.py
@brief A collection of math tools for use in the project.
@author: SLCCE Inc. (Madison Thompson @madisonthompson27)
@copyright: SLCCE Inc. 2026
'''

'''
@class MathToolsStudent
@brief A collection of math tool functions that use lists to manipulate data.
       Students should implement each method according to the TODOs and docstrings.
@author: SLCCE Inc. (Madison Thompson @madisonthompson27) and (you! @yourgithubusername) #FIXME
@copyright: SLCCE Inc. 2026
'''
class MathToolsStudent:

    def __init__(self):
        '''
        Initializes all result attributes to their identity values.

        Attributes:
            self.sum        (int/float) : stores the result of addition operations. Starts at 0.
            self.difference (int/float) : stores the result of subtraction operations. Starts at 0.
            self.product    (int/float) : stores the result of multiplication operations. Starts at 0.
            self.quotient   (int/float) : stores the result of division operations. Starts at 0.
            self.factorList (list)      : stores the result of factor operations. Starts as empty list.
        '''
        self.sum = 0
        self.difference = 0
        self.product = 0
        self.quotient = 0
        self.factorList = []

    def addition(self, a, b, *args):
        '''
        Adds two or more numbers together and stores the result in self.sum.

        Parameters:
            a     (int/float) : the first number to add. Required.
            b     (int/float) : the second number to add. Required.
            *args (int/float) : any number of additional values to add. Optional.

        Returns:
            self.sum (int/float) : the sum of all provided values.

        Example:
            addition(3, 4)       -> returns 7,  self.sum = 7
            addition(1, 2, 3, 4) -> returns 10, self.sum = 10
        '''
        pass
        #TODO: implement addition of two or more inputted values

    def subtraction(self, a, b, *args):
        '''
        Subtracts b and any additional values from a, and stores the result in self.difference.

        Parameters:
            a     (int/float) : the starting value to subtract from. Required.
            b     (int/float) : the first value to subtract. Required.
            *args (int/float) : any number of additional values to subtract. Optional.

        Returns:
            self.difference (int/float) : the result of a - b - args[0] - args[1] - ...

        Example:
            subtraction(10, 3)       -> returns 7,  self.difference = 7
            subtraction(20, 5, 3, 2) -> returns 10, self.difference = 10
        '''
        pass
        #TODO: implement subtraction of two or more inputted values

    def multiplication(self, a, b, *args):
        '''
        Multiplies two or more numbers together and stores the result in self.product.

        Parameters:
            a     (int/float) : the first number to multiply. Required.
            b     (int/float) : the second number to multiply. Required.
            *args (int/float) : any number of additional values to multiply. Optional.

        Returns:
            self.product (int/float) : the product of all provided values.

        Example:
            multiplication(3, 4)    -> returns 12, self.product = 12
            multiplication(2, 3, 4) -> returns 24, self.product = 24
        '''
        pass
        #TODO: implement multiplication of two or more inputted values

    def division(self, a, b, *args):
        '''
        Divides a by b and any additional values, and stores the result in self.quotient.
        Raises ZeroDivisionError if any divisor is 0.

        Parameters:
            a     (int/float) : the numerator (value to be divided). Required.
            b     (int/float) : the first divisor. Required. Must not be 0.
            *args (int/float) : any number of additional divisors. Optional. Must not be 0.

        Returns:
            self.quotient (float) : the result of a / b / args[0] / args[1] / ...

        Raises:
            ZeroDivisionError : if b or any value in args is 0.

        Example:
            division(10, 2)       -> returns 5.0,  self.quotient = 5.0
            division(100, 5, 4)   -> returns 5.0,  self.quotient = 5.0
            division(10, 0)       -> raises ZeroDivisionError
        '''
        pass
        #TODO: implement division of two or more inputted values

    def forLoopMath(self, numList, operation):
        '''
        Performs a math operation on all values in a list using a for loop with index access.
        The first element of the list is used as the starting value for subtraction,
        multiplication, and division. Addition starts from 0.
        Returns 0 immediately if the list is empty.

        Parameters:
            numList   (list of int/float) : the list of numbers to operate on.
            operation (str)               : the operation to perform. Must be one of:
                                            "addition"       -> adds all values, stores in self.sum
                                            "subtraction"    -> subtracts from first value, stores in self.difference
                                            "multiplication" -> multiplies from first value, stores in self.product
                                            "division"       -> divides from first value, stores in self.quotient

        Returns:
            (int/float) : the result of the operation, drawn from the appropriate attribute.
            Returns 0 if numList is empty.

        Raises:
            ZeroDivisionError : if operation is "division" and any element after index 0 is 0.

        Example:
            forLoopMath([1, 2, 3, 4], "addition")       -> returns 10
            forLoopMath([20, 5, 3, 2], "subtraction")   -> returns 10  (20 - 5 - 3 - 2)
            forLoopMath([2, 3, 4],     "multiplication") -> returns 24  (2 * 3 * 4)
            forLoopMath([100, 5, 4],   "division")       -> returns 5.0 (100 / 5 / 4)
            forLoopMath([],            "addition")       -> returns 0
        '''
        pass
        #TODO: return 0 if numList is empty
        #TODO: implement for loop addition       (accumulate into self.sum, return self.sum)
        #TODO: implement for loop subtraction    (seed from numList[0], loop from index 1, return self.difference)
        #TODO: implement for loop multiplication (seed from numList[0], loop from index 1, return self.product)
        #TODO: implement for loop division       (seed from numList[0], loop from index 1, return self.quotient)

    def popListMath(self, numList, operation):
        '''
        Performs a math operation on all values in a list using pop().
        pop() removes and returns the last element of the list each iteration,
        so the list will be empty after this method runs.
        The first element popped is used as the starting value for subtraction,
        multiplication, and division. Addition starts from 0.
        Returns 0 immediately if the list is empty.

        Parameters:
            numList   (list of int/float) : the list of numbers to operate on.
                                            WARNING: this list will be empty after the call.
            operation (str)               : the operation to perform. Must be one of:
                                            "addition"       -> adds all values, stores in self.sum
                                            "subtraction"    -> subtracts from first popped value, stores in self.difference
                                            "multiplication" -> multiplies from first popped value, stores in self.product
                                            "division"       -> divides from first popped value, stores in self.quotient

        Returns:
            (int/float) : the result of the operation, drawn from the appropriate attribute.
            Returns 0 if numList is empty.

        Raises:
            ZeroDivisionError : if operation is "division" and any popped value after the first is 0.

        Example:
            popListMath([1, 2, 3, 4], "addition")       -> returns 10,  numList is now []
            popListMath([20, 5, 3, 2], "subtraction")   -> returns 10,  numList is now []
            popListMath([2, 3, 4],     "multiplication") -> returns 24,  numList is now []
            popListMath([100, 5, 4],   "division")       -> returns 5.0, numList is now []
            popListMath([],            "addition")       -> returns 0
        '''
        pass
        #TODO: return 0 if numList is empty
        #TODO: implement pop list addition       (accumulate into self.sum, return self.sum)
        #TODO: implement pop list subtraction    (seed from first pop(), loop remaining, return self.difference)
        #TODO: implement pop list multiplication (seed from first pop(), loop remaining, return self.product)
        #TODO: implement pop list division       (seed from first pop(), loop remaining, return self.quotient)

    def indexListParity(self, numList, parity):
        '''
        Finds all even or odd numbers in a list, prints each one, and returns them in a new list.
        The original list is not modified. Result is also stored in self.numList.

        Parameters:
            numList (list of int) : the list of numbers to search through.
            parity  (str)         : which numbers to find. Must be one of:
                                    "even" -> collect numbers where num % 2 == 0
                                    "odd"  -> collect numbers where num % 2 != 0

        Returns:
            self.numList (list of int) : a new list containing only the even or odd numbers.
            Returns an empty list if no matches are found or if numList is empty.

        Example:
            indexListParity([1, 2, 3, 4, 5, 6], "even") -> prints 2, 4, 6 and returns [2, 4, 6]
            indexListParity([1, 2, 3, 4, 5, 6], "odd")  -> prints 1, 3, 5 and returns [1, 3, 5]
            indexListParity([1, 3, 5],           "even") -> returns []
        '''
        pass
        #TODO: implement index list for even
        #TODO: implement index list for odd

    def sortListDirection(self, numList, direction):
        '''
        Sorts a list of numbers in ascending or descending order in-place using a
        bubble sort algorithm (nested for loops with index swapping).
        Result is also stored in self.numList.

        Parameters:
            numList   (list of int/float) : the list of numbers to sort.
                                            NOTE: the original list is modified in-place.
            direction (str)               : the sort direction. Must be one of:
                                            "ascending"  -> smallest to largest
                                            "descending" -> largest to smallest

        Returns:
            self.numList (list of int/float) : the sorted list.
            If direction is neither "ascending" nor "descending", the list is returned unsorted.

        Example:
            sortListDirection([3, 1, 4, 1, 5], "ascending")  -> returns [1, 1, 3, 4, 5]
            sortListDirection([3, 1, 4, 1, 5], "descending") -> returns [5, 4, 3, 1, 1]
            sortListDirection([],              "ascending")  -> returns []
        '''
        pass
        #TODO: implement sort list ascending
        #TODO: implement sort list descending

    def sublistParity(self, numList, parity):
        '''
        Removes all even or odd numbers from the input list in-place, keeping only
        numbers that match the given parity. Result is also stored in self.numList.

        HINT: modifying a list while iterating over it directly causes elements to be
        skipped. Iterate over a copy of the list (numList[:]) to avoid this.

        Parameters:
            numList (list of int) : the list to prune in-place.
                                    NOTE: the original list is modified — numbers that
                                    don't match parity are removed from it.
            parity  (str)         : which numbers to KEEP. Must be one of:
                                    "even" -> remove all odd numbers, keep even
                                    "odd"  -> remove all even numbers, keep odd

        Returns:
            self.numList (list of int) : the pruned list containing only matching numbers.

        Example:
            sublistParity([1, 2, 3, 4, 5, 6], "even") -> returns [2, 4, 6], numList is now [2, 4, 6]
            sublistParity([1, 2, 3, 4, 5, 6], "odd")  -> returns [1, 3, 5], numList is now [1, 3, 5]
            sublistParity([],                 "even") -> returns []
        '''
        pass
        #TODO: iterate over a copy of numList (use numList[:]) to avoid skipping elements
        #TODO: remove numbers that do NOT match parity from the original numList
        #TODO: store result in self.numList and return it

    def indexListThreshold(self, numList, threshold, comparison):
        '''
        Finds all numbers in a list that are strictly larger or smaller than a threshold,
        and returns a list of their indices. Also builds a dictionary mapping each index
        to its value. Result indices are stored in self.numList.

        NOTE: comparisons are strict (> and <), so values equal to the threshold are excluded.

        Parameters:
            numList    (list of int/float) : the list of numbers to search.
            threshold  (int/float)         : the value to compare each element against.
            comparison (str)               : the comparison direction. Must be one of:
                                             "larger"  -> find indices where numList[i] > threshold
                                             "smaller" -> find indices where numList[i] < threshold

        Returns:
            self.numList (list of int) : a list of indices where the condition is met.
            indexDict    (dict)        : a dictionary of {index: value} for each matching element.
            Returns an empty list and empty dict if no matches are found or numList is empty.

        Example:
            indexListThreshold([10, 20, 30], 15, "larger")  -> returns [1, 2], dict = {1: 20, 2: 30}
            indexListThreshold([10, 20, 30], 25, "smaller") -> returns [0, 1], dict = {0: 10, 1: 20}
            indexListThreshold([5, 10, 15],  10, "larger")  -> returns [2],    dict = {2: 15}
            indexListThreshold([5, 10, 15],  10, "smaller") -> returns [0],    dict = {0: 5}
        '''
        pass
        #TODO: find the indices of all numbers larger or smaller than the threshold
        #TODO: append those indices to a new list AND dictionary (with the value as the dict value)
        #TODO: store result in self.numList and return both the list and the dictionary

    def sublistFactors(self, numList, result):
        '''
        Finds all factors of a given integer and returns them as a sorted list.
        A factor is any integer that divides evenly into result (remainder of 0).
        Result is also stored in self.numList.

        Parameters:
            numList (list) : unused placeholder parameter — leave it in the signature.
            result  (int)  : the number to find factors of. Should be a positive integer.
                             Passing 0 will return an empty list.

        Returns:
            self.numList (list of int) : a sorted list of all factors of result.

        Example:
            sublistFactors([], 12) -> returns [1, 2, 3, 4, 6, 12]
            sublistFactors([], 7)  -> returns [1, 7]
            sublistFactors([], 1)  -> returns [1]
            sublistFactors([], 0)  -> returns []
        '''
        pass
        #TODO: loop from 1 to result (inclusive) using range()
        #TODO: check if result % i == 0 (i.e. i is a factor)
        #TODO: append factors to a new list
        #TODO: store result in self.numList and return it