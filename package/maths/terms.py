from math import pi, sqrt, tan 
from package.maths.formas import Formas

numeroReta = 0
numeroCirculo = 0
numeroRetangulo = 0
numeroQuadrado = 0
numeroTriangulo = 0
numeroLosango = 0
numeroTrapezio = 0
numeroPentagono = 0

class Ponto():
    n = 0
    _x = 0
    _y = 0

    def __init__(self, x, y):  
        self._x = x
        self._y = y
        Ponto.n += 1
        self._n = Ponto.n
        forma = Formas()
        forma.adicionar(self)

    def setX(self, x):
        self._x = float(x)

    def setY(self, y):
        self._y = float(y)

    def getX(self):
        if self._x.is_integer():
            return int(self._x)
        return self._x
    
    def getY(self):
        if self._y.is_integer():
            return int(self._y)
        return self._y

    def toPrint(self):
        print(f'Eu sou o ponto e minhas coordenadas são: x = {self.getX()} e y = {self.getY()}')

    def atualizar(self, x=None, y=None):
        if x is not None:
            self.setX(x)
        if y is not None:
            self.setY(y)

    def distanciaEntrePontos(self, xp, yp):
        xp = float(xp)
        yp = float(yp)
        if xp.is_integer():
            xp = int(xp)
        if yp.is_integer():
            yp = int(yp)
        return (f'A distância do ponto ({self.getX()}, {self.getY()}) para o ponto ({xp}, {yp}) é {sqrt((xp - self.getX())**2 + (yp - self.getY())**2):.2f}')        

    def distanciaDaOrigem(self):
        return (f'A distância do ponto ({self.getX()}, {self.getY()}) para a origem (0, 0) é {sqrt(self.getX()**2+self.getY()**2):.2f}')

    def getTipo(self):
        return "Ponto"
    
    def getNumero(self):
        return self._n

class Reta(Ponto):
    _n = 0
    _a = 0
    _b = 0

    def __init__(self, a, b):
        global numeroReta
        numeroReta += 1
        super().__init__(a, b) 
        self._a = a
        self._b = b
        self._n = numeroReta
        forma = Formas()
        forma.adicionar(self)

    def setA(self, a):
        self._a = float(a)

    def setB(self, b):
        self._b = float(b)

    def interpolar(self, x):
        y = self._a * x + self._b
        return y
    
    def reta_ponto(self, xp, yp):
        return yp == self._a * xp + self._b

    def estaNaReta(self, xp, yp):
        if Reta.reta_ponto(self, xp, yp):
            return (f'O ponto está na reta y = {self._a}x + {self._b}.')
        else:
            return (f'O ponto não está na reta y = {self._a}x + {self._b}.')

    def toPrint(self):
        if self._a == self._b:
            print(f'Esta {self.getTipo()} não é possível de ser traçada.')
        else:
            print(f'Eu sou a {self.getTipo()} e meus parâmetros são: a = {self._a} e b = {self._b}')

    def atualizar(self, a=None, b=None):
        if a is not None:
            self.setA(a)
        if b is not None:
            self.setB(b)
    
    def caculaDistancia(self, xp, yp):
        if Reta.reta_ponto(self,xp,yp):
            return (f'Como o ponto ({xp}, {yp}) está na reta, a sua distância para a mesma é 0.')
        else:
            distancia = abs(self._a * xp - yp + self._b) / sqrt(self._a**2 + 1)
            return (f'A distância do ponto ({xp}, {yp}) é {distancia:.2f}')

    def getTipo(self):
        return "Reta"

    def getNumero(self):
        return self._n

    def getA(self):
        if self._a.is_integer():
            return int(self._a)
        return self._a
        
    def getB(self):
        if self._b.is_integer():
            return int(self._b)
        return self._b
    
class Circulo(Ponto):
    _n = 0
    _raio = 0
    _area = 0
    _x  = 0
    _y = 0
    _circunferencia = 0

    def __init__(self, x, y, raio):
        global numeroCirculo
        numeroCirculo += 1
        super().__init__(x, y)
        self._raio = raio
        self.calculaArea()
        self.calculaCircunferencia()
        self._n = numeroCirculo
        forma = Formas()
        forma.adicionar(self)

    def calculaArea(self):
        self._area = pi * self._raio ** 2
    
    def calculaCircunferencia(self):
        self._circunferencia = 2*pi*self._raio
    
    def setRaio(self, raio):
        self._raio = raio

    def toPrint(self):        
        if self._raio <= 0 or self._area <= 0:
            print(f'Este {self.getTipo()} não é possível')
        else:
            print(f'Eu sou o {self.getTipo()}, meu raio é {self.getRaio()}, minha circunferência é {self.getCircunferencia():.2f} e minha área é {self.getArea():.2f}.')
            print(f'As coordenadas do meu centro são x = {self._x} e y = {self._y}.')

    def getRaio(self):
        if self._raio.is_integer:
            return int(self._raio)
        return self._raio

    def getCircunferencia(self):
        if self._circunferencia.is_integer():
            return int(self._circunferencia)
        return self._circunferencia
    
    def getArea(self):
        if self._area.is_integer():
            return self._area
        return self._area

    def atualizar(self, x=None, y=None, raio=None):
        super().atualizar(x, y)
        if raio is not None:
            self.setRaio(raio)
        self.calculaArea()
        self.calculaCircunferencia()

    def circulo_ponto(self, xp, yp):
        return sqrt((xp - self._x)**2 + (yp - self._y)**2)

    def verificaPosicao(self, xp, yp):
        distancia = self.circulo_ponto(xp,yp)
        if distancia < self._raio:
            return (f'O ponto ({xp}, {yp}) está dentro do {self.getTipo()}.')
        elif distancia == self._raio:
            return (f'O ponto ({xp}, {yp}) está na borda do {self.getTipo()}.')
        else:
            return (f'O ponto ({xp}, {yp}) está fora do {self.getTipo()}.')

    def getTipo(self):
        return "Círculo"

    def getNumero(self):
        return self._n


class Retangulo(Ponto):
    _n = 0
    _r1 = Ponto
    _r2 = Ponto
    _r3 = Ponto
    _r4 = Ponto
    _base = 0
    _area = 0
    _perimetro = 0

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        global numeroRetangulo
        numeroRetangulo += 1
        self.setPontos(x1, y1, x2, y2, x3, y3, x4, y4)
        self._n = numeroRetangulo
        forma = Formas()
        forma.adicionar(self)
        

    def setPontos(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self._r1 = Ponto(x1, y1)
        self._r2 = Ponto(x2, y2)
        self._r3 = Ponto(x3, y3)
        self._r4 = Ponto(x4, y4)
        self.calculaAltura()
        self.calculaBase()
        self.calculaArea()
        self.calculaPerimetro()

    def calculaBase(self):
        self._base = abs(self._r3.getX() - self._r1.getX())

    def calculaAltura(self):
        self._altura = abs(self._r3.getY() - self._r1.getY())

    def calculaArea(self):
        self._area = self._base * self._altura

    def calculaPerimetro(self):
        self._perimetro = 2 * (self._base + self._altura)

    def getBase(self):
        return self._base

    def getAltura(self):
        return self._altura

    def getArea(self):
        return self._area

    def getPerimetro(self):
        return self._perimetro

    def getR1(self):
        return self._r1

    def getR2(self):
        return self._r2

    def getR3(self):
        return self._r3

    def getR4(self):
        return self._r3

    def toPrint(self):
        if self._area <= 0 or self._perimetro <= 0:            
            print('Este Retângulo não é possível')
        else:
            print(f'Eu sou o retângulo e minhas medidas são {self._base} de base, {self._altura} de altura, minha área é {self._area:.2f}, meu perímetro é {self._perimetro:.2f}.')
            print(f'As coordenadas dos meus vértices são: ({self._r1.getX()}, {self._r1.getY()}), ({self._r2.getX()}, {self._r2.getY()}), ({self._r3.getX()}, {self._r3.getY()}), ({self._r4.getX()}, {self._r4.getY()}).')

    def atualizar(self, x1=None, y1=None, x2=None, y2=None, x3=None, y3=None, x4=None, y4=None):
        if x1 is not None and y1 is not None and x2 is not None and y2 is not None and x3 is not None and y3 is not None and x4 is not None and y4 is not None:
            self.setPontos(x1, y1, x2, y2, x3, y3, x4, y4)

    def verificaPosicao(self, xp, yp):
        if self._r1.getX() < xp < self._r3.getX() and self._r1.getY() < yp < self._r3.getY():
            return (f'O ponto ({xp}, {yp}) está dentro do retângulo.')
        elif (self._r1.getX() <= xp <= self._r3.getX() and (yp == self._r1.getY() or yp == self._r3.getY())) or (self._r1.getY() <= yp <= self._r3.getY() and (xp == self._r1.getX() or xp == self._r3.getX())):
            return (f'O ponto ({xp}, {yp}) está na borda do retângulo.')
        else:
            return (f'O ponto ({xp}, {yp}) está fora do retângulo.')
            
    def getTipo(self):
        return "Retângulo"
    
    def getNumero(self):
        return self._n


class Quadrado(Ponto):
    _n = 0
    _q1 = Ponto
    _q2 = Ponto
    _q3 = Ponto
    _q4 = Ponto
    _lado = 0
    _area = 0
    _perimetro = 0
    _diagonais = 0

    def __init__(self, x1, y1, x2, y2, x3, y3, x4,y4):
        global numeroQuadrado
        numeroQuadrado += 1
        super().__init__(x1,y2)
        self.setPontos(x1, y1, x2, y2, x3,y3,x4,y4)
        self._n = numeroQuadrado
        forma = Formas()
        forma.adicionar(self)
    
    def setPontos(self, x1, y1, x2, y2, x3,y3,x4,y4):
        self._q1 = Ponto(x1, y1)
        self._q2 = Ponto(x2, y2)
        self._q3 = Ponto(x3, y3)
        self._q4 = Ponto(x4, y4)
        self.calculaLado()
        self.calculaArea()
        self.calculaPerimetro()
        self.calculaDiagonais()

    def distancia(self, p1, p2):
        return sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

    def ehQuadrado(self):
        d1 = self.distancia(self._q1, self._q2)
        d2 = self.distancia(self._q2, self._q3)
        d3 = self.distancia(self._q3, self._q4)
        d4 = self.distancia(self._q4, self._q1)
        
        return d1 == d2 == d3 == d4
    
    def calculaLado(self):
        self._lado = abs(self._q3.getX() - self._q1.getX())

    def calculaArea(self):
        self._area = self._lado ** 2

    def calculaPerimetro(self):
        self._perimetro = self._lado * 4

    def getLado(self):
        return self._lado

    def getArea(self):
        return self._area

    def getPerimetro(self):
        return self._perimetro

    def getQ1(self):
        return self._q1

    def getQ2(self):
        return self._q2

    def getQ3(self):
        return self._q3

    def getQ4(self):
        return self._q4

    def calculaDiagonais(self):
        self._diagonais = sqrt(2) * self._lado

    def toPrint(self):
        if self._area <= 0 or self._perimetro <= 0:
            print('Este Quadrado não é possível')
        else:
            print(f'Eu sou o quadrado e minhas medidas são {self._lado} em cada lado, minha área é {self._area:.2f}, meu perímetro é {self._perimetro:.2f}.')
            print(f'As coordenadas dos meus vértices são ({self._q1.getX()}, {self._q1.getY()}), ({self._q2.getX()}, {self._q2.getY()}).')

    def atualizar(self, x1=None, y1=None, x2=None, y2=None, x3=None, y3=None, x4=None, y4=None):
        if x1 is not None and y1 is not None and x2 is not None and y2 is not None and x3 is not None and y3 is not None and x4 is not None and y4 is not None:
            self.setPontos(x1, y1, x2, y2, x3, y3, x4, y4)

    def verificaPosicao(self, xp, yp):
        p = Ponto(xp, yp)
        if self.estaNaBorda(p):
            return (f"O ponto ({xp},{yp}) está na borda do Quadrado")
        elif self.estaDentro(p):
            return (f"O ponto ({xp},{yp}) está dentro do Quadrado")
        else:
            return (f"O ponto ({xp},{yp}) está fora do Quadrado")

    def estaNaBorda(self, ponto):
        x, y = ponto.getX(), ponto.getY()
        vertices = [self._q1, self._q2, self._q3, self._q4]
        for i in range(len(vertices)):
            p1 = vertices[i]
            p2 = vertices[(i + 1) % len(vertices)]
            if self.estaNoSegmento(x, y, p1.getX(), p1.getY(), p2.getX(), p2.getY()):
                return True
        return False

    def estaNoSegmento(self, px, py, ax, ay, bx, by):
        cross_product = (py - ay) * (bx - ax) - (px - ax) * (by - ay)
        if abs(cross_product) > 1e-6:  # Not on the line
            return False
        dot_product = (px - ax) * (bx - ax) + (py - ay) * (by - ay)
        if dot_product < 0:
            return False
        squared_length = (bx - ax) ** 2 + (by - ay) ** 2
        if dot_product > squared_length:
            return False
        return True

    def estaDentro(self, ponto):
        x = ponto.getX()
        y = ponto.getY()
        vertices = [self._q1, self._q2, self._q3, self._q4]
        n = len(vertices)
        inside = False
        p1x, p1y = vertices[0].getX(), vertices[0].getY()
        for i in range(n+1):
            p2x, p2y = vertices[i % n].getX(), vertices[i % n].getY()
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    def getTipo(self):
        return "Quadrado"
    
    def getNumero(self):
        return self._n


class Triangulo(Ponto):
    _n = 0
    _tipo = None
    _altura = 0
    _base = 0
    _area = 0
    _perimetro = 0
    _ladoA = 0
    _ladoB = 0
    _ladoC = 0

    def __init__(self, x1, y1, x2, y2, x3, y3):    
        global numeroTriangulo
        numeroTriangulo += 1    
        self.setPontos(x1, y1, x2, y2, x3, y3)
        self._n = numeroTriangulo
        forma = Formas()
        forma.adicionar(self)
        
    def calcula_distancia(self, x1, y1, x2, y2):
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def calcularPerimetro(self):
        self._perimetro = self._base + self._altura + sqrt(self._base ** 2 + self._altura ** 2)
    
    def setPontos(self,x1, y1, x2, y2, x3, y3):
        self._t1 = Ponto(x1,y1)
        self._t2 = Ponto(x2,y2)
        self._t3 = Ponto(x3,y3)
        self.calculaLados()
        self.calculaBase()
        self.calculaAltura()
        self.calcularPerimetro()
        self.calculaArea()
        self.verificaTipo()

    def ehPossivel(self):
        if self._ladoA + self._ladoB > self._ladoC and self._ladoA + self._ladoC > self._ladoB and self._ladoB + self._ladoC > self._ladoA:
            return True
        else:
            return False

    def calculaLados(self):
        self._ladoA = self.calcula_distancia(self._t1.getX(), self._t1.getY(), self._t2.getX(), self._t2.getY())
        self._ladoB = self.calcula_distancia(self._t2.getX(), self._t2.getY(), self._t3.getX(), self._t3.getY())
        self._ladoC = self.calcula_distancia(self._t3.getX(), self._t3.getY(), self._t1.getX(), self._t1.getY())

    def verificaTipo(self):
        if self._ladoA == self._ladoB == self._ladoC:
            self._tipo = 'Equilátero'
        elif self._ladoA == self._ladoB or self._ladoA == self._ladoC or self._ladoC == self._ladoB:
            self._tipo = 'Isósceles'
        elif self._t1.getX() == self._t2.getX() or self._t1.getX() == self._t3.getX() or self._t2.getX() == self._t3.getX():
            if self._t1.getY() == self._t2.getY() or self._t1.getY() == self._t3.getY() or self._t3.getY() == self._t2.getY():
                self._tipo = 'Retângulo'
        else:
            self._tipo = 'Escaleno'
        return self._tipo


    def calculaArea(self):
        self._area = (self._base * self._altura) / 2
    
    def calculaBase(self):
        self._base = self.calcula_distancia(self._t1.getX(), self._t1.getY(), self._t2.getX(), self._t2.getY())

    def calcularPerimetro(self):
        self._perimetro = self._base + self._altura + sqrt(self._base ** 2 + self._altura ** 2)

    def calculaAltura(self):
        if self._tipo == 'Retângulo':
            self._altura = self._ladoC
        elif self._tipo == 'Isósceles':
            if self._ladoA == self._ladoB or self._ladoA == self._ladoC:
                self._altura = sqrt(self._ladoA**2 - (self._base/2)**2)            
            else:
                self._altura = sqrt(self._ladoB**2 - (self._base/2)**2)
        else:
            self._altura = (sqrt(3) / 2) * self._ladoA
    
    def getArea(self):
        return self._area
    
    def getBase(self):
        return self._base

    def getPerimetro(self):
        return self._perimetro

    def getAltura(self):
        return self._altura

    def getT1(self):
        return self._t1

    def getT2(self):
        return self._t2

    def getT3(self):
        return self._t3

    def toPrint(self):
            print(f'Eu sou o triângulo {self._tipo}, minha base é {self._base}, minha altura é {self._altura}, minha área é {self._area:.2f}, meu perímetro é {self._perimetro:.2f}.')
            print(f'As coordenadas dos meus vértices são ({self._t1.getX()}, {self._t1.getY()}), ({self._t2.getX()}, {self._t2.getY()}), ({self._t3.getX()}, {self._t3.getY()}).')

    def atualizar(self, x1=None, y1=None, x2=None, y2=None, x3=None, y3=None):
        if x1 is not None and y1 is not None and x2 is not None and y2 is not None and x3 is not None and y3 is not None:
            self.setPontos(x1, y1, x2, y2, x3, y3)

    def verificaPosicao(self, xp, yp):
        area_total = self._area
        subtri1 = Triangulo(self._t1.getX(), self._t1.getY(), self._t2.getX(), self._t2.getY(), xp, yp)
        subtri2 = Triangulo(self._t2.getX(), self._t2.getY(), self._t3.getX(), self._t3.getY(), xp, yp)
        subtri3 = Triangulo(self._t3.getX(), self._t3.getY(), self._t1.getX(), self._t1.getY(), xp, yp)
        area_subtri = subtri1._area + subtri2._area + subtri3._area
        if abs(area_total - area_subtri) < 0.0001:
            return (f'O ponto ({xp},{yp}) está dentro do Triângulo {self._tipo}')
        elif area_subtri > area_total:
            return (f'O ponto ({xp},{yp}) está fora do Triângulo {self._tipo}') 
        else:
            return (f'O ponto ({xp},{yp}) está na borda do Triângulo {self._tipo}')

    def getTipo(self):
        return self._tipo
    
    def getNumero(self):
        return self._n

class Losango(Ponto):
    _n = 0
    _l1 = Ponto
    _l2 = Ponto
    _l3 = Ponto
    _l4 = Ponto
    _d1 = 0
    _d2 = 0
    _area = 0
    _perimetro = 0

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        global numeroLosango
        numeroLosango += 1
        super().__init__(x1,y1)
        self.setPontos(x1, y1, x2, y2, x3, y3, x4, y4)
        self._n = numeroLosango
        forma = Formas()
        forma.adicionar(self)

    def setPontos(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self._l1 = Ponto(x1, y1)
        self._l2 = Ponto(x2, y2)
        self._l3 = Ponto(x3, y3)
        self._l4 = Ponto(x4, y4)
        self._d1 = sqrt((x2 - x4) ** 2 + (y2 - y4) ** 2)
        self._d2 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
        self.calculaArea()
        self.calculaPerimetro()

    def distancia(self, p1, p2):
        return sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

    def is_angulo_reto(self, p1, p3, p2, p4):
        # Verifica se as diagonais são perpendiculares
        v1 = (p3.x - p1.x, p3.y - p1.y)
        v2 = (p4.x - p2.x, p4.y - p2.y)
        produto_escalar = v1[0] * v2[0] + v1[1] * v2[1]
        return produto_escalar == 0

    def verificaLosango(self):
        # Verifica se todos os lados são iguais
        lado1 = self.distancia(self._l1, self._l2)
        lado2 = self.distancia(self._l2, self._l3)
        lado3 = self.distancia(self._l3, self._l4)
        lado4 = self.distancia(self._l4, self._l1)
        lados_iguais = lado1 == lado2 == lado3 == lado4

        # Verifica se as diagonais se cruzam ao meio e são perpendiculares
        diagonais_cruzam_ao_meio = (self._l1.x + self._l3.x) / 2 == (self._l2.x + self._l4.x) / 2 and \
                                   (self._l1.y + self._l3.y) / 2 == (self._l2.y + self._l4.y) / 2
        diagonais_perpendiculares = self.is_angulo_reto(self._l1, self._l3, self._l2, self._l4)

        return lados_iguais and diagonais_cruzam_ao_meio and diagonais_perpendiculares

    def calculaArea(self):
        self._area = (self._d1 * self._d2) / 2

    def calculaPerimetro(self):
        self._perimetro = 2 * (self._d1 + self._d2)

    def getArea(self):
        return self._area

    def getPerimetro(self):
        return self._perimetro

    def getL1(self):
        return self._l1
    
    def getL2(self):
        return self._l2
    
    def getL3(self):
        return self._l3
    
    def getL4(self):
        return self._l4
    
    def getD1(self):
        return self._d1
    
    def getD2(self):
        return self._d2

    def toPrint(self):
        if self._area <= 0 or self._perimetro <= 0:
            print('Este Losango não é possível')
        else:
            print(f'Eu sou o losango, minhas diagonais são {self._d1} e {self._d2}, minha área é {self._area:.2f}, meu perímetro é {self._perimetro:.2f}.')
            print(f'As coordenadas dos meus vértices são ({self._l1.getX()}, {self._l1.getY()}), ({self._l2.getX()}, {self._l2.getY()}), ({self._l3.getX()}, {self._l3.getY()}), ({self._l4.getX()}, {self._l4.getY()}).')

    def atualizar(self, x1=None, y1=None, x2=None, y2=None, x3=None, y3=None, x4=None, y4=None):
        if x1 is not None and y1 is not None and x2 is not None and y2 is not None and x3 is not None and y3 is not None and x4 is not None and y4 is not None:
            self.setPontos(x1, y1, x2, y2, x3, y3, x4, y4)

    def verificaPosicao(self, xp, yp):
        p = Ponto(xp, yp)
        if self.estaNaBorda(p):
            return ("O ponto está na borda do Losango")
        elif self.estaDentro(p):
            return ("O ponto está dentro do Losango")
        else:
            return ("O ponto está fora do Losango")

    def estaNaBorda(self, ponto):
        x, y = ponto.getX(), ponto.getY()
        vertices = [self._l1, self._l2, self._l3, self._l4]
        for i in range(len(vertices)):
            p1 = vertices[i]
            p2 = vertices[(i + 1) % len(vertices)]
            if self.estaNoSegmento(x, y, p1.getX(), p1.getY(), p2.getX(), p2.getY()):
                return True
        return False

    def estaNoSegmento(self, px, py, ax, ay, bx, by):
        cross_product = (py - ay) * (bx - ax) - (px - ax) * (by - ay)
        if abs(cross_product) > 1e-6:  # Not on the line
            return False
        dot_product = (px - ax) * (bx - ax) + (py - ay) * (by - ay)
        if dot_product < 0:
            return False
        squared_length = (bx - ax) ** 2 + (by - ay) ** 2
        if dot_product > squared_length:
            return False
        return True

    def estaDentro(self, ponto):
        x = ponto.getX()
        y = ponto.getY()
        vertices = [self._l1, self._l2, self._l3, self._l4]
        n = len(vertices)
        inside = False
        p1x, p1y = vertices[0].getX(), vertices[0].getY()
        for i in range(n+1):
            p2x, p2y = vertices[i % n].getX(), vertices[i % n].getY()
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    def getTipo(self):
        return "Losango"
    
    def getNumero(self):
        return self._n


class TrapezioRet(Ponto):
    _n = 0
    _tr1 = Ponto
    _tr2 = Ponto
    _tr3 = Ponto
    _tr4 = Ponto
    _bmaior = 0
    _bmenor = 0
    _altura = 0
    _area = 0
    _perimetro = 0
    _isReto = None

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        global numeroTrapezio
        numeroTrapezio += 1
        super().__init__(x1,y1)        
        self.setPontos(x1, y1, x2, y2, x3, y3, x4, y4)
        self._n = numeroTrapezio
        forma = Formas()
        forma.adicionar(self)

    def setPontos(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self._tr1 = Ponto(x1, y1)
        self._tr2 = Ponto(x2, y2)
        self._tr3 = Ponto(x3, y3)
        self._tr4 = Ponto(x4, y4)
        self._bmaior = x4 - x3
        self._bmenor = x2 - x1
        self._altura = y3 - y1
        self.calculaArea()
        self.calculaPerimetro()
        self.verificaReto()
   
    def getArea(self):
        return self._area
    
    def getPerimetro(self):
        return self._perimetro

    def getAltura(self):
        return self._altura

    def getEhReto(self):
        if self._isReto:
            return 'Sim'
        else:
            return 'Não'
    
    def getTr1(self):
        return self._tr1
    
    def getTr2(self):
        return self._tr2
    
    def getTr3(self):
        return self._tr3
    
    def getTr4(self):
        return self._tr4

    def getBMaior(self):
        return self._bmaior
    
    def getBMenor(self):
        return self._bmenor
    
    def verificaReto(self):
        xs = (self._tr1.getX(), self._tr2.getX(), self._tr3.getX(), self._tr4.getX())
        ys = (self._tr1.getY(), self._tr2.getY(), self._tr3.getY(), self._tr4.getY())

        if len(set(xs)) != len(xs) or len(set(ys)) != len(ys):
            self._isReto = True
        else:
            self._isReto = False

    def calculaArea(self):
        self._area = ((self._bmaior + self._bmenor) * self._altura) / 2

    def calculaPerimetro(self):
        lado = sqrt(((self._bmaior - self._bmenor) / 2) ** 2 + self._altura ** 2)
        self._perimetro = self._bmaior + self._bmenor + 2 * lado 

    def toPrint(self):
        if ( self._isReto == False ):
            print('Este Trapézio não é reto')
        elif self._area <= 0 or self._perimetro <= 0 or (self._perimetro <= 0 and self._area <= 0):
            print('Este Trapézio não é possível')
        else:
            print(f'Eu sou o trapézio, minha base maior é {self._bmaior}, minha base menor é {self._bmenor}, minha altura é {self._altura}, minha área é {self._area:.2f}, meu perímetro é {self._perimetro:.2f}.')
            print(f'As coordenadas dos meus vértices são ({self._tr1.getX()}, {self._tr1.getY()}), ({self._tr2.getX()}, {self._tr2.getY()}), ({self._tr3.getX()}, {self._tr3.getY()}), ({self._tr4.getX()}, {self._tr4.getY()}).')

    def atualizar(self, x1=None, y1=None, x2=None, y2=None, x3=None, y3=None, x4=None, y4=None):
        if x1 is not None and y1 is not None and x2 is not None and y2 is not None and x3 is not None and y3 is not None and x4 is not None and y4 is not None:
            self.setPontos(x1, y1, x2, y2, x3, y3, x4, y4)        

    def verificaPosicao(self, xp, yp):
        # Vetores dos lados do trapézio
        v1 = (self._tr2.getX() - self._tr1.getX(), self._tr2.getY() - self._tr1.getY())
        v2 = (self._tr3.getX() - self._tr2.getX(), self._tr3.getY() - self._tr2.getY())
        v3 = (self._tr4.getX() - self._tr3.getX(), self._tr4.getY() - self._tr3.getY())
        v4 = (self._tr1.getX() - self._tr4.getX(), self._tr1.getY() - self._tr4.getY())
        
        # Vetor do ponto para o primeiro vértice
        vp1 = (self._tr1.getX() - xp, self._tr1.getY() - yp)
        # Vetor do ponto para o segundo vértice
        vp2 = (self._tr2.getX() - xp, self._tr2.getY() - yp)
        # Vetor do ponto para o terceiro vértice
        vp3 = (self._tr3.getX() - xp, self._tr3.getY() - yp)
        # Vetor do ponto para o quarto vértice
        vp4 = (self._tr4.getX() - xp, self._tr4.getY() - yp)
        
        # Função para calcular o produto vetorial de dois vetores 2D
        def produto_vetorial(v1, v2):
            return v1[0] * v2[1] - v1[1] * v2[0]
        
        # Calculando os produtos vetoriais para determinar a orientação
        d1 = produto_vetorial(v1, vp1)
        d2 = produto_vetorial(v2, vp2)
        d3 = produto_vetorial(v3, vp3)
        d4 = produto_vetorial(v4, vp4)
        
        # Verificando a posição do ponto em relação aos vetores
        if (d1 > 0 and d2 > 0 and d3 > 0 and d4 > 0) or (d1 < 0 and d2 < 0 and d3 < 0 and d4 < 0):
            return (f'O ponto ({xp}, {yp}) está dentro do Trapézio')
        elif (d1 == 0 or d2 == 0 or d3 == 0 or d4 == 0):
            return (f'O ponto ({xp}, {yp}) está na borda do Trapézio')
        else:
            return (f'O ponto ({xp}, {yp}) está fora do Trapézio')

    def getTipo(self):
        return "Trapézio"

    def getNumero(self):
        return self._n

class Pentagono(Ponto):
    _n = 0
    _p1 = Ponto
    _p2 = Ponto
    _p3 = Ponto
    _p4 = Ponto
    _p5 = Ponto
    _lado = 0
    _area = 0
    _perimetro = 0

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, lado):
        global numeroPentagono
        numeroPentagono += 1
        super().__init__(x1,y1)
        self.setPontos(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, lado)
        self._n = numeroPentagono
        forma = Formas()
        forma.adicionar(self)

    def setPontos(self, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, lado):
        self._p1 = Ponto(x1, y1)
        self._p2 = Ponto(x2, y2)
        self._p3 = Ponto(x3, y3)
        self._p4 = Ponto(x4, y4)
        self._p5 = Ponto(x5, y5)
        self._lado = lado
        self.calculaArea()
        self.calculaPerimetro()

    def calculaArea(self):
        self._area = (5 * self._lado ** 2) / (4 * tan(pi / 5))

    def getLado(self):
        return self._lado

    def calculaPerimetro(self):
        self._perimetro = 5 * self._lado

    def getArea(self):
        return self._area

    def getPerimetro(self):
        return self._perimetro

    def getP1(self):
        return self._p1
    
    def getP2(self):
        return self._p2
    
    def getP3(self):
        return self._p3
    
    def getP4(self):
        return self._p4
    
    def getP5(self):
        return self._p5

    def toPrint(self):
        if self._area <= 0 or self._perimetro <= 0 or (self._perimetro <= 0 and self._area <= 0):
            print(f'Este {self.getTipo()} não é possível')
        else:
            print(f'Eu sou o {self.getTipo()} nº {self.getNumero()}, meu lado é {self._lado}, minha área é {self._area:.2f}, meu perímetro é {self._perimetro:.2f}.')
            print(f'As coordenadas dos meus vértices são ({self._p1.getX()}, {self._p1.getY()}), ({self._p2.getX()}, {self._p2.getY()}), ({self._p3.getX()}, {self._p3.getY()}), ({self._p4.getX()}, {self._p4.getY()}), ({self._p5.getX()}, {self._p5.getY()}).')

    def atualizar(self, x1=None, y1=None, x2=None, y2=None, x3=None, y3=None, x4=None, y4=None, x5=None, y5=None, lado=None):
        if x1 is not None and y1 is not None and x2 is not None and y2 is not None and x3 is not None and y3 is not None and x4 is not None and y4 is not None and x5 is not None and y5 is not None:
            self.setPontos(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, lado)        

    def verificaPosicao(self, xp, yp):
        p = Ponto(xp, yp)
        if self.estaNaBorda(p):
            return (f"O ponto ({xp},{yp}) está na borda do Pentágono")
        elif self.estaDentro(p):
            return (f"O ponto ({xp},{yp}) está dentro do Pentágono")
        else:
            return (f"O ponto ({xp},{yp}) fora do Pentágono")

    def estaNaBorda(self, ponto):
        x, y = ponto.getX(), ponto.getY()
        vertices = [self._p1, self._p2, self._p3, self._p4, self._p5]
        for i in range(len(vertices)):
            p1 = vertices[i]
            p2 = vertices[(i + 1) % len(vertices)]
            if self.estaNoSegmento(x, y, p1.getX(), p1.getY(), p2.getX(), p2.getY()):
                return True
        return False

    def estaNoSegmento(self, px, py, ax, ay, bx, by):
        # Check if point (px, py) is on the line segment from (ax, ay) to (bx, by)
        cross_product = (py - ay) * (bx - ax) - (px - ax) * (by - ay)
        if abs(cross_product) > 1e-6:  # Not on the line
            return False
        dot_product = (px - ax) * (bx - ax) + (py - ay) * (by - ay)
        if dot_product < 0:
            return False
        squared_length = (bx - ax) ** 2 + (by - ay) ** 2
        if dot_product > squared_length:
            return False
        return True

    def estaDentro(self, ponto):
        x = ponto.getX()
        y = ponto.getY()
        vertices = [self._p1, self._p2, self._p3, self._p4, self._p5]
        n = len(vertices)
        inside = False
        p1x, p1y = vertices[0].getX(), vertices[0].getY()
        for i in range(n+1):
            p2x, p2y = vertices[i % n].getX(), vertices[i % n].getY()
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside


    def getTipo(self):
        return "Pentágono"

    def getNumero(self):
        return self._n