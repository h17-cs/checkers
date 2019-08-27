import random
import time
import threading
from DatabaseManager import *

db = DatabaseManager(None, "db.csv")
dict_lock = threading.Lock()

users = "joe josh john matt mike charles charlotte maggie martha jackie jamie andy alex tom dick harry steven susan nancy".split()
passwords = "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua".split()

passkeys = {}

global failures, globcount, END

failures = 0
globcount = 0
END = False


def dlock():
    dict_lock.acquire()


def dunlock():
    dict_lock.release()


def createsome(i):
    global failures, globcount, END
    count = 0
    while not END and count < i:
        uname = "%s_%03d" % (random.choice(users), int(random.random()*1000))
        passwd = "%s%d" % (random.choice(passwords), int(random.random()*10))
        if db.addUser(uname, passwd):
            dlock()
            globcount += 1
            passkeys[uname] = passwd
            dunlock()
            count += 1
            print(globcount, "- added", uname, ":", passwd)
        else:
            failures += 1
        time.sleep(random.random()*.01)


def querysome(i):
    global failures, globcount, END
    count = 0
    while not END and count < i:
        uname = "%s_%03d" % (random.choice(users), int(random.random()*1000))
        passwd = "%s%d" % (random.choice(passwords), int(random.random()*10))
        res = db.queryForUser(uname, passwd)
        dlock()
        globcount += 1
        dunlock()
        count += 1
        print(globcount, "- queried", uname, ",", passwd, ":", res)
        time.sleep(random.random()*.02)


def removesome(i):
    global failures, globcount, END
    count = 0
    time.sleep(random.random()*.06+.2)
    while not END and count < i:
        uname = random.choice(list(passkeys.keys()))
        passwd = passkeys[uname]
        if db.deleteUser(uname, passwd):
            dlock()
            globcount += 1
            try:
                del passkeys[uname]
            except KeyError:
                print("Eh, a little too enthusiastic")
            dunlock()
            count += 1
            print(globcount, "- removed", uname, ":", passwd)
        else:
            failures += 1
        time.sleep(random.random()*.05)


def refresh():
    for i in range(6):
        time.sleep(30)
        print("\t\t\t", "Flushing")
        db.flush()


threads = []

for i in range(15):
    threads.append(threading.Thread(target=createsome, args=(200,)))

for i in range(100):
    threads.append(threading.Thread(target=querysome, args=(200,)))

for i in range(10):
    threads.append(threading.Thread(target=removesome, args=(200,)))

threads.append(threading.Thread(target=refresh))

print("Target actions is 3000 adds, 2000 removes, 20000 queries")


def run():
    global failures, globcount, END
    try:
        for t in threads:
            t.start()

        k = input("\t\t\tPress enter whenever")
    except:
        pass
    END = True
    for t in threads:
        t.join()
    db.flush()
    print("Failures:", failures)
