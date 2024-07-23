from package.menu.utils import Utils, time
from package.maths.terms import TrapezioRet
from package.maths.formas import Formas

class MenuTrapezio():
    
    def telaCriar():
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-2-7 |
        +----------------------------------------------+
        | Criação de Trapézio                          |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para se criar um trapézio, digite as         |
        | coordenadas dos quatro vértices no formato   |
        | do ponto (x,y), sendo as primeiras           |
        | coordenadas dadas as do vértice superior     |
        | esquerdo, o segundo do vértice superior      |
        | direito, o próximo do vértice inferior       |
        | direito e o último do inferior esquerdo,     |
        | são aceitos valores inteiros ou decimais.    |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 1,1,5,1,0,5,6,5                          |
        | 2º) 1,1,5,1,0.5,5.1,6,5.1                    |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X1,Y1,X2,Y2,X3,Y3,X4,Y4 - Criar o trapézio   |
        | VI - Voltar ao Menu Inicial                  |        
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen()
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),8,MenuTrapezio,'telaCriar')    

        Utils.clearScreen()
        trapezio = TrapezioRet(coordenadas[0],coordenadas[1],coordenadas[2],coordenadas[3],coordenadas[4],coordenadas[5],coordenadas[6],coordenadas[7])
        Utils.verificaArea(trapezio.getArea(),MenuTrapezio,'telaCriar')
        MenuTrapezio.telaCriado(trapezio)
    
    def telaCriado(trapezio):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-2-7-1 |
        +----------------------------------------------+
        | Trapézio criado com sucesso!                 |
        +----------------------------------------------+
        | Dados:                                       
        |                                        
        | - Trapézio Reto: {"Sim" if trapezio._isReto else "Não"}
        | - Altura: {Utils.formatarNumero(trapezio.getAltura())}
        | - Base menor: {Utils.formatarNumero(trapezio.getBMenor())}
        | - Base maior: {Utils.formatarNumero(trapezio.getBMaior())}
        | - Área: {Utils.formatarNumero(trapezio.getArea())}
        | - Perímetro: {Utils.formatarNumero(trapezio.getPerimetro())}
        | - Coordenadas dos vértices são:
        |   v1 = ({Utils.formatarNumero(trapezio.getTr1().getX())},{Utils.formatarNumero(trapezio.getTr1().getY())}) | v2 = ({Utils.formatarNumero(trapezio.getTr2().getX())},{Utils.formatarNumero(trapezio.getTr2().getY())})
        |   v3 = ({Utils.formatarNumero(trapezio.getTr3().getX())},{Utils.formatarNumero(trapezio.getTr3().getY())}) | v4 = ({Utils.formatarNumero(trapezio.getTr4().getX())},{Utils.formatarNumero(trapezio.getTr4().getY())}).
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v':
            Utils.clearScreen() 
            MenuTrapezio.telaCriar()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()
            MenuTrapezio.telaCriado(trapezio)

    def escolhaDaFigura():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        trapezios = formas.pegarPorTipo('Trapézio')
        for i, trapezio in enumerate(trapezios):
            if str(trapezio.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(trapezio.getNumero()))
                strLista = strLista + '        | ' + str(trapezio.getNumero()) + ') (x1,y1) = (' + str(trapezio.getTr1().getX()) +','+ str(trapezio.getTr1().getY()) + ') | (x2,y2) = (' + str(trapezio.getTr2().getX())+','+ str(trapezio.getTr2().getY()) + ') | (x3,y3) = (' + str(trapezio.getTr3().getX())+','+str(trapezio.getTr3().getY()) + ') | (x4,y4) = (' + str(trapezio.getTr4().getX()) + ',' + str(trapezio.getTr4().getY()) + ') | BMAIOR = ' + str(trapezio.getBMaior()) + ' | BMENOR = ' + str(trapezio.getBMenor()) 
                if i != len(trapezios) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-3-7 |
        +----------------------------------------------+
        | Seus trapézios disponíveis são               |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Trapézio Escolhido             |
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
            Trapezio = formas.pegarPorTipoENumero('Trapézio',opcaoSelecionada)
            MenuTrapezio.telaInterferencia(Trapezio)
        

    def telaInterferencia():
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-3-7-1 |
        +----------------------------------------------+
        | Interferência no Trapézio                    |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para verificar onde um ponto está em relação |
        | a um trapézio já criado, é necessário passar |
        | as coordenadas do ponto(x,y), sendo valores  |
        | inteiros ou decimais.                        |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 1,2                                      |
        | 2º) 1,2.4                                    |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X,Y - Verificar Interferência no Trapézio     |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        coordenadas = valores.split(',')

        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen() 
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),2,MenuTrapezio,'telaInterferencia')

        Utils.clearScreen()
        MenuTrapezio.telaInterferido(coordenadas[0],coordenadas[1])

    def telaInterferido(xp,yp):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-3-7-2 |
        +----------------------------------------------+
        | Interferência verificada com sucesso!        |
        +----------------------------------------------+
        | Dados:
        |
        | - Coordenadas do ponto: ({Utils.formatarNumero(xp)},{Utils.formatarNumero(yp)})
        | - {TrapezioRet.verificaPosicao(xp,yp)}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuTrapezio.telaInterferencia()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()
            MenuTrapezio.telaInterferencia(TrapezioRet)

    def atualizacao():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        trapezios = formas.pegarPorTipo('Trapézio')
        for i, trapezio in enumerate(trapezios):
            if str(trapezio.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(trapezio.getNumero()))
                strLista = strLista + '        | ' + str(trapezio.getNumero()) + ') (x1,y1) = (' + str(trapezio.getTr1().getX()) +','+ str(trapezio.getTr1().getY()) + ') | (x2,y2) = (' + str(trapezio.getTr2().getX())+','+ str(trapezio.getTr2().getY()) + ') | (x3,y3) = (' + str(trapezio.getTr3().getX())+','+str(trapezio.getTr3().getY()) + ') | (x4,y4) = (' + str(trapezio.getTr4().getX()) + ',' + str(trapezio.getTr4().getY()) + ') | BMAIOR = ' + str(trapezio.getBMaior()) + ' | BMENOR = ' + str(trapezio.getBMenor()) 
                if i != len(trapezios) - 1:
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
        | Menu                                   0-5-8 |
        +----------------------------------------------+
        | Trapézios disponíveis para atualizar         |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Trapézio                       |
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
            trapezio = formas.pegarPorTipoENumero('Trapézio',opcaoSelecionada)
            MenuTrapezio.telaNovosValores(trapezio)

    def telaNovosValores(trapezio):
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-8-1 |
        +----------------------------------------------+
        | Atualização do Trapézio                      |
        +----------------------------------------------+
        |                                              |
        | Por favor, passe os novos dados do trapézio  |
        | que será alterado (coordenadas dos quatro    |
        | vértices, base maior e base menor),          |
        | podendo ser valores inteiros ou decimais.    |
        |                                              |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X1,Y1,X2,Y2,X3,Y3,X4,Y4,BMAIOR,BMENOR -      |
        | Atualizar o Trapézio                         |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen() 
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),10,MenuTrapezio,'telaNovosValores')    

        Utils.clearScreen()
        trapezio.atualizar(coordenadas[0],coordenadas[1],coordenadas[2],coordenadas[3],coordenadas[4],coordenadas[5],coordenadas[6],coordenadas[7],coordenadas[8],coordenadas[9])
        Utils.verificaArea(trapezio.getArea(),MenuTrapezio,'telaNovosValores')
        formas = Formas()
        formas.atualizar(trapezio)
        MenuTrapezio.atualizado(trapezio)

    def atualizado(trapezio):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-8-2 |
        +----------------------------------------------+
        | Trapézio atualizado com sucesso!             |
        +----------------------------------------------+
        | Dados do seu novo Trapézio:                  |
        |                                              |
        | - Trapézio Reto: {"Sim" if trapezio._isReto else "Não"}
        | - Altura: {Utils.formatarNumero(trapezio.getAltura())}
        | - Base menor: {Utils.formatarNumero(trapezio.getBMenor())}
        | - Base maior: {Utils.formatarNumero(trapezio.getBMaior())}
        | - Área: {Utils.formatarNumero(trapezio.getArea())}
        | - Perímetro: {Utils.formatarNumero(trapezio.getPerimetro())}
        | - Coordenadas dos vértices são:
        |   v1 = ({Utils.formatarNumero(trapezio.getTr1().getX())},{Utils.formatarNumero(trapezio.getTr1().getY())}) | v2 = ({Utils.formatarNumero(trapezio.getTr2().getX())},{Utils.formatarNumero(trapezio.getTr2().getY())})
        |   v3 = ({Utils.formatarNumero(trapezio.getTr3().getX())},{Utils.formatarNumero(trapezio.getTr3().getY())}) | v4 = ({Utils.formatarNumero(trapezio.getTr4().getX())},{Utils.formatarNumero(trapezio.getTr4().getY())}).
        +----------------------------------------------+
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuTrapezio.telaNovosValores()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.opcaoNaoDisponivel()
            MenuTrapezio.atualizado(trapezio)

    def delecao():
        Utils.clearScreen()
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        trapezios = formas.pegarPorTipo('Trapézio')
        for i, trapezio in enumerate(trapezios):
            if str(trapezio.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(trapezio.getNumero()))
                strLista = strLista + '        | ' + str(trapezio.getNumero()) + ') (x1,y1) = (' + str(trapezio.getTr1().getX()) +','+ str(trapezio.getTr1().getY()) + ') | (x2,y2) = (' + str(trapezio.getTr2().getX())+','+ str(trapezio.getTr2().getY()) + ') | (x3,y3) = (' + str(trapezio.getTr3().getX())+','+str(trapezio.getTr3().getY()) + ') | (x4,y4) = (' + str(trapezio.getTr4().getX()) + ',' + str(trapezio.getTr4().getY()) + ') | BMAIOR = ' + str(trapezio.getBMaior()) + ' | BMENOR = ' + str(trapezio.getBMenor()) 
                if i != len(trapezios) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-6-8 |
        +----------------------------------------------+
        | Seus Trapézios disponíveis são               |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Trapézio que será deletado     |
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
            trapezio = formas.pegarPorTipoENumero('Trapézio',opcaoSelecionada)
            MenuTrapezio.confirmarDelecao(trapezio)

    def confirmarDelecao(trapezio):
        Utils.clearScreen()
        
        opcoesDisponiveis = {'S','s','N','n'}

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-6-8-1 |
        +----------------------------------------------+
        | Confirmação de deleção                       |
        +----------------------------------------------+
        |
        | Deseja realmente deletar o Trapézio: v1 = ({Utils.formatarNumero(trapezio.getTr1().getX())},{Utils.formatarNumero(trapezio.getTr1().getY())}) | v2 = ({Utils.formatarNumero(trapezio.getTr2().getX())},{Utils.formatarNumero(trapezio.getTr2().getY())}) | v3 = ({Utils.formatarNumero(trapezio.getTr3().getX())},{Utils.formatarNumero(trapezio.getTr3().getY())}) | v4 = ({Utils.formatarNumero(trapezio.getTr4().getX())},{Utils.formatarNumero(trapezio.getTr4().getY())}), base menor = {Utils.formatarNumero(trapezio.getBMenor())} e base maior = {Utils.formatarNumero(trapezio.getBMaior())}?
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
            formas.deleta(trapezio)            
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