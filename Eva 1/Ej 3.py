matrix = [[1,2,3],
        [4,5,7],
        [7,8,9]]

def isPrime(n):
    for i in range(2, n - 1):
        if n % i == 1:
            return True
        else:
            return False

def sumValues(matrix):
    result = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if (y + x)% 2 == 1 and isPrime(matrix[x][y]) == True:
                result += (matrix[x][y])
    return result

print(sumValues(matrix))
