def intersection(arrays):

    """
    YOUR CODE HERE
    """

    cache = {}

    big_array = []
    return_array = []

    for x in arrays:
        big_array +=x

    # print(big_array)

    for y in big_array:
        if y not in cache:
            cache[y] = 1
        else:
            cache[y] +=1

    # print(cache)

    for i in cache:
        if cache[i] >1:
            return_array.append(i)

    return return_array



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
