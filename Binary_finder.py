n=(input("input whatever you want"))
p=[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,92,59,60,61,62,63,64,91,93,94,95,96,123,124,125,126]
q=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","!","","#","$","%","&","'","(",")","*","+",",","-",".","/","*",";","<",">","?","@","[","]","^","_","`","{"]

z=""
lo=len(q)

k=""
for u in n:
        
        if (u.isdigit()== True ):
            m=int(u)
        else:
            for x in range(lo):
                if u==q[x]:
                    m=p[x]
                    break
        
        y=""
        a=0
        if (m==1):
            z=z+'01'
            continue
            
            
        while True:
            l=int(m/2)
            l=int(l)
            d=m%2
            d=str(d)
            y=d+y
            if l==1:
                d=1
                d=str(d)
                y=d+y
                break
            m=l
        z=z+y
print("the binary of the random thing you input is",z)


