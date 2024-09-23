from itertools import combinations_with_replacement 

"""
Input value
n : index of the square pyramidal number

Return value: the n-th square pyramidal number
"""
def make_square_pyramidal(n):
    return int((2*n**3+3*n**2+n)/6)


"""
Input values
    m : maximum value of the positive integers that we are checking
    n : index of the largest square pyramidal number we are using to compute the sums
    limit: the maximum number of square pyramidal numbers in the sum
    threshold: the threshold for m

Return value: a list of positive integers between threshold and f(n) that CANNOT be represented as at most "limit"
              numbers of square pyramidal numbers.
"""

def sum_of_square_pyramidals(m, n, limit, threshold):
    numbers_up_to_m = list(range(threshold, m)) 
    for j in combinations_with_replacement(map(make_square_pyramidal, list(range(n + 1))), limit):
        if sum(j) in numbers_up_to_m:
            numbers_up_to_m.remove(sum(j))
    return numbers_up_to_m


"""
Want to show: For any integer m such that 1 <= m < 100000, m can be written as a sum of at most 8
              square pyramidal numbers.


The largest square pyramidal number we can take is the 30th square pyramidal number.
Therefore, take n = 30, limit = 8, and threshold = 1.

"""
print("these are numbers that cannot be represented as a sum of at most eight square pyramidal numbers:",sum_of_square_pyramidals(10000, 30, 8, 1)) #actual return value: []

