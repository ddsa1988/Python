import logging
import os
import random
from pathlib import Path

# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key


def main() -> None:
    logger: logging.Logger = logging.getLogger(__name__)

    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    NUMBER_OF_QUIZ_FILES: int = 1
    QUIZ_OPTIONS: str = "ABCD"

    directory_path: str = f"{Path(__file__).parent}{os.sep}files"

    if (not os.path.isdir(directory_path)):
        try:
            path: Path = Path(directory_path)
            path.mkdir()
        except PermissionError as ex:
            logger.warning(
                f"Insufficient permissions to create directory: {ex}")
            return
        except OSError as ex:
            logger.warning(f"Failed to create directory: {ex}")
            return

    capitals: dict[str, str] = {"Alabama": "Montgomery", "Alaska": "Juneau", "Arizona":
                                "Phoenix", "Arkansas": "Little Rock", "California": "Sacramento", "Colorado":
                                "Denver", "Connecticut": "Hartford", "Delaware": "Dover", "Florida":
                                "Tallahassee", "Georgia": "Atlanta", "Hawaii": "Honolulu", "Idaho": "Boise",
                                "Illinois": "Springfield", "Indiana": "Indianapolis", "Iowa": "Des Moines",
                                "Kansas": "Topeka", "Kentucky": "Frankfort", "Louisiana": "Baton Rouge",
                                "Maine": "Augusta", "Maryland": "Annapolis", "Massachusetts": "Boston",
                                "Michigan": "Lansing", "Minnesota": "Saint Paul", "Mississippi": "Jackson",
                                "Missouri": "Jefferson City", "Montana": "Helena", "Nebraska": "Lincoln",
                                "Nevada": "Carson City", "New Hampshire": "Concord", "New Jersey": "Trenton",
                                "New Mexico": "Santa Fe", "New York": "Albany", "North Carolina": "Raleigh",
                                "North Dakota": "Bismarck", "Ohio": "Columbus", "Oklahoma": "Oklahoma City",
                                "Oregon": "Salem", "Pennsylvania": "Harrisburg", "Rhode Island": "Providence",
                                "South Carolina": "Columbia", "South Dakota": "Pierre", "Tennessee":
                                "Nashville", "Texas": "Austin", "Utah": "Salt Lake City", "Vermont":
                                "Montpelier", "Virginia": "Richmond", "Washington": "Olympia", "WestVirginia": "Charleston", "Wisconsin": "Madison", "Wyoming": "Cheyenne"}

    # Generate the quiz files.
    for quiz_num in range(NUMBER_OF_QUIZ_FILES):
        try:
            with open(file=f"{directory_path}{os.sep}capitals_quiz_{quiz_num + 1}.txt", mode="w", encoding="utf-8") as quiz_file, open(file=f"{directory_path}{os.sep}capitals_quiz_answers_{quiz_num + 1}.txt", mode="w", encoding="utf-8") as answer_file:
                # Create the header for the quiz
                quiz_file.write("Name:\n\nDate:\n\nPeriod:\n\n")
                quiz_file.write((" " * 20) + f"State Capitals Quiz (Form {quiz_num + 1})\n\n")

                # Shuffle the order of the states
                states: list[str] = list(capitals.keys())
                random.shuffle(states)

                # Loop through all states, making a question for each
                for num in range(len(capitals)):
                    correct_answer: str | None = capitals.get(states[num])

                    if (correct_answer == None):
                        continue

                    wrong_answers: list[str] = list(capitals.values())
                    wrong_answers.remove(correct_answer)

                    wrong_answers = random.sample(wrong_answers, len(QUIZ_OPTIONS) - 1)

                    answer_options: list[str] = wrong_answers + [correct_answer]
                    random.shuffle(answer_options)

                    quiz_file.write(f"{num + 1}. Capital of {states[num]}:\n")

                    # Write the question and the answer options to the quiz file.
                    quiz_file.writelines(f"{QUIZ_OPTIONS[i]}. {answer_options[i]}\n" for i in range(len(QUIZ_OPTIONS)))
                    quiz_file.write("\n")

                    # Write the answer key to a file.
                    number_str: str = str(num + 1) if num + 1 > 9 else "0" + str(num + 1)
                    answer_file.write(f"{number_str}. {QUIZ_OPTIONS[answer_options.index(correct_answer)]}\n")

        except PermissionError as ex:
            logger.warning(f"Insufficient permissions to create directory: {ex}")
            return
        except OSError as ex:
            logger.warning(f"Failed to create directory: {ex}")
            return


if (__name__ == "__main__"):
    main()
