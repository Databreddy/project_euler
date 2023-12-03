# Unsolved on 3 Dec 2023

# Version: 1.4
# Author: Bevlin Reddy / bevlinrdut@gmail.com
# Project Euler: problem 3: largest prime factor
# URL: https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13, 29
# What is the largest prime factor of the number?
#
# Creation Date: 03-Dec-23

import math

check_number_1 = 112
factor_list = []
prime_flag_1 = 0  # 1 = prime number
prime_flag_2 = 0  # 1 = prime number
factor_list_2 = []


# ----------------------------------------------------------------
# test if number is prime

def findFactors(number):
    
    global prime_flag_1
    for i in range(2, math.ceil(math.sqrt(number))):
        if number % i == 0:
            factor_list.append(i)

    if len(factor_list) == 0:
        prime_flag_1 = 1

    return prime_flag_1, factor_list


# find prime factors as follows:
# if element in factor list is prime or perfect square, then print element.
def find_prime_factors(factor_list_1):
    for j in range(0, len(factor_list_1)):
        prime_flag_2, factor_list_2 = isPrime(factor_list_1[j])
        print(prime_flag_1, factor_list_2[j])

        if prime_flag_2 == 1:
            factor_list_2.append(factor_list_2[j])
            print("###", factor_list_2)
    
    return factor_list_2

#----------------------------------------------------------------
# determine if number is prime

def isPrime(prime_flag_1, factor_list):
    
    print(prime_flag_1, factor_list)
    
    if prime_flag_1 == 1:
        print(str(check_number_1) + " is prime")
        print(factor_list_1)
    else:
        print(str(check_number_1) + " is not prime")
        print(factor_list_1)



# ----------------------------------------------------------------
# Main loop

prime_flag_1, factor_list_1 = findFactors(check_number_1)
print("*** ", factor_list)

prime_flag_2, factor_list_2 = isPrime(prime_flag_1, factor_list_1)
print("+++ ", factor_list_2)