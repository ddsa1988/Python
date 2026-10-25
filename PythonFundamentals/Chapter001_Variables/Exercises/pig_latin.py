# Pig latin is a silly made-up language that alters English words. If a word
# begins with a vowel, the word yay is added to the end of it. If a word begins
# with a consonant or consonant cluster (like ch or gr), that consonant or con-
# sonant cluster is moved to the end of the word and followed by ay.

def translate_to_pig_latin(text: str) -> str:
    VOWELS: list[str] = ['a', 'e', 'i', 'o', 'u', 'y']
    pig_latin: list[str] = []

    words: list[str] = text.split()
    print(words)

    return ""


def main():
    content: str = "My name is AL SWEIGART and I am 4,000 years old."

    expected_output: str = "Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay."

    output: str = translate_to_pig_latin(content)

    # print(output == expected_output)


if (__name__ == "__main__"):
    main()
