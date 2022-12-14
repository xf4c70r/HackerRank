if __name__ == '__main__':
    s = input()
    alpha=False
    char=False
    dig=False
    lower=False
    upper=False
    
    for i in s :
        if i.isalnum()==True :
            alpha=True
        if i.isalpha()==True :
            char=True
        if i.isdigit()==True :
            dig=True
        if i.islower()==True :
            lower=True
        if i.isupper()==True :
            upper=True
        
    print(alpha)
    print(char)
    print(dig)
    print(lower)
    print(upper)
