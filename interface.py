# Une solution en programmation dynamique pour le probléme du Sac à Dos (avec interface graphique)
from tkinter import *
root = Tk()
#On récupère  le poid maximal et le nombre des objets 
TitleLabel= Label(root,text="Solution du Problème du Sac à Dos ",font=("Times New Roman", 14) )
TitleLabel.grid(row=0,column=1,pady=(20, 15),padx=(5,0))
Title2Label= Label(root,text="(Programmation Dynamique) ",font=("Times New Roman", 14) )
Title2Label.grid(row=0,column=2,pady=(20, 15))
indice=1
numberLabel= Label(root,text="Combien d'objets y a-t-il ? ",font=("Times New Roman", 12) )
numberLabel.grid(row=indice,column=1,pady=(5, 5))
numberEntry= Entry(root,width=40)
numberEntry.grid(row=indice,column=2,pady=(5, 5))
indice+=1
maxPoidLabel= Label(root,text="Quel est le poids maximal du sac à dos ? ",font=("Times New Roman", 12) )
maxPoidLabel.grid(row=indice,column=1,pady=(5, 5))
maxPoidEntry= Entry(root,width=40)
maxPoidEntry.grid(row=indice,column=2,pady=(5, 5))
indice+=1
#Fonction appelée pour inserer les poids et gains des objets  
def addElements():
    numberOfElement=int(numberEntry.get())
    entriesPoids=[]
    entriesGain=[]
    # On affiche un tableau à remplir avec les poids et gains des objets   
    for element in range(numberOfElement):
        elementString= "Poids de l'objet: "+ str(element)
        elementLabel= Label(root,text=elementString,font=("Times New Roman", 12) )
        elementLabel.grid(row=element+4,column=1,pady=(5, 5))
        entriesPoids.append( Entry(root,width=30))
        entriesPoids[element].grid(row=element+4,column=2,pady=(5, 5))
        
        elementStringGain= "Gain de l'objet: "+ str(element)
        elementLabelGain= Label(root,text=elementStringGain,font=("Times New Roman", 12) )
        elementLabelGain.grid(row=element+4,column=3,pady=(5, 5))
        entriesGain.append(Entry(root,width=30))
        entriesGain[element].grid(row=element+4,column=4,pady=(5, 5))
 
    return entriesPoids, entriesGain;

#Fonction appelée quand on clique sur le button d'insertion d'objets 
def clickedElements():
    n=int(numberEntry.get())
    W=int(maxPoidEntry.get())
    Wi,Vi= addElements()
    #Fonction appelée quand on clique sur le button d'affichage du gain maximal du sac à dos   
    def clickMaxGain():
        We = [0 for x in range(n)]
        Ve = [0 for x in range(n)]
        for object in range(n):
             We[object]=int (Wi[object].get())
             Ve[object] =int (Vi[object].get())
        SacADos(W, We, Ve, n, indice+n+4)
    #Fonction appelée pour calculer le gain maximal du sac à dos      
    def SacADos(W, Wi, Vi, n,indiceRes): 
        # tableau K[][] pour mémoriser les gains 
        K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
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
        # On Affiche les objets ajoutés au sac à dos en utilisant le tableau créé 
        while continu == True:
            if K[p][q]==0: 
                 continu =False
            elif K[p-1][q]== K[p][q]:
                 p-= 1
            else:
                 objectstring= "L'objet avec le poids = "+ str(Wi[p-1])+ " et le gain = "+ str(Vi[p-1])+" est ajouté au sac à dos"
                 objectlabel= Label(root,text=objectstring,font=("Times New Roman", 12) )
                 objectlabel.grid(row=indiceRes,column=2)
                 q=q-Wi[p-1]
                 p-=1
            indiceRes+=1
        # On Affiche le gain maximal du sac à dos qui est la valeur du derniere cas du tableau créé 
        maxg=" Le gain maximal du sac à dos est : "+str( K[n][W])
        maxlabel=Label(root,text=maxg,font=("Times New Roman", 14))
        maxlabel.grid(row=indiceRes,column=3,pady=(5, 5))
    # Button pour afficher le gain maximal du sac à dos et son contenu (objets selectionés)  
    afficherGain= Button(root,text="Afficher le gain maximal",font=("Times New Roman", 10),command=clickMaxGain)
    afficherGain.grid(row=indice+n+2,column=2,pady=(5, 5))

 # Button pour afficher un tableau à remplir avec les poids et gains des objets   
afficherElements= Button(root,text="Inserer les objects",font=("Times New Roman", 10),command=clickedElements)
afficherElements.grid(row=indice,column=2,pady=(5, 5))

root.mainloop()