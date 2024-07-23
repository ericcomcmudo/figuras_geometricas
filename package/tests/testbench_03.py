from package.maths.terms import Retangulo

def workspace():
    #Criando Retangulo
    retangulo1 = Retangulo(10,2,1,4,2,7,6,8)
    #Característica
    retangulo1.toPrint()
    #verificando posição    
    retangulo1.verificaPosicao(2,2)
    #atualizando
    retangulo1.atualizar(1,1,4,1,4,4,1,4)
    #Característica
    retangulo1.toPrint()
    #verificando posição denotro   
    retangulo1.verificaPosicao(2,2)
    retangulo1.verificaPosicao(3,3)
    #verificando posição na borda   
    retangulo1.verificaPosicao(1,1)
    retangulo1.verificaPosicao(2,1)
    #verificando posição na fora 
    retangulo1.verificaPosicao(0,0)
    retangulo1.verificaPosicao(5,5)

if __name__ == "__main__":
    workspace()

else:
    workspace()
