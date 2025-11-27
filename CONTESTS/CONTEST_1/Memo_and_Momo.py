x,y,k=map(int,input().split())
x_div=(x%k==0)
y_div=(y%k==0)
if x_div and y_div:
    print("Both")
elif x_div:
    print("Memo")
elif y_div:
    print("Momo")
else:
    print("No One")