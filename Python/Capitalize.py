def solve(s):
    split = s.split(" ")
    caps = []

    for _ in split:
        caps.append(_.capitalize())

    string = " ".join(caps)   
    return string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()

"""
Another Method : 

def solve(s): return s.title()
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()

"""
