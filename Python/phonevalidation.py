import re
for _ in range(int(input())):
    regex_pattern = r"^[7-9][0-9]{9}$" 
    if (re.match(regex_pattern, input())):
        print("YES")
    else :
        print("NO")
