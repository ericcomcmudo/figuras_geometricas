from package.maths.terms import Quadrado

def workspace():
    #Criando quadrado
    quadrado1 = Quadrado(1,2,2,4,2,6,7,1)
    #caracteristicas
    quadrado1.toPrint() 
    #verificando para o ponto
    quadrado1.verificaPosicao(1,2)
    #atualizando
    quadrado1.atualizar(0,0,1,0,1,1,0,1)
    #caracteristicas
    quadrado1.toPrint() 
    #verificando para o ponto
    quadrado1.verificaPosicao(0.5,0.5) 
    quadrado1.verificaPosicao(2,2) 
    quadrado1.verificaPosicao(1,0)

if __name__ == "__main__":
    workspace()

else:
    workspace()
