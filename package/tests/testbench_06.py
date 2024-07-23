from package.maths.terms import Circulo

def workspace():
    #Criando o Círculo    
    circulo1 = Circulo(3,4,4)
    #Características
    circulo1.toPrint()
    #Atualizando
    circulo1.atualizar(2,8,9)
    #Características
    circulo1.toPrint()
    #verificando ponto
    circulo1.verificaPosicao(11,8)
    circulo1.verificaPosicao(4,4)
    circulo1.verificaPosicao(48,78)

if __name__ == "__main__":
    workspace()

else:
    workspace()