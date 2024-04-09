import time

# Definição das listas A e B
A = [0, "kombi", "fusca", "belina", 4, "dodge", "gordini", "", 6, "variant", "brasilia", "opala", 7, "corcel", "santana", "quantum", 11, "scort", "rural", "variant", 23, "sp2", "willis", "simca", 44, "decave", "uno", "veraneio"]
B = [21, "macaco", "zebra", "tartaruga", "tubarão", "formiga", 55, "leão", "elefante", "girafa", "coelho", "pato", 60, "gato", "cobra", "aranha", "cabra", "besouro", 73, "borboleta", "boi", "tigre", "leopardo", "anta", 101, "mula", "burro", "calango", "lagartixa", "sapo", 202, "balcia", "urso", "hiena", "rato", "gorila"]

# Implementação do algoritmo de busca sequencial
def busca_sequencial(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# Implementação do algoritmo de busca sequencial com adição ao final
def busca_sequencial_com_adicao(lista, elemento):
    if elemento in lista:
        return lista.index(elemento)
    else:
        lista.append(elemento)
        return len(lista) - 1

# Função para execução de cada exercício
def executar_exercicio(lista, exercicio, adicionar=False):
    tempos = []
    for elemento in lista:
        inicio = time.time()
        if adicionar:
            resultado = busca_sequencial_com_adicao(lista, elemento)
        else:
            resultado = busca_sequencial(lista, elemento)
        fim = time.time()
        tempo_execucao = fim - inicio
        tempos.append(tempo_execucao)
        print(f"Exercício {exercicio}: Elemento: {elemento}, Resultado: {resultado}, Tempo de execução: {tempo_execucao}")
    return tempos

# Execução dos exercícios
tempos_exercicio_1 = executar_exercicio(A, 1)
print("-------")
tempos_exercicio_2 = executar_exercicio(A, 2, adicionar=True)
print("-------")
tempos_exercicio_3 = executar_exercicio(B, 3)
print("-------")
tempos_exercicio_4 = executar_exercicio(B, 4, adicionar=True)
print("-------")
tempos_exercicio_5 = executar_exercicio(A, 5)
print("-------")
tempos_exercicio_6 = executar_exercicio(B, 6)
print("-------")
tempos_exercicio_7_a = executar_exercicio(A, 7)
print("-------")
tempos_exercicio_7_b = executar_exercicio(B, 7)
print("-------")
tempos_exercicio_8_a = executar_exercicio(A, 8, adicionar=True)
print("-------")
tempos_exercicio_8_b = executar_exercicio(B, 8, adicionar=True)

# Função para cálculo da média de tempo de execução
def calcular_media_tempos(tempos):
    return sum(tempos) / len(tempos)

# Exibição dos resultados
print("Média de tempos de execução:")
print("Exercício 1:", calcular_media_tempos(tempos_exercicio_1))
print("Exercício 2:", calcular_media_tempos(tempos_exercicio_2))
print("Exercício 3:", calcular_media_tempos(tempos_exercicio_3))
print("Exercício 4:", calcular_media_tempos(tempos_exercicio_4))
print("Exercício 5:", calcular_media_tempos(tempos_exercicio_5))
print("Exercício 6:", calcular_media_tempos(tempos_exercicio_6))
print("Exercício 7 (Lista A):", calcular_media_tempos(tempos_exercicio_7_a))
print("Exercício 7 (Lista B):", calcular_media_tempos(tempos_exercicio_7_b))
print("Exercício 8 (Lista A):", calcular_media_tempos(tempos_exercicio_8_a))
print("Exercício 8 (Lista B):", calcular_media_tempos(tempos_exercicio_8_b))
