from tkinter import *
root = Tk()

val = [1, 4, 5,7] 
wt = [1, 3, 4, 5] 
W = 70
n = len(val) 

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
            objectstring= "L'objet avec le poids = "+ str(wt[p-1])+ " et le gain = "+ str(val[p-1])+" est ajouté au sac à dos"
            objectlabel= Label(root,text=objectstring )
            objectlabel.pack()
            q=q-wt[p-1]
            p-=1
    maxg=" Le gain maximal du sac à dos est : "+str( K[n][W])
    maxlabel=Label(root,text=maxg)
    maxlabel.pack()
    
def click():
    SacADos(W, wt, val, n)
   
afficherGain= Button(root,text="Afficher le gain maximal",command=click)
afficherGain.pack()
root.mainloop()