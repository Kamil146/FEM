import numpy as np
import matplotlib as mat

#Preprocesing
c=0
f=0
x_a=0
x_b=1
wezly=np.array([[1,0],
               [2,1],
               [3,0.5],
               [4,0.75]])
elementy=np.array([[1,1,3],
                   [2,4,2],
                   [3,3,4]])

twb_L = 'D'
twb_P = 'D'
wwb_L = 0
wwb_P = 1


print("\n",wezly)
print(elementy)

n=100;

def generujTabliceGeometrii(p,k,n):
    tmp = (k-p) / (n-1)
    matrix = np.array([1,p])
    matrix2 = np.array([1,1,2])
    print(matrix)

    for i in range(1, n, 1):
        matrix = np.block([
            [matrix],
            [i+1, i * tmp + p],
        ])
    for i in range (1,n,1):
        matrix2 = np.block([
            [matrix2],
            [i,i,i+1]
        ])


    return matrix,matrix2



WEZLY,ELEMENTY = generujTabliceGeometrii(x_a,x_b,n)
print(WEZLY)
print(ELEMENTY)
