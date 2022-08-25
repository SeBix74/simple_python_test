from unittest import TestCase

from test_methods.simple_list_operations import SimpleListOperations


class TestSimpleListOperations(TestCase):

    def setUp(self):
        self.simple_operations = SimpleListOperations()

    def test_add_5(self):
        self.simple_operations.add_5()
        expected_value = 5
        expected_list_length = 5
        actual_list_length = len(self.simple_operations.list_to_modify)
        assert expected_value in self.simple_operations.list_to_modify and actual_list_length == expected_list_length, \
            f"{expected_value} is missing and list length is {actual_list_length} instead of {expected_list_length}"

    def test_get_second_element(self):
        second_element = self.simple_operations.get_second_element()
        list_length = len(self.simple_operations.list_to_modify)
        assert second_element == 3 and list_length == 3, f"Got {second_element} and list length is {list_length}"

    def test_add_many_numbers(self):
        self.simple_operations.add_many_numbers()
        assert all(
            item in self.simple_operations.list_to_modify for item in [10, 11, 12]), "Elements 10, 11, 12 are missing"

    def test_change_to_ascending_order(self):
        self.simple_operations.set_elements_in_ascending_order()
        sorted_list = self.simple_operations.list_to_modify
        assert all(sorted_list[index - 1] <= sorted_list[index] for index in range(1, len(sorted_list))), \
            f"List is not sorted in ascending order: {self.simple_operations.list_to_modify}"

    def test_double_values_with_lambda_function(self):
        result = self.simple_operations.double_all_elements_with_lambda_func()
        expected_values = [8, 6, 4, 2]
        assert all(result_value in expected_values for result_value in result), f"Verify output." \
                                                                                f"Expected: {expected_values}, " \
                                                                                f"actual: {result}"

    def test_double_values_with_list_comprehension(self):
        result = self.simple_operations.double_all_elements_with_list_comprehension()
        expected_values = [8, 6, 4, 2]
        assert all(result_value in expected_values for result_value in result), f"Verify output." \
                                                                                f"Expected: {expected_values}, " \
                                                                                f"actual: {result}"

    def test_generate_list(self):
        expected_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = self.simple_operations.generate_list()
        assert all(value in expected_values for value in result) and len(expected_values) == len(result), \
            f"Validate generated values.\nexpected: {expected_values}\nactual: {result}"
