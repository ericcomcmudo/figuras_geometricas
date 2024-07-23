from package.maths.terms import TrapezioRet

def workspace():
    #criando o Trapezio Retangulo
    trapezio1 = TrapezioRet(1,2,3,4,5,6,7,8)
    #caracteristicas
    trapezio1.toPrint()    
    #atualizando
    trapezio1.atualizar(1,1,5,1,0,5,6,5)
    #caracteristicas
    trapezio1.toPrint()
    #verificações
    trapezio1.verificaPosicao(2,2)
    trapezio1.verificaPosicao(5,1)
    trapezio1.verificaPosicao(7,3)
    
if __name__ == "__main__":
    workspace()

else:
    workspace()