import itertools

from examine_sentence import (
    includes_advanced_punctuation,
    ends_with_punctuation,
    first_letter_is_capitalized,
)


def generate_report(sentence: str) -> str:
    """
    Generate a report that indicates whether a sentence:

      1. starts with a capital letter
      2. ends with a *basic* punctuation symbol
      3. contains *advanced* punctuation
    """

    report_entries = []

    letter_case = "uppercase" if first_letter_is_capitalized(sentence) else "lowercase"
    report_entries.append(f"Sentence starts with '{sentence[0]}' ({letter_case})")

    if ends_with_punctuation(sentence):
        report_entries.append(f"Sentence ends with a/an '{sentence[-1]}'")

    does_or_not = "does" if includes_advanced_punctuation(sentence) else "does not"
    report_entries.append(f"Sentence {does_or_not} include *advanced* punctuation")

    return "\n".join(
        itertools.chain(
            [
                "Analysis:",
                "",
            ],
            (f"  {idx}. {entry}" for idx, entry in enumerate(report_entries, start=1)),
        )
    )


def main():
    another_sentence = "yes"

    while another_sentence == "yes":
        sentence = input("Enter a sentence: ")

        report = generate_report(sentence)
        print(report)
        print()

        another_sentence = input(
            "Would you like to check another sentence? (yes/no): "
        ).lower()

        print()


if __name__ == "__main__":
    main()
