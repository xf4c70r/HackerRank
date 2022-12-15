def print_formatted(number):
    leng = len(str(bin(number))[2:])
    for i in range(1,number+1):
        print(
        str(i).rjust(leng," "),
        str(oct(i))[2:].upper().rjust(leng," ") ,  
        str(hex(i))[2:].upper().rjust(leng," "),
        str(bin(i))[2:].upper().rjust(leng," ")
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)