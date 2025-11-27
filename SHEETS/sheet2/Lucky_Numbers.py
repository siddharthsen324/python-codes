a,b=map(int,input().split())
def lucky(n):
    for d in str(n):
        if d!='4' and d!='7':
            return False
    return True
found=False
for num in range(a,b+1):
    if(lucky(num)):
        print(num,end=" ")
        found=True
if not found:
    print(-1)            

