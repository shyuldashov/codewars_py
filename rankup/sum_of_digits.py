def digital_root(n):
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    if total < 10:  # Recursion exit condition
        return total

    return digital_root(total)  # recursive call


if __name__ == '__main__':

    # Original Kata: https://www.codewars.com/kata/541c8630095125aba6000c00/

    read_values = [16, 942, 132189, 493193]

    for num in read_values:
        print(digital_root(num))
