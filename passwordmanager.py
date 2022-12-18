import hashlib


def hash_password(password):
    """
    Hash a password for storing.
    :param password: The password to be hashed
    :type password: str
    :return: A hashed password
    :rtype: str
    """
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password, hashed_password):
    """
    Verify a stored password against one provided by user
    :param password: The password provided by the user
    :type password: str
    :param hashed_password: A stored password
    :type hashed_password: str
    :return: True if the password is correct, False otherwise
    :rtype: bool
    """
    return hash_password(password) == hashed_password


# save the password hash to the file
def save_password(password_hash):
    with open("passwords.txt", "a") as file:
        file.write(password_hash + "\n")

# open the file and check if the password is in the file
def check_password(password_hash):
    with open("passwords.txt", "r") as file:
        for line in file:
            if password_hash == line.strip():
                return True
        return False

# test the functions
if __name__ == "__main__":
    password = input("Enter a password: ")
    password_hash = hash_password(password)
    save_password(password_hash)
    print("saved password")
    password = input("Enter the password again: ")
    if check_password(hash_password(password)):
        print("You entered the correct password")
    else:
        print("I'm sorry but the password does not match")