from package.menu.utils import Utils, time
from package.maths.terms import Circulo
from package.maths.formas import Formas


class MenuCirculo():
    
    def telaCriar():
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-2-3 |
        +----------------------------------------------+
        | Criação de Círculo                           |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para se criar um círculo, deve-se fornecer   |
        | as coordenadas do ponto de centro do círculo |
        | e o valor do raio (x,y,raio), podendo ser    |
        | valores inteiros ou decimais.                |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 3,4,4                                    |
        | 2º) 3,4.8,4                                  |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X,Y,RAIO - Criar o Círculo                   |
        | VI - Voltar ao Menu Inicial                  |        
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen() 
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),3,MenuCirculo,'telaCriar')

        Utils.clearScreen()
        circulo = Circulo(coordenadas[0],coordenadas[1],coordenadas[2])
        Utils.verificaArea(circulo.getArea(),MenuCirculo,'telaCriar')
        MenuCirculo.telaCriado(circulo)


    def telaCriado(circulo):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-2-3-1 |
        +----------------------------------------------+
        | Círculo criado com sucesso!                  |
        +----------------------------------------------+
        | Dados:
        |
        | - Coordenadas centro: ({Utils.formatarNumero(circulo.getX())},{Utils.formatarNumero(circulo.getY())})
        | - Raio: {Utils.formatarNumero(circulo.getRaio())}
        | - Circunferência: {Utils.formatarNumero(circulo.getCircunferencia())}
        | - Área: {Utils.formatarNumero(circulo.getArea())}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuCirculo.telaCriar()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.opcaoNaoDisponivel()
            MenuCirculo.telaCriado(circulo)

    def escolhaDaFigura():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        circulos = formas.pegarPorTipo('Círculo')
        for i, circulo in enumerate(circulos):
            if str(circulo.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(circulo.getNumero()))
                strLista = strLista + '        | ' + str(circulo.getNumero()) + ') X = ' + str(circulo.getX()) + ' | Y = ' + str(circulo.getY()) + ' | RAIO = ' + str(circulo.getRaio())
                if i != len(circulos) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-3-2 |
        +----------------------------------------------+
        | Seus círculos disponíveis são                |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Círculo Escolhido              |
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
            Circulo = formas.pegarPorTipoENumero('Círculo',opcaoSelecionada)
            MenuCirculo.telaInterferencia(Circulo)
        

    def telaInterferencia(Circulo):
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-3-2-1 |
        +----------------------------------------------+
        | Interferência no Círculo                     |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para verificar onde um ponto está em relação |
        | a esse círculo já criado, é necessário passar|
        | as coordenadas do ponto(x,y), sendo valores  |
        | inteiros ou decimais.                        |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 1,2                                      |
        | 2º) 1,2.4                                    |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X,Y - Verificar Interferência no Círculo     |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        coordenadas = valores.split(',')

        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen() 
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),2,MenuCirculo,'telaInterferencia')

        Utils.clearScreen()
        MenuCirculo.telaInterferido(coordenadas[0],coordenadas[1],Circulo)

    def telaInterferido(xp,yp,Circulo):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-3-2-2 |
        +----------------------------------------------+
        | Interferência verificada com sucesso!        |
        +----------------------------------------------+
        | Dados:
        |
        | - Coordenadas do ponto: ({Utils.formatarNumero(xp)},{Utils.formatarNumero(yp)})
        | - {Circulo.verificaPosicao(xp,yp)}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuCirculo.telaInterferencia()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()
            MenuCirculo.telaInterferencia(Circulo)

    def atualizacao():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        circulos = formas.pegarPorTipo('Círculo')
        for i, circulo in enumerate(circulos):
            if str(circulo.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(circulo.getNumero()))
                strLista = strLista + '        | - '  + str(circulo.getTipo()) + '(' + str(circulo.getNumero()) + ') : X = ' + str(circulo.getX()) + ' | Y = ' + str(circulo.getY()) + ' | RAIO = ' + str(circulo.getRaio())
                if i != len(circulos) - 1:
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
        | Menu                                   0-5-3 |
        +----------------------------------------------+
        | Círculos disponíveis para atualizar          |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Círculo                        |
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
            Circulo = formas.pegarPorTipoENumero('Círculo',opcaoSelecionada)
            MenuCirculo.telaNovosValores(Circulo)

    def telaNovosValores(Circulo):
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-3-1 |
        +----------------------------------------------+
        | Atualização do Círculo                       |
        +----------------------------------------------+
        |                                              |
        | Por favor, passe os novos dados do círculo   |
        | que será alterado (x,y,raio), podendo ser    |
        | valores inteiros ou decimais.                |
        |                                              |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X,Y,RAIO - Atualizar o Círculo               |
        | VI - Voltar ao Menu Inicial                  |        
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen() 
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),3,MenuCirculo,'telaNovosValores')

        Utils.clearScreen()
        Circulo.atualizar(coordenadas[0],coordenadas[1],coordenadas[2])
        Utils.verificaArea(Circulo.getArea(),MenuCirculo,'telaNovosValores')
        formas = Formas()
        formas.atualizar(Circulo)
        MenuCirculo.atualizado(Circulo)

    def atualizado(Circulo):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-3-2 |
        +----------------------------------------------+
        | Círculo atualizado com sucesso!              |
        +----------------------------------------------+
        | Dados do seu novo círculo:
        |
        | - Coordenadas centro: ({Utils.formatarNumero(Circulo.getX())},{Utils.formatarNumero(Circulo.getY())})
        | - Raio: {Utils.formatarNumero(Circulo.getRaio())}
        | - Circunferência: {Utils.formatarNumero(Circulo.getCircunferencia())}
        | - Área: {Utils.formatarNumero(Circulo.getArea())}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuCirculo.telaNovosValores()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.opcaoNaoDisponivel()
            MenuCirculo.atualizado(Circulo)

    def delecao():
        Utils.clearScreen()
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        circulos = formas.pegarPorTipo('Círculo')
        for i, circulo in enumerate(circulos):
            if str(circulo.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(circulo.getNumero()))
                strLista = strLista + '        | - '  + str(circulo.getTipo()) + '(' + str(circulo.getNumero()) + ') : X = ' + str(circulo.getX()) + ' | Y = ' + str(circulo.getY()) + ' | RAIO = ' + str(circulo.getRaio())
                if i != len(circulos) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-6-3 |
        +----------------------------------------------+
        | Seus Círculos disponíveis são                |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Círculo que será deletado      |
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
            circulo = formas.pegarPorTipoENumero('Círculo',opcaoSelecionada)
            MenuCirculo.confirmarDelecao(circulo)

    def confirmarDelecao(circulo):
        Utils.clearScreen()
        
        opcoesDisponiveis = {'S','s','N','n'}

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-6-3-1 |
        +----------------------------------------------+
        | Confirmação de deleção                       |
        +----------------------------------------------+
        |
        | Deseja realmente deletar o Círculo: (x,y) = ({Utils.formatarNumero(circulo.getX())},{Utils.formatarNumero(circulo.getY())}) e raio = {Utils.formatarNumero(circulo.getRaio())}?
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
            formas.deleta(circulo)            
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