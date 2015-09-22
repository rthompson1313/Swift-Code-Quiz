'''
Python file count.py
by Ryan Thompson
This file was written for Swift Navigation.
The program counts from 0 to 100 in integers and prints
"Fizz" when the count is a multiple of 3, prints "Buzz"
when the count is a multiple of 5, and prints the count
otherwise.
'''

count_max = 100

for i in range(0, count_max):       #iterate through the range of 0 to count_max
    if i == 0:                      #handle the 0 condition
        print i
    else:   
        if i%3 == 0:                #detect multiples of 3
            print "Fizz"
        if i%5 == 0:                #detect multiples of 5
            print "Buzz"
        if i%3 > 0 and i%5 > 0:     #ensure that count is neither a multiple of 3 or 5
            print i