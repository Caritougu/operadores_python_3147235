#Operadores en python         
'''
los operadores en python siguen el orden jerarquico:

1.         ( )
2.         **
3.      /, * , %  
4.        +, -,
5.          =




si hay parentesis dentro del parentesis se resuelve primero el parentesis interno 


1./, * , %,
2. +, -,
3. =

Si hay opreciones en el mismo nivel de jerarquia, se resuelven de izquierda a derecha 


'''

a = 3
b = 2
c = 1
x = 5

y = ((2*a+c)/7) * (a+(4*a)/c)
print(y)