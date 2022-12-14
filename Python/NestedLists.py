if __name__ == '__main__':
  s = []
  n = []
  n_listed = []
  for _ in range(int(input())):
        name = input()
        n.append(name)
        score = float(input())
        s.append(score)
  b = min (s) 
  a = max (s) 
  for i in range(len(s)):
    if s[i] < a and s[i] > b :
      a = s[i]
  for j in range(len(s)):
    if s[j] == a:
      n_listed.append(n[j])
  for k in sorted(n_listed):
    print(k)
