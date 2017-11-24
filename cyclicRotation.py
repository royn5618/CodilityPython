//Cyclic Rotation
//Input = [1, 2 , 3 , 4]
//Iterations = 3
//Output = [4, 1, 2, 3]

def solution(A, K):
    # write your code in Python 3.6
    length_A = len(A)
    my_list = []
    for i in range(length_A):
        pos = (i + K) % length_A
        my_list.insert(pos,A[i])
    return my_list
    
//codility evaluation - https://codility.com/demo/results/trainingWUCTZZ-4RU/
