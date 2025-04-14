# Faça um jogo pa o usuário adicinhar uma palavra secreta.
# Você vai propor uma palavra secreta qualquer e vai
#dar a possibilidade para o usuário digitar apenas uma letra.
# Quando o usuário digitar uma letra, você vai conferir se 
# a letra digitada está na palavra secreta.
    # - Se a letra digitada estiver na palavra secreta,
    # - Se a letra digitada não estiver na palavra secreta; exiba. *
# Faça a contadem de tentativas do seu usuário.


import os # Importa o módulo os para limpar a tela

palavra_secreta = 'paladino'


# Lista para armazenar as letras que o jogador acertou
letras_acertadas = []   
numero_tentativas = 0  # Contador de tentativas do jogador

# Loop principal do jogo, que continuará até o jogador acertar a palavra secreta
while True:
    # Solicita ao jogador que digite uma letra
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1  # Incrementa o contador de tentativas
    # Verifica se o jogador digitou mais de uma letra
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')  # Exibe uma mensagem de erro
        continue  # Reinicia o loop para pedir uma nova entrada

    # Verifica se a letra digitada está na palavra secreta
    if letra_digitada in palavra_secreta:
        # Adiciona a letra acertada à lista de letras acertadas
        letras_acertadas += letra_digitada
    
    palavra_formada = ''  # Variável para armazenar a palavra formada até o momento
    # Percorre cada letra da palavra secreta para exibir o progresso do jogador
    for letra_cetreta in palavra_secreta:
        if letra_cetreta in letras_acertadas:
            palavra_formada += letra_cetreta  # Adiciona a letra acertada à palavra formada
        else:
            # Exibe um asterisco (*) para as letras que ainda não foram descobertas
           palavra_formada += '*'
    print('palavra_formada: ', palavra_formada)  # Exibe a palavra formada até o momento
            
    if palavra_formada == palavra_secreta:
        os.system('cls')# Limpa a tela do console para mostrar a mensagem de vitória
        print('Você Ganhou!')  # Mensagem de vitória
        print('A palavra secreta era:', palavra_secreta)
        print('Tentativas: ', numero_tentativas)  # Exibe a palavra secreta

        #Zera as variáveis para reiniciar o jogo
        letras_acertadas = []   
        numero_tentativas = 0