from package.maths.terms import Ponto

def workspace():
    #Criando o Ponto
    ponto1 = Ponto(3,4)
    #Características
    ponto1.toPrint()
    #distancia da origem
    ponto1.distanciaDaOrigem()
    #distancia do ponto
    ponto1.distanciaEntrePontos(6,9)
    #Atualizando
    ponto1.setX(6)
    ponto1.setY(8)
    #Características
    ponto1.toPrint()
    #distancia da origem
    ponto1.distanciaDaOrigem()
    #distancia do ponto
    ponto1.distanciaEntrePontos(6,9)

if __name__ == "__main__":
    workspace()

else:
    workspace()


