import os

restaurantes = [{'nome':'teste','categoria':'teste','ativo':False}]

def exibir_nome_programa():
    print("""𝒮𝒶𝒷ℴ𝓇 ℰ𝓍𝓅𝓇ℯ𝓈𝓈""")

def finalizar_app():
    exibir_subtitulo('Finalizando app')

def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal:')
    main()

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*'* (len(texto))
    print(f'{linha}\n{texto}\n{linha}')
    print()

def exibir_opcoes():
    print('1.Cadastrar Restaurante')
    print('2.Listar Restaurante')
    print('3.Ativar/Destaivar Restaurante')
    print('4.Sair\n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}:')
    dados_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes:')
    print(f'{'Nome do Restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | {'Status'}')
    print('-'*60)
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria= restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_menu_principal()

def alterar_status_restaurante():
    exibir_subtitulo('Alternando Status do Restaurante:')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o status:')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo']= not restaurante['ativo']
            mensagem = f'O Restaurante {nome_do_restaurante} foi ativado com sucesso!'if restaurante['ativo'] == True else f'O Restaurante {nome_do_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado.')
    voltar_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))  
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida ==2:
            listar_restaurantes( )
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
        elif opcao_escolhida ==4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()