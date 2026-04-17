'''
@file MathToolsStudent_test.py
@brief Test cases for MathToolsStudent class functions.
@author: SLCCE Inc. (Madison Thompson @madisonthompson27)
@copyright: SLCCE Inc. 2026
'''

import unittest
from students.MathToolsStudent import MathToolsStudent as MathTools


class TestAddition(unittest.TestCase):

    def setUp(self):
        self.mt = MathTools()

    def test_two_positive_numbers(self):
        self.assertEqual(self.mt.addition(3, 4), 7)

    def test_negative_numbers(self):
        self.assertEqual(self.mt.addition(-3, -4), -7)

    def test_floats(self):
        self.assertAlmostEqual(self.mt.addition(1.5, 2.5), 4.0)

    def test_zeros(self):
        self.assertEqual(self.mt.addition(0, 0), 0)

    def test_stores_result_in_attribute(self):
        self.mt.addition(3, 4)
        self.assertEqual(self.mt.sum, 7)


class TestSubtraction(unittest.TestCase):

    def setUp(self):
        self.mt = MathTools()

    def test_two_numbers(self):
        self.assertEqual(self.mt.subtraction(10, 3), 7)

    def test_negative_result(self):
        self.assertEqual(self.mt.subtraction(3, 10), -7)

    def test_zeros(self):
        self.assertEqual(self.mt.subtraction(0, 0), 0)

    def test_stores_result_in_attribute(self):
        self.mt.subtraction(10, 3)
        self.assertEqual(self.mt.difference, 7)


class TestMultiplication(unittest.TestCase):

    def setUp(self):
        self.mt = MathTools()

    def test_two_numbers(self):
        self.assertEqual(self.mt.multiplication(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(self.mt.multiplication(5, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(self.mt.multiplication(-3, 4), -12)

    def test_two_negatives(self):
        self.assertEqual(self.mt.multiplication(-3, -4), 12)

    def test_floats(self):
        self.assertAlmostEqual(self.mt.multiplication(2.5, 4.0), 10.0)

    def test_stores_result_in_attribute(self):
        self.mt.multiplication(3, 4)
        self.assertEqual(self.mt.product, 12)


class TestDivision(unittest.TestCase):

    def setUp(self):
        self.mt = MathTools()

    def test_two_numbers(self):
        self.assertEqual(self.mt.division(10, 2), 5.0)

    def test_float_result(self):
        self.assertAlmostEqual(self.mt.division(7, 2), 3.5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            self.mt.division(10, 0)

    def test_negative_divisor(self):
        self.assertEqual(self.mt.division(10, -2), -5.0)

    def test_stores_result_in_attribute(self):
        self.mt.division(10, 2)
        self.assertEqual(self.mt.quotient, 5.0)


class TestForLoopMath(unittest.TestCase):

    def setUp(self):
        self.mt = MathTools()

    # --- empty list ---

    def test_empty_list_returns_zero(self):
        self.assertEqual(self.mt.forLoopMath([], "addition"), 0)

    # --- addition ---

    def test_addition_basic(self):
        self.assertEqual(self.mt.forLoopMath([1, 2, 3, 4], "addition"), 10)

    def test_addition_single_element(self):
        self.assertEqual(self.mt.forLoopMath([7], "addition"), 7)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.mt.forLoopMath([-1, -2, -3], "addition"), -6)

    def test_addition_mixed_numbers(self):
        self.assertEqual(self.mt.forLoopMath([-5, 5, 10], "addition"), 10)

    def test_addition_accumulates_across_calls(self):
        # self.sum persists between calls on the same instance
        self.mt.forLoopMath([1, 2, 3], "addition")
        result = self.mt.forLoopMath([4, 5, 6], "addition")
        self.assertEqual(result, 21)

    # --- subtraction ---

    def test_subtraction_basic(self):
        self.assertEqual(self.mt.forLoopMath([20, 5, 3, 2], "subtraction"), 10)

    def test_subtraction_single_element(self):
        self.assertEqual(self.mt.forLoopMath([7], "subtraction"), 7)

    def test_subtraction_negative_result(self):
        self.assertEqual(self.mt.forLoopMath([3, 10], "subtraction"), -7)

    def test_subtraction_stores_attribute(self):
        self.mt.forLoopMath([10, 3], "subtraction")
        self.assertEqual(self.mt.difference, 7)

    # --- multiplication ---

    def test_multiplication_basic(self):
        self.assertEqual(self.mt.forLoopMath([2, 3, 4], "multiplication"), 24)

    def test_multiplication_single_element(self):
        self.assertEqual(self.mt.forLoopMath([7], "multiplication"), 7)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.mt.forLoopMath([5, 0, 3], "multiplication"), 0)

    def test_multiplication_stores_attribute(self):
        self.mt.forLoopMath([3, 4], "multiplication")
        self.assertEqual(self.mt.product, 12)

    # --- division ---

    def test_division_basic(self):
        self.assertAlmostEqual(self.mt.forLoopMath([100, 5, 4], "division"), 5.0)

    def test_division_single_element(self):
        self.assertEqual(self.mt.forLoopMath([7], "division"), 7)

    def test_division_float_result(self):
        self.assertAlmostEqual(self.mt.forLoopMath([7, 2], "division"), 3.5)

    def test_division_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            self.mt.forLoopMath([10, 0], "division")

    def test_division_stores_attribute(self):
        self.mt.forLoopMath([10, 2], "division")
        self.assertEqual(self.mt.quotient, 5.0)


class TestPopListMath(unittest.TestCase):

    def setUp(self):
        self.mt = MathTools()

    # --- empty list ---

    def test_empty_list_returns_zero(self):
        self.assertEqual(self.mt.popListMath([], "addition"), 0)

    # --- addition ---

    def test_addition_basic(self):
        self.assertEqual(self.mt.popListMath([1, 2, 3, 4], "addition"), 10)

    def test_addition_single_element(self):
        self.assertEqual(self.mt.popListMath([7], "addition"), 7)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.mt.popListMath([-1, -2, -3], "addition"), -6)

    def test_addition_list_consumed_after_call(self):
        nums = [1, 2, 3]
        self.mt.popListMath(nums, "addition")
        self.assertEqual(nums, [])

    def test_addition_accumulates_across_calls(self):
        self.mt.popListMath([1, 2, 3], "addition")
        result = self.mt.popListMath([4, 5, 6], "addition")
        self.assertEqual(result, 21)

    # --- subtraction ---

    def test_subtraction_basic(self):
        # pop() pulls from the end, so [20, 5, 3, 2] seeds with 2, then 2-3-5-20 = -26
        self.assertEqual(self.mt.popListMath([20, 5, 3, 2], "subtraction"), -26)

    def test_subtraction_single_element(self):
        self.assertEqual(self.mt.popListMath([7], "subtraction"), 7)

    def test_subtraction_two_elements(self):
        # seeds with 3 (last), then 3 - 10 = -7
        self.assertEqual(self.mt.popListMath([10, 3], "subtraction"), -7)

    def test_subtraction_stores_attribute(self):
        self.mt.popListMath([10, 3], "subtraction")
        self.assertEqual(self.mt.difference, -7)

    # --- multiplication ---

    def test_multiplication_basic(self):
        self.assertEqual(self.mt.popListMath([2, 3, 4], "multiplication"), 24)

    def test_multiplication_single_element(self):
        self.assertEqual(self.mt.popListMath([7], "multiplication"), 7)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.mt.popListMath([5, 0, 3], "multiplication"), 0)

    def test_multiplication_stores_attribute(self):
        self.mt.popListMath([3, 4], "multiplication")
        self.assertEqual(self.mt.product, 12)

    # --- division ---

    def test_division_basic(self):
        # pop() pulls from the end: seeds with 4, then 4/5/100 = 0.008
        self.assertAlmostEqual(self.mt.popListMath([100, 5, 4], "division"), 0.008)

    def test_division_single_element(self):
        self.assertEqual(self.mt.popListMath([7], "division"), 7)

    def test_division_two_elements(self):
        # seeds with 2 (last), then 2/7 ≈ 0.2857
        self.assertAlmostEqual(self.mt.popListMath([7, 2], "division"), 2 / 7)

    def test_division_stores_attribute(self):
        self.mt.popListMath([2, 10], "division")
        self.assertAlmostEqual(self.mt.quotient, 10 / 2)


class TestIndexListParity(unittest.TestCase):

    def setUp(self):
        self.mt = MathTools()

    def test_even_numbers(self):
        self.assertEqual(self.mt.indexListParity([1, 2, 3, 4, 5, 6], "even"), [2, 4, 6])

    def test_odd_numbers(self):
        self.assertEqual(self.mt.indexListParity([1, 2, 3, 4, 5, 6], "odd"), [1, 3, 5])

    def test_all_even_input(self):
        self.assertEqual(self.mt.indexListParity([2, 4, 6], "even"), [2, 4, 6])

    def test_no_matches_returns_empty(self):
        self.assertEqual(self.mt.indexListParity([1, 3, 5], "even"), [])

    def test_empty_list(self):
        self.assertEqual(self.mt.indexListParity([], "even"), [])

    def test_invalid_parity_string_returns_empty(self):
        self.assertEqual(self.mt.indexListParity([1, 2, 3], "neither"), [])

    def test_stores_result_in_attribute(self):
        self.mt.indexListParity([1, 2, 3, 4], "even")
        self.assertEqual(self.mt.numList, [2, 4])


class TestSortListDirection(unittest.TestCase):

    def setUp(self):
        self.mt = MathTools()

    def test_ascending(self):
        self.assertEqual(self.mt.sortListDirection([3, 1, 4, 1, 5], "ascending"), [1, 1, 3, 4, 5])

    def test_descending(self):
        self.assertEqual(self.mt.sortListDirection([3, 1, 4, 1, 5], "descending"), [5, 4, 3, 1, 1])

    def test_already_sorted_ascending(self):
        self.assertEqual(self.mt.sortListDirection([1, 2, 3], "ascending"), [1, 2, 3])

    def test_already_sorted_descending(self):
        self.assertEqual(self.mt.sortListDirection([3, 2, 1], "descending"), [3, 2, 1])

    def test_single_element(self):
        self.assertEqual(self.mt.sortListDirection([42], "ascending"), [42])

    def test_empty_list(self):
        self.assertEqual(self.mt.sortListDirection([], "ascending"), [])

    def test_invalid_direction_returns_unsorted(self):
        self.assertEqual(self.mt.sortListDirection([3, 1, 2], "sideways"), [3, 1, 2])

    def test_negative_numbers_ascending(self):
        self.assertEqual(self.mt.sortListDirection([-3, -1, -2], "ascending"), [-3, -2, -1])


class TestSublistParity(unittest.TestCase):

    def setUp(self):
        self.mt = MathTools()

    def test_keep_even_mixed(self):
        result = self.mt.sublistParity([1, 2, 3, 4, 5, 6], "even")
        self.assertEqual(result, [2, 4, 6])

    def test_keep_odd_mixed(self):
        result = self.mt.sublistParity([1, 2, 3, 4, 5, 6], "odd")
        self.assertEqual(result, [1, 3, 5])

    def test_all_match_parity(self):
        self.assertEqual(self.mt.sublistParity([2, 4, 6], "even"), [2, 4, 6])

    def test_none_match_parity_consecutive(self):
        result = self.mt.sublistParity([1, 3, 5], "even")
        self.assertEqual(result, [])

    def test_empty_list(self):
        self.assertEqual(self.mt.sublistParity([], "even"), [])

    def test_stores_result_in_attribute(self):
        self.mt.sublistParity([1, 2, 3, 4], "even")
        self.assertEqual(self.mt.numList, [2, 4])


class TestIndexListThreshold(unittest.TestCase):

    def setUp(self):
        self.mt = MathTools()

    def test_larger_basic(self):
        indices, d = self.mt.indexListThreshold([10, 20, 30], 15, "larger")
        self.assertEqual(indices, [1, 2])
        self.assertEqual(d, {1: 20, 2: 30})

    def test_smaller_basic(self):
        indices, d = self.mt.indexListThreshold([10, 20, 30], 25, "smaller")
        self.assertEqual(indices, [0, 1])
        self.assertEqual(d, {0: 10, 1: 20})

    def test_none_larger(self):
        indices, d = self.mt.indexListThreshold([1, 2, 3], 10, "larger")
        self.assertEqual(indices, [])
        self.assertEqual(d, {})

    def test_none_smaller(self):
        indices, d = self.mt.indexListThreshold([10, 20, 30], 5, "smaller")
        self.assertEqual(indices, [])
        self.assertEqual(d, {})

    def test_all_larger(self):
        indices, d = self.mt.indexListThreshold([10, 20, 30], 5, "larger")
        self.assertEqual(indices, [0, 1, 2])
        self.assertEqual(d, {0: 10, 1: 20, 2: 30})

    def test_threshold_equal_not_included(self):
        # comparisons are strict (> and <), not >= or <=
        indices_l, _ = self.mt.indexListThreshold([5, 10, 15], 10, "larger")
        self.assertEqual(indices_l, [2])
        indices_s, _ = self.mt.indexListThreshold([5, 10, 15], 10, "smaller")
        self.assertEqual(indices_s, [0])

    def test_empty_list(self):
        indices, d = self.mt.indexListThreshold([], 10, "larger")
        self.assertEqual(indices, [])
        self.assertEqual(d, {})

    def test_invalid_comparison_returns_empty(self):
        indices, d = self.mt.indexListThreshold([1, 2, 3], 2, "equal")
        self.assertEqual(indices, [])
        self.assertEqual(d, {})

    def test_stores_index_list_in_attribute(self):
        self.mt.indexListThreshold([10, 20, 30], 15, "larger")
        self.assertEqual(self.mt.numList, [1, 2])


class TestSublistFactors(unittest.TestCase):

    def setUp(self):
        self.mt = MathTools()

    def test_factors_of_12(self):
        self.assertEqual(self.mt.sublistFactors([], 12), [1, 2, 3, 4, 6, 12])

    def test_factors_of_prime(self):
        self.assertEqual(self.mt.sublistFactors([], 7), [1, 7])

    def test_factors_of_1(self):
        self.assertEqual(self.mt.sublistFactors([], 1), [1])

    def test_factors_of_perfect_square(self):
        self.assertEqual(self.mt.sublistFactors([], 16), [1, 2, 4, 8, 16])

    def test_factors_of_large_number(self):
        self.assertEqual(self.mt.sublistFactors([], 100), [1, 2, 4, 5, 10, 20, 25, 50, 100])

    def test_factors_of_zero_returns_empty(self):
        # range(1, 1) is empty, so no factors are appended
        self.assertEqual(self.mt.sublistFactors([], 0), [])

    def test_stores_result_in_attribute(self):
        self.mt.sublistFactors([], 6)
        self.assertEqual(self.mt.numList, [1, 2, 3, 6])


if __name__ == "__main__":
    unittest.main()