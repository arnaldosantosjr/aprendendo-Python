def inserir_no_inicio(array, elemento):# Define uma função que recebe o array original e o elemento a ser inserido como argumentos.
    '''
    insere um elemento no iníco de um array em Python
    Arg:
        array: O array original.
        elemento: O elemento a ser inserido.

    Returns:
        Um novo array com o elemento inserido no início
    '''

    # Criar um novo array com um espaço extra
    novo_array =[0] * (len(array) + 1) # Cria um novo array com um tamanho igual ao do array original mais um espaço para o novo elemento. Inicializa todos os elementos com 0.

    #Desloca os elementos para a direira
    for i in range(len(array)):# Itera sobre os elementos do array original.
        novo_array[i +1] = array[i] #Desloca cada elemento do array original para a posição seguinte no novo array.
    
    #insere um novo elemento no início
    novo_array [0] = elemento #  Insere o novo elemento na primeira posição (índice 0) do novo array.

    return novo_array
#Exemplo de uso

array = [0, 2, 4, 8]
novo_elemento = 10

novo_array = inserir_no_inicio(array, novo_elemento)
print(novo_array) #Output: [10, 0, 2, 4, 6, 8]