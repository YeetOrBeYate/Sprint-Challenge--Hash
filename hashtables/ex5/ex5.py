def finder(files, queries):

    """
    YOUR CODE HERE
    """

    cache = {}

    return_array = []

    for x in files:
       y = x.split("/")
       if y[-1] not in cache:
           cache[y[-1]] = [x]
       else:
           cache[y[-1]].append(x) 
            
    # print(cache)

    for y in queries:
        if y in cache:
            return_array +=cache[y]

    return return_array
     


if __name__ == "__main__":
    files = [
        "/usr/local/share/foo.txt",
        "/usr/bin/ls",
        "/home/davidlightman/foo.txt",
        "/bin/su"
    ]
    queries = [
        "ls",
        "foo.txt",
        "nosuchfile.txt"
    ]
    print(finder(files, queries))
