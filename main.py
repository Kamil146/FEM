import numpy as np
import matplotlib.pyplot as plt

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

n=10;

def generujTabliceGeometrii(p,k,n):
    tmp = (k-p) / (n-1)
    matrix = np.array([1,p])
    matrix2 = np.array([1,1,2])


    for i in range(1, n, 1):
        matrix = np.block([
            [matrix],
            [i+1, i * tmp + p],
        ])
    for i in range (2,n,1):
        matrix2 = np.block([
            [matrix2],
            [i,i,i+1]
        ])


    return matrix,matrix2



WEZLY,ELEMENTY = generujTabliceGeometrii(x_a,x_b,n)


def generujGeomtrie(wezly):
    y=np.zeros(wezly.shape[0])
    plt.plot(wezly[:,1],y,marker='o')
    for i in range(0,np.size(y),1):
        plt.text(x=wezly[i,1],y=y[i]-0.008,s=int(wezly[i,0]),color='red')
    for i in range(0, np.size(y)-1, 1):
        plt.text(x=(wezly[i, 1]+wezly[i+1, 1])/2, y=y[i] + 0.005, s=int(i+1),color='blue')
    plt.show()


generujGeomtrie(WEZLY)

