import threading
import random

# Função que irá procurar o maior elemento em uma parte do vetor
def find_max(vetor, start, end, result, index):
    max_value = vetor[start]
    for i in range(start + 1, end):
        if vetor[i] > max_value:
            max_value = vetor[i]
    result[index] = max_value

def main():
    # Inicializa o vetor de inteiros randômicos
    tamanho_vetor = 100
    vetor = [random.randint(0, 1000) for _ in range(tamanho_vetor)]

    # Lista para armazenar o maior valor encontrado por cada thread
    result = [None, None]

    # Define os intervalos para cada thread
    mid = len(vetor) // 2

    # Cria duas threads para processar cada parte do vetor
    t1 = threading.Thread(target=find_max, args=(vetor, 0, mid, result, 0))
    t2 = threading.Thread(target=find_max, args=(vetor, mid, len(vetor), result, 1))

    # Inicia as threads
    t1.start()
    t2.start()

    # Espera as threads terminarem
    t1.join()
    t2.join()

    # O maior valor será o maior entre os resultados das duas threads
    maior_elemento = max(result)

    # Exibe o resultado
    print(f"O vetor é: {vetor}")
    print(f"O maior elemento encontrado foi: {maior_elemento}")

if __name__ == "__main__":
    main()
