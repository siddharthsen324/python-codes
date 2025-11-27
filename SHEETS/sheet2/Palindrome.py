n=input()
rev=n[::-1]
rev_non_zero=str(int(rev))
print(rev_non_zero)
if n==rev:
    print("YES")
else:
    print("NO")