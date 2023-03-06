mensaje1="Introduzca la primera variable:"
mensaje2="Introduzca la segunda variable:"
variable1=input(mensaje1)
variable2=input(mensaje2)
if(variable1>variable2):
    print("La primera variable,",variable1,"es la mayor")
elif(variable1==variable2):
    print("Las dos variables son iguales.")
else:
    print("La segunda variable,",variable2,"es la mayor")