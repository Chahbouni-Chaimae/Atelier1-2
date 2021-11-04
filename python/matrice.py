
def chercher_element(A,n):
    l=0
    c=0
    for i in range(len(A)):
        for j in range(len(A[i])):
           if A[i][j] == n:     
               l=i
               c=j
               
    if l==0 & c==0:
               print ("L'element",n," cherche ne se trouve pas")
    else:
        print ("L'element",n," cherche se trouve dans la matriceet sa position est:i=" , l+1, "j=" , c+1)

A = ( [1, 4, 6, 8],[9, 11, 0, 5])
x=int(input("entrez l'element cherche:"))
chercher_element(A,x)

