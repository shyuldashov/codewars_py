def move_zeros(lst):
    """The function moves all zeros to the end, preserving the order of the rest of the elements.
    
    Algorithm: Bubble Sort

    Args:
        lst (list): list of integers

    Returns:
        list: sorted list of integers
    """
    for i in range(len(lst)):
        for j in range(0, len(lst)-i-1):
            if lst[j] == 0:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


if __name__ == '__main__':
    
    # Original Kata: https://www.codewars.com/kata/52597aa56021e91c93000cb0

    print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))  # [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
    print(move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
        # [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(move_zeros([0, 0]))


