def tri_selection(A):
   for i in range(len(A)):
       min = i
       for j in range(i+1, len(A)):
           if A[min] > A[j]:
               min = j               
       tmp = A[i]
       A[i] = A[min]
       A[min] = tmp
   return A
A = [-60, 0, 1, 4] 
tri_selection(A)
print ("Le tableau trié est:")
for i in range(len(A)):
    print ("%d" %A[i])