# Change direction of the iteration using variables
import time

my_var = 0
i = 1

while True:
    while my_var <10:
        print(my_var)
        time.sleep(0.5)
        my_var +=i
    print("loop complete...changing direction!")
   # my_var = 0
    i= -i

    while my_var >0:
        print(my_var)
        time.sleep(0.5)
        my_var +=i
    print ("loop complete...changing direction")
    i= -i
