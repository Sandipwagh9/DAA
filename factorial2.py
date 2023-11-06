def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

ans=fact(4)
print(ans)
