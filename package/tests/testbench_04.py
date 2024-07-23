from math import sqrt
from package.maths.terms import Triangulo

def workspace():
    #Criando o triangulo
    Trianguloangulo1 = Triangulo(0,0,4,0,2,3)
    #Caracteristicas
    Trianguloangulo1.toPrint()
    #tipo então salva tudo e a gente continua depois
    print(Trianguloangulo1._tipo)
    #verificar método de atualizacao
    Trianguloangulo1.atualizar(0,0,6,0,3,(3*sqrt(3)))
    Trianguloangulo1.toPrint()
    print(Trianguloangulo1._tipo)
    #verificando posicões
    Trianguloangulo1.verificaPosicao(3,3)
    Trianguloangulo1.verificaPosicao(1,1)
    Trianguloangulo1.verificaPosicao(3,1) 
    Trianguloangulo1.verificaPosicao(6,6)
    Trianguloangulo2 = Triangulo(0,0,4,0,0,3)
    Trianguloangulo2.ehPossivel()

if __name__ == "__main__":
    workspace()

else:
    workspace()