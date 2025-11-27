s = input().replace(" ", "")
if "+" in s:
    a,rest = s.split('+',1)
    b,c = rest.split('=')
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b == c:
        print("Yes")
    else:
        print(a + b)
elif "-" in s:
    a,rest = s.split('-',1)
    print(a)
    print(rest)
    b,c = rest.split('=')
    print(b)
    print(c)
    a = int(a)
    b = int(b)
    c = int(c)
    if a - b == c:
        print("Yes")
    else:
        print(a - b)
elif "*" in s:
    a,rest = s.split('*',1)
    print(a)
    print(rest)
    b, c = rest.split('=',1)
    print(b)
    print(c)
    a = int(a)
    b = int(b)
    c = int(c)
    if a * b == c:
        print("Yes")
    else:
        print(a * b)
    

