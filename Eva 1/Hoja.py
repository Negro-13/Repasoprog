matrix = [
    [1,2,3],
    [4,5,6],
    [7,11,9]
]

def isprime (num):
    count = 2
    for i in range(num - 1):
        if num % count != 0:
            count += 1
        else:
            return True


def count (matrix):
    result = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            num = x + y
            if isprime (matrix[x][y]) == True:
                result.append(matrix[x][y])
    return result

print(count (matrix))