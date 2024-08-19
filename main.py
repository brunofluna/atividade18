#Atividade 18
import os

dados = ('Nome Completo', 'Data de Nascimento', 'CPF', 'Profissão', 'E-mail', 'Endereço', 'Telefone')

usuario_completo = [
    {
        dados[0]: 'Bruno Luna',
        dados[1]: '25/02/1984',
        dados[2]: '97874698134',
        dados[3]: 'Programador',
        dados[4]: 'bruno@brunoluna.com.br',
        dados[5]: 'QE 13 Guará II, Brasília-DF',
        dados[6]: '61 981071050'

    }
]

while True:
    print('1 - Cadastrar Usuário.')
    print('2 - Listar Usuários.')
    print('3 - Alterar Dados.')
    print('4 - Excluir.')
    print('5 - Sair do Programa.')

    opcao = input('Opção do Usuário: ')
    
    os.system('cls')
    
    match opcao:
        case '1':
            novo_usuario = input('Informe os dados: ')
            usuario_completo.append(novo_usuario)
            print(f'Novos dados inseridos: {novo_usuario}')
            continue
        case '2':
            for i in range(len(usuario_completo)):
                print(f'Dados dos usuários: {usuario_completo}')
            continue
        case '3':
            indice = int(input('Informe o índice a alterar: '))
            campo = input('Informe o campo a ser alterado:')
            indice -= 1
            try:
                usuario_completo[indice][campo] = input('Informe o dado a ser alterado {campo}: ')
            except:
                print('Não foi possível alterar!')
            print(f'Novos dados do índice {indice + 1}: \n')
            for i in range(len(usuario_completo)):
                print(f'Listagem dos usuários: {usuario_completo}')
            continue
        case '4':
            indice = int(input('Informe o indice do usuário a ser excluido: '))
            indice -= 1
            try:
                del[usuario_completo[indice]]
            except:
                print('Não foi possível deletar o índice.')
            for i in range(len(usuario_completo)):
                print(f'{usuario_completo}')
