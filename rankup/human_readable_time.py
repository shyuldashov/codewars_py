def make_readable(seconds):
    hh = seconds // 3600
    mm = seconds // 60 % 60
    ss = seconds % 60

    return f'{hh:0>2}:{mm:0>2}:{ss:0>2}'


# # №2
# def make_readable(seconds):
#     return '{0:0>2}:{1:0>2}:{2:0>2}'.format(seconds // 3600, seconds // 60 % 60, seconds % 60)


if __name__ == "__main__":

    # Original Kata: https://www.codewars.com/kata/52685f7382004e774f0001f7/

    read_values = [0, 5, 60, 86399, 359999]

    for n in read_values:
        print(make_readable(n))
