class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question: str) -> None:
        self.question = question
        self._responses: list[str] = []

    @property
    def question(self) -> str:
        return self._question

    @question.setter
    def question(self, question: str) -> None:
        if (type(question) != str):
            raise TypeError("question must be a string type.")

        if (question.strip() == ""):
            raise ValueError("question can't be empty.")

        self._question = question.strip().title()

    def get_question(self) -> str:
        """Get the survey question."""
        return "Question: " + self.question

    def store_response(self, response: str) -> None:
        """Store a single response to the survey."""
        if (type(response) != str):
            raise TypeError("response must be a string type.")

        if (response.strip() == ""):
            raise ValueError("response can't be empty.")

        self._responses.append(response.strip())

    def get_responses(self) -> str:
        """Show all the responses that have been given."""

        # responses_formatted: list[str] = []
        # for response in self._responses:
        #     responses_formatted.append("- " + response)

        responses_formatted: list[str] = ["- " + response for response in self._responses]

        return "\n".join(responses_formatted)
