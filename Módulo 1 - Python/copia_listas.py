#Este es el listado inicial de empresas que han solicitado la subvención
empresas=["El Corte Inglés","ACCIONA","Endesa","Fagor","HP"]
#No quiero que le pase nada al listado, creo una copia y sigo trabajando con ella
empresa_copia=empresas.copy()
#Hago la simulación y el sistema me devuelve "HP"; Ésta es la empresa que no puede recibir subvención.
#La elimino
eliminada="HP"
empresa_copia.remove(eliminada)
#imprimo el nuevo listado de empresas, ya actualizado.
print("Las empresas que todavía pueden recibir subvención son: ",empresa_copia)
#Para estar seguro de que mi listado inicial sigue igual, imprimo la lista empresas y...
#Oh, sorpresa
print("Listado inicial",empresas)