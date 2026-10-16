import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu(qtd_produtos):
    print('\n--- Menu ---')
    print(f'Produtos cadastrados: ')
    print('1 - Cadastrar produto')
    print('2 - Consultar produto')
    print('3 - Listar produtos')
    print('0 - Sair')

def cadastrar_produto(produtos):
    clear_screen()
    print('\n---Cadastro---')
    nome = input('Nome do produto: ')
    preco_valido = False
    while not preco_valido:
        preco = float(input('Preço do produto (maior que zero): '))
        if preco > 0:
            preco_valido = True
        else:
            print('Preço inválido. Digite um valor maior que zero.')
    produtos.append((nome, preco))
    clear_screen()
    print('Mensagem: Produto cadastrado com sucesso!')

def consultar_produto(produtos):
    clear_screen()
    print('\n---Consulta---')  
    nome_busca = input('Digite o nome do produto: ')
    encontrado = False
    i = 0
    while i < len(produtos):
        if produtos[i][0] == nome_busca:
            clear_screen()
            print(
                f'Produto encontrado: '
                f'{produtos[i][0]} - R$ {produtos[i][1]:.2f}'
            )
            encontrado = True
        i += 1
    if not encontrado:
        clear_screen()
        print(f'Aviso: Produto {nome_busca} não encontrado.')

produtos = []
continuar = True

def listar_produtos(produtos):
    for produto in produtos:
        clear_screen()
        print(produto)

produtos = []
continuar = True

while continuar:
    mostrar_menu(len(produtos))
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        cadastrar_produto(produtos)
    elif opcao == '2':
        consultar_produto(produtos)
    elif opcao == '3':
        listar_produtos(produtos)
    elif opcao == '0':
        continuar = False
    else:
        print('Opção inválida.')