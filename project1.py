# solved on 3 Dec 2023

# Version: 1.1
# Author: Bevlin Reddy / bevlinrdut@gmail.com
# Project Euler: problem 1 - multiples of 3 and 5
# URL: https://projecteuler.net/problem=1
# Description: find the sum of all multiples of 3 and 5 less than 1000
# Creation Date: 02-Dec-23

sum = 0
max_num = 1000

for i in range(0,max_num):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print("Sum = " + str(sum))

