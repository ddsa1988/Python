import unittest

from models.survey import AnonymousSurvey

# https://realpython.com/python-unittest/


class SurveyTesting(unittest.TestCase):
    def setUp(self) -> None:
        """Will be executed before each test method."""
        self._survey = AnonymousSurvey("What language did you first learn to speak?")

    def tearDown(self) -> None:
        """Will be executed after each test method."""
        return super().tearDown()

    def test_store_single_response(self) -> None:
        pass


if (__name__ == "__main__"):
    unittest.main()
