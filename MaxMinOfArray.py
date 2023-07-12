def maxMinSum(array):
    if not array:
        return "Empty Array."

    length = len(array)
    minimum = array[0]
    maximum = array[0]

    for i in range(length):
        if array[i] < minimum:
            minimum = array[i]
        elif array[i] > maximum:
            maximum = array[i]

    return minimum + maximum


if __name__ == "__main__":
    array = list(map(int, input().strip('[').strip(']').split(',')))
    print(maxMinSum(array))
