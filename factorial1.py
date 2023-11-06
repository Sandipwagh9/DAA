def fact(n):
    ans=1
    for i in range(1,n+1):
        ans=ans*i
    return ans

ans=fact(4)
print(ans)