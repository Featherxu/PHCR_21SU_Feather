import time

my_string = "my name is: Feather Xu"

while True:
    temp_str = ''
    first_name = ''

    for letter  in my_string:
        time.sleep(0.25)
        print(letter)
        if temp_str !="My name is:" :
            temp_str+= letter
            print(temp_str)
            continue
        if letter!=' ':
            first_name+= letter
            print(first_name)
        else:
            break

    print ("Loop Complete...First name is Feather")
