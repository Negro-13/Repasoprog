matrix = [
    [1,2,3],
    [4,5,6],
    [7,11,9]
]

def isprime (num):
    count = 2
    for i in range(n - 1):
        if n % count == 0:
            return True
        else:
            return False


def count (matrix):
    result = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            num = x + y
            if num % 2 == 1:
                result.append(matrix[x][y])
    return result

print(count (matrix))