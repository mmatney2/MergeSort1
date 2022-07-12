def digital_root2(num):
    soma=0
    while num//10 !=0:
        soma = soma + num%10 #=6
        num=num//10 #=7
    soma = soma + num 
    # return soma
    if soma//10 == 0:
        return soma
    else:
        return digital_root2(soma) 
print(digital_root2(76))

def array_diff(a, b):
    for n in b:
        while n in a:
            a.remove(n)
    return a

print(array_diff([1, 1,2, 2,3], [1, 2]))