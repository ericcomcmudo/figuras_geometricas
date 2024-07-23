from package.menu.utils import Utils, time
from package.maths.terms import Retangulo
from package.maths.formas import Formas

class MenuRetangulo():
    
    def telaCriar():
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-2-4 |
        +----------------------------------------------+
        | Criação de Retângulo                         |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para se criar um retângulo, digite as        |
        | coordenadas dos quatro vértices no formato   |
        | do ponto (X,Y), sendo as primeiras           |
        | coordenadas dadas as do vértice superior     |
        | esquerdo, o segundo do vértice superior      |
        | direito, o próximo do vértice inferior       |
        | direito e o último do inferior esquerdo,     |
        | são aceitos valores inteiros ou decimais.    |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 10,2,1,4,2,7,6,8                         |
        | 2º) 10,2.5,1,4,2.5,7,6,8                     |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X1,Y1,X2,Y2,X3,Y3,X4,Y4 - Criar o Retângulo  |
        | VI - Voltar ao Menu Inicial                  |        
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen()
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),8,MenuRetangulo,'telaCriar')    

        Utils.clearScreen()
        retangulo = Retangulo(coordenadas[0],coordenadas[1],coordenadas[2],coordenadas[3],coordenadas[4],coordenadas[5],coordenadas[6],coordenadas[7])
        Utils.verificaArea(retangulo.getArea(),MenuRetangulo,'telaCriar')
        MenuRetangulo.telaCriado(retangulo)

    def telaCriado(retangulo):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-2-4-1 |
        +----------------------------------------------+
        | Retângulo criado com sucesso!                |
        +----------------------------------------------+
        | Dados:
        |
        | - Medida da Base: {Utils.formatarNumero(retangulo.getBase())}
        | - Altura: {Utils.formatarNumero(retangulo.getAltura())}
        | - Área: {Utils.formatarNumero(retangulo.getArea())}
        | - Perímetro: {Utils.formatarNumero(retangulo.getPerimetro())}
        | - Coordenadas dos vértices são:
        |   v1 = ({Utils.formatarNumero(retangulo.getR1().getX())},{Utils.formatarNumero(retangulo.getR1().getY())}) | v2 = ({Utils.formatarNumero(retangulo.getR2().getX())},{Utils.formatarNumero(retangulo.getR2().getY())})
        |   v3 = ({Utils.formatarNumero(retangulo.getR3().getX())},{Utils.formatarNumero(retangulo.getR3().getY())}) | v4 = ({Utils.formatarNumero(retangulo.getR4().getX())},{Utils.formatarNumero(retangulo.getR4().getY())}).
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuRetangulo.telaCriar()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()
            MenuRetangulo.telaCriado(retangulo)

    def escolhaDaFigura():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        retangulos = formas.pegarPorTipo('Retângulo')
        for i, retangulo in enumerate(retangulos):
            if str(retangulo.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(retangulo.getNumero()))
                strLista = strLista + '        | ' + str(retangulo.getNumero()) + ') (x1,y1) = (' + str(retangulo.getR1().getX()) +','+ str(retangulo.getR1().getY()) + ') | (x2,y2) = (' + str(retangulo.getR2().getX())+','+ str(retangulo.getR2().getY()) + ') | (x3,y3) = (' + str(retangulo.getR3().getX())+','+str(retangulo.getR3().getY()) + ') | (x4,y4) = (' + str(retangulo.getR4().getX()) + ',' + str(retangulo.getR4().getY()) + ')'
                if i != len(retangulos) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-3-3 |
        +----------------------------------------------+
        | Seus retângulos disponíveis são              |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Retângulo Escolhido            |
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
            Retangulo = formas.pegarPorTipoENumero('Retângulo',opcaoSelecionada)
            MenuRetangulo.telaInterferencia(Retangulo)
        

    def telaInterferencia():
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-3-3-1 |
        +----------------------------------------------+
        | Interferência no Retângulo                   |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para verificar onde um ponto está em relação |
        | a um retângulo já criado, é necessário passar|
        | as coordenadas do ponto(x,y), sendo valores  |
        | inteiros ou decimais.                        |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 1,2                                      |
        | 2º) 1,2.4                                    |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X,Y - Verificar Interferência no Retângulo   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        coordenadas = valores.split(',')

        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen() 
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),2,MenuRetangulo,'telaInterferencia')

        Utils.clearScreen()
        MenuRetangulo.telaInterferido(coordenadas[0],coordenadas[1])

    def telaInterferido(xp,yp):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-3-3-2 |
        +----------------------------------------------+
        | Interferência verificada com sucesso!        |
        +----------------------------------------------+
        | Dados:
        |
        | - Coordenadas do ponto: ({Utils.formatarNumero(xp)},{Utils.formatarNumero(yp)})
        | - {Retangulo.verificaPosicao(xp,yp)}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v':
            Utils.clearScreen() 
            MenuRetangulo.telaInterferencia()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()
            MenuRetangulo.telaInterferencia(Retangulo)

    def atualizacao():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        retangulos = formas.pegarPorTipo('Retângulo')
        for i, retangulo in enumerate(retangulos):
            if str(retangulo.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(retangulo.getNumero()))
                strLista = strLista + '        | ' + str(retangulo.getNumero()) + ') (x1,y1) = (' + str(retangulo.getR1().getX()) +','+ str(retangulo.getR1().getY()) + ') | (x2,y2) = (' + str(retangulo.getR2().getX())+','+ str(retangulo.getR2().getY()) + ') | (x3,y3) = (' + str(retangulo.getR3().getX())+','+str(retangulo.getR3().getY()) + ') | (x4,y4) = (' + str(retangulo.getR4().getX()) + ',' + str(retangulo.getR4().getY()) + ')'
                if i != len(retangulos) - 1:
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
        | Menu                                   0-5-4 |
        +----------------------------------------------+
        | Retângulos disponíveis para atualizar        |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Retângulo                      |
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
            retangulo = formas.pegarPorTipoENumero('Retângulo',opcaoSelecionada)
            MenuRetangulo.telaNovosValores(retangulo)

    def telaNovosValores(retangulo):
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-4-1 |
        +----------------------------------------------+
        | Atualização do Retângulo                     |
        +----------------------------------------------+
        |                                              |
        | Por favor, passe os novos dados do retângulo |
        | que será alterado (coordenadas dos quatro    |
        | vértices),podendo ser valores inteiros ou    |
        | decimais.                                    |
        |                                              |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X1,Y1,X2,Y2,X3,Y3,X4,Y4 - Atualizar o        |
        | Retângulo                                    |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen() 
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),8,MenuRetangulo,'telaNovosValores')    

        Utils.clearScreen()
        retangulo.atualizar(coordenadas[0],coordenadas[1],coordenadas[2],coordenadas[3],coordenadas[4],coordenadas[5],coordenadas[6],coordenadas[7])
        Utils.verificaArea(retangulo.getArea(),MenuRetangulo,'telaNovosValores')
        formas = Formas()
        formas.atualizar(retangulo)
        MenuRetangulo.atualizado(retangulo)

    def atualizado(retangulo):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-4-2 |
        +----------------------------------------------+
        | Retângulo atualizado com sucesso!            |
        +----------------------------------------------+
        | Dados do seu novo Retângulo:                 |
        |                                              |
        | - Medida da Base: {Utils.formatarNumero(retangulo.getBase())}
        | - Altura: {Utils.formatarNumero(retangulo.getAltura())}
        | - Área: {Utils.formatarNumero(retangulo.getArea())}
        | - Perímetro: {Utils.formatarNumero(retangulo.getPerimetro())}
        | - Coordenadas dos vértices são:
        |   v1 = ({Utils.formatarNumero(retangulo.getR1().getX())},{Utils.formatarNumero(retangulo.getR1().getY())}) | v2 = ({Utils.formatarNumero(retangulo.getR2().getX())},{Utils.formatarNumero(retangulo.getR2().getY())})
        |   v3 = ({Utils.formatarNumero(retangulo.getR3().getX())},{Utils.formatarNumero(retangulo.getR3().getY())}) | v4 = ({Utils.formatarNumero(retangulo.getR4().getX())},{Utils.formatarNumero(retangulo.getR4().getY())}).
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuRetangulo.telaNovosValores()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.opcaoNaoDisponivel()
            MenuRetangulo.atualizado(retangulo)

    def delecao():
        Utils.clearScreen()
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        retangulos = formas.pegarPorTipo('Retângulo')
        for i, retangulo in enumerate(retangulos):
            if str(retangulo.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(retangulo.getNumero()))
                strLista = strLista + '        | ' + str(retangulo.getNumero()) + ') (x1,y1) = (' + str(retangulo.getR1().getX()) +','+ str(retangulo.getR1().getY()) + ') | (x2,y2) = (' + str(retangulo.getR2().getX())+','+ str(retangulo.getR2().getY()) + ') | (x3,y3) = (' + str(retangulo.getR3().getX())+','+str(retangulo.getR3().getY()) + ') | (x4,y4) = (' + str(retangulo.getR4().getX()) + ',' + str(retangulo.getR4().getY()) + ')'
                if i != len(retangulos) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-6-4 |
        +----------------------------------------------+
        | Seus Retângulos disponíveis são              |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Retângulo que será deletado    |
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
            retangulo = formas.pegarPorTipoENumero('Retângulo',opcaoSelecionada)
            MenuRetangulo.confirmarDelecao(retangulo)

    def confirmarDelecao(retangulo):
        Utils.clearScreen()
        
        opcoesDisponiveis = {'S','s','N','n'}

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-6-4-1 |
        +----------------------------------------------+
        | Confirmação de deleção                       |
        +----------------------------------------------+
        |
        | Deseja realmente deletar o Retângulo: v1 = ({Utils.formatarNumero(retangulo.getR1().getX())},{Utils.formatarNumero(retangulo.getR1().getY())}) | v2 = ({Utils.formatarNumero(retangulo.getR2().getX())},{Utils.formatarNumero(retangulo.getR2().getY())}) | v3 = ({Utils.formatarNumero(retangulo.getR3().getX())},{Utils.formatarNumero(retangulo.getR3().getY())}) | v4 = ({Utils.formatarNumero(retangulo.getR4().getX())},{Utils.formatarNumero(retangulo.getR4().getY())})?
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
            formas.deleta(retangulo)            
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
        