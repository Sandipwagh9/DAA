def knapsack(W,wt,val,n):

    if(W==0 or n==0):
        return 0
    
    if(wt[n-1]>W):
        return knapsack(W,wt,val,n-1)
    else:
        return max(val[n-1]+knapsack(W-wt[n-1],wt,val,n-1),
                   knapsack(W,wt,val,n-1))

if __name__=="__main__":
    profit=[60,100,120]
    weight=[10,20,30]
    n=len(profit)
    print(knapsack(50,weight,profit,n))
