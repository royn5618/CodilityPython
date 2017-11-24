//Binary-Gap Problem
//Input N = a decimal number
//Binary Gap in the number
//Binary Gap - The maximum number of zeros bounded by 1 on both sides in the binary form of the decimal number
//Ex: Input = 5618 ; Binary(N) = 1010111110010 ; Output = 2

def solution(N):
    # write your code in Python 3.6
    binary = str(bin(N)[2:])
    a = []
    a = binary.split("1")
    a.pop()
    b = max(a, key=len)
    return len(b)
    
//codility evaluation - https://codility.com/demo/results/training3RY25G-ABY/
