# Repetir Enquqnto horário menor que 17
    # receber e armazenar voto
    # Verificar para quem foi o voto
    # Contar o voto para o candifdato escolhido
    # Verificar o horário
    # Ir para próximo eleitor
# Mostrar total de votos para cada candidato
horario = 8
candidato1 = 0
candidato2 = 0
nulo = 0

while (horario <17):
    voto = int(input('Voto: '))
    if voto == 22:
       candidato1 = candidato1 + 1
    elif voto == 13:
        candidato2 = candidato2 + 1
    else:
        nulo = nulo + 1
    horario =int(input('Horário:'))
print(f'Candidato 1: {candidato1}')
print(f'Candidato 2: {candidato2}')
print(f'Nulo: {nulo}')
