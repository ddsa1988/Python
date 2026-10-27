# Pig latin is a silly made-up language that alters English words. If a word
# begins with a vowel, the word yay is added to the end of it. If a word begins
# with a consonant or consonant cluster (like ch or gr), that consonant or con-
# sonant cluster is moved to the end of the word and followed by ay.

def split_text(text: str, separator: str) -> list[str]:
    if (type(text) != str):
        raise TypeError("Text must be a string type.")

    if (type(separator) != str):
        raise TypeError("Separator must be a string type")

    new_list: list[str] = text.split(separator)

    return new_list


def english_to_pig_latin(word: str) -> str:
    VOWELS: list[str] = ['a', 'e', 'i', 'o', 'u', 'y']

    if (type(word) != str):
        raise TypeError("Word must be a string type.")

    if (len(word.strip()) == 0):
        return word

    # A list of the words in pig latin
    pig_latin: list[str] = []

    # Separate the non-letters at the start of this word
    prefix_non_letters: str = ""

    while (len(word) > 0 and not word[0].isalpha()):
        prefix_non_letters += word[0]
        word = word[1:]

    if (len(word) == 0):
        pig_latin.append(prefix_non_letters)
        return " ".join(pig_latin)

    # Separate the non-letters at the end of this word
    suffix_non_letters: str = ""

    while (not word[-1].isalpha()):
        suffix_non_letters = word[-1] + suffix_non_letters
        word = word[:-1]

    # Remember if the word was in uppercase or title case:
    was_upper: bool = word.isupper()
    was_title: bool = word.istitle()

    # Make the word lowercase for translation
    word = word.lower()

    # Separate the consonants at the start of this word:
    prefix_consonants: str = ""

    while (len(word) > 0 and not word[0] in VOWELS):
        prefix_consonants += word[0]
        word = word[1:]

    # Add the pig latin ending to the word
    if (len(prefix_consonants) > 0):
        word += prefix_consonants + "ay"
    else:
        word += "yay"

    # Set the word back to uppercase or title case
    if (was_upper):
        word = word.upper()

    if (was_title):
        word = word.title()

    # Add the non-letters back to the start or end of the word
    pig_latin.append(prefix_non_letters + word + suffix_non_letters)

    # Return and join all the words back together into a single string
    return " ".join(pig_latin)


def main() -> None:
    content: str = "My name is AL SWEIGART and I am 4,000 years old."

    expected_output: str = "Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay."

    text_splitted: list[str] = split_text(text=content, separator=" ")

    output: str = " ".join([english_to_pig_latin(item)
                           for item in text_splitted])

    print(output)

    print(expected_output == output)


if (__name__ == "__main__"):
    main()
