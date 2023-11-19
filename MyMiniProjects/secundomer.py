import time
sec = 0

while sec != 101:
    print(sec)
    time.sleep(1)
    sec += 1
    if sec == 101:
        print("на этом все :)")