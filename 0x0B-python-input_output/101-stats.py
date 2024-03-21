#!/usr/bin/python3
""" script that reads stdin
line by line and computes metrics:

Input format: <IP Address> -
[<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning
"""


def print_stat(file_size, stat):
    """print status code ascending order

    Args:
        file_size (int): file size
        stat (dict): status code and occurence
    """
    print("File size: {}".format(file_size))
    for k in sorted(stat):
        print("{}: {}".format(k, stat[k]))


if __name__ == "__main__":
    import sys
    valid = ['200', '301', '400', '401', '403', '404', '405', '500']
    stat = {}
    count = 0
    file_size = 0
    try:
        for line in sys.stdin:

            if count == 10:
                print_stat(file_size, stat)
                count = 1
            else:
                count += 1
            line = line.split()
            try:
                file_size += int(line[-1])
            except (IndexError, ValueError):
                pass
            try:
                if line[-2] in valid:
                    if stat.get(line[-2], -1) == -1:
                        stat[line[-2]] = 1
                    else:
                        stat[line[-2]] += 1
            except (IndexError):
                pass
        print_stat(file_size, stat)
    except KeyboardInterrupt:
        print_stat(file_size, stat)
        raise
