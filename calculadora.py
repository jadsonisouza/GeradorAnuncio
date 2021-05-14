from datetime import datetime

temp = []  # Lista Temporária, recebe os dados temporáriamente e depois exclui.
princ = []  # Lista principal, onde armazena todos os dados digitados

# ====================[ CABEÇALHO ]====================#
while True:
    print(' ******************************************')
    print(' *              Divulga Tudo              *')
    print(' ******************************************')
    print('\n =================[ MENU ]=================')
    print(' =                                        =')
    print(' =            1 - Novo Anúncio            =')
    print(' =                                        =')
    print(' =            2 - Pesquisar Anúncio       =')
    print(' =                                        =')
    print(' =            3 - Sair                    =')
    print(' =                                        =')

    # Comando para seleção do menu
    menu = int(input(' ==========================================\n :: '))

    # Opção para novo anúncio
    if menu == 1:

        while True: #laço de repetição

            # Coletando os dados do anúncio.
            temp.append(str.capitalize(input('\n  Anúncio: ')))# 0
            temp.append(str.capitalize(input('  Cliente: ')))  # 1
            temp.append(str.capitalize(input('  Data Inicio [Ex: **/**/****]: '))) # 2
            temp.append(str.capitalize(input('  Data Fim [Ex: **/**/****]: ')))  # 3
            temp.append(float(input(f'  Investimento: [Ex: 2.50] R$')))

            # Copiar a lista temporaria para definitiva.
            princ.append(temp[:])

            # Apagando a lista temporaria, após enviar para lista principal.
            temp.clear()

            # Opção para criar novo anuncio, após inserir um.
            resp = str(input('\n  Quer criar novo? [S/N] \n  :: '))

            # Opção para interromper a inclusão de novo anuncio.
            if resp in 'Nn':
                break

    # Opção para consultar anúncio já cadastrado
    elif menu == 2:

        # Caso não tenha anúncio cadastrado exibe a mensagem abaixo
        if len(princ) == 0:
            print('\n [!] A lista está vazia, favor cadastre novo anúncio !!!')

        #Caso tenha anúncio cadastrado
        elif len(princ) != 0:

            print('\n  Segue nossa lista de cadastrados:') #Mostra o nome dos clientes cadastrado
            for b in princ:
                print(f'  {b[1]}')

            while True:


                cons = str.capitalize(input('\n  Digite o nome do cliente: \n  :: '))
                for p in princ:

                    # ===========================[ CONVERSÃO DATA ]===========================#
                    data1 = datetime.strptime(p[2], '%d/%m/%Y').date()
                    data2 = datetime.strptime(p[3], '%d/%m/%Y').date()
                    # ===========================[ DIAS ]===========================#
                    diferenca = abs((data2 - data1).days)

                    #retorna os dados para o usuário
                    if p[1] == cons:
                        print('\n =================[ Dados do Anúncio ]=================')
                        print(
                            f'\n  Nome do Anúncio:{p[0]}\n  Nome do Cliente: {p[1]}\n  Data inicio: {p[2]}\n  Data Término: {p[3]}\n  Investimento diário: R${p[4]:.2f}'.replace('.',','))

                        print('\n ===============[ Resultado da Pesquisa ]===============')

                        # ===========================[ CONVERSÃO DATA ]===========================#
                        data1 = datetime.strptime(p[2], '%d/%m/%Y').date()
                        data2 = datetime.strptime(p[3], '%d/%m/%Y').date()
                        # ===========================[ DIAS ]===========================#
                        diferenca = abs((data2 - data1).days)

                        # ===========================[ CALCULOS ]===========================#
                        valor_total = p[4] * diferenca
                        n2 = int(30 * valor_total) / 1  # ---> Alcance pago 01
                        n3 = int(12 * n2) / 100  # ---> Cliques 01
                        n4 = int(3 * n3) / 20  # ---> Compartilhamento 01

                        # ===========================[ CALCULOS ]===========================#
                        n5 = int(n4 * 40)  # ---> Alcance orgânico 01
                        n6 = int(12 * n5) / 100  # ---> Cliques 02
                        n7 = int(3 * n6) / 20  # ---> Compartilhamento 02

                        # ===========================[ CALCULOS ]===========================#
                        n8 = int(n7 * 40)  # // ---> Alcance orgânico 02
                        a1 = int(12 * n8) / 100  # // ---> Cliques 03
                        a2 = int(3 * a1) / 20  # // ---> Compartilhamento 03

                        # ===========================[ CALCULOS ]===========================#
                        a3 = int(a2 * 40)  # // ---> Alcance orgânico 03
                        qtd_views = int(n2 + n5 + n8 + a3)
                        qtd_cliques = int(n3 + n6 + a1)
                        qtd_share = int(n4 + n7 + a2)

                        # ========================[ Exibe para o Usuário ]========================#
                        print(f'\n  Valor total investido: R${valor_total:.2f}'.replace('.',','))
                        print(f'  Quantidade de visualizações: {qtd_views}')
                        print(f'  Quantidade de cliques: {qtd_cliques}')
                        print(f'  Quantidade de Compartilhamentos: {qtd_share}')

                #Filtro por periodo
                resp2 = input('\n  Quer filtrar esse anúncio por período? [S/N] \n  :: ').upper()[0]
                if resp2 == 'N':
                    break
                if resp2 in 'S':
                    while True:
                        resp4 = int(input('  Digite a quantidade de dias que deseja filtrar:\n  :: '))
                        if resp4 <= diferenca and resp4 > 0:

                            # ===========================[ CALCULOS ]===========================#
                            valor_total = p[4] * resp4
                            n2 = int(30 * valor_total) / 1  # ---> Alcance pago 01
                            n3 = int(12 * n2) / 100  # ---> Cliques 01
                            n4 = int(3 * n3) / 20  # ---> Compartilhamento 01

                            # ===========================[ CALCULOS ]===========================#
                            n5 = int(n4 * 40)  # ---> Alcance orgânico 01
                            n6 = int(12 * n5) / 100  # ---> Cliques 02
                            n7 = int(3 * n6) / 20  # ---> Compartilhamento 02

                            # ===========================[ CALCULOS ]===========================#
                            n8 = int(n7 * 40)  # // ---> Alcance orgânico 02
                            a1 = int(12 * n8) / 100  # // ---> Cliques 03
                            a2 = int(3 * a1) / 20  # // ---> Compartilhamento 03

                            # ===========================[ CALCULOS ]===========================#
                            a3 = int(a2 * 40)  # // ---> Alcance orgânico 03
                            qtd_views = int(n2 + n5 + n8 + a3)
                            qtd_cliques = int(n3 + n6 + a1)
                            qtd_share = int(n4 + n7 + a2)

                            # ========================[ Exibe para o Usuário ]========================#
                            print(f'\n  Valor total investido: R${valor_total:.2f}'.replace('.',','))
                            print(f'  Quantidade de visualizações: {qtd_views}')
                            print(f'  Quantidade de cliques: {qtd_cliques}')
                            print(f'  Quantidade de Compartilhamentos: {qtd_share}')
                            break

                        #Opção exibida se o usuário solicitar uma quantidade de dias maiores do que foi cadastrado
                        else:
                            print('  [!] A quantidade de dias digitada é diferente do contratado! Tente novamente\n')

                    #Opção para realizar nova consulta
                    resp1 = str(input('\n  Quer consultar outro anuncio? [S/N] \n  :: ')).upper()[0]

                    if resp1 == 'N':
                        break
    # Opção para sair do programa
    elif menu == 3:
        break

    # Opção para quem não digitar nenhuma das 3 opções
    else:
        print('\n  [!] Você digitou uma opção inválida ')