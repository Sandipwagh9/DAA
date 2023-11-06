def TowerofHanoi(n,from_rod,to_rod,aux_rod):
    if n==0:
        return
    TowerofHanoi(n-1,from_rod,aux_rod,to_rod)
    print("Moved disk",n,"From Rod",from_rod,"To Rod",to_rod)
    TowerofHanoi(n-1,aux_rod,to_rod,from_rod)

n=3
TowerofHanoi(3,"A","C","B")