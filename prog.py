# Une solution en programmation dynamique pour le probléme du Sac à Dos 
def SacADos(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    # tableau K[][]  
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    continu = True
    p=n 
    q=W
    while continu == True:
        if K[p][q]==0: 
            continu =False
        elif K[p-1][q]== K[p][q]:
            p-= 1
        else:
            print("L'objet avec le poids = ",wt[p-1]," et le gain = ",val[p-1]," est ajouté au sac à dos")
            q=q-wt[p-1]

    
    return K[n][W] 
  
# Programme test  
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
resultat = SacADos(W, wt, val, n)
print("Le gain maximal du sac à dos est :" , resultat) 
  
