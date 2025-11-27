s=int(input())
for _ in range(s):
    n=input().strip()      
    for ch in reversed(n):
        print(ch,end=" ")
    print()    
    # while n>0:
    #     last=n%10
    #     print(last,end=" ")
    #     n=n//10
    # print()    
        