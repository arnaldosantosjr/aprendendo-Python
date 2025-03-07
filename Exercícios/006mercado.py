'''
O programa adiciona até 10 ítens na lista de compras
e pergunta o valor a medida em que o ítem é inserido
Quando chega a 10 ítens o programa para de receber ítens 
e mostra o valor total da compra
A tecla p para a contagem e calcula os alores já inseridos '''
qtd = 0 #quantidade de alimento 
tecla = 'c'
total = 0.0

while (qtd < 10 and tecla !='p'):
    preco = float(input('Preço: '))
    total = total + preco
    qtd = qtd + 1
    tecla =input('pressione qualquer tecla para continuar ou "p" para parar')
    print(f'O total da compra é R$ {total}.')