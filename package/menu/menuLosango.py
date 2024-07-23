from package.menu.utils import Utils, time
from package.maths.terms import Losango
from package.maths.formas import Formas

class MenuLosango():
    
    def telaCriar():
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-2-8 |
        +----------------------------------------------+
        | Criação de Losango                           |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para se criar um losango, digite as          |
        | coordenadas dos quatro vertices no formato   |
        | do ponto (x,y), sendo as primeiras           |
        | coordenadas dadas as do vértice superior,    |
        | o segundo do vértice direito, o próximo do   |
        | vértice inferior e o último do esquerdo,     |
        | são aceitos valores inteiros ou decimais.    |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 0,0,2,2,4,0,2,-2                         |
        | 2º) 0.5,0.5,2,2,4,0.5,2,-2                   |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X1,Y1,X2,Y2,X3,Y3,X4,Y4 - Criar o Losango    |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen()
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),8,MenuLosango,'telaCriar')    

        Utils.clearScreen()
        losango = Losango(coordenadas[0],coordenadas[1],coordenadas[2],coordenadas[3],coordenadas[4],coordenadas[5],coordenadas[6],coordenadas[7])
        Utils.verificaArea(losango.getArea(),MenuLosango,'telaCriar')
        MenuLosango.telaCriado(losango)
    
    def telaCriado(losango):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-2-8-1 |
        +----------------------------------------------+
        | Losango criado com sucesso!                  |
        +----------------------------------------------+
        | Dados:                                       |
        |                                              |
        | - Medidas das diagonais: {Utils.formatarNumero(losango.getD1())} e {Utils.formatarNumero(losango.getD2())}
        | - Área: {Utils.formatarNumero(losango.getArea())}
        | - Perímetro: {Utils.formatarNumero(losango.getPerimetro())}
        | - Coordenadas dos vértices são:
        |   v1 = ({Utils.formatarNumero(losango.getL1().getX())},{Utils.formatarNumero(losango.getL1().getY())}) | v2 = ({Utils.formatarNumero(losango.getL2().getX())},{Utils.formatarNumero(losango.getL2().getY())})
        |   v3 = ({Utils.formatarNumero(losango.getL3().getX())},{Utils.formatarNumero(losango.getL3().getY())}) | v4 = ({Utils.formatarNumero(losango.getL4().getX())},{Utils.formatarNumero(losango.getL4().getY())})
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v':
            Utils.clearScreen() 
            MenuLosango.telaCriar()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI':
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()
            MenuLosango.telaCriado(losango)

    def escolhaDaFigura():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        losangos = formas.pegarPorTipo('Losango')
        for i, losango in enumerate(losangos):
            if str(losango.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(losango.getNumero()))
                diagonal1 = f'{losango.getD2():.2f}'
                diagonal2 = f'{losango.getD1():.2f}'
                strLista = strLista + '        | ' + str(losango.getNumero()) + ') (x1,y1) = (' + str(losango.getL1().getX()) +','+ str(losango.getL1().getY()) + ') | (x2,y2) = (' + str(losango.getL2().getX())+','+ str(losango.getL2().getY()) + ') | (x3,y3) = (' + str(losango.getL3().getX())+','+str(losango.getL3().getY()) + ') | (x4,y4) = (' + str(losango.getL4().getX()) + ',' + str(losango.getL4().getY()) + ') | Diagonal1 = ' + diagonal1 + ' | Diagonal2 = ' + diagonal2
                if i != len(losangos) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-3-6 |
        +----------------------------------------------+
        | Seus losangos disponíveis são                |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do losango Escolhido              |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI':
            Utils.clearScreen()
            Utils.menuInicial()
        elif opcaoSelecionada not in opcoesDisponiveis: 
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()            
        else:
            Utils.clearScreen()
            formas = Formas()
            Losango = formas.pegarPorTipoENumero('Losango',opcaoSelecionada)
            MenuLosango.telaInterferencia(Losango)
        

    def telaInterferencia(Losango):
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-3-6-1 |
        +----------------------------------------------+
        | Interferência no losango                     |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para verificar onde um ponto está em relação |
        | a esse losango já criado, é necessário passar|
        | as coordenadas do ponto(x,y), sendo valores  |
        | inteiros ou decimais.                        |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 1,2                                      |
        | 2º) 1,2.4                                    |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X,Y - Verificar Interferência no Losango     |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        coordenadas = valores.split(',')

        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),2,MenuLosango,'telaInterferencia')

        Utils.clearScreen()
        MenuLosango.telaInterferido(coordenadas[0],coordenadas[1],Losango)

    def telaInterferido(xp,yp,Losango):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-3-6-2 |
        +----------------------------------------------+
        | Interferência verificada com sucesso!        |
        +----------------------------------------------+
        | Dados:                                       |
        |                                              |
        | - Coordenadas do ponto: ({Utils.formatarNumero(xp)},{Utils.formatarNumero(yp)})
        | - {Losango.verificaPosicao(xp,yp)}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v':
            Utils.clearScreen() 
            MenuLosango.telaInterferencia()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.opcaoNaoDisponivel()
            MenuLosango.telaInterferencia(Losango)

    def atualizacao():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        losangos = formas.pegarPorTipo('Losango')
        for i, losango in enumerate(losangos):
            if str(losango.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(losango.getNumero()))
                diagonal1 = f'{losango.getD2():.2f}'
                diagonal2 = f'{losango.getD1():.2f}'
                strLista = strLista + '        | ' + str(losango.getNumero()) + ') (x1,y1) = (' + str(losango.getL1().getX()) +','+ str(losango.getL1().getY()) + ') | (x2,y2) = (' + str(losango.getL2().getX())+','+ str(losango.getL2().getY()) + ') | (x3,y3) = (' + str(losango.getL3().getX())+','+str(losango.getL3().getY()) + ') | (x4,y4) = (' + str(losango.getL4().getX()) + ',' + str(losango.getL4().getY()) + ') | Diagonal1 = ' + diagonal1 + ' | Diagonal2 = ' + diagonal2
                if i != len(losangos) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '

        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-5-7 |
        +----------------------------------------------+
        | Losangos disponíveis para atualizar          |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Losango                        |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI':
            Utils.clearScreen()
            Utils.menuInicial()
        elif opcaoSelecionada not in opcoesDisponiveis: 
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()
        else:
            formas = Formas()
            Losango = formas.pegarPorTipoENumero('Losango',opcaoSelecionada)
            MenuLosango.telaNovosValores(Losango)

    def telaNovosValores(Losango):
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-7-1 |
        +----------------------------------------------+
        | Atualização do Losango                       |
        +----------------------------------------------+
        |                                              |
        | Por favor, passe os novos dados do losango   |
        | que será alterado (coordenadas dos quatro    |
        | vértices),podendo ser valores inteiros ou    |
        | decimais.                                    |
        |                                              |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X1,Y1,X2,Y2,X3,Y3,X4,Y4 - Atualizar o Losango|
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen() 
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),8,MenuLosango,'telaNovosValores')    

        Utils.clearScreen()
        Losango.atualizar(coordenadas[0],coordenadas[1],coordenadas[2],coordenadas[3],coordenadas[4],coordenadas[5],coordenadas[6],coordenadas[7])
        Utils.verificaArea(Losango.getArea(),MenuLosango,'telaNovosValores')
        formas = Formas()
        formas.atualizar(Losango)
        MenuLosango.atualizado(Losango)

    def atualizado(Losango):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-7-2 |
        +----------------------------------------------+
        | Losango atualizado com sucesso!              |
        +----------------------------------------------+
        | Dados do seu novo losango:                   |
        |                                              |
        | - Medidas das diagonais: {Utils.formatarNumero(Losango.getD1())} e {Utils.formatarNumero(Losango.getD2())}
        | - Área: {Utils.formatarNumero(Losango.getArea())}
        | - Perímetro: {Utils.formatarNumero(Losango.getPerimetro())}
        | - Coordenadas dos vértices são:
        |   v1 = ({Utils.formatarNumero(Losango.getL1().getX())},{Utils.formatarNumero(Losango.getL1().getY())}) | v2 = ({Utils.formatarNumero(Losango.getL2().getX())},{Utils.formatarNumero(Losango.getL2().getY())})
        |   v3 = ({Utils.formatarNumero(Losango.getL3().getX())},{Utils.formatarNumero(Losango.getL3().getY())}) | v4 = ({Utils.formatarNumero(Losango.getL4().getX())},{Utils.formatarNumero(Losango.getL4().getY())})
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuLosango.telaNovosValores()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.opcaoNaoDisponivel()
            MenuLosango.atualizado(Losango)
        
    def delecao():
        Utils.clearScreen()
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        losangos = formas.pegarPorTipo('Losango')
        for i, losango in enumerate(losangos):
            if str(losango.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(losango.getNumero()))
                diagonal1 = f'{losango.getD2():.2f}'
                diagonal2 = f'{losango.getD1():.2f}'
                strLista = strLista + '        | ' + str(losango.getNumero()) + ') (x1,y1) = (' + str(losango.getL1().getX()) +','+ str(losango.getL1().getY()) + ') | (x2,y2) = (' + str(losango.getL2().getX())+','+ str(losango.getL2().getY()) + ') | (x3,y3) = (' + str(losango.getL3().getX())+','+str(losango.getL3().getY()) + ') | (x4,y4) = (' + str(losango.getL4().getX()) + ',' + str(losango.getL4().getY()) + ') | Diagonal1 = ' + diagonal1 + ' | Diagonal2 = ' + diagonal2
                if i != len(losangos) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '


        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-6-7 |
        +----------------------------------------------+
        | Seus Losangos disponíveis são                |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Losango que será deletado      |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI':
            Utils.clearScreen()
            Utils.menuInicial()
        elif opcaoSelecionada not in opcoesDisponiveis: 
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()
        else:
            formas = Formas()
            losango = formas.pegarPorTipoENumero('Losango',opcaoSelecionada)
            MenuLosango.confirmarDelecao(losango)

    def confirmarDelecao(losango):
        Utils.clearScreen()
        
        opcoesDisponiveis = {'S','s','N','n'}

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-6-7-1 |
        +----------------------------------------------+
        | Confirmação de deleção                       |
        +----------------------------------------------+
        |
        | Deseja realmente deletar o Losango: v1 =({Utils.formatarNumero(losango.getL1().getX())},{Utils.formatarNumero(losango.getL1().getY())}) | v2 = ({Utils.formatarNumero(losango.getL2().getX())},{Utils.formatarNumero(losango.getL2().getY())}) | v3 = ({Utils.formatarNumero(losango.getL3().getX())},{Utils.formatarNumero(losango.getL3().getY())}) | v4 = ({Utils.formatarNumero(losango.getL4().getX())},{Utils.formatarNumero(losango.getL4().getY())})?
        |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | S - Sim                                      |
        | N - Não                                      |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if opcaoSelecionada not in opcoesDisponiveis: 
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()
        elif opcaoSelecionada in ['S','s']:
            formas = Formas()
            formas.deleta(losango)            
            Utils.clearScreen()
            print('Ponto deletado!')
            time.sleep(3)
            Utils.clearScreen()
            Utils.menuInicial()
        elif opcaoSelecionada in ['N','n']:            
            Utils.clearScreen()
            print('Deleção cancelada!')
            time.sleep(3)
            Utils.clearScreen()
            Utils.menuInicial()