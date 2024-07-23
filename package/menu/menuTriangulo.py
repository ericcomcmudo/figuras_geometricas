from package.menu.utils import Utils, time
from package.maths.terms import Triangulo
from package.maths.formas import Formas

class MenuTriangulo():
    
    def telaCriar():
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-2-6 |
        +----------------------------------------------+
        | Criação de Triângulo                         |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para se criar um triângulo, digite as        |
        | coordenadas dos três vértices no formato     |
        | do ponto (x,y), são aceitos valores          |
        | inteiros ou decimais.                        |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 0,0,4,0,2,3                              |
        | 2º) 0,0,4,0,2.5,3                            |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X1,Y1,X2,Y2,X3,Y3 - Criar o Triângulo        |
        | VI - Voltar ao Menu Inicial                  |        
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen()
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),6,MenuTriangulo,'telaCriado')    

        Utils.clearScreen()
        triangulo = Triangulo(coordenadas[0],coordenadas[1],coordenadas[2],coordenadas[3],coordenadas[4],coordenadas[5])
        Utils.verificaArea(triangulo.getArea(),MenuTriangulo,'telaCriar')

        if triangulo.ehPossivel() == False:
            formas = Formas()
            formas.deleta(triangulo)      
            MenuTriangulo.telaCriar()
        
        MenuTriangulo.telaCriado(triangulo)

    
    def telaCriado(triangulo):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-2-6-1 |
        +----------------------------------------------+
        | Triângulo criado com sucesso!                |
        +----------------------------------------------+
        | Dados:                                       
        |                                        
        | - Tipo: {triangulo.getTipo()}
        | - Medida da Base: {triangulo.getBase():.2f}
        | - Altura: {triangulo.getAltura():.2f}
        | - Área: {triangulo.getArea():.2f}
        | - Perímetro: {triangulo.getPerimetro():.2f}
        | - Coordenadas dos vértices são:
        |   v1 = ({triangulo.getT1().getX():.2f},{triangulo.getT1().getY():.2f}) | v2 = ({triangulo.getT2().getX():.2f},{triangulo.getT2().getY():.2f})
        |   v3 = ({triangulo.getT3().getX():.2f},{triangulo.getT3().getY():.2f})
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuTriangulo.telaCriar()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.clearScreen()
            Utils.opcaoNaoDisponivel()            
            MenuTriangulo.telaCriado(triangulo)

    def escolhaDaFigura():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        triangulos = formas.pegarPorTipo('Triângulo')
        for i, triangulo in enumerate(triangulos):
            if str(triangulo.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(triangulo.getNumero()))
                strLista = strLista + '        | ' + str(triangulo.getNumero()) + ') (x1,y1) = (' + str(triangulo.getT1().getX()) +','+ str(triangulo.getT1().getY()) + ') | (x2,y2) = (' + str(triangulo.getT2().getX())+','+ str(triangulo.getT2().getY()) + ') | (x3,y3) = (' + str(triangulo.getT3().getX())+','+str(triangulo.getT3().getY()) + ')'
                if i != len(triangulos) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-3-5 |
        +----------------------------------------------+
        | Seus triângulos disponíveis são              |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Triângulo Escolhido            |
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
            Triangulo = formas.pegarPorTipoENumero('Triângulo',opcaoSelecionada)
            MenuTriangulo.telaInterferencia(Triangulo)
        

    def telaInterferencia():
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-3-5-1 |
        +----------------------------------------------+
        | Interferência no Triângulo                   |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para verificar onde um ponto está em relação |
        | a um triângulo já criado, é necessário passar|
        | as coordenadas do ponto(x,y), sendo valores  |
        | inteiros ou decimais.                        |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 1,2                                      |
        | 2º) 1,2.4                                    |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X,Y - Verificar Interferência no Triângulo     |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        coordenadas = valores.split(',')

        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),2,MenuTriangulo,'telaInterferencia')

        Utils.clearScreen()
        MenuTriangulo.telaInterferido(coordenadas[0],coordenadas[1])

    def telaInterferido(xp,yp):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-3-5-2 |
        +----------------------------------------------+
        | Interferência verificada com sucesso!        |
        +----------------------------------------------+
        | Dados:
        |
        | - Coordenadas do ponto: ({Utils.formatarNumero(xp)},{Utils.formatarNumero(yp)})
        | - {Triangulo.verificaPosicao(xp,yp)}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')

        if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
            Utils.clearScreen()
            MenuTriangulo.telaInterferencia()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.opcaoNaoDisponivel()
            MenuTriangulo.telaInterferencia(Triangulo)

    def atualizacao():
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        triangulos = formas.pegarPorTipo('Triângulo')
        for i, triangulo in enumerate(triangulos):
            if str(triangulo.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(triangulo.getNumero()))
                strLista = strLista + '        | ' + str(triangulo.getNumero()) + ') (x1,y1) = (' + str(triangulo.getT1().getX()) +','+ str(triangulo.getT1().getY()) + ') | (x2,y2) = (' + str(triangulo.getT2().getX())+','+ str(triangulo.getT2().getY()) + ') | (x3,y3) = (' + str(triangulo.getT3().getX())+','+str(triangulo.getT3().getY()) + ')'
                if i != len(triangulos) - 1:
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
        | Menu                                   0-5-6 |
        +----------------------------------------------+
        | Triângulos disponíveis para atualizar        |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Triângulo                      |
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
            triangulo = formas.pegarPorTipoENumero('Triângulo',opcaoSelecionada)
            MenuTriangulo.telaNovosValores(triangulo)

    def telaNovosValores(triangulo):
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-6-1 |
        +----------------------------------------------+
        | Atualização do Triângulo                     |
        +----------------------------------------------+
        |                                              |
        | Por favor, passe os novos dados do triângulo |
        | que será alterado (coordenadas dos três      |
        | vértices), podendo ser valores inteiros      |
        | ou decimais.                                 |
        |                                              |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X1,Y1,X2,Y2,X3,Y3 - Atualizar o Triângulo    |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI':
            Utils.clearScreen() 
            Utils.menuInicial()

        coordenadas = Utils.verificaInputDeCoordenadas(valores.split(','),6,MenuTriangulo,'telaNovosValores')    

        Utils.clearScreen()
        triangulo.atualizar(coordenadas[0],coordenadas[1],coordenadas[2],coordenadas[3],coordenadas[4],coordenadas[5])
        Utils.verificaArea(triangulo.getArea(),MenuTriangulo,'telaNovosValores')
        formas = Formas()
        formas.atualizar(triangulo)
        MenuTriangulo.atualizado(triangulo)

    def atualizado(triangulo):
        Utils.clearScreen()        
        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-5-6-2 |
        +----------------------------------------------+
        | Triângulo atualizado com sucesso!            |
        +----------------------------------------------+
        | Dados do seu novo Triângulo:                 |
        |                                              |
        | - Tipo: {triangulo.getTipo()}
        | - Medida da Base: {triangulo.getBase():.2f}
        | - Altura: {triangulo.getAltura():.2f}
        | - Área: {triangulo.getArea():.2f}
        | - Perímetro: {triangulo.getPerimetro():.2f}
        | - Coordenadas dos vértices são:
        |   v1 = ({triangulo.getT1().getX():.2f},{triangulo.getT1().getY():.2f}) | v2 = ({triangulo.getT2().getX():.2f},{triangulo.getT2().getY():.2f})
        |   v3 = ({triangulo.getT3().getX():.2f},{triangulo.getT3().getY():.2f})
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
            MenuTriangulo.telaNovosValores()
        elif opcaoSelecionada == 'VI' or opcaoSelecionada == 'vi' or opcaoSelecionada == 'Vi'  or opcaoSelecionada == 'vI': 
            Utils.clearScreen()
            Utils.menuInicial()
        else:
            Utils.opcaoNaoDisponivel()
            MenuTriangulo.atualizado(triangulo)

    def delecao():
        Utils.clearScreen()
        opcoesDisponiveis = []
        strLista = ''
        formas = Formas()
        triangulos = formas.pegarPorTipo('Triângulo')
        for i, triangulo in enumerate(triangulos):
            if str(triangulo.getNumero()) not in opcoesDisponiveis:
                opcoesDisponiveis.append(str(triangulo.getNumero()))
                strLista = strLista + '        | ' + str(triangulo.getNumero()) + ') (x1,y1) = (' + str(triangulo.getT1().getX()) +','+ str(triangulo.getT1().getY()) + ') | (x2,y2) = (' + str(triangulo.getT2().getX())+','+ str(triangulo.getT2().getY()) + ') | (x3,y3) = (' + str(triangulo.getT3().getX())+','+str(triangulo.getT3().getY()) + ')'
                if i != len(triangulos) - 1:
                    strLista = strLista + '\n'
        if strLista != '' and strLista[-1:] == '\n':
            strLista = strLista[:-1]

        if strLista == '':
            strLista = '        | Nenhuma figura cadastrada. '

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                   0-6-6 |
        +----------------------------------------------+
        | Seus Triângulos disponíveis são              |
        +----------------------------------------------+
{strLista}
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | N - Número do Triângulo que será deletado    |
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
            triangulo = formas.pegarPorTipoENumero('Triângulo',opcaoSelecionada)
            MenuTriangulo.confirmarDelecao(triangulo)

    def confirmarDelecao(triangulo):
        Utils.clearScreen()
        
        opcoesDisponiveis = {'S','s','N','n'}

        opcaoSelecionada = input (f'''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                 0-6-6-1 |
        +----------------------------------------------+
        | Confirmação de deleção                       |
        +----------------------------------------------+
        |
        | Deseja realmente deletar o Triângulo: v1 = ({triangulo.getT1().getX():.2f},{triangulo.getT1().getY():.2f}) | v2 = ({triangulo.getT2().getX():.2f},{triangulo.getT2().getY():.2f}) | v3 = ({triangulo.getT3().getX():.2f},{triangulo.getT3().getY():.2f})?
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
            formas.deleta(triangulo)            
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