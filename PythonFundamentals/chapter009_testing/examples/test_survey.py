import unittest

from models.survey import AnonymousSurvey

# https://realpython.com/python-unittest/


class SurveyTesting(unittest.TestCase):
    def setUp(self) -> None:
        """Fixture: Will be executed before each test method."""
        self._survey = AnonymousSurvey("What language did you first learn to speak?")

    def tearDown(self) -> None:
        """Fixture: Will be executed after each test method."""
        del self._survey

    # @unittest.skip("Not implemented")
    def test_store_single_response(self) -> None:
        survey_responses: list[str] = self._survey.get_responses()

        self._survey.store_response(response="English")

        self.assertIn("English", survey_responses)

    def test_store_three_responses(self) -> None:
        survey_responses: list[str] = self._survey.get_responses()

        responses_for_test: list[str] = ["English", "Spanish", "Mandarin"]

        for response in responses_for_test:
            self._survey.store_response(response=response)

        for response in responses_for_test:
            self.assertIn(response, survey_responses)


if (__name__ == "__main__"):
    unittest.main()
