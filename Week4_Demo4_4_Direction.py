import time

start = 0
stop = 10
step =1

while True:
    for x in range(start, stop,step):
        print(x)
        time.sleep(0.5)
    print("Loop Complete...changing direction")

    new_start = stop
    stop = start
    start = new_start
    step = -step
