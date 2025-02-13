for i in range(1,6) :
    print(" * " * i)
    
num =5
for i in range(1,6) :
    print(("  " * (num-i))+(" * " * i))
    
for i in range(5, 0, -1) :
    print(" * " * i)
    
for i in range(5, 0, -1) :
    print(("  " * (num-i))+(" * " * i))
    
name="Yanshu"
for i in range(0,6,1) :
    print((" " * i) + name[i])

alp="ABCDE"
for i in range(0,5,1) :
    print(alp[i]*(i+1))
    
alp="ABCDE"
for i in range(0,6,1) :
    print( alp[:i])
    
for i in range(4,0,-1) :
    print( alp[:i])
    
for i in range(1,6) :
    print( " " * (5-i) + " *" *i)
    
for i in range(5,0,-1) :
    print( " " * (5-i) + " *" *i)
    
for i in range(1,6) :
    print( " " * (5-i) + " *" *i)
    
 
