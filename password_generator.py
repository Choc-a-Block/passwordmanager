from secrets import choice
from string import digits, punctuation, ascii_letters


def generate_pwd(password_length, use_digits=True, use_punctuation=True, use_ascii_chars=True) -> str:
    """
    Generate a random password, using the specified length, digits, punctuation and ascii characters.
    :param password_length: The length of the password to be generated
    :type password_length: int
    :param use_digits: If True, at least one digit will be included in the password, defaults to True (optional)
    :type use_digits: bool
    :param use_punctuation: If True, the password will contain punctuation characters, defaults to True (optional)
    :type use_punctuation: bool
    :param use_ascii_chars: If True, the password will contain at least one uppercase letter and one lowercase letter,
    defaults to True (optional)
    :type use_ascii_chars: bool
    :return: A string of random characters
    """
    if password_length <= use_digits + use_punctuation + use_ascii_chars:
        raise ValueError("The password length must be greater than the number of character types used.")
    password = ""
    if use_digits:
        password += choice(digits)  # add at least one digit
    if use_punctuation:
        password += choice(punctuation)  # add at least one punctuation character
    if use_ascii_chars:
        password += choice(ascii_letters)  # add at least one uppercase / lowercase letter
    for i in range(password_length - len(password)):
        password += choice(digits + punctuation + ascii_letters)
    return password
