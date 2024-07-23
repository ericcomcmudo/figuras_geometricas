from package.maths.terms import Losango

def workspace():
    #criando o losango
    losango1 = Losango(7,6,1,2,3,4,5,6)
    #verificando
    losango1.verificaPosicao(4,4.5)
    losango1.verificaPosicao(0,0)
    losango1.verificaPosicao(3,4)
    #caracteristicas
    losango1.toPrint()
    #atualizando 
    losango1.atualizar(0,0,2,2,4,0,2,-2)
    #caracteristicas
    losango1.toPrint()
    #verificando
    losango1.verificaPosicao(2,0)
    losango1.verificaPosicao(5,5)
    losango1.verificaPosicao(2,2)

if __name__ == "__main__":
    workspace()

else:
    workspace()
