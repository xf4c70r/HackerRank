import email.utils
import re
for _ in range(int(input())):
    regex_pattern = r"^[a-zA-Z][\w\-\.]*@[A-Za-z]+\.[a-zA-Z]{1,3}$"
    x = email.utils.parseaddr(input())  
    if (re.match(regex_pattern, x[1])):
        print(email.utils.formataddr(x))
