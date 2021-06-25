
import time
animals = ["cat","dog","rabbit","sloth","owl", "bear"]

test_list = ['hammer','dog','rabbit','tree','bear','grass','elephant']

while True:
    for item in test_list:
        if item in animals:
            print(item, "is an animal")
            print(item + 's', 'are awesome!', '\n')
            time.sleep(0.5)
        else:
            print(item + 's', "are not animals", "\n")

    print('test complete...')
    test.sleep(5)
