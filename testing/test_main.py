import unittest
import sys
import os
# Add the parent folder to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from testing.remove_direction_and_keyword_test import TestRemoveDirectionAndKeyword

red = '\033[91m'
reset = '\033[0m'
gray = '\033[90m'

total_tests = 344


class EmojiTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def wasSuccessful(self):
        # Check if there are any errors or failures
        return self.failures == [] and self.errors == []

    def printErrors(self):
        # Print out any errors or failures
        super().printErrors()
        if self.wasSuccessful():
            # Print a custom message with green text (ANSI escape code) and emojis if all tests pass
            print('\033[92mAll tests passed! 🎉🎉🎉\033[0m')


class EmojiTextTestRunner(unittest.TextTestRunner):
    def __init__(self, *args, **kwargs):
        # Ensure we use the EmojiTestResult class
        kwargs['resultclass'] = EmojiTestResult
        super().__init__(*args, **kwargs)


def create_test_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRemoveDirectionAndKeyword))
    return test_suite


if __name__ == '__main__':
    suite = create_test_suite()
    runner = EmojiTextTestRunner(verbosity=2)
    runner.run(suite)
