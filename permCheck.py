// An array A is a permutation is it is an ordered/unordered sequence in the range (1, N)
// Input = array of numbers
// If A is a permutation, return 1, else return 0

// Implementation 1 - Failed for cases where sum of non-perm array was equal to a perm array of same size
// codility validation - https://codility.com/demo/results/training6RJ7EA-SFH/

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    sum_of_all = int(N*(N+1)/2)
    sum_of_A = sum(A)
    if sum_of_all == sum_of_A:
        return 1
    else:
        return 0
        
// Implmentation 2 - Passed for all test cases
 
def solution(A):
    # write your code in Python 3.6
    N = len(A)
    my_list = list(range(1,N+1))
    A.sort()
    for i,j in zip(A, my_list):
        if i == j:
            continue
        else:
            return 0
    return 1
    
// Codility Validation - https://codility.com/demo/results/training44WZYM-WE5/
