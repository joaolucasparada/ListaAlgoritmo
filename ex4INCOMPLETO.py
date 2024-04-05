# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
A = [0, "kombi", "fusca", "belina", 4, "dodge", "gordini", "tl", 6, "variant", "brasilia", "opala", 7, "corcel", "santana", "quantum", 11, "scort", "rural", "variante", 23, "sp2", "willis", "simca", 44, "decavê", "uno", "veraneio"]
An = len(A)
B = [21, "macaco", "zebra", "tartaruga", "tubarão", "formiga", 55, "leão", "elefante", "girafa", "coelho", "pato", 60, "gato", "cobra", "aranha", "cabra", "besouro", 73, "borboleta", "boi", "tigre", "leopardo", "anta", 101, "mula", "burro", "calango", "lagartixa", "sapo", 202, "baleia", "urso", "hiena", "rato", "gorila"]
Bn = len(B)

def busca_linear(x):
    for p in range(1):
        i = 0
        while i < An:
            if A[i] == x:
                return A[i], A[i+1], A[i+2], A[i+3]
            else:
                i = i + 1
print("dimensão da lista A = ", An)                
tempo_inicial = time.time()
print("\nchave (0) = ", busca_linear(4))
print("chave (6) = ", busca_linear(6))
print("chave (7) = ", busca_linear(7))
print("chave (11) = ", busca_linear(11))
print("chave (23) = ", busca_linear(23))
print("chave (44) = ", busca_linear(44))
tempo_final = time.time()

print("tempo de execução = ", tempo_final - tempo_inicial)