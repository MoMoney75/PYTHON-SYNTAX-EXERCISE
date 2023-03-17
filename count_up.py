def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    # num1 = start
    # num2 = stop + 1
    # for i in range(num1, num2):
    #     return i

    while start <= stop:
        print(start)
        start = start + 1


count_up(5, 7)
