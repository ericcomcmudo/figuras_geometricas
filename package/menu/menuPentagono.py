from package.menu.utils import Utils, time
from package.maths.terms import Pentagono
from package.maths.formas import Formas

class MenuPentagono():
    
    def telaCriar():
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-2-9 |
        +----------------------------------------------+
        | Criação de Pentágono                         |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para se criar um pentágono, digite as        |
        | coordenadas dos cinco vértices no formato    |
        | do ponto (x,y), sendo as primeiras           |
        | coordenadas dadas as do vértice superior     |
        | e segue um a um para a direita, e por        |
        | último, dê também a dimensão do lado,        |
        | são aceitos valores inteiros ou decimais.    |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 1,2,3,4,5,6,7,8,9,10,11                  |
        | 2º) 0,0,1,0,1.30,0.95,0.72,1.76,-0.27,1.76,1 |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X1,Y1,X2,Y2,X3,Y3,X4,Y4,X5,Y5,Lado - Criar o |
        | Pentágono                                    | 
        | VI - Voltar ao Menu Inicial                  |        
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen()
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),11,MenuPentagono,'telaCriar')    

        Utils.clearScreen()
        pentagono = Pentagono(coordenadas[0],coordenadas[1],coordenadas[2],coordenadas[3],coordenadas[4],coordenadas[5],coordenadas[6],coordenadas[7],coordenadas[8],coordenadas[9],coordenadas[10])
        Utils.verificaArea(pentagono.getArea(),MenuPentagono,'telaCriar')
        MenuPentagono.telaCriado(pentagono)
    
    def telaCriado(pentagono):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-2-9-1 |
        +----------------------------------------------+
        | Pentágono criado com sucesso!                |
        +----------------------------------------------+
        | Dados:                                       |
        |                                              |
        | - Medida dos lados: {Utils.formatarNumero(pentagono.getLado())}
        | - Área: {Utils.formatarNumero(pentagono.getArea())}
        | - Perímetro: {Utils.formatarNumero(pentagono.getPerimetro())}
        | - Coordenadas dos vértices são:
        |   v1 = ({Utils.formatarNumero(pentagono.getP1().getX())},{Utils.formatarNumero(pentagono.getP1().getY())}) | v2 = ({Utils.formatarNumero(pentagono.getP2().getX())},{Utils.formatarNumero(pentagono.getP2().getY())})
        |   v3 = ({Utils.formatarNumero(pentagono.getP3().getX())},{Utils.formatarNumero(pentagono.getP3().getY())}) | v4 = ({Utils.formatarNumero(pentagono.getP4().getX())},{Utils.formatarNumero(pentagono.getP4().getY())}) 
        |   v5 = ({Utils.formatarNumero(pentagono.getP5().getX())},{Utils.formatarNumero(pentagono.getP5().getY())})
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v':
            Utils.clearScreen() 
            MenuPentagono.telaCriar()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()
            MenuPentagono.telaCriado(pentagono)

    def escolhaDaFigura():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        pentagonos = formas.pegarPorTipo('Pentágono')
        for i, pentagono in enumerate(pentagonos):
            if str(pentagono.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(pentagono.getNumero()))
                strLista = strLista + '        | ' + str(pentagono.getNumero()) + ') (x1,y1) = (' + str(pentagono.getP1().getX()) +','+ str(pentagono.getP1().getY()) + ') | (x2,y2) = (' + str(pentagono.getP2().getX())+','+ str(pentagono.getP2().getY()) + ') | (x3,y3) = (' + str(pentagono.getP3().getX())+','+str(pentagono.getP3().getY()) + ') | (x4,y4) = (' + str(pentagono.getP4().getX()) + ',' + str(pentagono.getP4().getY()) + ') | (x5,y5) = (' + str(pentagono.getP5().getX()) + ',' + str(pentagono.getP5().getY()) + ') | LADO = ' + str(pentagono.getLado())
                if i != len(pentagonos) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-3-8 |
        +----------------------------------------------+
        | Seus pentágonos disponíveis são              |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Pentágono Escolhido            |
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
            Pentagono = formas.pegarPorTipoENumero('Pentágono',opcaoSelecionada)
            MenuPentagono.telaInterferencia(Pentagono)

    def telaInterferencia(Pentagono):
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-3-8-1 |
        +----------------------------------------------+
        | Interferência no Pentágono                   |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para verificar onde um ponto está em relação |
        | a um pentágono já criado, é necessário passar|
        | as coordenadas do ponto(x,y), sendo valores  |
        | inteiros ou decimais.                        |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 1,2                                      |
        | 2º) 1,2.4                                    |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X,Y - Verificar Interferência no Pentágono   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        coordenadas = valores.split(',')

        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen() 
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),2,MenuPentagono,'telaInterferencia')

        Utils.clearScreen()
        MenuPentagono.telaInterferido(coordenadas[0],coordenadas[1],Pentagono)

    def telaInterferido(xp,yp,Pentagono):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-3-9-2 |
        +----------------------------------------------+
        | Interferência verificada com sucesso!        |
        +----------------------------------------------+
        | Dados:
        |
        | - Coordenadas do ponto: ({Utils.formatarNumero(xp)},{Utils.formatarNumero(yp)})
        | - {Pentagono.verificaPosicao(xp,yp)}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuPentagono.telaInterferencia()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()
            MenuPentagono.telaInterferencia(Pentagono)

    def atualizacao():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        pentagonos = formas.pegarPorTipo('Pentágono')
        for i, pentagono in enumerate(pentagonos):
            if str(pentagono.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(pentagono.getNumero()))
                strLista = strLista + '        | ' + str(pentagono.getNumero()) + ') (x1,y1) = (' + str(pentagono.getP1().getX()) +','+ str(pentagono.getP1().getY()) + ') | (x2,y2) = (' + str(pentagono.getP2().getX())+','+ str(pentagono.getP2().getY()) + ') | (x3,y3) = (' + str(pentagono.getP3().getX())+','+str(pentagono.getP3().getY()) + ') | (x4,y4) = (' + str(pentagono.getP4().getX()) + ',' + str(pentagono.getP4().getY()) + ') | (x5,y5) = (' + str(pentagono.getP5().getX()) + ',' + str(pentagono.getP5().getY()) + ') | LADO = ' + str(pentagono.getLado())
                if i != len(pentagonos) - 1:
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
        | Menu                                   0-5-9 |
        +----------------------------------------------+
        | Pentagonos disponíveis para atualizar        |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Pentágono                      |
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
            Pentagono = formas.pegarPorTipoENumero('Pentágono',opcaoSelecionada)
            MenuPentagono.telaNovosValores(Pentagono)

    def telaNovosValores(Pentagono):
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-9-1 |
        +----------------------------------------------+
        | Atualização do Pentágono                     |
        +----------------------------------------------+
        |                                              |
        | Por favor, passe os novos dados do pentágono |
        | que será alterado (coordenadas dos cinco     |
        | vértices e do lado),podendo ser valores      |
        | inteiros ou decimais.                        |
        |                                              |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X1,Y1,X2,Y2,X3,Y3,X4,Y4,X5,Y5 - Atualizar o  |
        | Pentágono.                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen() 
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),11,MenuPentagono,'telaNovosValores')    

        Utils.clearScreen()
        Pentagono.atualizar(coordenadas[0],coordenadas[1],coordenadas[2],coordenadas[3],coordenadas[4],coordenadas[5],coordenadas[6],coordenadas[7],coordenadas[8],coordenadas[9],coordenadas[10])
        Utils.verificaArea(Pentagono.getArea(),MenuPentagono,'telaNovosValores')
        formas = Formas()
        formas.atualizar(Pentagono)
        MenuPentagono.atualizado(Pentagono)

    def atualizado(pentagono):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-9-2 |
        +----------------------------------------------+
        | Pentágono atualizado com sucesso!            |
        +----------------------------------------------+
        | Dados do seu novo Pentágono:                 |
        |                                              |
        | - Medida dos lados: {Utils.formatarNumero(pentagono.getLado())}
        | - Área: {Utils.formatarNumero(pentagono.getArea())}
        | - Perímetro: {Utils.formatarNumero(pentagono.getPerimetro())}
        | - Coordenadas dos vértices são:
        |   v1 = ({Utils.formatarNumero(pentagono.getP1().getX())},{Utils.formatarNumero(pentagono.getP1().getY())}) | v2 = ({Utils.formatarNumero(pentagono.getP2().getX())},{Utils.formatarNumero(pentagono.getP2().getY())})
        |   v3 = ({Utils.formatarNumero(pentagono.getP3().getX())},{Utils.formatarNumero(pentagono.getP3().getY())}) | v4 = ({Utils.formatarNumero(pentagono.getP4().getX())},{Utils.formatarNumero(pentagono.getP4().getY())}) 
        |   v5 = ({Utils.formatarNumero(pentagono.getP5().getX())},{Utils.formatarNumero(pentagono.getP5().getY())})
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuPentagono.telaNovosValores()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.opcaoNaoDisponivel()
            MenuPentagono.atualizado(Pentagono)

    def delecao():
        Utils.clearScreen()
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        pentagonos = formas.pegarPorTipo('Pentágono')
        for i, pentagono in enumerate(pentagonos):
            if str(pentagono.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(pentagono.getNumero()))
                strLista = strLista + '        | ' + str(pentagono.getNumero()) + ') (x1,y1) = (' + str(pentagono.getP1().getX()) +','+ str(pentagono.getP1().getY()) + ') | (x2,y2) = (' + str(pentagono.getP2().getX())+','+ str(pentagono.getP2().getY()) + ') | (x3,y3) = (' + str(pentagono.getP3().getX())+','+str(pentagono.getP3().getY()) + ') | (x4,y4) = (' + str(pentagono.getP4().getX()) + ',' + str(pentagono.getP4().getY()) + ') | (x5,y5) = (' + str(pentagono.getP5().getX()) + ',' + str(pentagono.getP5().getY()) + ') | LADO = ' + str(pentagono.getLado())
                if i != len(pentagonos) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-6-9 |
        +----------------------------------------------+
        | Seus Pentágonos disponíveis são              |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Pentágono que será deletado    |
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
            pentagono = formas.pegarPorTipoENumero('Pentágono',opcaoSelecionada)
            MenuPentagono.confirmarDelecao(pentagono)

    def confirmarDelecao(pentagono):
        Utils.clearScreen()
        
        opcoesDisponiveis = {'S','s','N','n'}

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-6-9-1 |
        +----------------------------------------------+
        | Confirmação de deleção                       |
        +----------------------------------------------+
        |
        | Deseja realmente deletar o Pentágono: v1 = ({Utils.formatarNumero(pentagono.getP1().getX())},{Utils.formatarNumero(pentagono.getP1().getY())}) | v2 = ({Utils.formatarNumero(pentagono.getP2().getX())},{Utils.formatarNumero(pentagono.getP2().getY())}) | v3 = ({Utils.formatarNumero(pentagono.getP3().getX())},{Utils.formatarNumero(pentagono.getP3().getY())}) | v4 = ({Utils.formatarNumero(pentagono.getP4().getX())},{Utils.formatarNumero(pentagono.getP4().getY())}) | v5 = ({Utils.formatarNumero(pentagono.getP5().getX())},{Utils.formatarNumero(pentagono.getP5().getY())}) e lado = {Utils.formatarNumero(pentagono.getLado())}?
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
            formas.deleta(pentagono)            
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