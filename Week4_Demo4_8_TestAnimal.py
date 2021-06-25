import time

animals = ["cat","dog","rabbit","sloth","owl", "bear"]

test = "dog"

while True:
    if test in animals:
        print(test, "is an animal")
        print(test + "s", "are awesome")
        time.sleep(0.5)

    else:
        print(test + "s","is not an animal")
