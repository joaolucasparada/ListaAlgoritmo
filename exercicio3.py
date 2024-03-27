# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:50:32 2024

@author: lab55
"""

import random
import time

A = []
for i in range(0, 50):
    A.append(i)
print("\nDimensão da lista A= ",len(A))
print("Lista A=", A)
tempo_inicial = time.time()
for p in range(1):
    for j in range(1, len(A)):
        temporario = A[j]
        i = j-1
        while i >= 0 and A[i] > temporario:
            A[i+ 1] = A[i]
            i-=1
        A[i+1] = temporario
tempo_final = time.time()
print("Matriz A ordenada = ", A)
print("Tempo de execução = ", tempo_final - tempo_inicial)

B = []
for i in range(0, 50):
    B.append(i)
B.sort(reverse=True)    
print("\nDimensão da lista B= ",len(B))
print("Lista B=", B)
tempo_inicial = time.time()
for p in range(1):
    for j in range(1, len(B)):
        temporario = B[j]
        i = j-1
        while i >= 0 and B[i] > temporario:
            B[i+ 1] = B[i]
            i-=1
        B[i+1] = temporario
tempo_final = time.time()
print("Matriz B ordenada = ", B)
print("Tempo de execução = ", tempo_final - tempo_inicial)

C = []
n = 0
while n < 50:
    n+=1
    a = random.randrange(0, 50, 1)
    C.append(a)
print("\nDimensão da lista C= ", len(C))    
print("Lista C= ", C)
tempo_inicial = time.time()
for p in range(1):
    for j in range(1, len(C)):
        temporario = C[j]
        i = j-1
        while i >= 0 and C[i] > temporario:
            C[i+ 1] = C[i]
            i-=1
        C[i+1] = temporario
tempo_final = time.time()
print("Matriz C ordenada = ", C)
print("Tempo de execução = ", tempo_final - tempo_inicial)

D = []
for i in range(0, 100):
    D.append(i)   
print("\nDimensão da lista D= ",len(D))
print("Lista D=", D)
tempo_inicial = time.time()
for p in range(1):
    for j in range(1, len(D)):
        temporario = D[j]
        i = j-1
        while i >= 0 and D[i] > temporario:
            D[i+ 1] = D[i]
            i-=1
        D[i+1] = temporario
tempo_final = time.time()
print("Matriz D ordenada = ", D)
print("Tempo de execução = ", tempo_final - tempo_inicial)

E = []
for i in range(0, 100):
    E.append(i)
E.sort(reverse=True)   
print("\nDimensão da lista E= ",len(E))
print("Lista E=", E)
tempo_inicial = time.time()
for p in range(1):
    for j in range(1, len(E)):
        temporario = E[j]
        i = j-1
        while i >= 0 and E[i] > temporario:
            E[i+ 1] = E[i]
            i-=1
        E[i+1] = temporario
tempo_final = time.time()
print("Matriz E ordenada = ", E)
print("Tempo de execução = ", tempo_final - tempo_inicial)

F = []
n = 0
while n < 100:
    n+=1
    a = random.randrange(0, 100, 1)
    F.append(a)
print("\nDimensão da lista F= ", len(F))    
print("Lista F= ", F)
tempo_inicial = time.time()
for p in range(1):
    for j in range(1, len(F)):
        temporario = F[j]
        i = j-1
        while i >= 0 and F[i] > temporario:
            F[i+ 1] = F[i]
            i-=1
        F[i+1] = temporario
tempo_final = time.time()
print("Matriz F ordenada = ", F)
print("Tempo de execução = ", tempo_final - tempo_inicial)









      
            

    
    
    


