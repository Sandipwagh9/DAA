def GCD(a,b):
    
    while b>0:
        temp=a
        a=b
        b=temp%b
    
    return a

ans=GCD(19,8)
print(ans)