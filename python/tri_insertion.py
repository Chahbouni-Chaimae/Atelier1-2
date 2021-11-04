def tri_insertion(A): 
    for i in range(1, len(A)): 
        k = A[i] 
        j = i-1
        while j >= 0 and k < A[j] : 
                A[j + 1] = A[j] 
                j -= 1
        A[j + 1] = k
A = [-60, 0, 1,4]
tri_insertion(A) 
print ("Le tableau trié est:")
for i in range(len(A)): 
    print ("% d" % A[i])