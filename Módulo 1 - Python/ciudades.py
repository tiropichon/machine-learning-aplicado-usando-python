ciudades=["madrid","barcelona","sevilla","valencia"]
ciudades.append("bilbao")
ciudades.append("salamanca")
print(ciudades[:])
print(len(ciudades))
ciudades.insert(1,"malaga")
print(ciudades[:])
del ciudades[1]
print(ciudades[:])
ciud_pops=ciudades.pop()
print(ciud_pops[:])