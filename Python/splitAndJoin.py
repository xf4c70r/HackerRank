def split_and_join(line):
    line_new = line.split(" ")
    return "-".join(line_new)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
