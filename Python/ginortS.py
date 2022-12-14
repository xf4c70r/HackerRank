if __name__ == '__main__':
    lower = list()
    upper = list()
    odd = list()
    even = list()
    S = input()
    S = list(S)
    for char in S:
        if char.islower():
            lower.append(char)
        elif char.isupper():
            upper.append(char)
        elif char.isdigit():
            if int(char) % 2 == 0 :
                even.append(char)
            else :
                odd.append(char)
    print(''.join(sorted(lower)+sorted(upper)+sorted(odd)+sorted(even)))
