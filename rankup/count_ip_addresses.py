def ips_between(start, end):
    """ Counts the number of addresses between two IPv4 addresses.

    Args:
        start (str): IPv4 address
        end (str): IPv4 address

    Returns:
        int: Number of addresses
    """

    arrays = list(zip(map(int, start.split('.')), map(int, end.split('.'))))

    count = 0
    for i in range(len(arrays)):
        s, e = arrays[i][0], arrays[i][1]
        count += (e * 256 ** (3 - i)) - (s * 256 ** (3 - i))
        
    return count


if __name__ == '__main__':

    # Original Kata: https://www.codewars.com/kata/526989a41034285187000de4

    print(ips_between("10.0.0.0", "10.0.0.50"))  # 50
    print(ips_between("10.0.0.0", "10.0.1.0"))  # 256
    print(ips_between("20.0.0.10", "20.0.1.0"))  # 246
    print(ips_between("214.177.196.187", "214.178.184.157"))  # 62434
    print(ips_between("48.198.97.237", "48.200.227.205"))  # 164320
    print(ips_between("31.195.173.177", "32.48.248.33"))  # 7162480
    print(ips_between("76.147.120.246", "76.154.12.248"))  # 431106
    print(ips_between("142.20.41.224", "142.20.60.95"))  #  4735
    print(ips_between("161.202.129.184", "165.217.131.10"))  #  68092242
    
    print(ips_between("0.0.0.0", "255.255.255.255"))  # 4294967295
