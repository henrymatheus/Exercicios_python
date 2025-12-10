
lista_frutas = []

while True:
    for indice, item in enumerate(lista_frutas):
        print(indice, item)

    adicionar_remover = input('Deseja adicionar ou remover item? (a/r)').lower()
    fruta = input('Adicione uma fruta: ')

    if not adicionar_remover or not fruta:
        print('escolha uma das opções.')
        continue
    
    
    if adicionar_remover == 'a':
        lista_frutas.append(fruta)
    elif adicionar_remover == 'r':
        lista_frutas.remove(fruta)


    # else:
    #     print('Escolha uma das opções')
    #     continue


    if fruta == 'sair':
        break