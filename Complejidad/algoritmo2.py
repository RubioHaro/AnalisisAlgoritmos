def codigo(n):
    j = 0
    for i in range(n):
        j=i+1
        print(i)
    print("-----")
    return j
    
    
print("resulto:"+ str(codigo(1)))
print("resulto:"+ str(codigo(2)))
print("resulto:"+ str(codigo(3)))
print("resulto:"+ str(codigo(100)))

## Complejidad O(n)