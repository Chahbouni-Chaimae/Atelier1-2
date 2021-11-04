def fréquence(str , c):
    cnt=0
    for i in str:
        if i==c:
          cnt+=1
    return cnt
str="hello world"
print(fréquence(str , 'l'))
   
