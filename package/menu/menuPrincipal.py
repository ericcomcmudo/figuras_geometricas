import time
from package.menu.menuPonto import MenuPonto
from package.menu.menuReta import MenuReta
from package.menu.menuCirculo import MenuCirculo
from package.menu.menuRetangulo import MenuRetangulo
from package.menu.menuQuadrado import MenuQuadrado
from package.menu.menuTriangulo import MenuTriangulo
from package.menu.menuLosango import MenuLosango
from package.menu.menuTrapezio import MenuTrapezio
from package.menu.menuPentagono import MenuPentagono
from package.menu.utils import Utils
from package.maths.formas import Formas
#from package.maths.terms import Circulo
#from package.maths.terms import Triangulo
#from package.maths.terms import Reta
#from package.maths.terms import Quadrado
#from package.maths.terms import Pentagono
#from package.maths.terms import TrapezioRet
#from package.maths.terms import Losango
#from package.maths.terms import Retangulo

class Menu():    

    def printMenuInicial(self):
        opcoe = {'1','2','3','4','5','6','7', 'aa', 'AA', 'Aa', 'aA'}
        Utils.clearScreen()
        while True:
            opcaoSelecionada = input ('''
            +----------------------------------------------+
            | PLANO CARTESIANO                    | v 1.0b |
            +----------------------------------------------+
            | Menu                                       0 |
            +----------------------------------------------+
            | Opções                                       |
            +----------------------------------------------+
            | 1 - Ver figuras disponíveis.                 |
            | 2 - Criar Forma.                             |
            | 3 - Checar interferências.                   |
            | 4 - Checar distância entre pontos.           |
            | 5 - Atualizar Forma.                         |
            | 6 - Deletar Forma.                           |
            | 7 - Ver minhas figuras.                      |
            | X - Sair do Programa.                        |
            | AA - Autor                                   |        
            +----------------------------------------------+
            Digite uma das opções: ''')
        
            if opcaoSelecionada == 'X' or opcaoSelecionada == 'x':
                Utils.sair()

            if opcaoSelecionada == 'AA' or opcaoSelecionada == 'Aa' or opcaoSelecionada == 'aA' or opcaoSelecionada == 'aa': 
                Utils.autor()

            if opcaoSelecionada not in opcoe:
                Utils.opcaoNaoDisponivel()               
                self.printMenuInicial()

            elif opcaoSelecionada == '1':
                Utils.clearScreen() 
                self.printMenuUm()
            elif opcaoSelecionada == '2':
                Utils.clearScreen()
                self.printMenuDois()
            elif opcaoSelecionada == '3':
                Utils.clearScreen()
                self.printMenuTres()
            elif opcaoSelecionada == '4':
                Utils.clearScreen()
                self.printMenuQuatro()
            elif opcaoSelecionada == '5':
                Utils.clearScreen()
                self.printMenuCinco()
            elif opcaoSelecionada == '6':
                Utils.clearScreen()
                self.printMenuSeis()
            elif opcaoSelecionada == '7':
                Utils.clearScreen()
                self.printMenuSete()

    def printMenuUm(self):
        opcaoSelecionada = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                     0-1 |
        +----------------------------------------------+
        | Figuras disponíveis                          |
        +----------------------------------------------+
        | - Ponto.                                     |
        | - Reta.                                      |
        | - Círculo.                                   |
        | - Retângulo.                                 |
        | - Quadrado.                                  |
        | - Triângulos.                                |
        | - Trapézio.                                  |
        | - Losango.                                   |
        | - Pentágono.                                 |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | V - Voltar                                   |
        +----------------------------------------------+
        Digite uma das opções: ''')

        if opcaoSelecionada == 'V' or  opcaoSelecionada == 'v': 
            self.printMenuInicial()
        else:
            Utils.opcaoNaoDisponivel()
            self.printMenuUm()

    def printMenuDois(self):
        opcoe = {'1','2','3','4','5','6','7','8','9'}

        opcaoSelecionada = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                     0-2 |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | 1 - Criar Ponto.                             |
        | 2 - Criar Reta.                              |
        | 3 - Criar Círculo.                           |
        | 4 - Criar Retângulo.                         |
        | 5 - Criar Quadrado.                          |
        | 6 - Criar Triângulos.                        |
        | 7 - Criar Losango.                           |
        | 8 - Criar Trapézio.                          |
        | 9 - Criar Pentágono.                         |
        | V - Voltar.                                  |
        +----------------------------------------------+
        Digite uma das opções: ''')
        
        if opcaoSelecionada == 'V' or  opcaoSelecionada == 'v': 
            self.printMenuInicial()
                
        if opcaoSelecionada not in opcoe:
            Utils.opcaoNaoDisponivel()
            self.printMenuDois()

        if opcaoSelecionada == '1':            
            Utils.clearScreen()
            MenuPonto.telaCriar()

        if opcaoSelecionada == '2':
            Utils.clearScreen()
            MenuReta.telaCriar()

        if opcaoSelecionada == '3':
            Utils.clearScreen()
            MenuCirculo.telaCriar()

        if opcaoSelecionada == '4':
            Utils.clearScreen()
            MenuRetangulo.telaCriar()

        if opcaoSelecionada == '5':
            Utils.clearScreen()
            MenuQuadrado.telaCriar()

        if opcaoSelecionada == '6':
            Utils.clearScreen()
            MenuTriangulo.telaCriar()

        if opcaoSelecionada == '7':
            Utils.clearScreen()
            MenuLosango.telaCriar()

        if opcaoSelecionada == '8':
            Utils.clearScreen()
            MenuTrapezio.telaCriar()

        if opcaoSelecionada == '9':
            Utils.clearScreen()
            MenuPentagono.telaCriar()

    def printMenuTres(self):
        opcoe = {'1','2','3','4','5','6','7','8'}
        Utils.clearScreen()
        while True:
            opcaoSelecionada = input ('''
            +----------------------------------------------+
            | PLANO CARTESIANO                    | v 1.0b |
            +----------------------------------------------+
            | Menu                                     0-3 |
            +----------------------------------------------+
            | Opções                                       |
            +----------------------------------------------+
            | 1 - Interferências na Reta.                  |
            | 2 - Interferências no Círculo.               |
            | 3 - Interferências na Retângulo.             |
            | 4 - Interferências no Quadrado.              |
            | 5 - Interferências na Triângulo.             |
            | 6 - Interferências no Losango.               |
            | 7 - Interferências no Trapézio               |
            | 8 - Interferências no Pentágono.             |
            | V - Voltar                                   |
            +----------------------------------------------+
            Digite uma das opções: ''')
        
            if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
                self.printMenuInicial()

            if opcaoSelecionada not in opcoe:
                Utils.opcaoNaoDisponivel()               
                self.printMenuTres()

            elif opcaoSelecionada == '1':
                Utils.clearScreen() 
                MenuReta.escolhaDaFigura()

            if opcaoSelecionada == '2':
                Utils.clearScreen()
                MenuCirculo.escolhaDaFigura()

            if opcaoSelecionada == '3':
                Utils.clearScreen()
                MenuRetangulo.escolhaDaFigura()

            if opcaoSelecionada == '4':
                Utils.clearScreen()
                MenuQuadrado.escolhaDaFigura()

            if opcaoSelecionada == '5':
                Utils.clearScreen()
                MenuTriangulo.escolhaDaFigura()

            if opcaoSelecionada == '6':
                Utils.clearScreen()
                MenuLosango.escolhaDaFigura()

            if opcaoSelecionada == '7':
                Utils.clearScreen()
                MenuTrapezio.escolhaDaFigura()

            if opcaoSelecionada == '8':
                Utils.clearScreen()
                MenuPentagono.escolhaDaFigura()
        
    def printMenuQuatro(self):
        valores = input ('''
        +----------------------------------------------+
        | PLANO CARTESIANO                    | v 1.0b |
        +----------------------------------------------+
        | Menu                                     0-4 |
        +----------------------------------------------+
        | Checar distância entre pontos                |
        +----------------------------------------------+
        | Instruções:                                  |
        |                                              |
        | Para checar a distância entre pontos deve-se |
        | informar a coordenada (x,y) dos pontos. Caso |
        | queira verificar a distância do ponto com a  |
        | origem, deve-se informar a coordenada apenas |
        | de um único ponto                            |
        |                                              |
        | Exemplos de input:                           |
        | 1º) 3,4,4,8 (entre dois pontos)              |
        | 2º) 2,2,4,8.2 (entre dois pontos)            |
        | 3º) 2,2 (do pontos a origem)                 |
        | 4º) 8.9,5 (do pontos a origem)               |
        +----------------------------------------------+
        | Opções                                       |
        +----------------------------------------------+
        | X,Y,X2,Y2 - Distância entre dois pontos      |
        | X,Y - Distência do ponto a origem            |
        | VI - Voltar ao Menu Inicial                  |
        +----------------------------------------------+
        Digite a opção desejada: ''')
        
        if valores == 'VI' or valores == 'vi' or valores == 'Vi'  or valores == 'vI': 
            Utils.menuInicial()
        
        valores = valores.split(',')

        if len(valores) not in [2, 4]:
            Utils.clearScreen()
            print(f'Deve-se fornecer dois ou quatro números separados por vírgula.')
            time.sleep(3)
            Utils.clearScreen()
            self.printMenuQuatro()
        else: 
            for value in valores:
                value = value.strip()
                if Utils.ehNumero(value) != True:
                    Utils.clearScreen()
                    print(f'O input possui valore(s) não numéricos. Tente novamente.')
                    time.sleep(3)
                    self.printMenuQuatro()
        
        if len(valores) == 2:
            MenuPonto.telaDistanciaEntrePontos(valores[0],valores[1])
        elif len(valores) == 4:
            MenuPonto.telaDistanciaEntrePontos(valores[0],valores[1],valores[2],valores[3])

    def printMenuCinco(self):
        opcoe = {'1','2','3','4','5','6','7','8','9'}
        Utils.clearScreen()
        while True:
            opcaoSelecionada = input ('''
            +----------------------------------------------+
            | PLANO CARTESIANO                    | v 1.0b |
            +----------------------------------------------+
            | Menu                                     0-5 |
            +----------------------------------------------+
            | Opçẽs                                        |
            +----------------------------------------------+
            | 1 - Atualizar um Ponto.                      |
            | 2 - Atualizar uma Reta.                      |
            | 3 - Atualizar um Círculo.                    |
            | 4 - Atualizar um Retângulo.                  |
            | 5 - Atualizar um Quadrado.                   |
            | 6 - Atualizar um Triângulo.                  |
            | 7 - Atualizar um Losango.                    |
            | 8 - Atualizar um Trapézio.                   |
            | 9 - Atualizar um Pentágono.                  |
            | V - Voltar                                   |
            +----------------------------------------------+
            Digite uma das opções: ''')
        
            if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
                self.printMenuInicial()

            if opcaoSelecionada not in opcoe:
                Utils.opcaoNaoDisponivel()               
                self.printMenuCinco()

            elif opcaoSelecionada == '1':
                Utils.clearScreen() 
                MenuPonto.atualizacao()

            if opcaoSelecionada == '2':
                Utils.clearScreen()
                MenuReta.atualizacao()

            if opcaoSelecionada == '3':
                Utils.clearScreen()
                MenuCirculo.atualizacao()

            if opcaoSelecionada == '4':
                Utils.clearScreen()
                MenuRetangulo.atualizacao()

            if opcaoSelecionada == '5':
                Utils.clearScreen()
                MenuQuadrado.atualizacao()

            if opcaoSelecionada == '6':
                Utils.clearScreen()
                MenuTriangulo.atualizacao()

            if opcaoSelecionada == '7':
                Utils.clearScreen()
                MenuLosango.atualizacao()

            if opcaoSelecionada == '8':
                Utils.clearScreen()
                MenuTrapezio.atualizacao()

            if opcaoSelecionada == '9':
                Utils.clearScreen()
                MenuPentagono.atualizacao()


    def printMenuSeis(self):
        opcoe = {'1','2','3','4','5','6','7','8','9'}
        Utils.clearScreen()
        while True:
            opcaoSelecionada = input ('''
            +----------------------------------------------+
            | PLANO CARTESIANO                    | v 1.0b |
            +----------------------------------------------+
            | Menu                                     0-6 |
            +----------------------------------------------+
            | Opçẽs                                        |
            +----------------------------------------------+
            | 1 - Deletar um Ponto.                        |
            | 2 - Deletar uma Reta.                        |
            | 3 - Deletar um Círculo.                      |
            | 4 - Deletar um Retângulo.                    |
            | 5 - Deletar um Quadrado.                     |
            | 6 - Deletar um Triângulo.                    |
            | 7 - Deletar um Losango.                      |
            | 8 - Deletar um Trapézio.                     |
            | 9 - Deletar um Pentágono.                    |
            | V - Voltar                                   |
            +----------------------------------------------+
            Digite uma das opções: ''')
        
            if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
                self.printMenuInicial()

            if opcaoSelecionada not in opcoe:
                Utils.opcaoNaoDisponivel()               
                self.printMenuCinco()

            elif opcaoSelecionada == '1':
                Utils.clearScreen() 
                MenuPonto.delecao()

            if opcaoSelecionada == '2':
                Utils.clearScreen()
                MenuReta.delecao()

            if opcaoSelecionada == '3':
                Utils.clearScreen()
                MenuCirculo.delecao()

            if opcaoSelecionada == '4':
                Utils.clearScreen()
                MenuRetangulo.delecao()

            if opcaoSelecionada == '5':
                Utils.clearScreen()
                MenuQuadrado.delecao()

            if opcaoSelecionada == '6':
                Utils.clearScreen()
                MenuTriangulo.delecao()

            if opcaoSelecionada == '7':
                Utils.clearScreen()
                MenuLosango.delecao()

            if opcaoSelecionada == '8':
                Utils.clearScreen()
                MenuTrapezio.delecao()

            if opcaoSelecionada == '9':
                Utils.clearScreen()
                MenuPentagono.delecao()

    def printMenuSete(self):
        Utils.clearScreen()
        opcoesDisponiveisPonto = []
        opcoesDisponiveisReta = []
        opcoesDisponiveisCirculo = []
        opcoesDisponiveisRetangulo = []
        opcoesDisponiveisQuadrado = []
        opcoesDisponiveisTriangulo = []
        opcoesDisponiveisLosango = []
        opcoesDisponiveisTrapezio = []
        opcoesDisponiveisPentagono = []

        strPrincipal = ''
        formas = Formas()
        #ponto
        if formas.quantidadeDeFiguras('Ponto') > 0 :
            strLista = ''
            strPrincipal = strPrincipal + '            | Ponto(s): ' + '\n'
            pontos = formas.pegarPorTipo('Ponto')
            for i, ponto in enumerate(pontos):
                if str(ponto.getNumero()) not in opcoesDisponiveisPonto:
                    opcoesDisponiveisPonto.append(str(ponto.getNumero()))
                    strLista = strLista + '            | ' + str(ponto.getNumero()) + ') X = ' + str(ponto.getX()) + ' | Y = ' + str(ponto.getY())
                    if i != len(pontos) - 1:
                        strLista = strLista + '\n'
            if strLista[-1:] == '\n':
                strLista = strLista[:-1]
            strPrincipal = strPrincipal + strLista
        #reta
        if formas.quantidadeDeFiguras('Reta') > 0 :
            strLista = ''
            if strPrincipal == '':
                strPrincipal = strPrincipal + '            | Reta(s): ' + '\n'
            else:
                strPrincipal = strPrincipal + '\n            | Reta(s): ' + '\n'
            retas = formas.pegarPorTipo('Reta')
            for i, reta in enumerate(retas):
                if str(reta.getNumero()) not in opcoesDisponiveisReta:
                    opcoesDisponiveisReta.append(str(reta.getNumero()))
                    strLista = strLista + '            | ' + str(reta.getNumero()) + ') y = ' + Utils.formatarNumero(reta.getA()) + 'x + ' + Utils.formatarNumero(reta.getB())
                    if i != len(retas) - 1:
                        strLista = strLista + '\n'
            if strLista[-1:] == '\n':
                strLista = strLista[:-1]
            strPrincipal = strPrincipal + strLista
        #Círculo
        if formas.quantidadeDeFiguras('Círculo') > 0 :
            strLista = ''
            if strPrincipal == '':
                strPrincipal = strPrincipal + '            | Círculo(s): ' + '\n'
            else:
                strPrincipal = strPrincipal + '\n            | Círculo(s): ' + '\n'
            circulos = formas.pegarPorTipo('Círculo')
            for i, circulo in enumerate(circulos):
                if str(circulo.getNumero()) not in opcoesDisponiveisCirculo:
                    opcoesDisponiveisCirculo.append(str(circulo.getNumero()))
                    strLista = strLista + '            | ' + str(circulo.getNumero()) + ') X = ' + str(circulo.getX()) + ' | Y = ' + str(circulo.getY()) + ' | RAIO = ' + str(circulo.getRaio())
                    if i != len(circulos) - 1:
                        strLista = strLista + '\n'
            if strLista[-1:] == '\n':
                strLista = strLista[:-1]
            strPrincipal = strPrincipal + strLista
        #Retângulo
        if formas.quantidadeDeFiguras('Retângulo') > 0 :
            strLista = ''
            if strPrincipal == '':
                strPrincipal = strPrincipal + '            | Retângulo(s): ' + '\n'
            else:
                strPrincipal = strPrincipal + '\n            | Retângulo(s): ' + '\n'
            retangulos = formas.pegarPorTipo('Retângulo')
            for i, retangulo in enumerate(retangulos):
                if str(retangulo.getNumero()) not in opcoesDisponiveisRetangulo:
                    opcoesDisponiveisRetangulo.append(str(retangulo.getNumero()))
                    strLista = strLista + '            | ' + str(retangulo.getNumero()) + ') (x1,y1) = (' + str(retangulo.getR1().getX()) +','+ str(retangulo.getR1().getY()) + ') | (x2,y2) = (' + str(retangulo.getR2().getX())+','+ str(retangulo.getR2().getY()) + ') | (x3,y3) = (' + str(retangulo.getR3().getX())+','+str(retangulo.getR3().getY()) + ') | (x4,y4) = (' + str(retangulo.getR4().getX()) + ',' + str(retangulo.getR4().getY()) + ')'
                    if i != len(retangulos) - 1:
                        strLista = strLista + '\n'
            if strLista[-1:] == '\n':
                strLista = strLista[:-1]
            strPrincipal = strPrincipal + strLista
        #Quadrado
        if formas.quantidadeDeFiguras('Quadrado') > 0 :
            strLista = ''
            if strPrincipal == '':
                strPrincipal = strPrincipal + '            | Quadrado(s): ' + '\n'
            else:
                strPrincipal = strPrincipal + '\n            | Quadrado(s): ' + '\n'
            quadrados = formas.pegarPorTipo('Quadrado')
            for i, quadrado in enumerate(quadrados):
                if str(quadrado.getNumero()) not in opcoesDisponiveisQuadrado:
                    opcoesDisponiveisQuadrado.append(str(quadrado.getNumero()))
                    strLista = strLista + '            | ' + str(quadrado.getNumero()) + ') (x1,y1) = (' + str(quadrado.getQ1().getX()) +','+ str(quadrado.getQ1().getY()) + ') | (x2,y2) = (' + str(quadrado.getQ2().getX())+','+ str(quadrado.getQ2().getY()) + ') | (x3,y3) = (' + str(quadrado.getQ3().getX())+','+str(quadrado.getQ3().getY()) + ') | (x4,y4) = (' + str(quadrado.getQ4().getX()) + ',' + str(quadrado.getQ4().getY()) + ')'
                    if i != len(quadrados) - 1:
                        strLista = strLista + '\n'
            if strLista[-1:] == '\n':
                strLista = strLista[:-1]
            strPrincipal = strPrincipal + strLista
        #Triângulo
        if formas.quantidadeDeFiguras('Triângulo') > 0 :
            strLista = ''
            if strPrincipal == '':
                strPrincipal = strPrincipal + '            | Triângulo(s): ' + '\n'
            else:
                strPrincipal = strPrincipal + '\n            | Triângulo(s): ' + '\n'
            triangulos = formas.pegarPorTipo('Triângulo')
            for i, triangulo in enumerate(triangulos):
                if str(triangulo.getNumero()) not in opcoesDisponiveisTriangulo:
                    opcoesDisponiveisTriangulo.append(str(triangulo.getNumero()))
                    strLista = strLista + '            | ' + str(triangulo.getNumero()) + ') (x1,y1) = (' + str(triangulo.getT1().getX()) +','+ str(triangulo.getT1().getY()) + ') | (x2,y2) = (' + str(triangulo.getT2().getX())+','+ str(triangulo.getT2().getY()) + ') | (x3,y3) = (' + str(triangulo.getT3().getX())+','+str(triangulo.getT3().getY()) + ')'
                    if i != len(triangulos) - 1:
                        strLista = strLista + '\n'
            if strLista[-1:] == '\n':
                strLista = strLista[:-1]
            strPrincipal = strPrincipal + strLista
        #Losango
        if formas.quantidadeDeFiguras('Losango') > 0 :
            strLista = ''
            if strPrincipal == '':
                strPrincipal = strPrincipal + '            | Losango(s): ' + '\n'
            else:
                strPrincipal = strPrincipal + '\n            | Losango(s): ' + '\n'
            losangos = formas.pegarPorTipo('Losango')
            for i, losango in enumerate(losangos):
                if str(losango.getNumero()) not in opcoesDisponiveisLosango:
                    opcoesDisponiveisLosango.append(str(losango.getNumero()))
                    diagonal1 = diagonal1 = f'{losango.getD2():.2f}'
                    diagonal2 = f'{losango.getD1():.2f}'
                    strLista = strLista + '            | ' + str(losango.getNumero()) + ') (x1,y1) = (' + str(losango.getL1().getX()) +','+ str(losango.getL1().getY()) + ') | (x2,y2) = (' + str(losango.getL2().getX())+','+ str(losango.getL2().getY()) + ') | (x3,y3) = (' + str(losango.getL3().getX())+','+str(losango.getL3().getY()) + ') | (x4,y4) = (' + str(losango.getL4().getX()) + ',' + str(losango.getL4().getY()) + ') | Diagonal1 = ' + diagonal1 + ' | Diagonal2 = ' + diagonal2
                    if i != len(losangos) - 1:
                        strLista = strLista + '\n'
            if strLista[-1:] == '\n':
                strLista = strLista[:-1]
            strPrincipal = strPrincipal + strLista
        #Trapézio
        if formas.quantidadeDeFiguras('Trapézio') > 0 :
            strLista = ''
            if strPrincipal == '':
                strPrincipal = strPrincipal + '            | Trapézio(s): ' + '\n'
            else:
                strPrincipal = strPrincipal + '\n            | Trapézio(s): ' + '\n'
            trapezios = formas.pegarPorTipo('Trapézio')
            for i, trapezio in enumerate(trapezios):
                if str(trapezio.getNumero()) not in opcoesDisponiveisTrapezio:
                    opcoesDisponiveisTrapezio.append(str(trapezio.getNumero()))
                    strLista = strLista + '            | ' + str(trapezio.getNumero()) + ') (x1,y1) = (' + str(trapezio.getTr1().getX()) +','+ str(trapezio.getTr1().getY()) + ') | (x2,y2) = (' + str(trapezio.getTr2().getX())+','+ str(trapezio.getTr2().getY()) + ') | (x3,y3) = (' + str(trapezio.getTr3().getX())+','+str(trapezio.getTr3().getY()) + ') | (x4,y4) = (' + str(trapezio.getTr4().getX()) + ',' + str(trapezio.getTr4().getY()) + ') | BMAIOR = ' + str(trapezio.getBMaior()) + ' | BMENOR = ' + str(trapezio.getBMenor()) 
                    if i != len(trapezios) - 1:
                        strLista = strLista + '\n'
            if strLista[-1:] == '\n':
                strLista = strLista[:-1]
            strPrincipal = strPrincipal + strLista
        #Pentágono
        if formas.quantidadeDeFiguras('Pentágono') > 0 :
            strLista = ''
            if strPrincipal == '':
                strPrincipal = strPrincipal + '            | Pentágono(s): ' + '\n'
            else:
                strPrincipal = strPrincipal + '\n            | Pentágono(s): ' + '\n'
            pentagonos = formas.pegarPorTipo('Pentágono')
            for i, pentagono in enumerate(pentagonos):
                if str(trapezio.getNumero()) not in opcoesDisponiveisPentagono:
                    opcoesDisponiveisPentagono.append(str(pentagono.getNumero()))
                    strLista = strLista + '            | ' + str(pentagono.getNumero()) + ') (x1,y1) = (' + str(pentagono.getP1().getX()) +','+ str(pentagono.getP1().getY()) + ') | (x2,y2) = (' + str(pentagono.getP2().getX())+','+ str(pentagono.getP2().getY()) + ') | (x3,y3) = (' + str(pentagono.getP3().getX())+','+str(pentagono.getP3().getY()) + ') | (x4,y4) = (' + str(pentagono.getP4().getX()) + ',' + str(pentagono.getP4().getY()) + ') | (x5,y5) = (' + str(pentagono.getP5().getX()) + ',' + str(pentagono.getP5().getY()) + ') | LADO = ' + str(pentagono.getLado())
                    if i != len(pentagonos) - 1:
                        strLista = strLista + '\n'
            if strLista[-1:] == '\n':
                strLista = strLista[:-1]
            strPrincipal = strPrincipal + strLista

        if strPrincipal == '':
            strPrincipal = '            | Nenhuma figura cadastrada'
        while True:
            opcaoSelecionada = input (f'''
            +----------------------------------------------+
            | PLANO CARTESIANO                    | v 1.0b |
            +----------------------------------------------+
            | Menu                                     0-7 |
            +----------------------------------------------+
            | Minhas Figuras                               |
            +----------------------------------------------+
{strPrincipal}
            +----------------------------------------------+
            | Opções                                       |
            +----------------------------------------------+
            | V - Voltar
            +----------------------------------------------+
            Digite uma das opções: ''')
        
            if opcaoSelecionada == 'V' or opcaoSelecionada == 'v': 
                self.printMenuInicial()
            else :
                Utils.opcaoNaoDisponivel()               
                self.printMenuSete()

#    def printMenuOito(self):
#        formas = Formas()
#        valores = input ('''
#        +----------------------------------------------+
#        | PLANO CARTESIANO                    | v 1.0b |
#        +----------------------------------------------+
#        | Menu                                     0-4 |
#        +----------------------------------------------+
#        | Criar Forma dinamicamente                    |
#        +----------------------------------------------+
#        | Instruções:                                  |
#        |                                              |
#        | Para checar criar uma Forma dinamicamente    |
#        | informe a coordenada (x,y) dos pontos. Para  |
#        | que o software identifique a forma e a crie. |
#        | são aceitos valores inteiros ou decimais.    |
#        |                                              |
#        | Exemplos de input:                           |
#        | 1º - Reta) 2,3                               |
#        | 2º - Círculo) 3,4,4                          |
#        | 3º - Retângulo) 10,2,1,4,2,7,6,8             |
#        | 4º - Quadrado) 1,2,2,4,2,6,7,1               |
#        | 5º - Triângulo) 0,0,4,0,2,3                  |
#        | 6º - Losango) 0,0,2,2,4,0,2,-2               |
#        | 7º - Trapézio) 1,1,5,1,0,5,6,5               |
#        | 8º - Pentágono) 1,2,3,4,5,6,7,8,9,10,11      |
#        +----------------------------------------------+
#        | Opções                                       |
#        +----------------------------------------------+
#        | ?,?,?,?,?,?,?,?,?,?,? - Variáveis            |
#        | V - Voltar                                   |
#        +----------------------------------------------+
#        Digite a opção desejada: ''')
#
#        Utils.clearScreen()
#
#        if valores == 'V' or  valores == 'v': 
#            self.printMenuInicial()
#
#        valoresValidados = []
#        for value in valores.split(','):
#            value = value.strip()
#            if Utils.ehNumero(value) != True:
#                Utils.clearScreen()
#                print(f'O input possui valore(s) não numéricos. Tente novamente.')
#                time.sleep(3)
#                Utils.clearScreen()
#                self.printMenuOito()
#            else: 
#                value = float(value)
#                if value.is_integer():
#                    valoresValidados.append(float(value))
#                else:
#                    valoresValidados.append(float(value))
#        
#        if len(valoresValidados) > 11:
#            print(f'O input possui mais de 11 números. Tente novamente.')
#            time.sleep(3)
#            Utils.clearScreen()
#            self.printMenuOito()
#
#        if len(valoresValidados) == 11 : 
#            pentagono = Pentagono(valoresValidados[0],valoresValidados[1],valoresValidados[2],valoresValidados[3],valoresValidados[4],valoresValidados[5],valoresValidados[6],valoresValidados[7],valoresValidados[8],valoresValidados[9],valoresValidados[10])
#            if pentagono.getArea() == 0:
#                formas.deleta(pentagono)
#                Utils.verificaArea(pentagono.getArea(),Menu,'printMenuOito')
#            MenuPentagono.telaCriado(pentagono)
#        if len(valoresValidados) % 2 != 0 and ( len(valoresValidados) not in [3,6]): 
#            print(f'O input possui valore(s) não numéricos. Tente novamente.')
#            time.sleep(3)
#            Utils.clearScreen()
#            self.printMenuOito()
#        elif len(valoresValidados) % 2 != 0 and len(valoresValidados) == 3 :
#            circulo = Circulo(valoresValidados[0],valoresValidados[1],valoresValidados[2])
#            if circulo.getArea() == 0:
#                formas.deleta(circulo)
#                Utils.verificaArea(circulo.getArea(),Menu,'printMenuOito')
#            MenuCirculo.telaCriado(circulo)
#        elif len(valoresValidados) % 2 != 0 and len(valoresValidados) == 6 :
#            triangulo = Triangulo(valoresValidados[0],valoresValidados[1],valoresValidados[2],valoresValidados[3],valoresValidados[4],valoresValidados[5])
#            Utils.verificaArea(triangulo.getArea(),Menu,'printMenuOito')
#
#            if triangulo.ehPossivel() == False:
#                formas.deleta(triangulo)
#                Utils.clearScreen()
#                print(f'O Triângulo não é possível, pois um lado é maior que a soma dos outros dois. Tente novamente.')
#                time.sleep(3)
#                self.printMenuOito()
#            else :
#                MenuTriangulo.telaCriado(triangulo)
#        elif len(valoresValidados) == 2:
#            if valoresValidados[0] == valoresValidados[1] and valoresValidados[1] == 0:
#                print(f'Não é possível criar uma reta com as cordenadas X = 0 e Y = 0.')
#                time.sleep(3)
#                Utils.clearScreen()
#                self.printMenuOito()
#            else:
#                reta = Reta(valoresValidados[0],valoresValidados[1])
#                MenuReta.telaCriado(reta)
#        elif len(valoresValidados) == 4:
#            quadrado = Quadrado(valoresValidados[0],valoresValidados[1],valoresValidados[2],valoresValidados[3],valoresValidados[4],valoresValidados[5],valoresValidados[6],valoresValidados[7])
#            if quadrado.ehQUadrado() :
#                if quadrado.getArea() == 0:
#                    formas.deleta(quadrado)
#                    Utils.verificaArea(quadrado.getArea(),Menu,'printMenuOito')
#                MenuQuadrado.telaCriado(quadrado)
#            else :
#                formas.deleta(quadrado)
#
#            trapezio = TrapezioRet(valoresValidados[0],valoresValidados[1],valoresValidados[2],valoresValidados[3],valoresValidados[4],valoresValidados[5],valoresValidados[6],valoresValidados[7])
#
#            if trapezio.getEhReto() :
#                if trapezio.getArea() == 0:                    
#                    formas.deleta(trapezio)
#                    Utils.verificaArea(trapezio.getArea(),Menu,'printMenuOito')
#                else:                
#                    MenuTrapezio.telaCriado(trapezio)
#            else :
#                formas.deleta(trapezio)
#
#            losango = Losango(valoresValidados[0],valoresValidados[1],valoresValidados[2],valoresValidados[3],valoresValidados[4],valoresValidados[5],valoresValidados[6],valoresValidados[7])
#
#            if losango.verificaLosango() :
#                if losango.getArea() == 0:                    
#                    formas.deleta(losango)
#                    Utils.verificaArea(losango.getArea(),Menu,'printMenuOito')
#                else:                
#                    MenuLosango.telaCriado(losango)
#            else :
#                formas.deleta(losango)
#            
#            retangulo = Retangulo(valoresValidados[0],valoresValidados[1],valoresValidados[2],valoresValidados[3],valoresValidados[4],valoresValidados[5],valoresValidados[6],valoresValidados[7])
#
#            if retangulo.verificaLosango() :
#                if retangulo.getArea() == 0:                    
#                    formas.deleta(retangulo)
#                    Utils.verificaArea(retangulo.getArea(),Menu,'printMenuOito')
#                else:                
#                    MenuRetangulo.telaCriado(retangulo)
#            else :
#                formas.deleta(retangulo)