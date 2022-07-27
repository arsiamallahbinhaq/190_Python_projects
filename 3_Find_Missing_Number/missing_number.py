def findMissingNumbers(n):
    numbers = set(n)
    length = n[-1]
    output = []
    for i in range(1, length + 1):
        if i not in numbers:
            output.append(i)
    return output

listNumbers = [1,3,4,5,6,8,10,12]
print(findMissingNumbers(listNumbers))
