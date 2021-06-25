import time
my_list = ["cat","dog","rabbit","sloth","owl", "bear"]

while True:

    for index,item in enumerate(my_list):
        print (index,item)
        time.sleep(0.5)

    print('Loop Complete...')

