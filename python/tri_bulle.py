
def tri_bulle(A):
    n = len(A)
   
    for i in range(n):
        for j in range(0, n-i-1):
           
            if A[j] > A[j+1] :
                A[j], A[j+1] = A[j+1], A[j]
A = [-60, 0, 1, 4]
tri_bulle(A)
print ("Le tableau trié est:")
for i in range(len(A)):
    print ("%d" %A[i])
