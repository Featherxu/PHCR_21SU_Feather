import time
my_string = "hello world"

while True:
    for letter in my_string:
        print(letter)
        time.sleep(0.5)

    print("Loop Complete")

