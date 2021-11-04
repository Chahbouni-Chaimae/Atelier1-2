N= int(input("entrez un nombre N:"))
nbr=0
while(N!=0):
    N = N// 10
    nbr+=1
print("nombre totale des chiffres dans le nombre choisi ", N , "est:" , nbr)
