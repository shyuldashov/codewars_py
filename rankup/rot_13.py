def rot13(message):
    out_line = ''
    r = 13  # ROT-13

    for char in message:
        if not char.isalpha():
            out_line += char
            continue

        if 65 <= ord(char) <= 90:
            out_line += chr((ord(char) + r - 65) % 26 + 65)

        elif 97 <= ord(char) <= 122:
            out_line += chr((ord(char) + r - 97) % 26 + 97)

    return out_line


if __name__ == '__main__':

    # Original Kata: https://www.codewars.com/kata/52223df9e8f98c7aa7000062/

    read_values = [
        "EBG13 rknzcyr.",  # "ROT13 example."
        "This is my first ROT13 excercise!",  # "Guvf vf zl svefg EBG13 rkprepvfr!"
        'clerk',  # pyrex
    ]

    for item in read_values:
        print(rot13(item))
