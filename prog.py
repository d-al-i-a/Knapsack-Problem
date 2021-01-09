# Une solution en programmation dynamique pour le probléme du Sac à Dos 

def SelectObjets(W, Wi, Vi, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    # tableau K[][]  
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif Wi[i-1] <= w: 
                K[i][w] = max(Vi[i-1] + K[i-1][w-Wi[i-1]],  K[i-1][w]) 
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
            print("L'objet avec le poids = ",Wi[p-1]," et le gain = ",Vi[p-1]," est ajouté au sac à dos")
            q=q-Wi[p-1]
            p-= 1
    
    return K[n][W] 
  
# Programme test  
Vi = [1, 4, 5, 7] #tableau des gains Vi
Wi = [1, 3, 4, 5] #tableau des poids Wi
W = 7   
n = len(Vi) 
resultat = SelectObjets(W, Wi, Vi, n)
print("Le gain maximal du sac à dos est :" , resultat) 
  
