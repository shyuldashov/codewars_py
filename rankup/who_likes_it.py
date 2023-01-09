def likes(names):
    line = ''
    
    if len(names) <= 1:
        line = f'{"no one" if not names else names[0]}'    
    
    elif len(names) == 2:
        line = f'{names[0]} and {names[1]}'
        
    else:
        line = ', '.join(names[:2]) + f' and {names[2] if len(names) == 3 else str(len(names[2:])) + " others"}'

    return line + f'{" likes this" if len(names) <= 1 else " like this"}'


if __name__ == '__main__':
    
    # Original Kata: https://www.codewars.com/kata/5266876b8f4bf2da9b000362

    print(likes([]))  # -->  "no one likes this"
    print(likes(['Peter']))  # -->  "Peter likes this"
    print(likes(['Jacob', 'Alex']))  # -->  "Jacob and Alex like this"
    print(likes(['Max', 'John', 'Mark']))  # -->  "Max, John and Mark like this"
    print(likes(['Alex', 'Jacob', 'Mark', 'Max']))  # -->  "Alex, Jacob and 2 others like this"s
    print(likes(['Alex', 'Jacob', 'Mark', 'Max', 'Agf', 'Gdf']))  # -->  "Alex, Jacob and 4 others like this"s
