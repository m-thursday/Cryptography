from Cryptodome.Hash import SHA256
from sys import argv
import itertools
import threading
import string
import time
import sys

def genLibrary(n):  # Generate a library of all possible passwords size n
    cList = list(string.digits + string.ascii_lowercase + string.ascii_uppercase + "#$%^&*")
    return [''.join(p) for p in itertools.product(cList, repeat=n)]

def passList(txt, o):  # Read txt file and create list of all hashed passwords
    passList = []
    with open(txt, "r") as infile:
        for line in infile:
            tmp = line.strip().strip('[]').split(',')
            if o == 0:
                pw = str(tmp[1].strip())
                passList.append(pw)
            if o == 1:
                salt = str(tmp[1].strip())
                pw = str(tmp[2].strip())
                var = [salt, pw]
                passList.append(var)
    return passList

def passHash(pString):  # Generate the hash of the password
    return str(SHA256.new(pString.encode('utf-8')).hexdigest())

def search(pw, lib):
    xFiles = []
    originStart = time.time()
    for word in lib:
        wHash = passHash(word)
        if wHash in pw:
            xFiles.append(word)
    originEnd = time.time()
    oTime = originEnd - originStart
    return xFiles, oTime

def saltSearch(pw, lib):
    i = 0
    xFiles = []
    saltStart = time.time()
    for user in pw:
        salt = user[0]
        for word in lib:
            wHash = passHash(word + salt)
            if wHash == user[1]:
                xFiles.append(word)
        i += 1
    saltEnd = time.time()
    sTime = saltEnd - saltStart
    return xFiles, sTime

def uInput():
    # n should be an integer and salt should be a bool
    script, n, salt = argv
    while not n.isnumeric():
        n = input("please input an integer: ")
    return n, salt

def setUp(n, salt):
    dictionary = genLibrary(int(n))

    txt = input("Give a file with passwords: ")
    passwords = passList(txt + '.txt', int(salt))

    return dictionary, passwords

def runTime(dictionary, passwords, salt):
    if salt == 0:
        correct_passwords, time_elapsed = search(passwords, dictionary)
    else:
        correct_passwords, time_elapsed = saltSearch(passwords, dictionary)

    print(f"\nPasswords: {correct_passwords}")
    print(f"Total Time: {time_elapsed} seconds")

def spinner():
    """Displays a spinner while the main process runs."""
    symbols = ["|", "/", "-", "\\"]
    idx = 0
    while not stop_spinner:
        sys.stdout.write("\r" + symbols[idx % len(symbols)] + " Working...")
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)  # Adjust for spinner speed
    sys.stdout.write("\rDone!            \n")  # Clear spinner line

def long_running_task(dictionary, passwords, salt):
    runTime(dictionary, passwords, int(salt))

if __name__ == "__main__":
    n, salt = uInput()

    dictionary, passwords = setUp(n, salt)

    # Create and start the spinner thread
    stop_spinner = False
    spinner_thread = threading.Thread(target=spinner)
    spinner_thread.start()

    # Perform the long-running task
    try:
        long_running_task(dictionary, passwords, salt)
    finally:
        # Stop the spinner and wait for the thread to finish
        stop_spinner = True
        spinner_thread.join()

