t=int(input())
for _ in range(t):
    n,m =map(int,input().split())
    start=min(n,m)
    end=max(n,m)
    count=0
    for i in range(start+1,end):
        if i%2!=0:
            count+=i
    print(count)        
