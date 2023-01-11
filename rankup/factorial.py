def fact(n):

    if n == 0:  # Recursion exit condition
        return 1

    return n * fact(n - 1)  # recursive call


if __name__ == '__main__':

    for num in range(2, 11):
        print(fact(num))
