def ehpar(x):
    return(x%2==0)

def par_ou_impar(x):
    if ehpar(x):
        return "par"
    else:
        return "impar"

print(par_ou_impar(4))
print(par_ou_impar(5))