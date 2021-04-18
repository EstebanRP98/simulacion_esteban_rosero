# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 17:57:14 2021

@author: EstebanRM
"""


import matplotlib.pyplot as plt
import numpy as np
import random

def generadorHistograma(size):
    print("Lista"+str(size))
    list = [random.randint(1,6) + random.randint(1,6) for i in range(size)]
    fig, hs = plt.subplots()
    hs.grid(True)
    hs.set_xticks(range(2,15))
    hs.set_title("Lanzamientos " + str(size))
    hs.set_xlabel("Numero del dado")
    hs.set_ylabel("Frecuencia")
    hs.hist(list, bins=np.arange(2,15)-0.5, rwidth=0.7, facecolor='blue')
    fig.savefig('histograma/lanzamiento'+str(size)+'.png')

def jugar():
    print("jugando")
    dados = [10, 100, 1000, 10000, 100000, 1000000]
    for cantidad in dados:
        generadorHistograma(cantidad)
        


if __name__ == "__main__":
    print("Ingreso a jugar")
    jugar()
    



    