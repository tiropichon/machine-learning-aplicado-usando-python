#LLamaremos a nuestra función como func_esp. Requerirá como argumentos los dos números.
def func_esp(a,b):
    resultado=(a+b)/(a-b)
    return resultado

var1=54
var2=34
res=func_esp(var1,var2)
print(res)