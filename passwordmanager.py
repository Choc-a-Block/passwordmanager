#!/usr/bin/python3
#imports
import hashlib
import base64
import os
from cryptography.fernet import Fernet

#functions

#Used to write to the default file generated when the program is first started.
def writeDefaultFile():
    o = open("passwords", "w")
    o.write("This is a file for passwordmanager.\n")
    o.close()

#Encodes the passwords file into UTF-8
def encodeFile():
    o = open("passwords", "r")
    file = o.read()
    encoded = file.encode("utf-8")
    o.close()
 
#Presents options menu for the user.
def userChoice():
    choice = int(input("1. Query for password.\n2. Add password to database.\nWhat do you wish to do?"))
    return choice 

#Encrypts the data fed into it using the Fernet key.
def encryptData(message):
    f = Fernet(key)
    encrypt = f.encrypt(message)
    return encrypt

#Gets and decrypts the data inside the passwords file, then returns the output.
def getContents():
    o = open("passwords", "r")
    encryptedContents = o.open()
    encryptedContentsBytes = encryptedContents.encode()
    f = Fernet(key)
    contents = f.decrypt(encryptedContentsBytes)
    return contents

#Sets a global variable called key, generates a hash from the users password, 
#and cuts it down to 32 characters (length of the key required by Fernet), then encodes the hash into a URL-safe, base64 format. (The format required by Fernet)
def setKey():
    global key
    password = input("Password?")
    keyHash = hashlib.sha256(password.encode()).digest()[0:32]
    print(keyHash)
    key = base64.urlsafe_b64encode(keyHash)
    print(key)

#Used when the user is trying to retreive an entry from their passwords file.
#Gets a query, decrypts the main passwords file, then searches it and prints out all matching results.
def getEntry():
    query = input("Query here:")
    with open("passwords", "r+") as o:
        entries = o.read()
        f = Fernet(key)
        entriesFile = f.decrypt(entries)
        for line in entriesFile():
            if query in line:
                print(line)

#Used when the user wishes to add an entry to their passwords file.
#Gets all relevant information, concatenates it, opens the passwords file and writes the new line, encrypted with the key defined in keySet.
def addEntry():
    ident = input("What is the website/identifier?")
    email = input("What is the email/username?")
    passw = input("What is the password?")
    concatStr = ("\n" + ident + "," + email + "," + passw)
    with open("passwords", "r+") as o:
        f = Fernet(key)
        encrypted = f.encrypt(concatStr)
        o.write(encrypted)

#Initial function to be run to detect if the required file "passwords" is present.
#If the required file is not present, it is created, initial message written and encoded, then encrypted.
def fileCheck():
    if not os.path.isfile('passwords'):
        os.mknod('passwords')
        passwordInit = input("Please create a password:")
        passwordInitEncoded = passwordInit.encode("utf-8")
        encHash = hashlib.sha256(passwordInitEncoded).digest()
        writeDefaultFile()
        encodeFile()
#       with open("passwords", "r+") as o:
#           contents = o.read
#           encContents = encryptData(contents)
#           o.write(encContents)
    else:
        pass

#Main function, simple interpreter of the choice made in userChoice. Exits if the choice is invalid...
def main(userChoice):
    if userChoice == 1:
        getEntry()
    elif userChoice == 2:
        addEntry()
    else:
        print("Invalid input. Exiting...")

#Main set of function calls.
fileCheck()
setKey()
choice = userChoice()
main(choice)
