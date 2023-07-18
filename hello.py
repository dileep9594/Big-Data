def checkanagram (s) :
    if len(s) == 1 or len(s) == 0 :
        return 1
    rev = ''
    for x in s:
        rev  += x
    print(rev) 

    if rev == s :
        return 1
    else : return 0
    
    
    

if __name__ == "__main__" : 
    result =  checkanagram("ram")
    print(result)
    