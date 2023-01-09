def find_the_number_plate(customer_id):
    number = (customer_id % 999) + 1
    serial = customer_id // 999

    return f'{chr(97 + serial % 26)}{chr(97 + (serial // 26) % 26)}{chr(97 + (serial // (26 ** 2)) % 26)}{number:0>3}'


if __name__ == '__main__':

    # Original Kata: https://www.codewars.com/kata/5f25f475420f1b002412bb1f/

    # Should be [aaa004, baa489, oba041, zzz999, aja802, rba100]
    read_values = [3, 1487, 40000, 17558423, 234567, 43056]

    for item in read_values:
        print(find_the_number_plate(item))
