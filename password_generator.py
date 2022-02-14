from secrets import choice
from string import digits, punctuation, ascii_letters


def generate_pwd(password_length, use_digits=True, use_punctuation=True,
                 use_ascii_chars=True) -> str:  # Password length, optional use_digits, use_punctuation and use_ascii_chars
    usable_chars = []
    if use_digits:
        usable_chars.append(digits)
    if use_punctuation:
        usable_chars.append(punctuation.replace("\\", "¬"))
    if use_ascii_chars:
        usable_chars.append(ascii_letters)
    usable_chars = [j for i in usable_chars for j in i]  # merging usable_chars into one item list
    return str(''.join(_ for _ in [choice(usable_chars) for __ in range(password_length)]))


def generate_pwd_web(
        password_length) -> str:  # At least one lowercase character, at least one uppercase character, and at least three digits
    alphabet = ascii_letters + digits + punctuation
    while True:
        password = ''.join(choice(alphabet) for _ in range(password_length))
        if (any(char.islower() for char in password)
                and any(char.isupper() for char in password)
                and sum(char.isdigit() for char in password) >= 3):
            break
    return password
