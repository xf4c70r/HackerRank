import re
T = []
def change(match):
    if match.group(0) == '&&':
        return 'and'
    elif  match.group(0) == '||':
        return 'or'
    
    
N = int(input())
for i in range(N):
    T.append(input())
    
t = '\n'.join(T)

print (re.sub(r"(?<= )(&&|\|\|)(?= )", change, t))
