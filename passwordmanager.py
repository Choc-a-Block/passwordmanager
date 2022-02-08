#!/usr/bin/python3
import hashlib
import base64
import os
from cryptography.fernet import Fernet

hash = hashlib.shake_256()

def writeDefaultFile():
    o = open("passwords", "w")
    o.write("This is a file for passwordmanager.\n")
    o.close()

def encodeFile():
    o = open("passwords", "r")
    file = o.read()
    encoded = file.encode("utf-8")
    o.close()
 
def userChoice():
    choice = int(input("1. Query for password.\n2. Add password to database.\nWhat do you wish to do?"))
    return choice 

def encryptData(message):
    f = Fernet(key)
    encrypt = f.encrypt(message)
    return encrypt

def getContents():
    o = open("passwords", "r")
    encryptedContents = o.open()
    encryptedContentsBytes = encryptedContents.encode()
    f = Fernet(key)
    contents = f.decrypt(encryptedContentsBytes)
    return contents

def setKey():
    global key
    password = input("Password?")
    keyHash = hashlib.sha256(password.encode()).digest()[0:32]
    print(keyHash)
    key = base64.urlsafe_b64encode(keyHash)
    print(key)

def getEntry():
    query = input("Query here:")
    with open("passwords", "r+") as o:
        entries = o.read()
        f = Fernet(key)
        entriesFile = f.decrypt(entries)
        for line in entriesFile():
            if query in line:
                print(line)

def addEntry():
    ident = input("What is the website/identifier?")
    email = input("What is the email/username?")
    passw = input("What is the password?")
    concatStr = ("\n" + ident + "," + email + "," + passw)
    with open("passwords", "r+") as o:
        f = Fernet(key)
        encrypted = f.encrypt(concatStr)
        o.write(encrypted)

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

def main(userChoice):
    if userChoice == 1:
        getEntry()
    elif userChoice == 2:
        addEntry()
    else:
        print("Invalid input. Exiting...")

fileCheck()
setKey()
choice = userChoice()
main(choice)
