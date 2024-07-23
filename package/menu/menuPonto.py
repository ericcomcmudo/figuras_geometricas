import sys
import time
from package.menu.utils import Utils
from package.maths.terms import Ponto
from package.maths.formas import Formas

class MenuPonto():
    
    def telaCriar():
        Utils.clearScreen()
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-2-1 |
        +----------------------------------------------+
        | Criação de Ponto                             |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para se criar um ponto as coordenadas (X,y)  |
        | devem ser digitadas separadas por vírgulas,  |
        | são aceitos valores inteiros ou decimais.    |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 1,2                                      |
        | 2º) 1,2.4                                    |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X,Y - Criar o Ponto                          |
        | VI - Voltar ao Menu Inicial                  |        
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),2,MenuPonto,'telaCriar')

        Utils.clearScreen()
        ponto = Ponto(coordenadas[0],coordenadas[1])
        MenuPonto.telaCriado(ponto)

    def telaCriado(ponto):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-2-1-1 |
        +----------------------------------------------+
        | Ponto criado com sucesso!                    |
        +----------------------------------------------+
        | Dados:
        |
        | - Coordenadas são: x = {Utils.formatarNumero(ponto.getX())} e y = {Utils.formatarNumero(ponto.getY())}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v':
            Utils.clearScreen() 
            MenuPonto.telaCriar()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()
            MenuPonto.telaCriado(ponto)
        
    def telaDistanciaEntrePontos(x, y, x1 = None, y1 = None):
        Utils.clearScreen()
        ponto = Ponto(float(x),float(y))

        if x1 == None:
            str = ponto.distanciaDaOrigem()
        else :
            str = ponto.distanciaEntrePontos(float(x1),float(y1))

        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-4-1 |
        +----------------------------------------------+
        | Distância verificada com sucesso!            |
        +----------------------------------------------+
        | Dados:                                       |
        |                                              |
        | - {str}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()
            if x1 == None:
                MenuPonto.telaDistanciaEntrePontos(x,y)
            else :
                MenuPonto.telaDistanciaEntrePontos(x,y,x1,y1)

    def atualizacao():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        pontos = formas.pegarPorTipo('Losango')
        for i, ponto in enumerate(pontos):
            if str(ponto.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(ponto.getNumero()))
                strLista = strLista + '        | ' + str(ponto.getNumero()) + ') (x,y) = (' + str(ponto.getX()) +','+ str(ponto.getY()) + ')'
                if i != len(pontos) - 1:
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
        | Menu                                   0-5-1 |
        +----------------------------------------------+
        | Pontos disponíveis para atualizar            |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Ponto                          |
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
            ponto = formas.pegarPorTipoENumero('Ponto',opcaoSelecionada)
            MenuPonto.telaNovosValores(ponto)

    def telaNovosValores(ponto):
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-1-1 |
        +----------------------------------------------+
        | Atualização do Ponto                         |
        +----------------------------------------------+
        |                                              |
        | Por favor, passe os novos dados do ponto     |
        | que será alterado (suas coordenadas),        |
        | podendo ser valores inteiros ou decimais.    |
        |                                              |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X,Y - Atualizar o Ponto                      |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen() 
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),2,MenuPonto,'telaNovosValores')    

        Utils.clearScreen()
        ponto.atualizar(coordenadas[0],coordenadas[1])
        Utils.verificaArea(ponto.getArea(),MenuPonto,'telaNovosValores')
        formas = Formas()
        formas.atualizar(ponto)
        MenuPonto.atualizado(ponto)

    def atualizado(ponto):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-1-2 |
        +----------------------------------------------+
        | Ponto atualizado com sucesso!                |
        +----------------------------------------------+
        | Dados do seu novo ponto:                   |
        |                                              |
        | - Coordenadas são: x = {Utils.formatarNumero(ponto.getX())} e y = {Utils.formatarNumero(ponto.getY())}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuPonto.telaNovosValores()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.opcaoNaoDisponivel()
            MenuPonto.atualizado(ponto)
                
    def delecao():
        Utils.clearScreen()
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        pontos = formas.pegarPorTipo('Ponto')
        for i, ponto in enumerate(pontos):
            if str(ponto.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(ponto.getNumero()))
                strLista = strLista + '        | ' + str(ponto.getNumero()) + ') x = ' + Utils.formatarNumero(ponto.getX()) + ' e y = ' + Utils.formatarNumero(ponto.getY())
                if i != len(pontos) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-6-1 |
        +----------------------------------------------+
        | Seus Pontos disponíveis são                  |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Ponto que será deletado        |
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
            Ponto = formas.pegarPorTipoENumero('Ponto',opcaoSelecionada)
            MenuPonto.confirmarDelecao(Ponto)

    def confirmarDelecao(Ponto):
        Utils.clearScreen()
        
        opcoesDisponiveis = {'S','s','N','n'}

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-6-1-1 |
        +----------------------------------------------+
        | Confirmação de deleção                       |
        +----------------------------------------------+
        |
        | Deseja realmente deletar o Ponto: (x = {Utils.formatarNumero(Ponto.getX())}, y = {Ponto.getY()}) ?
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
            formas.deleta(Ponto)            
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
            