nombre = (2.16,3.43,9.22,2.32,4.23,4.26,0.97)
alpha = nombre[0]
for i in range(len(nombre)) :
    if nombre[i]>alpha:
        alpha = nombre[i]
print(alpha)
