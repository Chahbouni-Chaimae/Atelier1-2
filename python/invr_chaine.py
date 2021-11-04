def reverse_string(string): 
    if len(string) == 0: 
        return string 
    else: 
        return reverse_string(string[1:]) + string[0] 
  
string = "is reverse"
  
print ("The original string  is : ",end="") 
print (string) 
  
print ("The reversed string is : ",end="") 
print (reverse_string(string)) 