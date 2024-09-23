
"""
Input value
n : index of the square pyramidal number

Return value: the n-th square pyramidal number
"""
def make_square_pyramidal(n):
    return int((2*n**3+3*n**2+n)/6)

"""
Define constants
c : the lower bound picked
m : the largest number m that we are checking if it can be written as a sum of at most four square pyramidal numbers
"""
c = 13000000
m = 15264785

#1st step
all_square_pyramidals = set()
for i in range(357):
    all_square_pyramidals.add(make_square_pyramidal(i))

#2nd step
second_step_combinations = set()
for j in all_square_pyramidals:
    for i in all_square_pyramidals:
        if ((i+j) <= m):
            second_step_combinations.add(i+j)

#third step
third_step_combinations = set()
for j in second_step_combinations:
    for i in all_square_pyramidals:
        if ((i+j) <= m):
            third_step_combinations.add(i+j)

#fourth step
fourth_step_combinations = set()
for j in third_step_combinations:
    for i in all_square_pyramidals:
        if (c <= (i+j) <= m):
            fourth_step_combinations.add(i+j)



print("The number of all possible sums of at most four square pyramidal numbers that are [] is ", len(fourth_step_combinations))
print("The total number in the range is ", m-c+1)
print("All numbers in the given range can be written as a sum of at most four square pyramidal numbers is ",(m-c+1) ==  len(fourth_step_combinations))
