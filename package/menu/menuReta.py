from package.menu.utils import Utils, time
from package.maths.terms import Reta
from package.maths.formas import Formas

class MenuReta():
    
    def telaCriar():
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-2-2 |
        +----------------------------------------------+
        | Criação da Reta                              |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para se criar uma reta, os dois coeficientes |
        | (a,b) da equação da reta devem ser digitados |
        | separados por vírgula, são aceitos valores   |
        | inteiros ou decimais.                        |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 1,2                                      |
        | 2º) 1,2.4                                    |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | A,B - Criar a Reta                           |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        coordenadas = valores.split(',')

        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),2,MenuReta,'telaCriar')

        Utils.clearScreen()
        reta = Reta(coordenadas[0],coordenadas[1])
        MenuReta.telaCriado(reta)

    def telaCriado(reta):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-2-2-1 |
        +----------------------------------------------+
        | Reta criada com sucesso!                     |
        +----------------------------------------------+
        | Dados:
        |
        | - Coeficientes da reta: a = {Utils.formatarNumero(reta.getA())} e b = {Utils.formatarNumero(reta.getB())}
        | - Equação reta: y = {Utils.formatarNumero(reta.getA())}x + {Utils.formatarNumero(reta.getB())}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v':
            Utils.clearScreen() 
            MenuReta.telaCriar()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.opcaoNaoDisponivel()
            MenuReta.telaCriado(reta)

    def escolhaDaFigura():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        retas = formas.pegarPorTipo('Reta')
        for i, reta in enumerate(retas):
            if str(reta.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(reta.getNumero()))
                strLista = strLista + '        | ' + str(reta.getNumero()) + ') a = ' + str(reta.getA()) + ' | b = ' + str(reta.getB())
                if i != len(retas) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-3-1 |
        +----------------------------------------------+
        | Suas retas disponíveis são                   |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número da Reta Escolhida                 |
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
            Reta = formas.pegarPorTipoENumero('Reta',opcaoSelecionada)
            MenuReta.telaInterferencia(Reta)

    def telaInterferencia(Reta):
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-3-1-1 |
        +----------------------------------------------+
        | Interferência na Reta                        |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para verificar se um ponto está nessa reta   |
        | já criada e descobrir a sua distância para a |
        | mesma, é necessário passar as coordenadas    |
        | do ponto(x,y), sendo valores inteiros ou     |
        | decimais.                                    |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 1,2                                      |
        | 2º) 1,2.4                                    |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X,Y - Verificar Interferência na Reta        |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        coordenadas = valores.split(',')

        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen() 
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),2,MenuReta,'telaInterferencia')

        Utils.clearScreen()
        MenuReta.telaInterferido(coordenadas[0],coordenadas[1],Reta)

    def telaInterferido(xp,yp,Reta):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-3-1-2 |
        +----------------------------------------------+
        | Interferência verificada com sucesso!        |
        +----------------------------------------------+
        | Dados:
        |
        | - Coordenadas do ponto: ({Utils.formatarNumero(xp)},{Utils.formatarNumero(yp)})
        | - {Reta.estaNaReta(xp,yp)}
        | - {Reta.caculaDistancia(xp,yp)}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuReta.telaInterferencia()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()
            MenuReta.telaInterferencia(Reta)

    def atualizacao():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        retas = formas.pegarPorTipo('Reta')
        for i, reta in enumerate(retas):
            if str(reta.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(reta.getNumero()))
                strLista = strLista + '        | ' + str(reta.getNumero()) + ') a = ' + str(reta.getA()) + ' | b = ' + str(reta.getB())
                if i != len(retas) - 1:
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
        | Menu                                   0-5-2 |
        +----------------------------------------------+
        | Retas disponíveis para atualizar             |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número da Reta                           |
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
            reta = formas.pegarPorTipoENumero('Reta',opcaoSelecionada)
            MenuReta.telaNovosValores(reta)

    def telaNovosValores(reta):
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-2-1 |
        +----------------------------------------------+
        | Atualização da Reta                          |
        +----------------------------------------------+
        |                                              |
        | Por favor, passe os novos dados da reta      |
        | que será alterada (seus coeficientes, a e b),|
        | podendo ser valores inteiros ou decimais.    |
        |                                              |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | A,B - Atualizar a Reta                       |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen() 
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),2,MenuReta,'telaNovosValores')    

        Utils.clearScreen()
        reta.atualizar(coordenadas[0],coordenadas[1])
        Utils.verificaArea(reta.getArea(),MenuReta,'telaNovosValores')
        formas = Formas()
        formas.atualizar(reta)
        MenuReta.atualizado(reta)

    def atualizado(reta):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-2-2 |
        +----------------------------------------------+
        | Reta atualizada com sucesso!                 |
        +----------------------------------------------+
        | Dados da sua nova reta:                      |
        |                                              |
        | - Coeficientes da reta: a = {Utils.formatarNumero(reta.getA())} e b = {Utils.formatarNumero(reta.getB())}
        | - Equação reta: y = {Utils.formatarNumero(reta.getA())}x + {Utils.formatarNumero(reta.getB())}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuReta.telaNovosValores()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.opcaoNaoDisponivel()
            MenuReta.atualizado(reta)

    def delecao():
        Utils.clearScreen()
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        retas = formas.pegarPorTipo('Reta')
        for i, reta in enumerate(retas):
            if str(reta.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(reta.getNumero()))
                strLista = strLista + '        | ' + str(reta.getNumero()) + ') a = ' + str(reta.getA()) + ' | b = ' + str(reta.getB())
                if i != len(retas) - 1:
                    strLista = strLista + '\n'
        if strLista[-1:] == '\n':
            strLista = strLista[:-1]

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-6-2 |
        +----------------------------------------------+
        | Suas Retas disponíveis são                   |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número da Reta que será deletada         |
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
            reta = formas.pegarPorTipoENumero('Reta',opcaoSelecionada)
            MenuReta.confirmarDelecao(reta)

    def confirmarDelecao(reta):
        Utils.clearScreen()
        
        opcoesDisponiveis = {'S','s','N','n'}

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-6-2-1 |
        +----------------------------------------------+
        | Confirmação de deleção                       |
        +----------------------------------------------+
        |
        | Deseja realmente deletar a Reta: a = {Utils.formatarNumero(reta.getA())} e b = {Utils.formatarNumero(reta.getB())} ?
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
            formas.deleta(reta)            
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