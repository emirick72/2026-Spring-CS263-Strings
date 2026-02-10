

def first_letter_is_capitalized(sentence: str) -> bool:
    """
    Check that the first letter of a sentence is capitalized.

    Args:
        sentence: The user-inputted string that gets checked.

    Returns:
        True if the first letter of the sentence is capitalized, False if otherwise.
    """
    
    if not sentence:
        return False
    
    if sentence[0].isupper():
        return True
    else:
        return False


def ends_with_punctuation(sentence: str) -> bool:
    """
    Check that a sentence ends with a period, question mark, or exclamation point.

    Args:
        sentence: The user-inputted string that gets checked.

    Returns:
        True if the sentence ends with a period, question mark, or an exclamation point,
        False if otherwise.
    """

    valid_punctuation = {'.', '?', '!'}
    if sentence and sentence[-1] in valid_punctuation:
        return True
    else:
        return False



def includes_advanced_punctuation(sentence: str) -> bool:
    """
    Check for quotes, commas, semicolons, colons, dashes, and ellipses.

    Args:
        sentence: The user-inputted string that gets checked.

    Returns:
        True if the sentence has quotes, commas, semicolons, colons, dashes, and ellipses,
        False if otherwise.
    """

    valid_advanced_punctuation = {'""', ',', ';', ':', '-', '...'}
    for char in sentence:
        if char in valid_advanced_punctuation:
            return True
    
    # Handle ellipses separately
    if "..." in sentence:
        return True
    return False
