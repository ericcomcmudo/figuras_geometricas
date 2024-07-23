from package.menu.utils import Utils, time
from package.maths.terms import Quadrado
from package.maths.formas import Formas

class MenuQuadrado():
    
    def telaCriar():
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-2-5 |
        +----------------------------------------------+
        | Criação de Quadrado                          |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para se criar um quadrado, digite as         |
        | coordenadas dos quatro vértices no formato   |
        | do ponto (x,y), sendo as primeiras           |
        | coordenadas dadas as do vértice superior     |
        | esquerdo, o segundo do vértice superior      |
        | direito, o próximo do vértice inferior       |
        | direito e o último do inferior esquerdo,     |
        | são aceitos valores inteiros ou decimais.    |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 1,2,2,4,2,6,7,1                          |
        | 2º) 1,2.6,2.6,4,2.6,6,7,1                    |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X1,Y1,X2,Y2,X3,Y3,X4,Y4 - Criar o Quadrado   |
        | VI - Voltar ao Menu Inicial                  |        
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen()
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),8,MenuQuadrado,'telaCriar')    

        Utils.clearScreen()
        quadrado = Quadrado(coordenadas[0],coordenadas[1],coordenadas[2],coordenadas[3],coordenadas[4],coordenadas[5],coordenadas[6],coordenadas[7])
        Utils.verificaArea(quadrado.getArea(),MenuQuadrado,'telaCriar')
        MenuQuadrado.telaCriado(quadrado)
    
    def telaCriado(quadrado):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-2-5-1 |
        +----------------------------------------------+
        | Quadrado criado com sucesso!                 |
        +----------------------------------------------+
        | Dados:                                       
        |                                              
        | - Medida dos lados: {Utils.formatarNumero(quadrado.getLado())}
        | - Área: {Utils.formatarNumero(quadrado.getArea())}
        | - Perímetro: {Utils.formatarNumero(quadrado.getPerimetro())}
        | - Coordenadas dos vértices são:
        |   v1 = ({Utils.formatarNumero(quadrado.getQ1().getX())},{Utils.formatarNumero(quadrado.getQ1().getY())}) | v2 = ({Utils.formatarNumero(quadrado.getQ2().getX())},{Utils.formatarNumero(quadrado.getQ2().getY())})
        |   v3 = ({Utils.formatarNumero(quadrado.getQ3().getX())},{Utils.formatarNumero(quadrado.getQ3().getY())}) | v4 = ({Utils.formatarNumero(quadrado.getQ4().getX())},{Utils.formatarNumero(quadrado.getQ4().getY())}).
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuQuadrado.telaCriar()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()
            MenuQuadrado.telaCriado(quadrado)

    def escolhaDaFigura():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        quadrados = formas.pegarPorTipo('Quadrado')
        for i, quadrado in enumerate(quadrados):
            if str(quadrado.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(quadrado.getNumero()))
                strLista = strLista + '        | ' + str(quadrado.getNumero()) + ') (x1,y1) = (' + str(quadrado.getQ1().getX()) +','+ str(quadrado.getQ1().getY()) + ') | (x2,y2) = (' + str(quadrado.getQ2().getX())+','+ str(quadrado.getQ2().getY()) + ') | (x3,y3) = (' + str(quadrado.getQ3().getX())+','+str(quadrado.getQ3().getY()) + ') | (x4,y4) = (' + str(quadrado.getQ4().getX()) + ',' + str(quadrado.getQ4().getY()) + ')'
                if i != len(quadrados) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '
            

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-3-4 |
        +----------------------------------------------+
        | Seus quadrados disponíveis são               |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Quadrado Escolhido             |
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
            Quadrado = formas.pegarPorTipoENumero('Quadrado',opcaoSelecionada)
            MenuQuadrado.telaInterferencia(Quadrado)
        

    def telaInterferencia():
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-3-4-1 |
        +----------------------------------------------+
        | Interferência no Quadrado                    |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para verificar onde um ponto está em relação |
        | a um quadrado já criado, é necessário passar |
        | as coordenadas do ponto(x,y), sendo valores  |
        | inteiros ou decimais.                        |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 1,2                                      |
        | 2º) 1,2.4                                    |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X,Y - Verificar Interferência no Quadrado    |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        coordenadas = valores.split(',')

        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen() 
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),2,MenuQuadrado,'telaInterferencia')

        Utils.clearScreen()
        MenuQuadrado.telaInterferido(coordenadas[0],coordenadas[1])

    def telaInterferido(xp,yp):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-3-4-2 |
        +----------------------------------------------+
        | Interferência verificada com sucesso!        |
        +----------------------------------------------+
        | Dados:
        |
        | - Coordenadas do ponto: ({Utils.formatarNumero(xp)},{Utils.formatarNumero(yp)})
        | - {Quadrado.verificaPosicao(xp,yp)}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v':
            Utils.clearScreen() 
            MenuQuadrado.telaInterferencia()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()
            MenuQuadrado.telaInterferencia(Quadrado)
    
    def atualizacao():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        quadrados = formas.pegarPorTipo('Quadrado')
        for i, quadrado in enumerate(quadrados):
            if str(quadrado.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(quadrado.getNumero()))
                strLista = strLista + '        | ' + str(quadrado.getNumero()) + ') (x1,y1) = (' + str(quadrado.getQ1().getX()) +','+ str(quadrado.getQ1().getY()) + ') | (x2,y2) = (' + str(quadrado.getQ2().getX())+','+ str(quadrado.getQ2().getY()) + ') | (x3,y3) = (' + str(quadrado.getQ3().getX())+','+str(quadrado.getQ3().getY()) + ') | (x4,y4) = (' + str(quadrado.getQ4().getX()) + ',' + str(quadrado.getQ4().getY()) + ')'
                if i != len(quadrados) - 1:
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
        | Menu                                   0-5-5 |
        +----------------------------------------------+
        | Quadrados disponíveis para atualizar         |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Quadrado                       |
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
            quadrado = formas.pegarPorTipoENumero('Quadrado',opcaoSelecionada)
            MenuQuadrado.telaNovosValores(quadrado)

    def telaNovosValores(quadrado):
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-5-1 |
        +----------------------------------------------+
        | Atualização do Quadrado                      |
        +----------------------------------------------+
        |                                              |
        | Por favor, passe os novos dados do quadrado  |
        | que será alterado (coordenadas dos quatro    |
        | vértices),podendo ser valores inteiros ou    |
        | decimais.                                    |
        |                                              |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X1,Y1,X2,Y2,X3,Y3,X4,Y4 - Atualizar o        |
        | Quadrado                                     |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen() 
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),8,MenuQuadrado,'telaNovosValores')    

        Utils.clearScreen()
        quadrado.atualizar(coordenadas[0],coordenadas[1],coordenadas[2],coordenadas[3],coordenadas[4],coordenadas[5],coordenadas[6],coordenadas[7])
        Utils.verificaArea(quadrado.getArea(),MenuQuadrado,'telaNovosValores')
        formas = Formas()
        formas.atualizar(quadrado)
        MenuQuadrado.atualizado(quadrado)

    def atualizado(quadrado):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-5-2 |
        +----------------------------------------------+
        | Quadrado atualizado com sucesso!             |
        +----------------------------------------------+
        | Dados do seu novo quadrado:                  |
        |                                              |
        | - Medida dos lados: {Utils.formatarNumero(quadrado.getLado())}
        | - Área: {Utils.formatarNumero(quadrado.getArea())}
        | - Perímetro: {Utils.formatarNumero(quadrado.getPerimetro())}
        | - Coordenadas dos vértices são:
        |   v1 = ({Utils.formatarNumero(quadrado.getQ1().getX())},{Utils.formatarNumero(quadrado.getQ1().getY())}) | v2 = ({Utils.formatarNumero(quadrado.getQ2().getX())},{Utils.formatarNumero(quadrado.getQ2().getY())})
        |   v3 = ({Utils.formatarNumero(quadrado.getQ3().getX())},{Utils.formatarNumero(quadrado.getQ3().getY())}) | v4 = ({Utils.formatarNumero(quadrado.getQ4().getX())},{Utils.formatarNumero(quadrado.getQ4().getY())}).
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuQuadrado.telaNovosValores()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.opcaoNaoDisponivel()
            MenuQuadrado.atualizado(quadrado)

    def delecao():
        Utils.clearScreen()
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        quadrados = formas.pegarPorTipo('Quadrado')
        for i, quadrado in enumerate(quadrados):
            if str(quadrado.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(quadrado.getNumero()))
                strLista = strLista + '        | ' + str(quadrado.getNumero()) + ') (x1,y1) = (' + str(quadrado.getQ1().getX()) +','+ str(quadrado.getQ1().getY()) + ') | (x2,y2) = (' + str(quadrado.getQ2().getX())+','+ str(quadrado.getQ2().getY()) + ') | (x3,y3) = (' + str(quadrado.getQ3().getX())+','+str(quadrado.getQ3().getY()) + ') | (x4,y4) = (' + str(quadrado.getQ4().getX()) + ',' + str(quadrado.getQ4().getY()) + ')'
                if i != len(quadrados) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-6-5 |
        +----------------------------------------------+
        | Seus Quadrados disponíveis são               |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Quadrado que será deletado     |
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
            quadrado = formas.pegarPorTipoENumero('Quadrado',opcaoSelecionada)
            MenuQuadrado.confirmarDelecao(quadrado)

    def confirmarDelecao(quadrado):
        Utils.clearScreen()
        
        opcoesDisponiveis = {'S','s','N','n'}

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-6-5-1 |
        +----------------------------------------------+
        | Confirmação de deleção                       |
        +----------------------------------------------+
        |
        | Deseja realmente deletar o Quadrado: v1 = ({Utils.formatarNumero(quadrado.getQ1().getX())},{Utils.formatarNumero(quadrado.getQ1().getY())}) | v2 = ({Utils.formatarNumero(quadrado.getQ2().getX())},{Utils.formatarNumero(quadrado.getQ2().getY())}) | v3 = ({Utils.formatarNumero(quadrado.getQ3().getX())},{Utils.formatarNumero(quadrado.getQ3().getY())}) | v4 = ({Utils.formatarNumero(quadrado.getQ4().getX())},{Utils.formatarNumero(quadrado.getQ4().getY())})?
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
            formas.deleta(quadrado)            
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