# Solved on 3 Dec 2023

# Version: 1.10
# Author: Bevlin Reddy / bevlinrdut@gmail.com
# Project Euler: problem 2:
# URL: https://projecteuler.net/problem=2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with and the first terms will be:
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
#
# Creation Date: 03-Dec-23

max_num = 4_000_000
term_low = 0
term_high = 1
term_n = 0
sum = 0
index = 0

while term_high < max_num:
    term_n = term_low + term_high
    term_low = term_high
    term_high = term_n

    index += 1
    # print(index, term_low, term_high)

    if term_n % 2 == 0:
        sum += term_n

print("Sum = " + str(term_low) + " " + str(sum))

